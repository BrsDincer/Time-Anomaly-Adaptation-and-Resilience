from util_main import CLASSINIT,PROCESS,NULL,ERROR,DOCUMENTATION,POINT,ErrorModule
import random

class Organism(object):
    def __init__(self,xPoint:POINT,yPoint:POINT,gridSize:int)->CLASSINIT:
        self.initialX = xPoint
        self.initialY = yPoint
        self.x = xPoint
        self.y = yPoint
        self.gridSize = gridSize
        self.defaultColor = (255,255,255)
        self.memory = []
    def __str__(self)->str:
        return "Organism Class & Parameters - Pre(Script)"
    def __call__(self)->NULL|None:
        return None
    def __getstate__(self)->ERROR:
        ErrorModule().Default
    def __repr__(self)->DOCUMENTATION|str:
        return Organism.__doc__
    def UpdateMemory(self,event:list|str|PROCESS)->PROCESS:
        self.memory.append(event)
        if len(self.memory) > 10:
            self.memory.pop(0)
    def MoveTowardsLine(self,targetY:POINT,probability:float)->PROCESS:
        if (self.y < targetY and random.random() < probability) or \
            (self.y > targetY and random.random() < probability):
                self.y += 1 if self.y < targetY else -1
        else:
            pass
    def ResetCondition(self)->PROCESS:
        self.x = self.initialX
        self.y = self.initialY
    def UpdateColor(self,anomalyActive:bool)->PROCESS:
        self.color = (255,0,0) if anomalyActive else (255,255,255)
    def ChangeColorBasedOnAlignment(self,isAligned:bool)->PROCESS:
        if isAligned:
            self.defaultColor = (0,255,0)
        else:
            self.defaultColor = (255,255,255)
    def ChangeColorBasedOnMemory(self)->PROCESS:
        if "anomaly" in self.memory[-1]:
            self.defaultColor = (0,255,40)
        else:
            self.defaultColor = (255,255,255)
    
        