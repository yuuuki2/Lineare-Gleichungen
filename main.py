import matplotlib.pyplot as plt
import numpy as np

funktion = input("Geben Sie eine Funktion (y = a * x + b) ein: ")

# Split the input string into separate variables
y, rest = funktion.split(" = ")
a, rest = rest.split(" * ")
x, b = rest.split(" + ")

def y(a,x,b):
    new_y = a * x + b

    return new_y

def definitionsmenge():
    d_menge = np.linspace(-10,10,num=20)

    return d_menge








def main():
    pass

