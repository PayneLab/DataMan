LOGS_FOLDER = 'logs/'

LOGGING = {
	'version':1,
	'disable_existing_loggers': False,
	'formatters':{
		'large':{
			'format':'%(asctime)s  %(levelname)s  %(process)d  %(pathname)s  %(funcName)s  Line %(lineno)d  %(message)s  '
		},
		'tiny':{
			'format':'%(asctime)s  %(message)s  '
		}
	},
	'handlers':{
		'errors_file':{
			'level':'ERROR',
		       'class':'logging.handlers.TimedRotatingFileHandler',
			'when':'midnight',
			'interval':1,
			'filename':LOGS_FOLDER+'ErrorLoggers.log',
			'formatter':'large',
		},
		'info_file':{
			'level':'INFO',
		       'class':'logging.handlers.TimedRotatingFileHandler',
			'when':'midnight',
			'interval':1,
			'filename':LOGS_FOLDER+'InfoLoggers.log',
			'formatter':'large',
		},
		'debug_file':{
			'level':'DEBUG',
		       'class':'logging.handlers.TimedRotatingFileHandler',
			'when':'midnight',
			'interval':1,
			'filename':LOGS_FOLDER+'DebugLoggers.log',
			'formatter':'large',
		},
        'request_handler': {
                'level':'DEBUG',
                'class':'logging.handlers.RotatingFileHandler',
                'filename': LOGS_FOLDER+'django_request.log',
                'formatter':'large',
		},
        'default_file': {
                'level':'DEBUG',
                'class':'logging.handlers.RotatingFileHandler',
                'filename': LOGS_FOLDER+'AutoInfoDebugLog.log',
                'formatter':'large',
		},
	},
	'loggers':{
		'error_logger':{
			'handlers':['errors_file'],
			'level':'ERROR',
			'propagate':False,
		},
		'django.request': {
			'handlers': ['errors_file','request_handler'],
			'propagate': False
		},
		'debug_logger':{
			'handlers':['debug_file'],
			'level':'DEBUG',
			'propagate':True,
		},
		'info_logger':{
			'handlers':['info_file'],
			'level':'INFO',
			'propagate':True,
		},

        '': {
            'handlers': ['default_file'],
            'level': 'DEBUG',
            'propagate': False
        },
	},
}
