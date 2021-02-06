# De klasse Simulator: Deze klasse houdt het aantal tijdstappen bij en voert de step
# methodes van elke agent uit.
import time

import pygame

from Agents.Hunter import Hunter
from Agents.Prey import Prey
from Model import Model


class Simulator():
    def __init__(self, wereld_object):
        pygame.init()
        self.Wereld = wereld_object
        self.Model = Model(wereld_object)
        self.BREEDTE = 800
        self.HOOGTE = 800
        #self.screen = pygame.display.set_mode((self.BREEDTE, self.HOOGTE))
        self.clock = pygame.time.Clock()
        self.achtergrond = [0, 0, 0]
        self.tijdstap = 0
        self.screen = pygame.display.set_mode((self.BREEDTE, self.HOOGTE))
        self.screenTitle = pygame.display.set_caption("Vincent Simulator")
        self.lijst_Prey_agents_in_wereld = []
        self.lijst_Hunter_agents_in_wereld = []

    def display_all_agents_to_screen(self):
        for eenagent in self.Wereld.lijstVanAlleAgentsInDeWorld:
            if isinstance(eenagent, Hunter):
                pygame.draw.circle(self.screen, eenagent.kleur_hunter, (int(eenagent.x_pos), int(eenagent.y_pos)), eenagent.size)
                self.aantal_hunters += 1
            elif isinstance(eenagent, Prey):
                pygame.draw.circle(self.screen, eenagent.kleur_prooi, (int(eenagent.x_pos), int(eenagent.y_pos)), eenagent.size)
                self.aantal_prooien += 1
            eenagent.step()

    def preys_RL_step(self):
        for een_agent_object in self.Wereld.lijstVanAlleAgentsInDeWorld:
            if isinstance(een_agent_object, Prey):
                een_agent_object.step_RL()

    def predators_RL_step(self):
        for een_agent_object in self.Wereld.lijstVanAlleAgentsInDeWorld:
            if isinstance(een_agent_object, Hunter):
                een_agent_object.step_RL()

    def preys_step(self):
        for eenagent in self.Wereld.lijstVanAlleAgentsInDeWorld:
            if isinstance(eenagent, Prey):
                eenagent.step()

    def predator_step(self):
        for eenagent in self.Wereld.lijstVanAlleAgentsInDeWorld:
            if isinstance(eenagent, Hunter):
                eenagent.step()

    def runSimulationWorld(self):

        running = True
        plot = True

        while running:
            if self.Wereld.getaantal_prooien() > 0 and self.Wereld.getaantal_hunters() > 0:

                #self.Wereld.reset()
                self.aantal_hunters = 0
                self.aantal_prooien = 0
                self.Model.showAmountOfAgentsInWorld(self.tijdstap)
                self.display_all_agents_to_screen()

                if len(self.Wereld.lijstVanAlleAgentsInDeWorld) == 0 or (self.Model.totaal_aantal_hunters_in_World() == 0 and self.Model.totaal_aantal_preys_in_World() >= 0)  and plot:
                    print("je bent hier geweest voor de plot")
                    plot = False
                    self.Model.showPlot()
                    running = False
            else:
                # hier kom ik nog niet doordat de getaantal prooien nog niet op punt staat wordt nog niet ge-update
                if len(self.Wereld.lijstVanAlleAgentsInDeWorld) == 0 and not plot:
                    running = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.tijdstap += 1
            pygame.display.update()
            self.screen.fill(self.achtergrond)
            time.sleep(1)

        print("The simulation is over")








    def voer_step_agent_uit(self, Agent):
        Agent.step()