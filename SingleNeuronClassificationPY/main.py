import matplotlib.pyplot as plt
from NetworkComponents import Network
from Examples import Examples

network = Network.Network(2)
examples = Examples.Examples("DataHandling/input.txt")

ax = []
ay = []
bx = []
by = []

for i in range(100):
    network.adapt(examples.get_random_example())

for i in range(len(examples.examples)):
    if network.work(examples.get_specific_example(i).inputs) == 1:
        ax.append(examples.get_specific_example(i).inputs[0])
        ay.append(examples.get_specific_example(i).inputs[1])
    else:
        bx.append(examples.get_specific_example(i).inputs[0])
        by.append(examples.get_specific_example(i).inputs[1])

plt.plot(ax, ay, "ro")
plt.plot(bx, by, "bo")
plt.ylabel("some numbers")
plt.show()
