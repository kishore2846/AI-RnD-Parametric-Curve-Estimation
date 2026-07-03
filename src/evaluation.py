import numpy as np
from scipy.spatial import cKDTree


def l1_distance(actual_x, actual_y, predicted_x, predicted_y):

    actual_points = np.column_stack((actual_x, actual_y))
    predicted_points = np.column_stack((predicted_x, predicted_y))

    tree = cKDTree(actual_points)

    distances, _ = tree.query(predicted_points)

    return np.mean(distances)