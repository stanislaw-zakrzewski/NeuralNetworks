import matplotlib.pyplot as plt
from NetworkComponents.Network import Network
from BackPropagation import train_network
from Examples.Examples import Examples


def show_results():
    ax = []
    ay = []
    bx = []
    by = []

    for i in range(len(es.examples)):
        ax.append(es.get_example(i).inputs[0])
        ay.append(es.get_example(i).outputs[0])
        bx.append(es.get_example(i).inputs[0])
        by.append(n.work(es.get_example(i).inputs))

    plt.plot(ax, ay, "ro")
    plt.plot(bx, by, "bo")
    plt.ylabel("some numbers")
    plt.show()


n = Network(1, 1, 1, 10)
es = Examples("input.txt", 1, 1)

for j in range(500):
    e = es.get_random_example()
    train_network(n, e.inputs, e.outputs)

show_results()
