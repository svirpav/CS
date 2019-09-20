import matplotlib.pyplot as plt


def quadPlot(arrayY, arrayX):
    y0 = arrayY * 1.5
    y1 = arrayY * 5
    y2 = arrayY * 7
    x = arrayX
    fig, axs = plt.subplots(2, 2)
    axs[0, 0].plot(x, y0, 'b')
    axs[0, 0].set_title("Axis[0, 0]")
    axs[0, 1].plot(x, y1, 'g')
    axs[0, 1].set_title("Axis[0, 1]")
    axs[1, 0].plot(x, y2, 'r')
    axs[1, 0].set_title("Axis[1, 0]")
    axs[1, 1].plot(x, y0, 'y')
    axs[1, 1].set_title("Axis[1, 1]")

    for ax in axs.flat:
        ax.set(xlabel='x-lable', ylabel='ylable')
    for ax in axs.flat:
        ax.label_outer()

    plt.show()


def dualPlot(arrayX, arrayY, arrayX1, arrayY1):
    x = arrayX
    y0 = arrayY * 1.5
    y1 = arrayY * 5
    y2 = arrayY * 7

    y00 = arrayY1 * 1.5
    y01 = arrayY1 * 5
    y02 = arrayY1 * 7
    x1 = arrayX1

    fig, (ax1, ax2) = plt.subplots(1, 2, num="Asymptotic notation",
                                   sharey=True)
    ax1.plot(x, y0)
    ax1.plot(x, y1)
    ax1.plot(x, y2)
    ax1.set_title("Logorithmic function grow")
    ax1.set_xlabel("Input Size")
    ax1.set_ylabel("Function sycle time")
    ax1.grid(True)
    ax2.plot(x1, y00)
    ax2.plot(x1, y01)
    ax2.plot(x1, y02)
    ax2.set_title("Polinominal grow")
    ax2.set_xlabel("Input Size")
    ax2.grid(True)
    plt.show()
