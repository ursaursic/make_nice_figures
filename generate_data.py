# This file produces various types of data
# End goal is to have a numpy array for plotting 

import numpy as np 


def simple_sin_plot(N, omega, noise):
    x = np.linspace(0, 100, N)
    y = np.sin(omega*x) + noise*np.random.random(N)
    return x, y


def simple_exp_plot_data(N, k, noise):
    x = np.linspace(0, 100, N)
    y = np.exp(-x/k) + noise*np.random.random(N)
    return x, y

def simple_histogram_data(N):
    return np.random.random(N)


