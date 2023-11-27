from simulation_class import Simulation
from util_main import CREATEDIRECTORY,DATAPATH
import pygame

if __name__ == "__main__":
    CREATEDIRECTORY(DATAPATH)
    pygame.init()
    pygame.display.set_caption("Time-Anomaly Adaptation/Resilience")
    simulation = Simulation()
    simulation.RunSimulation()

    