import numpy as np
import math

def sigmoidDerivative(x):
    fx = sigmoid(x)
    return fx * (1 - fx)
