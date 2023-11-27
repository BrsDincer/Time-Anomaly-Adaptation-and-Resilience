from util_main import CLASSINIT,PROCESS,DOCUMENTATION,NULL,ERROR,GridSize,ErrorModule
from grid_cell import GridCellConfiguration
import random,time

class SimulationEnvironment(object):
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