# De klasse Model: Deze bevat referenties naar alle agents van een bepaalde type (bijvoorbeeld HunterModel).
# De model klasse kan gebruikt worden om statistieken op te vragen van een bepaald type agent.
# Bijvoorbeeld het aantal prooi agents actief in de simulatie. Verder kan het gebruikt worden om agents in de simulator aan te maken en te verwijderen.
from Agents.Hunter import Hunter
from Agents.Prey import Prey
import matplotlib.pyplot as plt

class Model():
    def __init__(self, World_object):
        self.World = World_object
        self.lijst_totaal_aantal_Prey_agents_geweest = []
        self.lijst_totaal_aantal_Hunters_agents_geweest = []


    def totaal_aantal_hunters_in_World(self):
        return len(self.lijst_totaal_aantal_Hunters_agents_geweest)

    def totaal_aantal_preys_in_World(self):
        return len(self.lijst_totaal_aantal_Prey_agents_geweest)

    def showAmountOfAgentsInWorld(self, timestep):
        lijst_Prey_agents = []
        lijst_Hunter_agents = []
        for een_agent_object in self.World.lijstVanAlleAgentsInDeWorld:
            if isinstance(een_agent_object, Prey):
                lijst_Prey_agents.append(een_agent_object)

            elif isinstance(een_agent_object, Hunter):
                lijst_Hunter_agents.append(een_agent_object)
        self.lijst_totaal_aantal_Prey_agents_geweest.append(len(lijst_Prey_agents))
        self.lijst_totaal_aantal_Hunters_agents_geweest.append(len(lijst_Hunter_agents))

        print("---------------STATS_SIMULATOR_PREY_HUNTER---------------")
        print("- timestep: ", timestep)
        print("- # preys:   ", len(lijst_Prey_agents))
        print("- # Hunters: ", len(lijst_Hunter_agents))
        print("---------------------------------------------------------")
        print("")
    def showPlot(self):
        plt.title(" Prey populatie en Hunter populatie")
        plt.xlabel("# tijdstappen")
        plt.ylabel("# agents in de wereld")
        #plt.hist(self.lijst_totaal_aantal_Prey_agents_geweest)
        plt.plot(self.lijst_totaal_aantal_Prey_agents_geweest)
        plt.plot(self.lijst_totaal_aantal_Hunters_agents_geweest)
        plt.show()


















