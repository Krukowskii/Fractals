import numpy as np
import matplotlib.pyplot as plt

def affine_transform(point, matrix):
    """Funkcja wykonująca przekształcenie afiniczne punktu."""
    a, b, c, d, e, f = matrix
    x, y = point
    new_x = a * x + b * y + e
    new_y = c * x + d * y + f
    return new_x, new_y

def generate_fractal(transforms, probabilities, iterations, initial_point=(0, 0)):
    """Funkcja generująca fraktal metodą IFS."""
    points = [initial_point]
    for _ in range(iterations):
        # Wybierz transformację zgodnie z wagami
        chosen_transform = np.random.choice(len(transforms), p=probabilities)
        # Wykonaj wybraną transformację na ostatnim punkcie
        new_point = affine_transform(points[-1], transforms[chosen_transform])
        points.append(new_point)
    return points

def plot_fractal(points):
    """Funkcja wizualizująca wygenerowany fraktal."""
    x = [point[0] for point in points]
    y = [point[1] for point in points]
    plt.scatter(x, y, s=1, c='b', marker='.')
    plt.axis('equal')
    plt.show()

# Definicja transformacji i prawdopodobieństw ich wyboru
transforms = [
    [0.14, 0.01, 0.0, 0.51, -1.31, 0.1],
    [0.43, 0.52, -0.45, 0.5, 1.49, -0.75],
    [0.45, -0.49, 0.47, 0.47, -1.62, -0.74],
    [0.49, 0.0, 0.0, 0.51, 0.02, 1.62]
]

probabilities = [0.1, 0.35, 0.35, 0.2]

# Generowanie fraktala
iterations = 100000
initial_point = (0, 0)
fractal_points = generate_fractal(transforms, probabilities, iterations, initial_point)

# Wizualizacja
plot_fractal(fractal_points)
