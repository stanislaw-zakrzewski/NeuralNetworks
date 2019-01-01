from examples import Examples
from functions import f_to_approximate as function
from network_components import Network
from plotting import approximation_results_plot as plot
from training import train

input_count = 1
output_count = 1
hidden_layers_count = 1
neurons_on_hidden_layers_count = 10

n = Network(input_count, output_count, hidden_layers_count, neurons_on_hidden_layers_count)

input_file = 'input.txt'

es = Examples(input_file, input_count, output_count)

epochs = 500
initial_learning_rate = 0.2
momentum = 0.9

train(n, es, epochs, initial_learning_rate, momentum)

plot(n, function)
