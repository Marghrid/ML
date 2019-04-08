import sys
import math
import numpy as np


class Thing:
    x=[]
    y = -1

    def __str__(self):
        return '(' + str(self.x) + ',\t' + str(self.y) + ')'

def read_input():
    data = []
    for line in sys.stdin.readlines():
        # print(line)
        line = line.replace(" ", "")
        line = line.split(',')    #line is a list
        if line[0] == 'x1':
            continue
        th = Thing();
        th.x = [float(line[0]), float(line[1]), float(line[2])]
        th.y  = float(line[3]);     # removes \n at the end
        data.append(th);

    #for th in data:
    #   print(th)

    return data

def euclidean_distance(x1, x2):
    return math.sqrt((x1[0]-x2[0])**2 + (x1[1]-x2[1])**2 + (x1[2]-x2[2])**2)

def get_neighbors(train, x_new, k):
    # Sort list by distance to new point
    train.sort(key=lambda coord: euclidean_distance(x_new, coord.x))
    
    # Create new list with the k closest neighbours' labels
    ret = []
    print("closest neighbours:")
    for bla in data[:k]:
        print(bla)
    return data[:k]

def print_all_distances(train, x_new):
    print("Distances to " + str(x_new))
    for point in train:
        print(str(point.x) + ", " + str(round(euclidean_distance(x_new, point.x), 4)))

def get_response(x_new, neighbors, num_classes=3):
    # Z = sum (1 / distance )
    Z = 0.0
    for point in neighbors:
        Z += 1.0/euclidean_distance(x_new, point.x)

    print ("Normalization constant: Z = " + str(Z))

    #estimate = (1/Z) sum(y/dist)
    weighted_ys = 0.0
    for point in neighbors:
        weighted_ys += point.y / euclidean_distance(x_new, point.x)

    return (1/Z) * weighted_ys

def predict(data, x_new, k):
    y_pred = []
    neighbors = get_neighbors(data, x_new, k)
    return get_response(x_new, neighbors)

############################################


data = read_input()
print_all_distances(data, [6.1, 0.4, 1.3])
y_pred = predict(data, [6.1, 0.4, 1.3], 3)

print("\n " + str(y_pred))


