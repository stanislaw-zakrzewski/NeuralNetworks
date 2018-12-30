from examples import Examples
from functions import f_to_approximate
from network_components import Network
from plotting import approximation_results_plot
from training import train

n = Network(1, 1, 1, 10)
es = Examples("input.txt", 1, 1)

train(n, es, 500)

approximation_results_plot(n, f_to_approximate)
