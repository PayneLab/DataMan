"""Project DataMan

These define the 'models' (like classes)
    with certain fields."""

from django.db import models
from datetime import datetime
import json
from django_mysql.models import ListTextField
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from os.path import basename
from os.path import relpath
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from django.core.exceptions import ValidationError

class Dataset(models.Model):
    _datasetName = models.TextField(verbose_name='Dataset Name',
                                   unique=True)
    _datasetID = models.AutoField(verbose_name='Dataset ID', primary_key=True,
                                    unique=True)
    _sample = models.ManyToManyField('Sample', verbose_name="Sample", blank=False)
    _experiment = models.ForeignKey('Experiment', on_delete=models.CASCADE,
                                   blank=True, null=True,verbose_name='Experiment')
    _instrument = models.ForeignKey('Instrument', verbose_name='Instrument', on_delete=models.SET_NULL, blank=False, null=True)
    _instrumentSetting = models.ForeignKey('InstrumentSetting',verbose_name="Instrument Setting",
                                    on_delete=models.SET_NULL, null=True, blank=True)
    if _instrument != 0:
        _instrument.limit_choices_to = {'_instrument': _instrument}
    _type = models.TextField(verbose_name='Type of data generated', null=True, blank=True)
    _operator = models.TextField(verbose_name='Operator', help_text ="The team member who ran the machine.", null=True, blank=True)
    #_status = models.ForeignKey("fileStatusOptions", on_delete=models.SET_NULL, verbose_name='Status', null=True)
    _status = models.TextField(verbose_name="File Status", null = True)
    _dateCreated = models.DateTimeField(verbose_name='Date Created', default=datetime.now)

    _fileLocation = models.TextField(verbose_name='Path to original file location', blank=True, null=True)
    _fileLocationRemote = models.TextField(verbose_name='Path to remote (supercomputer) file location', blank=True, null=True)
    _fileName = models.TextField(verbose_name='File Name', null=True, blank=False)

    _acquisitionStart = models.DateTimeField(verbose_name='Upload Date',default=datetime.now, null=True, blank=True)
    _acquisitionEnd = models.DateTimeField(verbose_name="Acquisition Date", default=datetime.now, null=True, blank=True)
    _fileSize = models.IntegerField(verbose_name='File Size', null=True, blank=True)
    _fileHash = models.TextField(verbose_name='File Hash', null=True, blank=True)
    _comments = models.TextField(verbose_name='Comments, Notes, or Details',blank=True,null=True)

    _extra_fields = models.TextField(blank=True, null=True)

    def extra_fields(self):
        return self._extra_fields
    def setExtraFields(self, value):
        self._extra_fields = value

    def clean(self):

        remote_path = self._fileLocationRemote
        local_path = self._fileLocation

        if not remote_path and not local_path:
            raise ValidationError("A file path must be specified.")


    def get_absolute_url(self):
        return reverse('dataset-detail', args=[str(self._datasetID)])

    def __str__(self):
        return str(self._datasetName)

    def datasetName(self):
        return self._datasetName
    def setDatasetName(self, value):
        self._datasetName = value
    def datasetID(self):
        return self._datasetID
    def setDatasetID(self, value):
        self._datasetID = value
    def experiment(self):
        return self._experiment
    def setExperiment(self, value):
        self._experiment = value
    def sample(self):
        return self._sample.all()
    #def setSample(self, value):
    #    self._sample = value
    def instrument(self):
        return self._instrument
    def setInstrument(self, _val):
        self.instrument = _val
    def instrumentSetting(self):
        return self._instrumentSetting
    def setInstrumentSetting(self, _val):
        self.instrumentSetting = _val
    def type(self):
        return self._type
    def setType(self, value):
        self._type = value
    def operator(self):
        return self._operator
    def setOperator(self, value):
        self._operator = value
    def status(self):
        return self._status
    def setStatus(self, value):
        self._status = value
    def dateCreated(self):
        return self._dateCreated
    def setDateCreated(self, value):
        self._dateCreated = value
    def fileLocation(self):
        return self._fileLocation
    def setFileLocation(self, value):
        self._fileLocation = value
    def fileLocationRemote(self):
        return self._fileLocationRemote
    def setFileLocationRemote(self, value):
        self._fileLocationRemote = value
    def fileName(self):
        return self._fileName
    def setFileName(self, value):
        self._fileName = value
    def acquisitionStart(self):
        return self._acquisitionStart
    def setAcquisitionStart(self, value):
        self._acquisitionStart = value
    def acquisitionEnd(self):
        return self._acquisitionEnd
    def setAcquisitionEnd(self, value):
        self._acquisitionEnd = value
    def fileSize(self):
        return self._fileSize
    def setFileSize(self, value):
        self._fileSize = value
    def fileHash(self):
        return self._fileHash
    def setFileHash(self, value):
        self._fileHash = value

class Sample(models.Model):
    _sampleName = models.TextField(verbose_name="Sample Name",
                                  unique=True)
    _sampleID = models.AutoField(primary_key=True,verbose_name="Sample ID",
                                   unique=True)
    _experiment = models.ForeignKey('Experiment', on_delete=models.CASCADE,
                                   blank=False, null=True,verbose_name='Experiment')
    # preceedingSample = models.TextField(verbose_name='Preceeding Sample')
    _storageCondition = models.TextField(verbose_name='Storage Condition')
    _storageLocation = models.TextField(verbose_name='Storage Location')
    _treatmentProtocol = models.ManyToManyField('Protocol', verbose_name='Treatment Protocol', blank=True)
    _dateCreated = models.DateTimeField(verbose_name='Date Created', default=datetime.now)
    _individual = models.ManyToManyField('Individual', verbose_name='Individual Identifier', blank=True)
    _organism = models.TextField(verbose_name='Organism')
    _organismModifications = models.TextField(verbose_name='Organism Modifications', default='None', null=True, blank=True)
    _comments = models.TextField(verbose_name='Comments, Notes, or Details',blank=True,null=True)

    _extra_fields = models.TextField(blank=True, null=True)

    def extra_fields(self):
        return self._extra_fields
    def setExtraFields(self, value):
        self._extra_fields = value

    def sampleName(self):
        return self._sampleName
    def setSampleName(self, value):
        self._sampleName = value
    def sampleID(self):
        return self._sampleID
    def setSampleID(self, value):
        self._sampleID = value
    def experiment(self):
        return self._experiment
    def setExperiment(self, value):
        self._experiment = value
    def storageCondition(self):
        return self._storageCondition
    def setStorageCondition(self, value):
        self._storageCondition = value
    def storageLocation(self):
        return self._storageLocation
    def setStorageLocation(self, value):
        self._storageLocation = value
    def treatmentProtocol(self):
        return self._treatmentProtocol
    def setTreatmentProtocol(self, value):
        self._treatmentProtocol = value
    def dateCreated(self):
        return self._dateCreated
    def setDateCreated(self, value):
        self._dateCreated = value
    def individual(self):
        return self._individual
    def setIndividual(self, value):
        self._individual.set(value)
    def organism(self):
        return self._organism
    def setOrganism(self, value):
        self._organism = value
    def organismModifications(self):
        return self._organismModifications
    def setOrganismModifications(self, value):
        self._organismModifications = value

    # this sets the default sort
    class Meta:
        ordering = ['_sampleName']

    def get_absolute_url(self):
        return reverse('sample-detail', args=[self.sampleID])

    def __str__(self):
        return str(self._sampleName)

class Individual(models.Model):
    _individualIdentifier = models.TextField(verbose_name='Individual Identifier',
                                      unique=True)
    _individualID = models.AutoField(verbose_name='Individual ID', unique=True, primary_key=True)
    _experiment = models.ForeignKey('Experiment', on_delete=models.CASCADE,
                                    blank=False, null=True, verbose_name='Experiment')
    _gender = models.TextField(verbose_name='Gender', null=True)
    _age = models.TextField(verbose_name='Age', null=True)
    _healthStatus = models.TextField(verbose_name='Health Status', null=True)
    _comments = models.TextField(verbose_name='Comments, Notes, or Details', blank=True, null=True)

    _extra_fields = models.TextField(blank=True, null=True)

    def individualIdentifier(self):
        return self._individualIdentifier
    def individualID(self):
        return self._individualID
    def experiment(self):
        return self._experiment

    def age(self): return self._age
    def gender(self): return self._gender
    def healthStatus(self): return self._healthStatus

    def extra_fields(self):
        return self._extra_fields
    def setExtraFields(self, value):
        self._extra_fields = value

    def setIndividualIdentifier(self, value):
        self._individualIdentifier = value
    def setIndividualID(self, value):
        self._individualID = value
    def setExperiment(self, value):
        self._experiment = value
    def setComments(self, value):
        self._comments = value

    class Meta:
        ordering = ['_individualIdentifier']

    def get_absolute_url(self):
        return reverse('individual-detail', args=[self.individualID()])

    def __str__(self):
        return self._individualIdentifier

class Experiment(models.Model):
    _experimentName = models.TextField(verbose_name='Experiment Name',
                                      unique=True)
    _experimentID = models.AutoField(verbose_name='Experiment ID', unique=True, primary_key=True)
    _projectLead = models.TextField(verbose_name='Project Lead')
    _teamMembers = models.TextField(verbose_name='Team Members',blank=True,null=True)
    _IRB = models.IntegerField(verbose_name='IRB Number',blank=True,null=True)
    _experimentalDesign = models.ForeignKey('ExperimentalDesign', on_delete=models.SET_NULL,
        verbose_name='Experimental Design', blank=True, null=True)
    _comments = models.TextField(verbose_name='Comments, Notes, or Details',blank=True,null=True)

    def experimentName(self):
        return self._experimentName
    def setExperimentName(self, value):
        self._experimentName = value
    def experimentID(self):
       return self._experimentID
    def setExperimentID(self, value):
        self._experimentID = value
    def projectLead(self):
        return self._projectLead
    def setProjectLead(self, value):
        self._projectLead = value
        return self._projectLead
    def teamMembers(self):
        return self._teamMembers
    def setTeamMembers(self, value):
        self._teamMembers = value
    def IRB(self):
        return self._IRB
    def setIRB(self, value):
        self._IRB = value
    def experimentalDesign(self):
        return self._experimentalDesign
    def setExperimentalDesign(self, value):
        self._experimentalDesign = value
    def comments(self): return self._comments
    def setComments(self, v): self._comments = v

    def get_absolute_url(self):
        return reverse('experiment-detail', args=[str(self._experimentID)])

    def __str__(self):
        return str(self._experimentName)

class CheckDuplicateStorage(FileSystemStorage):
    def save(self, name, content, max_length=None):
        if self.exists(name):
            old_copy = self.open(name, 'rb')
            if old_copy.size==content.size:
                if old_copy.read()==content.read():
                    #The file is exactly the same as one already in the system.
                    return name
            #Same name, not the same file
            #This is where I'd like to ask the user
            raise ValidationError("There is a different file named %s" % basename(name))

        return super(CheckDuplicateStorage, self)._save(name, content)

class File(models.Model):
    _file = models.FileField('File', upload_to=settings.MEDIA_ROOT+'/files/%Y/',
            blank = False, storage=CheckDuplicateStorage(), unique=True)

    def file(self):
        return self._file
    def relative_path(self):
        return relpath(self._file.path, settings.MEDIA_ROOT)
    def url(self):
        p = settings.MEDIA_URL
        return (p + self.relative_path())

    def __str__(self):
        return basename(self._file.name)
class detailedField(models.Model):
    _name = models.CharField(unique=True, primary_key=True,
            blank=False, null=False, max_length = 25, verbose_name= "Name")
    _description = models.TextField(verbose_name="Description",blank=True, null=True)
    _files = models.ManyToManyField('File', verbose_name="Related files or images", blank=True)

    class Meta:# this sets the default sort
        ordering = ['_name']

    def __str__(self):
        return str(self._name)
    def name(self):
        return self._name
    def setName(self, value):
        self._name = value
    def description(self):
        return self._description
    def setDescription(self, value):
        self._description = value
    def files(self):
        return self._files
    def addFile(self, file):
        self._files.add(file)

class InstrumentSetting(detailedField):
    _instrument = models.ForeignKey("Instrument", on_delete=models.CASCADE,
                                    blank=False, null=True,verbose_name='Instrument')
    comments = models.TextField(verbose_name="Comments", blank=True, null=True)
    def __str__(self):
        return self._name
    def instrument(self):
        return self._instrument
    def setInstrument(self, value):
        self._instrument = value
class Instrument(detailedField):
    def __str__(self):
        return self._name
    #redefined for the html template
    def description(self):
        return self._description
    def file(self):
        return self._file
class ExperimentalDesign(detailedField):
    _extra_fields = ListTextField(
        verbose_name = 'Extra Fields for Individuals', null=True, blank=True,
        base_field = models.CharField(blank=True,null=True,max_length=100),
        #Text fields are not allowed, and these are headers/category names
    )

    _extra_fields_samples = ListTextField(
        verbose_name = 'Extra Fields for Samples', null=True, blank=True,
        base_field = models.CharField(blank=True,null=True,max_length=100),
    )
    _extra_fields_datasets = ListTextField(
        verbose_name = 'Extra Fields for Datasets', null=True, blank=True,
        base_field = models.CharField(blank=True,null=True,max_length=100)
    )

    def __str__(self):
        return str(self._name)

    def extra_fields(self):
        return self._extra_fields
    def set_extra_fields(self, value):
        self._extra_fields = value

    def extra_fields_samples(self):
        return self._extra_fields_samples
    def set_extra_fields_samples(self, value):
        self._extra_fields_samples = value

    def extra_fields_datasets(self):
        return self._extra_fields_datasets
    def set_extra_fields_datasets(self, value):
        self._extra_fields_datasets = value
class Protocol(detailedField):
    def __str__(self):
        return self._name

class fileStatusOption(models.Model):
    _option = models.CharField(unique=True, primary_key=True,
        blank=False, null=False, max_length = 20, verbose_name="Status")
    def __str__(self):
        return self._option

class FileRead(models.Model):
    lead = models.CharField(blank=False, max_length = 200, verbose_name='Project Lead')
    _File = models.FileField(blank=False, upload_to='files/')
    def file(self):
        return self._File()
    def __str__(self):
        return self._File()
