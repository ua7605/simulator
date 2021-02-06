
# De environment klasse deze houdt referenties bij naar alle agents in de simulator.
# De environment klasse bevat verder ook de functionaliteit om na te gaan welke agents zich in de buurt van een bepaalde locatie bevinden.

import ray.rllib
import gym

from Agents.Hunter import Hunter
from Simulator import Simulator
from wereld import World


class PredatorEnvironment(gym.Env):
    def __init__(self,env_config):
        self.aantal_Preys = 80
        self.aantal_agents = 10

        # Er zijn vijf mogelijke acties: [up, down, left, right, reproduce if possible]
        self.num_actions = 5
        self.action_space = (self.aantal_agents, self.num_actions)

        # vier observaties voor de preditor agent:  [age, energy, relative x closest prey, relative y closest prey]
        self.observation_space = (self.aantal_agents, 4)
        self.simulator = Simulator(World(aantalProoien=80, aantalHunters=10))

        # Dit zal wel moeten worden geupdated na iedere tijdstap omdat het aantal agents doorheen het spel niet constant is.
        self.agents_to_index = {"Agent " + str(i + 1 ): i for i in range(self.aantal_agents)}

    def reset(self):
        self.simulator.Wereld.reset()
        pass

    # De step methode returned observaties, rewards en done. Deze data dient in een
    # Python dict datastructuur aangeboden te worden.
    # action is een dictionary die voor elke agent zijn actie gaat bevatten
    # vier mogelijke moves : [up = 0, down = 1, left = 2, right = 3]
    def step(self, action):
        lijst_Hunter_agents = []
        for een_agent_object in self.simulator.Wereld.lijstVanAlleAgentsInDeWorld:
            if isinstance(een_agent_object, Hunter):
                lijst_Hunter_agents.append(een_agent_object)
        for predator in lijst_Hunter_agents:
            predator.action_from_RL_step(action)

        # Call explicit step method for all hunters
        self.simulator.predators_RL_step()

        self.simulator.preys_step()

        obs = self.get_observation()
        obs = self.create_dictionary(obs)

        dones = self.check_dones()
        # Create new predators
        return obs # ,rewards, dones, infos

    def create_dictionary(self, data):
        return {key: data[val] for key, val in self.agents_to_index.items()}

    # De observaties gaan bepalen voor de predator
    def get_observation(self):
        lijst_Hunter_agents = []
        for een_agent_object in self.simulator.Wereld.lijstVanAlleAgentsInDeWorld:
            if isinstance(een_agent_object, Hunter):
                lijst_Hunter_agents.append(een_agent_object)
        obs_batch = []
        for predator in lijst_Hunter_agents:
            obs = [predator.get_age(), predator.get_energyLevel(), predator.relative_x_closest_prey(), predator.relative_y_closest_prey()]
            obs_batch.append(obs)
        return obs_batch

    def check_dones(self):
        lijst_Hunter_agents = []
        for een_agent_object in self.simulator.Wereld.lijstVanAlleAgentsInDeWorld:
            if isinstance(een_agent_object, Hunter):
                lijst_Hunter_agents.append(een_agent_object)
        if len(lijst_Hunter_agents) == 0:
            dones = {'__all__': True}
        else:
            dones = {'__all__': False}
        return dones