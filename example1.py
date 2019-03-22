import numpy as np
from unfolding_tool import unfold
from plotter import plotit


# load in the data
responses = np.load('data/response0.npy')
errors = np.load('data/error0.npy')
response_functions = np.load('data/rfs.npy')
true_solution = np.load('data/ds0.npy')

# unknown default spectrum
default_spectrum = (np.ones(len(true_solution)) / len(true_solution)) * np.sum(true_solution)


# unfold
params = {'Omega': 8, 'max_iter': 200, 'tol': 1E-4}
maxed_solution = unfold(responses, errors, response_functions, default_spectrum, method='MAXED', params=params)
gravel_solution = unfold(responses, errors, response_functions, default_spectrum, method='Gravel', params=params)

# plot the solutions
plotit(default_spectrum, maxed_solution, true_solution, 'MAXED')
plotit(default_spectrum, gravel_solution, true_solution, 'Gravel')
