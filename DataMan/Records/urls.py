"""Project DataMan

These define the urls that can be accessed
from the main website url. The view function
handling it is stated along with a page name
that the path can be accessed by."""

#These will be the url patterns for the records app
#Which keeps track of the records (Patient, Sample, Dataset, Experiments)

from django.urls import path
from . import views

views.start_job()

urlpatterns = [
    path('', views.records, name = 'records'),

	#upload pages
    path('upload/', views.upload, name = 'upload'),
    path('upload/confirm', views.upload_confirm, name = 'upload_confirm'),

	#backup page; under development
	path('backup/', views.backup, name='backup'),

	#successful entry/upload page
	path('success/', views.success, name='success'),
	path('response/', views.success, name='response'),

    #add pages with form
	path('about/', views.about, name='about'),
    path('add/', views.create_new, name = 'create-new'),
    path('add/samples/', views.add_sample, name = 'add-sample'),
    path('add/samples/<int:experiment>', views.add_sample, name = 'add-samples'),
    path('add/datasets/', views.add_dataset, name = 'add-dataset'),
    path('add/datasets/<int:experiment>', views.add_dataset, name = 'add-dataset'),
    path('add/individual/', views.add_individual, name = 'add-individual'),
    path('add/individual/<int:experiment>', views.add_individual, name = 'add-individual'),
    path('add/experiments/', views.add_experiment, name = 'add-experiment'),

	#for editing
    path('add/experiments/<int:pk>/', views.edit_experiment, name = 'edit-experiment'),
    path('add/individual/<int:pk>/', views.edit_individual, name = 'edit-individual'),
    path('add/samples/<int:pk>/', views.edit_sample, name = 'edit-sample'),
    path('add/datasets/<int:pk>/', views.edit_dataset, name = 'edit-dataset'),

    path('add/instrument/', views.add_instrument, name = 'add-instrument'),
    path('add/instrument-setting/', views.add_instrument_setting, name = 'add-instrument-setting'),
    path('add/protocol/', views.add_protocol, name = 'add-protocol'),
    path('add/file-status/', views.add_file_status, name = 'add-file-status'),
    path('add/experimental-design/', views.add_experimental_design, name = 'add-experimental-design'),


    path('add/instrument/<str:pk>', views.add_instrument, name = 'add-instrument'),
    path('add/instrument-setting/<str:pk>', views.add_instrument_setting, name = 'add-instrument-setting'),
    path('add/protocol/<str:pk>', views.add_protocol, name = 'add-protocol'),
    path('add/file-status/<str:pk>', views.add_file_status, name = 'add-file-status'),
    path('add/experimental-design/<str:pk>', views.add_experimental_design, name = 'add-experimental-design'),

    path('archive/', views.archive, name = 'archive'),
    path('samples/', views.SampleView.as_view(), name = 'samples'),
	#filtered by experiment
    path('samples/<int:experiment>', views.SampleView.as_view(), name = 'samples'),
    path('datasets/', views.DatasetView.as_view(), name = 'datasets'),
    path('individuals/', views.IndividualView.as_view(), name = 'individuals'),
    path('experiments/', views.ExperimentView.as_view(), name = 'experiments'),

    path('instruments/', views.InstrumentView.as_view(), name = 'instruments'),
    path('settings/', views.SettingsView.as_view(), name = 'settings'),
    path('protocols/', views.ProtocolView.as_view(), name = 'protocols'),
    path('experiment-designs/', views.ExpDesignView.as_view()),
    path('exp-designs/', views.ExpDesignView.as_view()),
    path('experimental-designs/', views.ExpDesignView.as_view(), name = 'exp-designs'),

    path('samples/<int:pk>/', views.SampleDetailView.as_view(),
         name = 'sample-detail'),
    path('datasets/<int:pk>/', views.DatasetDetailView.as_view(),
         name = 'dataset-detail'),
    path('experiments/<int:pk>/', views.ExperimentDetailView.as_view(),
         name = 'experiment-detail'),
    path('individuals/<int:pk>/', views.IndividualDetailView.as_view(),
         name = 'individual-detail'),
]
