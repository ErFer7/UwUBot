# -*- coding: utf-8 -*-

'''
Testes básicos com IA.
'''

from math import exp
from random import random, randint, seed


class Neuron():

    '''
    Neurônio.
    '''

    value: float
    bias: float
    connected_neurons: list
    axons_weight: list

    def __init__(self, connected_neurons: list, axons_weight: list, bias: float):

        self.value = 0.0
        self.bias = bias
        self.connected_neurons = connected_neurons
        self.axons_weight = axons_weight

    def __repr__(self):
        return f"{self.value:.3f}"

    def sigmoid(self, value: float):
        '''
        Sigmoide.
        '''

        return 1 / (1 + exp(-value))

    def input(self, value: float):
        '''
        Entrada do neurônio.
        '''

        self.value = value + self.bias

    def update(self):
        '''
        Atualiza o valor do neurônio.
        '''

        weighted_sum = 0.0

        for i, neuron in enumerate(self.connected_neurons):
            weighted_sum += neuron.value * self.axons_weight[i]

        weighted_sum += self.bias

        self.value = self.sigmoid(weighted_sum)

    def mutate(self, max_step: float):
        '''
        Faz uma mutação no neurônio com base no passo máximo de mutação.
        '''

        self.bias += random() * max_step * -randint(0, 1)

        for i, _ in enumerate(self.axons_weight):
            self.axons_weight[i] += random() * max_step * -randint(0, 1)


class Brain():

    '''
    Cérebro.
    '''

    layers: list
    layer_count: int
    height: int

    def __init__(self):

        self.layers = []
        self.layer_count = 5
        self.height = 11

        self.layers.append([])

        for _ in range(self.height):

            self.layers[0].append(Neuron(None, None, 0.0))

        for i in range(1, self.layer_count):

            self.layers.append([])

            for _ in range(self.height):

                axons_weight = [random() * -randint(0, 1) for _ in range(self.height)]

                self.layers[i].append(Neuron(self.layers[i - 1], axons_weight, 0.0))

    def input(self, values: list):
        '''
        Entrada do cérebro.
        '''

        for i, neuron in enumerate(self.layers[0]):
            neuron.input(values[i])

    def run(self):
        '''
        Executa o cérebro.
        '''

        for i in range(1, self.layer_count):

            for j in range(self.height):

                self.layers[i][j].update()

        result = []

        for j in range(self.height):

            result.append(self.layers[self.layer_count - 1][j].value)

        return result


def string_to_value(string: str):
    '''
    Spring para valor.
    '''

    res = []

    for char in string:
        res.append(ord(char) / 255)

    return res

def value_to_string(values: list):
    '''
    Valor para string.
    '''

    string = ''

    for value in values:
        string += chr(int(value * 255))
    
    return string

# seed(0)

brain = Brain()

string = "Oi, bom dia"

brain.input(string_to_value(string))
res = brain.run()

for layer in brain.layers:
    print(layer)

print(string)
print(value_to_string(res))
