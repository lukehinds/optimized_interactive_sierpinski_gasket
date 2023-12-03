import matplotlib.pyplot as plt
import numpy as np

def optimized_interactive_sierpinski_gasket(iterations, update_interval):
    # Vertices of the initial triangle
    vertices = np.array([[0, 0], [1, 0], [0.5, np.sqrt(3)/2]])

    # Starting point
    point = np.array([0.5, np.sqrt(3)/4])

    # Store points for batch plotting
    points = [point]

    plt.ion()  # Turn on interactive mode
    fig, ax = plt.subplots()
    ax.set_aspect('equal', adjustable='box')

    for i in range(iterations):
        # Choose a random vertex
        vertex = vertices[np.random.randint(0, 3)]

        # Move halfway from the current point to the chosen vertex
        point = (point + vertex) / 2
        points.append(point)

        # Update the plot at specified intervals
        if i % update_interval == 0:
            ax.scatter(*zip(*points), s=0.1, color='blue')
            plt.draw()
            plt.pause(0.001)  # Tiny pause for the plot to update
            points = []

    # Plot remaining points
    ax.scatter(*zip(*points), s=0.1, color='blue')
    plt.draw()
    plt.ioff()  # Turn off interactive mode
    plt.show()

# Number of iterations and interval for updating the plot
iterations = 10000
update_interval = 100  # Update the plot every 100 iterations

optimized_interactive_sierpinski_gasket(iterations, update_interval)

