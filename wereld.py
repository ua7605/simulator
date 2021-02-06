import pygame

from Agents.Hunter import Hunter
from Agents.Prey import Prey



class World():
    EXTENDED_RADIUS = 30

    def __init__(self, aantalProoien, aantalHunters):
        # hier wordt de simulatie wereld gemaakt:
        #pygame.init()
        self.isdisplayed = True
        self.aantal_prooien = aantalProoien
        self.aantal_hunters = aantalHunters
        self.lijstVanAlleAgentsInDeWorld = []
        self.kleur_hunter_agent = [100, 0, 0]
        self.kleur_Prooi_agent = [0, 100, 0]
        self.hoogte_scherm = 800#800
        self.breedte_scherm = 800#600


        # Hier worden al de agents aangemaakt (zowel de hunters als de prys).
        for eenprooiaanmaken in range(aantalProoien):
                                        # 0.17                  6
            prooi_agent = Prey(age=0, birth_rate=0.12, max_age=5, een_World_object=self)
        for eenHunteraanmaken in range(aantalHunters):
            een_hunter_agent = Hunter(age=0, max_age=20, energy_per_pry_eaten=15, energy_to_reproduce=30, energy_level=20, een_World_object=self)


    def reset(self):
        self.lijstVanAlleAgentsInDeWorld.clear()
        for eenprooiaanmaken in range(self.aantal_prooien):
            prooi_agent = Prey(age=0, birth_rate=0.12, max_age=5, een_World_object=self)
        for eenHunteraanmaken in range(self.aantal_hunters):
            een_hunter_agent = Hunter(age=0, max_age=20, energy_per_pry_eaten=15, energy_to_reproduce=30, energy_level=20, een_World_object=self)

    def gethoogtescherm(self):
        return self.hoogte_scherm


    def addAgent(self, Agent):
        self.lijstVanAlleAgentsInDeWorld.append(Agent)

    def nearbyAgents(self, Agent):
        # Hier worden alle agent die bij elkaar in de buurt zijn gezocht
        lijstNearAgent = []
        for een_Agent_in_World in self.lijstVanAlleAgentsInDeWorld:                                         # Agent.SENSING_RANGE + self.EXTENDED_RADIUS
            if een_Agent_in_World.isAlive and Agent.afstandTussenDezeAgentEnEenAndere(een_Agent_in_World) <= (Agent.getagentSize()+ self.EXTENDED_RADIUS) and een_Agent_in_World != Agent:
                lijstNearAgent.append(een_Agent_in_World)
        return lijstNearAgent

    def dichsteBuur(self, Agent, het_type_agent):
        dichsteafstand = 10000000000
        buur = None
        # Hier ga de dichste buur gaan zoeken bij een agent die op een straal van SENSING_RANGE ligt.
        for agent_in_lijstnearbyAgents in self.nearbyAgents(Agent):
            if isinstance(agent_in_lijstnearbyAgents, het_type_agent) and Agent.afstandTussenDezeAgentEnEenAndere(agent_in_lijstnearbyAgents) < dichsteafstand:
                buur = agent_in_lijstnearbyAgents
                dichsteafstand = Agent.afstandTussenDezeAgentEnEenAndere(agent_in_lijstnearbyAgents)
        return buur

    def getaantal_prooien(self):
        return self.aantal_prooien
    def getaantal_hunters(self):
        return self.aantal_hunters

    def verhoog_aantal_hunters(self):
        self.aantal_hunters += 1

    def verhoog_aantal_prooien(self):
        self.aantal_prooien += 1










    def display_all_agents_to_screen(self):
        for eenagent in self.lijstVanAlleAgentsInDeWorld:
            eenagent.step()
            if isinstance(eenagent, Hunter):
                eenagent.maakAgentZichtBaarOnScreen()
                self.aantal_hunters += 1
            elif isinstance(eenagent, Prey):
                eenagent.maakAgentZichtBaarOnScreen()
                self.aantal_prooien += 1

    def runSimulationWorld(self):
        t = 0

        while self.aantal_prooien > 0 and self.aantal_hunters > 0:
            self.aantal_hunters = 0
            self.aantal_prooien = 0
            self.display_all_agents_to_screen()
            pygame.display.update()
        print("The simulation is over")








