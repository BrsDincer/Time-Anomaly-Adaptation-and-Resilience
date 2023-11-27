from util_main import CLASSINIT,PROCESS,NULL,ERROR,DOCUMENTATION,POINT,ErrorModule
import random

class Organism(object):
    """
    Represents an organism within a dynamic simulation environment.

    The Organism class models the behavior and state of an individual organism in a simulated ecosystem. Each organism has a position, represented by x and y coordinates, and can move within a grid of a specified size. Organisms have the ability to remember past events, adapt their behavior based on these memories, and change color based on specific conditions.

    Attributes:
        initialX (POINT): The initial x-coordinate of the organism.
        initialY (POINT): The initial y-coordinate of the organism.
        x (POINT): The current x-coordinate of the organism.
        y (POINT): The current y-coordinate of the organism.
        gridSize (int): The size of the grid within which the organism moves.
        defaultColor (tuple): The default color of the organism.
        memory (list): A list representing the organism's memory of past events.

    Methods:
        UpdateMemory(event): Records a new event in the organism's memory.
        MoveTowardsLine(targetY, probability): Moves the organism towards a specified line based on a probability.
        ResetCondition(): Resets the organism's position to its initial coordinates.
        UpdateColor(anomalyActive): Changes the organism's color based on anomaly activity.
        ChangeColorBasedOnAlignment(isAligned): Changes the organism's color if it is aligned with others.
        ChangeColorBasedOnMemory(): Changes the organism's color based on its recent memory, specifically in response to anomalies.
    """
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
    
        