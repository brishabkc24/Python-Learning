"""Exercise 3: unpack (x, y) tuples, print each distance from the origin and find the farthest point."""

points = [(3, 4), (6, 8), (1, 1)]

farthest = points[0]
farthest_distance = 0

for point in points:
    x, y = point
    distance = (x * x + y * y) ** 0.5
    print(point, "->", distance)
    if distance > farthest_distance:
        farthest_distance = distance
        farthest = point

print("Farthest:", farthest)
