"""Project DataMan
    Custom exceptions
    """

class UploadMissingFieldError(Exception):
    #When worklists are uploaded, there
    #may be missing fields. This error
    #type will flag the fatal missing fields.
    def __init__(self, msg="Your file is missing information."):
        super(UploadMissingFieldError, self).__init__(msg)
