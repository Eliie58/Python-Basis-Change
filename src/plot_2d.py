import numpy as np
import matplotlib.pyplot as plt


def add_quiver(ax, point_a, point_b, color):
    ax.quiver(point_a[0], point_a[1], point_b[0], point_b[1], units='xy', scale=1, color=color)
    return ax


def plot_basis(ax, matrix):
    origin = np.zeros(2)
    ax = add_quiver(ax, origin, matrix[0], 'red')
    ax = add_quiver(ax, origin, matrix[1], 'green')
    return ax


def plot_figure(ax, matrix, vector, vector_canonical):
    matrix = matrix.T
    origin = np.zeros(2)

    point1 = matrix[0] * vector[0]
    point2 = matrix[1] * vector[1]

    ax = plot_basis(ax, matrix)
    ax = add_quiver(ax, origin, vector_canonical, 'orange')
    ax = add_quiver(ax, origin, point1, (0.0, 0.0, 0.0, 0.1))
    ax = add_quiver(ax, point1, point2, (0.0, 0.0, 0.0, 0.5))

    ax = format_axis(ax)
    return ax


def format_axis(ax):
    ax.set_xlim([-4, 4])
    ax.set_ylim([-4, 4])
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    return ax


def plot(old_matrix, new_matrix, old_vector, vector_canonical, new_vector):
    fig = plt.figure()
    ax_old = fig.add_subplot(1, 2, 1)
    ax_old.set_title('Vector in Old Basis')
    ax_new = fig.add_subplot(1, 2, 2)
    ax_new.set_title('Vector in New Basis')
    plot_figure(ax_old, old_matrix, old_vector, vector_canonical)
    plot_figure(ax_new, new_matrix, new_vector, vector_canonical)
    plt.show()
