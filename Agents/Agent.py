# De Agent klasse: Deze klasse bevat een step methode die voor 1-stap het gedrag van een bepaalde agent beschrijft.
# Verder bevat deze klasse properties die de state van de agent beschrijven. De step-methode zal in staat zijn om de properties
# van zichzelf aan te passen maar ook om de properties van andere agents aan te passen.
# Om te interageren met de andere agents bevat de Agent klasse ook een referentie naar de environment klasse.
# Via deze environment klasse kan de Agent opvragen welke agents er in de buurt zijn.
import random
from abc import ABC, abstractmethod

import pygame




class Agent():
    SIZE = 5
    SENSING_RANGE = 20
    def __init__(self, age, max_age, een_World_object):


        # De agent krijgt de wereld mee waar hij in gaat werken.
        self.World = een_World_object
        # Hierdoor weet de wereld hoeveel agents er op elk ogenblik in de werkeld zijN
        self.World.addAgent(self) # Dit is zeer belangerijk dat dit wordt uitgevoerd zo weet de world steeds hoeveel agents er in zijn world zijn.


        self.age = age
        self.start_age = age
        #self.energy_level = energy_level

        # De positie in het speel veld
        self.x_pos = random.randrange(start=0, stop=self.World.breedte_scherm)
        self.y_pos = random.randrange(start=0, stop=self.World.hoogte_scherm)

        self.max_age = max_age

        # Waardes voor de snelheid van beweging:
        self.speed_X_richting = 4
        self.speed_Y_richting = 4

        # vermenigvuldiging snelheid:
        self.reproduction = 0.02
        self.size = self.SIZE

        self.isAlive = True

    def getagentSize(self):
        return self.size

    def get_age(self):
        return self.age

    def maakAgentZichtBaarOnScreen(self):
        pass
    def eat(self):
        pass

    def reproduce(self):
        pass

    def die(self):
        pass

    def step_RL(self):
        pass
    def step(self):
        pass

    def get_x_pos(self):
        return self.x_pos

    def get_y_pos(self):
        return self.y_pos



    def action_from_RL_step(self, action):
        to_x = None
        to_y = None
        # naar boven:
        if action == 0:
            to_x = 0
            to_y = 0

        # naar rechts
        elif action == 1:
            to_x = 1
            to_y = 0

        # naar onder
        elif action == 2:
            to_x = 0
            to_y = -1

        # naar links
        elif action == 3:
            to_x = -1
            to_y = 0

        elif action == 4:
            self.reproduce()

        if action != 4:
            dx = self.x_pos + to_x
            dy = self.y_pos + to_y
            if self.isInWindow(dx=dx, dy=dy):
                self.x_pos = dx
                self.y_pos = dy






    def isInWindow(self, dx, dy):
        tx = self.x_pos + dx
        ty = self.y_pos + dy
        if self.size / 2 < tx < self.World.breedte_scherm - self.size / 2 and self.size/2 < ty < self.World.hoogte_scherm - self.size / 2:
            return True
        else:
            return False

    def afstandTussenDezeAgentEnEenAndere(self, Agent):
        # Deze method gaat zeggen hoe ver deze agent ligt van een andere agent die is opgegeven:
        # Dit kan je snel doen door de stelling van pytagoras te gaan toepassen:
        return ((self.x_pos - Agent.x_pos)**2 + (self.y_pos - Agent.y_pos)**2)**0.5
