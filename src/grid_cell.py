from util_main import CLASSINIT,PROCESS,NULL,ERROR,DOCUMENTATION,CONDITION,ErrorModule

class GridCellConfiguration(object):
    """
    Manages the state of an individual cell within the simulation grid.

    This class represents a single cell in the simulation's grid. Each cell has a state that can change based on the environmental conditions, particularly in response to anomalies. The class provides a method to update the cell's state, reflecting changes in the simulation environment.

    Attributes:
        state (str): The current state of the grid cell, typically 'normal' or 'alert'.

    Methods:
        UpdateState(environmentState): Updates the state of the grid cell based on the provided environment state. The state changes to 'alert' during an anomaly and reverts to 'normal' otherwise.
    """
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