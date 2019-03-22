import numpy as np
from unfolding_tool import unfold
from plotter import plotit


# load in the data
group_structure = np.load('data/struct.npy')
responses = np.load('data/response2.npy')
errors = np.load('data/error2.npy')
response_functions = np.load('data/rfs.npy')
true_solution = np.load('data/ds2.npy')

# default spectrum off by value of one half
default_spectrum = np.load('data/ds0.npy')

# unfold with maxed
params = {'Omega': 8, 'max_iter': 200, 'tol': 1E-4}
maxed_solution = unfold(responses, errors, response_functions, default_spectrum, method='MAXED', params=params)
gravel_solution = unfold(responses, errors, response_functions, default_spectrum, method='Gravel', params=params)

# plot the solutions
plotit(default_spectrum, maxed_solution, true_solution, 'MAXED')

plotit(default_spectrum, gravel_solution, true_solution, 'Gravel')
