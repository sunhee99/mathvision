from enum import Enum
import numpy as np

class HomographyType(Enum):
    UNKNOWUN = -1
    NORMAL = 0
    CONCAVE = 1
    TWIST = 2
    REFLECTION = 3

    def __str__(self) -> str:
        return str(self.name)

def classifyHomography(pts1: np.ndarray, pts2: np.ndarray) -> int:
    if len(pts1) != 4 or len(pts2) != 4:
        return HomographyType.UNKNOWUN

    origin_v = np.cross(pts1 - np.roll(pts1, shift=-1, axis=0), pts1 - np.roll(pts1, shift=1, axis=0))
    compare_v = np.cross(pts2 - np.roll(pts2, shift=-1, axis=0), pts2 - np.roll(pts2, shift=1, axis=0))

    a = origin_v * compare_v
    hgraphy = (a < 0).sum()

    if hgraphy == 4:
        return HomographyType.REFLECTION
    elif hgraphy == 2:
        return HomographyType.TWIST
    elif hgraphy in [1, 3]:
        return HomographyType.CONCAVE
    return HomographyType.NORMAL


def polyArea(points):
    area = 0
    n = len(points)

    for i in range(n-1):
        area += (points[i][0] * points[i+1][1])
        area += (points[i][1] * points[i+1][0])

    area = abs(area)/2.0
    return area

