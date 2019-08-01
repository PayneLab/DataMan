"""Project DataMan

These use the django forms to make
    data entry easy."""

from django import forms
from datetime import datetime
from datetime import timedelta
from django.core.exceptions import ValidationError
from Records.models import *
import json

STATUS_OPTIONS = [#Probably eventually replace with something not hard coded in
    ('In Progress','In Progress'), #Maybe a fixture, maybe just add them manually
    ('Submitted','Submitted'),     # once it's uploaded
    ('Analyzed','Analyzed'),
    ('Released','Released'),
    ('Archived','Archived'),
    ('Deleted','Deleted'),
    ('Revoked','Revoked'),
    ('Replaced','Replaced')
    ]

class InstrumentForm(forms.ModelForm):
    new_files = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), label = 'Upload New ', required=False)
    class Meta:
        model = Instrument
        fields = ['_name', '_description', '_files', 'new_files']
class InstrumentSettingForm(forms.ModelForm):
    new_files = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), label = 'Upload New ', required=False)
    class Meta:
        model = InstrumentSetting
        fields = ['_name', '_description', '_files', 'new_files']
class ProtocolForm(forms.ModelForm):
    new_files = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), label = 'Upload New ', required=False)
    class Meta:
        model = Protocol
        fields = ['_name', '_description', '_files', 'new_files']

    def __init__(self, post_data = None, files_data = None):
        if post_data and files_data:
            return super(ProtocolForm, self).__init__(post_data, files_data)
        return super(ProtocolForm, self).__init__()

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)

class fileStatusOptionForm(forms.ModelForm):
    class Meta:
        model = fileStatusOption
        exclude = []
class ExperimentalDesignForm(forms.ModelForm):
    new_files = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), label = 'Upload New ', required=False)
    class Meta:
        model = ExperimentalDesign
        fields = ['_name', '_description', '_files', 'new_files', '_extra_fields', '_extra_fields_samples','_extra_fields_datasets']

class DateInput(forms.DateInput):
    input_type = 'date'
class TimeInput(forms.TimeInput):
    input_type = 'time'
class DateTimeInput(forms.MultiWidget):
    def __init__(self, attrs = None,date_format=None, time_format='%H:%M'):
        widgets=(DateInput(attrs=attrs),
            forms.TimeInput(attrs=attrs, format=time_format))
        super(DateTimeInput, self).__init__(widgets, attrs)

    def decompress(self, value):
        if value:
            return [value.date(), value.time().replace(second = 0, microsecond=0)]
        return [None, None]

class UploadFileForm(forms.ModelForm):
    readFail = False
    class Meta:
        model = FileRead
        fields = ['_File']

    def __init__(self,  *args, extraFields=None, **kwargs,):
        super(UploadFileForm, self).__init__(*args, **kwargs)
        if extraFields!=None:
            for f in extraFields:
                self.fields[f] = forms.CharField(label=f)

    def clean(self):
        data = self.cleaned_data
        if self.readFail: #conditionals from views
            raise forms.ValidationError('Invalid file')
        else:
            return data

class ListFieldsForm(forms.ModelForm):
    class Meta:
        model = FileRead
        fields = []
    def __init__(self,  *args, extraFields=None, **kwargs):
        super(ListFieldsForm, self).__init__(*args, **kwargs)
        if extraFields!=None:
            for f in extraFields:
                self.fields[f] = forms.CharField(label=f)
    def save(self):
        return self.cleaned_data

class AddSampleForm(forms.ModelForm):
    def __name__(self, *args, **kwargs):
        super(AddSampleForm, self).__name__

    class Meta:
        model = Sample
        fields = ['_sampleName', '_individual',
                  '_storageCondition', '_storageLocation', '_treatmentProtocol',
                  '_dateCreated','_organism', '_organismModifications', '_comments']
        widgets = {'_dateCreated':DateInput()}

    def __init__(self, *args, extraFields=None, **kwargs):
        super(AddSampleForm, self).__init__(*args, **kwargs)
        if extraFields!=None:
            for f in extraFields:
                self.fields[f] = forms.CharField(label=f)

class SelectExperiment(forms.ModelForm):
    _experiment = forms.ModelChoiceField(label='Experiment', queryset=Experiment.objects.all(), widget=forms.Select(attrs={"onChange":'form.submit()'}))
    class Meta:
        model = Individual
        fields = ['_experiment']

class AddIndividualForm(forms.ModelForm):
    class Meta:
        model = Individual
        exclude = ['_individualID','_extra_fields']
    def __init__(self,  *args, extraFields=None, **kwargs,):
        super(AddIndividualForm, self).__init__(*args, **kwargs)
        if extraFields!=None:
            for f in extraFields:
                self.fields[f] = forms.CharField(label=f)
class AddDatasetForm(forms.ModelForm):
    _status = forms.CharField(label='File Status', widget=forms.Select(choices=STATUS_OPTIONS))
    class Meta:
        model = Dataset
        fields = ['_datasetName','_sample', '_instrument','_instrumentSetting','_type',
                  '_operator','_dateCreated',#'_acquisitionStart',#'_acquisitionEnd',
                  '_status','_fileName','_fileLocation','_fileLocationRemote',
                  '_fileSize', '_comments']
        widgets = {
            '_dateCreated':DateInput(),
            '_acquisitionStart':DateTimeInput(),
            '_acquisitionEnd':DateTimeInput(),
        }

    def __init__(self, *args, extraFields=None, **kwargs):
        super(AddDatasetForm, self).__init__(*args, **kwargs)
        if extraFields!=None:
            for f in extraFields:
                self.fields[f] = forms.CharField(label=f)


class AddExperimentForm(forms.ModelForm):
    class Meta:
        model = Experiment
        fields = ['_experimentName','_projectLead','_teamMembers',
                  '_IRB', '_comments', '_experimentalDesign']

    def __init__(self, *args, ask_design=False, **kwargs):
        super(AddExperimentForm, self).__init__(*args, **kwargs)
        if not ask_design:
            self.fields["_experimentalDesign"].widget = forms.widgets.HiddenInput()
            self.fields["_experimentalDesign"].label = ''

class BackUpSelectForm(forms.Form):
	source = forms.CharField(label='Use backup from:', widget=forms.Select(choices=[('Local', 'Local'), ('Box', 'Box')]))
	file = forms.FilePathField(label='Restore from local', path=settings.BACKUP_LOCATION, allow_folders=False)
	file.choices.sort(reverse=True)

	def __init__(self, *args, **kwargs):
		remote_files = kwargs.pop('remote_files', None)
		super(BackUpSelectForm, self).__init__(*args, **kwargs)
		if remote_files:
			self.fields['remote_file'] = forms.CharField(label='Restore from Box', widget=forms.Select(choices=remote_files))
