# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import random

import pygame

from Simulator import Simulator
from wereld import World

if __name__ == '__main__':
                            # 80                    # 10
    wereld_object = World(aantalProoien=70, aantalHunters=10)
    simulator = Simulator(wereld_object=wereld_object)
    simulator.runSimulationWorld()