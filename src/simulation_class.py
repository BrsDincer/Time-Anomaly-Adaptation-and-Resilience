from util_main import CLASSINIT,PROCESS,NULL,LORENZCALCULATION,DATAPATH,DOCUMENTATION,ERROR,CellSize,OrganismCount,ConstantY,ScreenSize,BaseProbability,AlphaValue,GridSize,ErrorModule
from environment_class import SimulationEnvironment
from collector_class import DataCollector
from organism_class import Organism
import random,pygame,time,os,pandas as pd
from scipy.integrate import odeint

class Simulation(object):
    """
    Manages and runs a dynamic ecosystem simulation inspired by concepts from chaos theory and adaptive learning.

    This class encapsulates the entire simulation environment, including the Lorenz attractor for modeling chaotic dynamics, an array of organisms with adaptive behaviors, and mechanisms for anomaly detection and response. It provides functionalities to run simulation iterations, draw the environment and organisms, and collect data for analysis.

    Attributes:
        environment (SimulationEnvironment): The simulation's environment, handling grid and anomaly states.
        dataCollector (DataCollector): Responsible for collecting and processing simulation data.
        organisms (list): A list of Organism objects representing entities in the simulation.
        anomalyCooldown (int): Cooldown counter to control the frequency of anomalies.
        screen (pygame.Surface): Pygame surface for rendering the simulation.
        font (pygame.font.Font): Font used for rendering text in the simulation.
        resilienceFactor (float): Represents the adaptive resilience factor of organisms.
        anomalyDuration (float): Duration of the current or last anomaly.
        lineFormationCount (int): Counter for successful line formations by organisms.
        formationData (list): Data collected about line formations and other stats.
        initialState (list): Initial state for the Lorenz attractor calculations.
        lorenzState (float): Current state of the Lorenz attractor.
        t (float): Time variable for Lorenz attractor calculations.

    Methods:
        CheckLineFormation(): Checks if organisms are aligned in a line.
        SaveData(): Saves the collected data into a DataFrame.
        RunIteration(): Executes one iteration of the simulation.
        DrawGridAndOrganism(): Renders the grid and organisms on the screen.
        DrawText(): Displays text information on the screen.
        RunSimulation(): Runs the main simulation loop.
    """
    def __init__(self)->CLASSINIT:
        self.environment = SimulationEnvironment(GridSize)
        self.dataCollector = DataCollector()
        self.organisms = [Organism(random.randint(0,GridSize-1),random.randint(0,GridSize-1),GridSize) for _ in range(OrganismCount)]
        self.anomalyCooldown = 1
        self.screen = pygame.display.set_mode((ScreenSize,ScreenSize+95))
        self.font = pygame.font.Font(None,20)
        self.resilienceFactor = 0 #R(t)
        self.anomalyDuration = 0
        self.lineFormationCount = 0
        self.formationData = []
        self.initialState = [1.0,1.0,1.0]
        self.lorenzState = 0
        self.t = 0.0
    def __str__(self)->str:
        return "Simulation Base - Pre(Script)"
    def __call__(self)->NULL|None:
        return None
    def __getstate__(self)->ERROR:
        ErrorModule().Default
    def __repr__(self)->DOCUMENTATION|str:
        return Simulation.__doc__
    def CheckLineFormation(self)->bool:
        return all(organism.y == ConstantY for organism in self.organisms)
    def SaveData(self)->PROCESS:
        return pd.DataFrame(
                self.formationData,
                columns=["Resilience","Anomaly Duration","Probability","Initial Probability","Alpha","Organism Count","Lorenz State"]
            )
    def RunIteration(self)->PROCESS:
        currentTime = time.time()
        self.anomalyDuration = currentTime - self.environment.lastAnomalyStartTime if self.environment.lastAnomalyStartTime else 0
        anomalyTriggered = self.environment.anomalyActive
        self.lorenzState = odeint(LORENZCALCULATION,self.initialState,[self.t,self.t+0.01])[-1]
        self.t += 0.01
        self.resilienceFactor += 1 if anomalyTriggered else 0
        probability = BaseProbability + (AlphaValue * self.resilienceFactor) * abs(self.lorenzState[0])
        if (self.anomalyCooldown <= 0 and random.random() < 0.1): #10% chance
            if self.environment.anomalyActive:
                self.environment.EndTimeAnomaly()
                self.anomalyCooldown = 1 #1 iterations cooldown
            else:
                self.environment.CreateTimeAnomaly()
                self.anomalyCooldown = 1 #1 iterations cooldown
        else:
            pass
        self.anomalyCooldown = max(0,self.anomalyCooldown-1)
        self.environment.UpdateGrid()
        self.dataCollector.CollectData(self.environment.timeRate)
        for org in self.organisms:
            if anomalyTriggered:
                org.ResetCondition()
                org.UpdateMemory("anomaly")
                org.ChangeColorBasedOnMemory()
            else:
                org.MoveTowardsLine(ConstantY,probability)
                org.UpdateMemory("normal")
                org.ChangeColorBasedOnMemory()
                formationBool = self.CheckLineFormation()
                if formationBool:
                    self.lineFormationCount += 1
                    self.formationData.append(
                            [
                                str(self.resilienceFactor),
                                str(self.anomalyDuration),
                                str(round(BaseProbability + AlphaValue * self.resilienceFactor,5)),
                                str(BaseProbability),
                                str(AlphaValue),
                                str(OrganismCount),
                                str(self.lorenzState[0])
                                ]
                        )
                    org.ResetCondition()
    def DrawGridAndOrganism(self)->PROCESS:
        for x in range(0,ScreenSize,CellSize):
            pygame.draw.line(self.screen,(180,180,180),(x,0),(x,ScreenSize))
        for y in range(0,ScreenSize,CellSize):
            pygame.draw.line(self.screen,(180,180,180),(0,y),(ScreenSize,y))
        for org in self.organisms:
            pygame.draw.circle(self.screen,org.defaultColor,(org.x*CellSize+CellSize//2,org.y*CellSize+CellSize//2),CellSize//3)
    def DrawText(self,text:str,textPosition:tuple)->PROCESS:
        testSurface = self.font.render(text,True,(255,255,255))
        self.screen.blit(testSurface,textPosition)
    def RunSimulation(self):
        running = True
        clock = pygame.time.Clock()
        timeNow = time.time()
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    if len(self.formationData) > 0:
                        dataFrame = self.SaveData()
                        savePath = os.path.join(DATAPATH,"lineformationdata.csv")
                        dataFrame.to_csv(savePath)
                    running = False
            self.screen.fill((10,10,10))
            self.RunIteration()
            self.DrawGridAndOrganism()
            passTime = time.time() - timeNow
            self.DrawText(text=f"Resilience Factor: {self.resilienceFactor}",
                          textPosition=(10,ScreenSize+15))
            self.DrawText(text=f"Probability: {BaseProbability + AlphaValue * self.resilienceFactor:.4f}",
                          textPosition=(10,ScreenSize+35))
            self.DrawText(text=f"Anomaly Duration: {self.anomalyDuration:.4f}",
                          textPosition=(10,ScreenSize+55))
            self.DrawText(text=f"Total-Elapsed Time: {passTime:.4f}",
                          textPosition=(218,ScreenSize+15))
            self.DrawText(text=f"Successful Line Form: {self.lineFormationCount}",
                          textPosition=(218,ScreenSize+35))
            self.DrawText(text=f"Lorenz State: {round(self.lorenzState[0],3)}",
                          textPosition=(218,ScreenSize+55))
            pygame.display.flip()
            clock.tick(20)
        pygame.quit()
        
        

        
            
        