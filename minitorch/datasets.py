import math
import random
from dataclasses import dataclass
from typing import List, Tuple


def make_pts(N: int) -> List[Tuple[float, float]]:
    """
    Generate a list of random 2D points in the range [0, 1].

    Args:
        N (int): The number of points to generate.

    Returns:
        List[Tuple[float, float]]: A list of N tuples, where each tuple represents a point (x1, x2).
    """
    X = []
    for i in range(N):
        x_1 = random.random()
        x_2 = random.random()
        X.append((x_1, x_2))
    return X


@dataclass
class Graph:
    N: int
    X: List[Tuple[float, float]]
    y: List[int]


def simple(N: int) -> Graph:
    """
    Generate a simple linearly separable dataset where points are classified
    based on whether their x-coordinate is less than 0.5.

    Args:
        N (int): The number of points to generate.

    Returns:
        Graph: A graph with N points and binary labels.
    """
    X = make_pts(N)
    y = [1 if x_1 < 0.5 else 0 for x_1, x_2 in X]
    return Graph(N, X, y)


def diag(N: int) -> Graph:
    """
    Generate a dataset where points are classified based on whether the sum
    of their x and y coordinates is less than 0.5.

    Args:
        N (int): The number of points to generate.

    Returns:
        Graph: A graph with N points and binary labels.
    """
    X = make_pts(N)
    y = [1 if x_1 + x_2 < 0.5 else 0 for x_1, x_2 in X]
    return Graph(N, X, y)


def split(N: int) -> Graph:
    """
    Generate a dataset where points are classified based on whether their
    x-coordinate is in the range (0.2, 0.8).

    Args:
        N (int): The number of points to generate.

    Returns:
        Graph: A graph with N points and binary labels.
    """
    X = make_pts(N)
    y = [1 if x_1 < 0.2 or x_1 > 0.8 else 0 for x_1, x_2 in X]
    return Graph(N, X, y)


def xor(N: int) -> Graph:
    """
    Generate a dataset where points are classified based on XOR logic
    applied to their coordinates.

    Args:
        N (int): The number of points to generate.

    Returns:
        Graph: A graph with N points and binary labels.
    """
    X = make_pts(N)
    y = [1 if (x_1 < 0.5 and x_2 > 0.5) or (x_1 > 0.5 and x_2 < 0.5) else 0 for x_1, x_2 in X]
    return Graph(N, X, y)


def circle(N: int) -> Graph:
    """
    Generate a dataset where points are classified based on their distance
    from the center of the space.

    Args:
        N (int): The number of points to generate.

    Returns:
        Graph: A graph with N points and binary labels.
    """
    X = make_pts(N)
    y = [1 if (x_1 - 0.5) ** 2 + (x_2 - 0.5) ** 2 > 0.1 else 0 for x_1, x_2 in X]
    return Graph(N, X, y)


def spiral(N: int) -> Graph:
    """
    Generate a spiral dataset, where points form two intertwined spirals.

    Args:
        N (int): The number of points to generate.

    Returns:
        Graph: A graph with N points and binary labels.
    """
    def x(t: float) -> float:
        return t * math.cos(t) / 20.0

    def y(t: float) -> float:   
        return t * math.sin(t) / 20.0

    
    X = [(x(10.0 * (float(i) / (N // 2))) + 0.5, y(10.0 * (float(i) / (N // 2))) + 0.5)
         for i in range(5 + 0, 5 + N // 2)]
    X += [(y(-10.0 * (float(i) / (N // 2))) + 0.5, x(-10.0 * (float(i) / (N // 2))) + 0.5)
          for i in range(5 + 0, 5 + N // 2)]
    y2 = [0] * (N // 2) + [1] * (N // 2)
    return Graph(N, X, y2)

datasets = {
    'Simple': simple,
    'Diag': diag,
    'Split': split,
    'Xor': xor,
    'Circle': circle,
    'Spiral': spiral
}