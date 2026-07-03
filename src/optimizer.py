from scipy.optimize import differential_evolution

from src.model import generate_points
from src.evaluation import l1_distance


def objective(values, data):

    theta, m, x_shift = values

    predicted_x, predicted_y = generate_points(
        theta,
        m,
        x_shift
    )

    score = l1_distance(
        data["x"],
        data["y"],
        predicted_x,
        predicted_y
    )

    return score


def estimate_parameters(data):

    bounds = [
        (0, 50),
        (-0.05, 0.05),
        (0, 100)
    ]

    result = differential_evolution(
        objective,
        bounds=bounds,
        args=(data,),
        seed=42,
        maxiter=30,
        polish=True
    )

    return result