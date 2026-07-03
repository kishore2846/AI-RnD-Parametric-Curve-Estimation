import numpy as np


def l1_distance(actual_x, actual_y, predicted_x, predicted_y):

    error_x = np.abs(actual_x - predicted_x)
    error_y = np.abs(actual_y - predicted_y)

    total_error = np.mean(error_x + error_y)

    return total_error