from util_main import CLASSINIT,PROCESS,DOCUMENTATION,NULL,ERROR,GridSize,ErrorModule
from grid_cell import GridCellConfiguration
import random,time

class SimulationEnvironment(object):
    """
    Manages the simulation environment, including grid configuration, time rate, and anomaly events.

    This class represents the environment in which the organisms exist and interact. It handles the state of the environment, including time rate changes due to anomalies and the Lorenz attractor's influence. The environment is comprised of a grid of cells, each with its own state that can be affected by anomalies.

    Attributes:
        timeRate (int): Represents the rate of time in the simulation environment.
        grid (list): A 2D grid of GridCellConfiguration objects representing the environment.
        anomalyActive (bool): Flag to indicate whether an anomaly is currently active.
        lastAnomalyStartTime (float): Timestamp of the last anomaly's start.

    Methods:
        CreateTimeAnomaly(): Triggers the start of a time anomaly in the environment.
        EndTimeAnomaly(): Ends the currently active time anomaly.
        UpdateGrid(): Updates the state of each cell in the grid based on the current environment state.
        GetGridStates(): Returns the current states of all cells in the grid.
        UpdateFromLorenz(lorenzState): Adjusts the time rate based on the current state of the Lorenz attractor.
    """
    def __init__(self,gridSize:int)->CLASSINIT:
        self.timeRate = 1
        self.grid = [[GridCellConfiguration() for _ in range(GridSize)] for _ in range(GridSize)]
        self.anomalyActive = False
        self.lastAnomalyStartTime = 0
    def __str__(self)->str:
        return "Simulation Environment - Pre(Script)"
    def __call__(self)->NULL|None:
        return None
    def __getstate__(self)->ERROR:
        ErrorModule().Default
    def __repr__(self)->DOCUMENTATION:
        return SimulationEnvironment.__doc__
    def CreateTimeAnomaly(self)->PROCESS:
        self.anomalyActive = True
        self.timeRate = random.choice([0.5,2,-1])
        self.lastAnomalyStartTime = time.time()
        return True
    def EndTimeAnomaly(self)->PROCESS:
        self.anomalyActive = False
        self.timeRate = 1
    def UpdateGrid(self)->PROCESS:
        environmentState = "anomaly" if self.timeRate != 1 else "Normal"
        for row in self.grid:
            for cell in row:
                cell.UpdateState(environmentState=environmentState)
    def GetGridStates(self)->PROCESS:
        return [[cell.state for cell in row] for row in self.grid]
    def UpdateFromLorenz(self,lorenzState:tuple|list)->PROCESS:
        x,_,_ = lorenzState
        self.timeRate = 1 + x / 10