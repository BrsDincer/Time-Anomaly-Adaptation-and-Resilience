from util_class import CLASSINIT,ERROR,DOCUMENTATION

class ErrorModule(object):
    def __init__(self)->CLASSINIT:
        self.error = NotImplementedError(NotImplemented)
    def __str__(self)->str:
        return "Error Module - Sub(Script)"
    def __call__(self)->ERROR:
        return self.error
    def __getstate__(self)->ERROR:
        raise self.error
    def __repr__(self)->DOCUMENTATION|str:
        return ErrorModule.__doc__
    @property
    def Default(self)->ERROR:
        raise self.error
    def Manuel(self,errorType:ERROR,errorMessage:str)->ERROR:
        raise errorType(errorMessage)