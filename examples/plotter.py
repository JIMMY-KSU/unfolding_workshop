import numpy as np
import matplotlib.pyplot as plt
from spectrum import Spectrum
from numpy.random import randint


def plotit(ds, us, ts, label):
    """Default, unfolded, true."""

    # get group structure
    gs = np.load('data/struct.npy')

    # plotting the solutions
    fig = plt.figure(randint(1E10), figsize=(10, 6))
    ax = fig.add_subplot(111)
    ax.set_xlabel('Energy')
    ax.set_ylabel('$\Phi$')
    ax.set_xscale('log')
    ax.set_yscale('log')

    spec_ds = Spectrum(gs, ds, 0)
    ax.plot(*spec_ds.plot('plot', 'differential'), label='Default', c='lightgrey')

    spec_ts = Spectrum(gs, ts, 0)
    ax.plot(*spec_ts.plot('plot', 'differential'), label='True', c='lightcoral')

    spec_mx = Spectrum(gs, us, 0)
    ax.plot(*spec_mx.plot('plot', 'differential'), label=label, c='darkblue')

    ax.legend()

    # plotting the errors
    fig = plt.figure(randint(1E10), figsize=(10, 6))
    ax = fig.add_subplot(111)
    ax.set_xlabel('Energy')
    ax.set_ylabel('Error %')
    ax.set_xscale('log')

    spec_er = Spectrum(gs, ((ts - us) / ts) * 100, 0)
    ax.plot(*spec_er.plot('plot', 'integral'), label=label, c='darkblue')

    ax.legend()
