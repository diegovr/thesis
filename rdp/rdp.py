# This algorithm works by iteratively identifying the point on a curve that is furthest
# from the line connecting the first and last points.
# The algorithm then recursively simplifies the subcurves on either side of the furthest point.
# This process continues until the distance to the furthest point is less than the specified epsilon.

# The Ramer-Douglas-Peucker algorithm is a simple and efficient algorithm for simplifying curves.
# It is often used in GIS applications to reduce the number of points in a polyline without
# significantly affecting the accuracy of the representation.
def rdp(points, epsilon):
    """
    Performs the Ramer-Douglas-Peucker algorithm on a set of points.

    Args:
      points: A list of points.
      epsilon: The maximum distance from the simplified curve to the original curve.

    Returns:
      A list of points that approximates the original curve.
    """

    # If there are less than 3 points, return the original points.
    if len(points) < 3:
        return points

    # Find the point that is furthest from the line connecting the first and last points.
    max_d = 0
    max_i = 0
    for i in range(1, len(points) - 1):
        d = abs(points[i] - (points[0] + points[-1]) / 2)
        if d > max_d:
            max_d = d
            max_i = i

    # If the distance to the furthest point is less than epsilon, return the original points.
    if max_d < epsilon:
        return points

    # Recursively simplify the subcurves on either side of the furthest point.
    return rdp(points[:max_i + 1], epsilon) + [points[max_i]] + rdp(points[max_i + 1:], epsilon)
