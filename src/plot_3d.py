import numpy as np
import matplotlib.pyplot as plt


def add_quiver(ax, point_a, point_b, color):
    ax.quiver(point_a[0], point_a[1], point_a[2], point_b[0], point_b[1], point_b[2], pivot='tail',
              color=color)
    return ax


def plot_basis(ax, matrix):
    origin = np.zeros(3)
    ax = add_quiver(ax, origin, matrix[0], 'red')
    ax = add_quiver(ax, origin, matrix[1], 'green')
    ax = add_quiver(ax, origin, matrix[2], 'blue')
    return ax


def plot_figure(ax, matrix, vector, vector_canonical):
    matrix = matrix.T
    origin = np.zeros(3)

    point1 = matrix[0] * vector[0]
    point2 = matrix[1] * vector[1]
    point3 = matrix[2] * vector[2]

    ax = plot_basis(ax, matrix)
    ax = add_quiver(ax, origin, vector_canonical, 'orange')
    ax = add_quiver(ax, origin, point1, (0.0, 0.0, 0.0, 0.1))
    ax = add_quiver(ax, point1, point2, (0.0, 0.0, 0.0, 0.5))
    ax = add_quiver(ax, point1 + point2, point3, (0.0, 0.0, 0.0, 1.0))

    ax = format_axis(ax)
    return ax


def format_axis(ax):
    ax.set_xlim([-4, 4])
    ax.set_ylim([-4, 4])
    ax.set_zlim([-4, 4])
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    return ax


def plot(old_matrix, new_matrix, old_vector, vector_canonical, new_vector):
    fig = plt.figure()
    ax_old = fig.add_subplot(1, 2, 1, projection='3d')
    ax_old.set_title('Vector in Old Basis')
    ax_new = fig.add_subplot(1, 2, 2, projection='3d')
    ax_new.set_title('Vector in New Basis')
    plot_figure(ax_old, old_matrix, old_vector, vector_canonical)
    plot_figure(ax_new, new_matrix, new_vector, vector_canonical)
    plt.show()
