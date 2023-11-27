from util_main import CLASSINIT,PROCESS,NULL,ERROR,DOCUMENTATION,CONDITION,ErrorModule

class GridCellConfiguration(object):
    def __init__(self)->CLASSINIT:
        self.state = "Normal"
    def __str__(self)->str:
        return "Grid Cell Configuration - Pre(Script)"
    def __call__(self)->NULL|None:
        return None
    def __getstate__(self)->ERROR:
        ErrorModule().Default
    def __repr__(self)->DOCUMENTATION|str:
        return GridCellConfiguration.__doc__
    def UpdateState(self,environmentState:CONDITION|str)->PROCESS:
        if environmentState == "anomaly":
            self.state = "alert"
        else:
            self.state = "normal"