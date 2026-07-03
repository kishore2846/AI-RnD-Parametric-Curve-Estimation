import numpy as np


def generate_curve(theta, m, x_shift, t):

    theta = np.radians(theta)

    x = (
        t * np.cos(theta)
        - np.exp(m * np.abs(t))
        * np.sin(0.3 * t)
        * np.sin(theta)
        + x_shift
    )

    y = (
        42
        + t * np.sin(theta)
        + np.exp(m * np.abs(t))
        * np.sin(0.3 * t)
        * np.cos(theta)
    )

    return x, y