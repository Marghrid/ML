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
        th.y  = int(line[3]);     # removes \n at the end
        data.append(th);

    #for th in data:
    #   print(th)

    return data


def misclassification_rate(data):
    count = [0, 0, 0]

    for th in data:
        ++count[th.y];

    return 1 - max(count)/sum(count)

def gini_index(data):
    if len(data) == 0:
        return 0
    sigma = 0
    count = [0, 0, 0]

    for th in data:
        count[th.y] += 1;

    for cl in [0, 1, 2]:
        pi = count[cl]/sum(count)
        sigma += pi * pi;

    return 1 - sigma;


def euclidean_distance(x1, x2):
    return math.sqrt((x1[0]-x2[0])**2 + (x1[1]-x2[1])**2 + (x1[2]-x2[2])**2)

def get_neighbors_labels(train, x_new, k):
    # Sort list by distance to new point
    train.sort(key=lambda coord: euclidean_distance(x_new, coord.x))
    
    # Create new list with the k closest neighbours' labels
    ret = []
    print("closest neighbours:")
    for i in range(k):
        print(data[i])
        ret.append(data[i].y)

    return ret

def print_all_distances(train, x_new):
    print("Distances to " + str(x_new))
    for point in train:
        print(str(point.x) + ", " + str(round(euclidean_distance(x_new, point.x), 4)))

def get_response(neighbors_labels, num_classes=3):
    class_votes = [0]*num_classes
    for lbl in neighbors_labels:
        class_votes[lbl] += 1

    print ("class votes: " + str(class_votes))
    return np.argmax(class_votes)

def predict(data, x_new, k):
    y_pred = []
    neighbors = get_neighbors_labels(data, x_new, k)
    return get_response(neighbors)

############################################


data = read_input()
print_all_distances(data, [6.1, 0.4, 1.3])
y_pred = predict(data, [6.1, 0.4, 1.3], 3)

print("\n " + str(y_pred))


