
# De environment klasse deze houdt referenties bij naar alle agents in de simulator.
# De environment klasse bevat verder ook de functionaliteit om na te gaan welke agents zich in de buurt van een bepaalde locatie bevinden.

import ray.rllib
import gym


# Dit is nodig om het expliciet gemoduleerd gedrag van de prooi te vervangen door een RL agent die
# die zelf zal leren om acties te nemen op basis van zijn observaties.
from Agents.Prey import Prey
from Simulator import Simulator
from wereld import World


class PreyEnvironment(gym.Env):
    def __init__(self,env_config):
        self.aantal_Preys = 80
        self.aantal_agents = 10
        self.num_actions = 4

        self.action_space = (self.aantal_agents, self.num_actions)
        # vier observaties voor de
        self.observation_space = (self.aantal_agents, 3)
        self.simulator = Simulator(World(aantalProoien=self.aantal_Preys, aantalHunters=self.aantal_agents))

        self.agents_to_index = {"agent " + str(i + 1): i for i in range(self.aantal_agents)}

    def reset(self):
        self.simulator.Wereld.reset()
        pass

    # De step methode returned observaties, rewards en done. Deze data dient in een
    # Python dict datastructuur aangeboden te worden.
    def step(self, action):
        lijst_Prey_agents = []
        for een_agent_object in self.simulator.Wereld.lijstVanAlleAgentsInDeWorld:
            if isinstance(een_agent_object, Prey):
                lijst_Prey_agents.append(een_agent_object)
        for prey in lijst_Prey_agents:
            prey.action_from_RL_step(action)# de action die van de RL zal komen.

        self.simulator.preys_RL_step()

        self.simulator.predator_step()

        obs = self.get_observation()
        obs = self.create_dictionary(obs)
        return obs

        #return <obs>, <reward: float>, <done: bool>
    def create_dictionary(self, data):
        return {key: data[val] for key, val in self.agents_to_index.items()}

    def get_observation(self):
        obs_batch = []
        lijst_Prey_agents = []
        for een_agent_object in self.simulator.Wereld.lijstVanAlleAgentsInDeWorld:
            if isinstance(een_agent_object, Prey):
                lijst_Prey_agents.append(een_agent_object)
        for prey in lijst_Prey_agents:
            obs = [prey.get_age(), prey.relative_x_closest_hunter(), prey.relative_y_closest_hunter()]
            obs_batch.append(obs)
        return obs_batch

    def check_dones(self):
        lijst_Prey_agents = []
        for een_agent_object in self.simulator.Wereld.lijstVanAlleAgentsInDeWorld:
            if isinstance(een_agent_object, Prey):
                lijst_Prey_agents.append(een_agent_object)
        if len(lijst_Prey_agents) == 0:
            dones = {'__all__': True}
        else:
            dones = {'__all__': False}

        return dones





