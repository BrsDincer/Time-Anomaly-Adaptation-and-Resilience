from util_class import PATH,PROCESS
import os

BASEPATH:PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATAPATH:PATH = os.path.join(BASEPATH,"data")

CREATEDIRECTORY:PROCESS = lambda x: os.mkdir(x) if not os.path.exists(x) else None

Sigma:float = 10.0
rho:float = 28.0
Beta:float = 8.0/3.0

def LORENZCALCULATION(currentState:tuple|list,
                      sigma:float or int=Sigma,
                      rho:float or int=rho,
                      beta:float or int=Beta)->PROCESS:
    x,y,z = currentState
    dxdt = sigma * (y-x)
    dydt = x * (rho-z) - y
    dzdt = x * y - beta * z
    return [dxdt,dydt,dzdt]

ScreenSize:int = 400
GridSize:int = 20
CellSize:int = ScreenSize//GridSize
ConstantY:float or int = GridSize//2
OrganismCount:int = 10
BaseProbability:float = 0.02
AlphaValue:float = 0.001
