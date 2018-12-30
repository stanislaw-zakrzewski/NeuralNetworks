import matplotlib.pyplot as plt
import numpy as np


def approximation_results_plot(network, f_to_approximate):
    ax = []
    ay = []
    bx = []
    by = []

    for i in np.arange(0.0, 10.0, 0.1):
        ax.append(i)
        ay.append(f_to_approximate(i))
        bx.append(i)
        by.append(network.work([i]))

    plt.title('Approximation using MLP network')
    plt.plot(ax, ay, "r", label='Function to approximate')
    plt.plot(bx, by, "b", label='Network results')
    plt.legend()
    plt.show()
