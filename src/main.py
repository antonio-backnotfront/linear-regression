import csv
import random

import numpy as np
import pandas as pd
from linear_regression import LinearRegression
import matplotlib.pyplot as plt

def main():
    shuffle("data/housing.csv")

    model = LinearRegression()
    with (open("data/housing.csv", "r")) as file:
        lines = file.readlines()
        parameter_names = file.readline()
        model.fit_gradient_descent(list(map(lambda line: line.split(","), lines)), parameter_names)



def shuffle(data_path):

    with (open(data_path, "r") as file):
        parameter_names = file.readline()
        lines = file.readlines()
    random.shuffle(lines)

    with open(data_path, "w") as file:
        file.writelines(parameter_names)
        file.writelines(lines)





if __name__ == "__main__":
    main()