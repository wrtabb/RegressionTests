
from numpy import sin
from numpy import arange
import matplotlib.pyplot as plt
import random

def function_true(x):
    return (sin(x) + sin((10.0/3.0)*x))**2

def generate_data():
    xmin, xmax = 0.0, 3.5
    print(f"Setting xmin to {xmin}; setting xmax to {xmax}")

    inputs = arange(xmin,xmax,0.01)
    results = function_true(inputs)
    plt.plot(inputs,results)
    save_name_true = "true_fuction.png"
    plt.savefig(save_name_true)
    print(f"Saved function plot as {save_name_true}")

    num = random.uniform(xmin,xmax)
    print("Random number =",num)
    return num

generate_data()
