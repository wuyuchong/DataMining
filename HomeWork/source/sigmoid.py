import numpy as np
import math

def sigmoid(Xi, thetas):
    params = - np.sum(Xi * thetas)
    outcome = 1 /(1 + math.exp(params))
    return outcome
