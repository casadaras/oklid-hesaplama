points = [(1, 5), (5, 8), (8, 1), (9, 5)]

def euclideanDistance(kordinat1, kordinat2):
    return pow(pow(kordinat1[0] - kordinat2[0], 2) + pow(kordinat1[1] - kordinat2[1], 2), 0.5)
distances = []

for _ in range(len(points) -1):
    for i in range(_ + 1, len(points)):
        distances.append(euclideanDistance(points[_], points[i]))

print (min(distances))
