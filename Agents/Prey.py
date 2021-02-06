import random

import pygame

from Agents import Hunter
from Agents.Agent import Agent
#from Agents.Hunter import Hunter


class Prey(Agent):

    def __init__(self, age, birth_rate, max_age, een_World_object):
        super().__init__(age, max_age, een_World_object)

        # De birth_rate is een getal dat in percentage wordt uitgedrukt dus is steeds een comma getal.
        self.birth_rate = birth_rate
        self.kleur_prooi = [0, 100, 0]


        # Zorgen dat er een cirkel wordt getoond:
        #self.maakAgentZichtBaarOnScreen()

    def reproduce(self):

        if random.random() <= self.birth_rate:
            # Als hier aan voldaan is wil dat zeggen dat er een pry object op het scherm bij zal moeten worden getoond.
            # -------------> sond self.age
            newPrey = Prey(age=self.start_age, birth_rate=self.birth_rate, max_age=self.max_age, een_World_object=self.World)
            self.World.lijstVanAlleAgentsInDeWorld.append(newPrey)

    def die(self):
        self.alive = False
        self.World.lijstVanAlleAgentsInDeWorld.remove(self)


    def relative_x_closest_hunter(self):
        closestHunter = self.World.dichsteBuur(Agent=self, het_type_agent=Hunter)
        return closestHunter.get_x_pos()


    def relative_y_closest_hunter(self):
        closestHunter = self.World.dichsteBuur(Agent=self, het_type_agent=Hunter)
        return closestHunter.get_y_pos()

    def step(self):
        self.age += 1
        dx = random.uniform(-self.speed_X_richting, self.speed_X_richting)
        dy = random.uniform(-self.speed_Y_richting, self.speed_Y_richting)
        if self.isInWindow(dx, dy):
            self.x_pos = self.x_pos + dx
            self.y_pos = self.y_pos + dy
            # Hier nbij met je wel nog gaan op passen dat de vorige cirkel verewijderd wordt.
            #self.maakAgentZichtBaarOnScreen()
        self.reproduce()
        if self.age >= self.max_age:
            #print("konijn gaat dood op age: ",self.age)
            self.die()

    def step_RL(self):
        self.age += 1
        self.reproduce()
        if self.age >= self.max_age:
            #print("konijn gaat dood op age: ",self.age)
            self.die()

    def stepRL(self, action):
        [up, down, left, right] = action
        x = left + right
        y = up + down
        self.age += 1
        done = False
        if self.isInWindow(x, y):
            self.x_pos += x
            self.y_pos += y
        self.reproduce()
        if self.age >= self.max_age:
            self.die()
            done = True
        obs = [self.age, self.relative_x_closest_hunter(), self.relative_y_closest_hunter()]
        return obs, done

        # Observatie van Prey = [age, relative x closest hunter, relative y closest hunter]



















