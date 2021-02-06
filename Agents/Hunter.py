import pygame
import random
from Agents.Agent import Agent
from Agents.Prey import Prey

class Hunter(Agent):

    def __init__(self, age, max_age, energy_per_pry_eaten, energy_to_reproduce, energy_level, een_World_object):
        super().__init__(age, max_age, een_World_object)
        # Waarde tussen 0 en 30
        self.energy_per_eaten_pry = energy_per_pry_eaten
        self.start_energy_per_eaten_pry = energy_per_pry_eaten
        # Waarde tussen 0 en 100
        self.energy_level_to_reproduce = energy_to_reproduce
        self.energy_level = energy_level
        self.start_energy_level = energy_level
        self.kleur_hunter = [100, 0, 0]

    def eat(self):
        self.energy_level += self.energy_per_eaten_pry

    def reproduce(self):
        #rand = random.uniform(0, 1)
        if self.energy_level > self.energy_level_to_reproduce:
            self.energy_level -= self.energy_level_to_reproduce
            newHunter_obj = Hunter(age=self.start_age, max_age=self.max_age, energy_per_pry_eaten=self.start_energy_per_eaten_pry, energy_to_reproduce=self.energy_level_to_reproduce, energy_level=self.start_energy_level, een_World_object=self.World)
            self.World.lijstVanAlleAgentsInDeWorld.append(newHunter_obj)

    def die(self):
        self.isAlive = False
        self.World.lijstVanAlleAgentsInDeWorld.remove(self)

    def relative_x_closest_prey(self):
        closestPrey = self.World.dichsteBuur(Agent=self, het_type_agent=Prey)
        return closestPrey.get_x_pos()

    def relative_y_closest_prey(self):
        closestPrey = self.World.dichsteBuur(Agent=self, het_type_agent=Prey)
        return closestPrey.get_y_pos()

    def get_energyLevel(self):
        return self.energy_level

    def step(self):
        dx = random.uniform(-self.speed_X_richting, self.speed_X_richting)
        dy = random.uniform(-self.speed_Y_richting, self.speed_Y_richting)
        if self.isInWindow(dx, dy):
            self.x_pos = self.x_pos + dx
            self.y_pos = self.y_pos + dy
            #self.maakAgentZichtBaarOnScreen()
        self.reproduce()
        dichstePry = self.World.dichsteBuur(Agent=self, het_type_agent=Prey)
        if dichstePry != None:

            if self.afstandTussenDezeAgentEnEenAndere(Agent=dichstePry) <= self.SENSING_RANGE:
                self.eat() # De hunter heeft net een prooi gegeten dus de prooi moet weg.
                #World.dichsteBuur(self.World, self, Prey).die()
                dichstePry.die()
        if self.energy_level <= 0 or self.age >= self.max_age:
            #print("==> energyLevel = ", self.energy_level)
            #print("==> age = ", self.age)
            self.die()
        self.energy_level -= 1
        self.age += 1



    def step_RL(self):
        done = False
        self.reproduce()
        dichstePry = self.World.dichsteBuur(Agent=self, het_type_agent=Prey)
        if dichstePry != None:
            if self.afstandTussenDezeAgentEnEenAndere(Agent=dichstePry) <= self.SENSING_RANGE:
                self.eat()  # De hunter heeft net een prooi gegeten dus de prooi moet weg.
                # World.dichsteBuur(self.World, self, Prey).die()
                dichstePry.die()
        if self.energy_level <= 0 or self.age >= self.max_age:
            self.die()
            done = False
        self.energy_level -= 1
        self.age += 1

        obs = [self.age, self.energy_level, self.relative_x_closest_prey(), self.relative_y_closest_prey()]
        return obs, done








