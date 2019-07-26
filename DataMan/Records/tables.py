"""Project DataMan

These define the tables used in the archive view pages."""

import django_tables2 as tables
from django_tables2.utils import A
from Records.models import Dataset, Sample, Experiment, Individual


class DatasetTable(tables.Table):
    _datasetName = tables.LinkColumn('dataset-detail', args=[A('pk')])
    _experiment = tables.LinkColumn('experiment-detail', args=[A('_experiment.pk')])
    _instrument =  tables.LinkColumn('instruments')
    _instrumentSetting =  tables.LinkColumn('settings')
    _dateCreated = tables.DateTimeColumn(format ='M d, Y')
    #_acquisitionStart = tables.DateTimeColumn(format ='M d, Y h:m')
    #_acquisitionEnd = tables.DateTimeColumn(format ='M d, Y h:m')

    class Meta:
        model = Dataset
        exclude = ['_datasetID','_sample','_acquisitionStart','_acquisitionEnd','_fileHash', '_extra_fields']


    def __init__(self, *args, new_or_existing=None, **kwargs):
        super(DatasetTable, self).__init__(*args, **kwargs)
        if new_or_existing:
            self.row_attrs = {
                'new-or-existing': lambda record: new_or_existing[record._datasetName]
            }
        else: self.row_attrs = {'new-or-existing':'EXISTING'}

class SampleTable(tables.Table):
    _sampleName = tables.LinkColumn('sample-detail', args=[A('pk')])
    _experiment = tables.LinkColumn('experiment-detail', args=[A('_experiment.pk')])
    _treatmentProtocol = tables.ManyToManyColumn(linkify_item=('protocols', {}))
    #_individual = tables.LinkColumn('individual-detail', args=[A('_individual.pk')], empty_values=())

    _dateCreated = tables.DateTimeColumn(format ='M d, Y')

    class Meta:
        model = Sample
        fields = ['_sampleName','_experiment','_sampleName',
                  '_storageCondition', '_storageLocation', '_treatmentProtocol',
                  '_dateCreated', '_individual', '_organism', '_organismModifications', '_comments']

    def __init__(self, *args, new_or_existing=None, **kwargs):
        super(SampleTable, self).__init__(*args, **kwargs)
        if new_or_existing:
            self.row_attrs = {
                'new-or-existing': lambda record: new_or_existing[record._sampleName]
            }
        else: self.row_attrs = {'new-or-existing':'EXISTING'}

class ExperimentTable(tables.Table):
    _experimentName = tables.LinkColumn('experiment-detail', args=[A('pk')])
    _experimentalDesign =  tables.LinkColumn('exp-designs')

    _comments = tables.TemplateColumn('{{record.comments|slice:":25"}}...')

    class Meta:
        model = Experiment
        fields = ['_experimentName','_projectLead','_teamMembers',
                  '_IRB','_comments','_experimentalDesign',]

    def __init__(self, *args, new_or_existing=None, **kwargs):
        super(ExperimentTable, self).__init__(*args, **kwargs)
        if new_or_existing:
            self.row_attrs = {
                'new-or-existing': lambda record: new_or_existing[record._experimentName]
            }
        else: self.row_attrs = {'new-or-existing':'EXISTING'}

class IndividualTable(tables.Table):
    _individualIdentifier = tables.LinkColumn('individual-detail', args=[A('pk')])
    _experiment = tables.LinkColumn('experiment-detail', args=[A('_experiment.pk')])

    class Meta:
        model = Individual
        exclude = ['_individualID', '_extra_fields']

    def __init__(self, *args, new_or_existing=None, **kwargs):
        super(IndividualTable, self).__init__(*args, **kwargs)
        if new_or_existing:
            self.row_attrs = {
                'new-or-existing': lambda record: new_or_existing[record._individualIdentifier]
            }
        else: self.row_attrs = {'new-or-existing':'EXISTING'}

class QCLabel(tables.Table):
    Quality_Controls = tables.Column()
