import sys


class point:
	x=[]
	y = -1

	def __str__(self):
		return '(' + str(self.x) + ',\t' + str(self.y) + ')'

def read_input():
	data = []
	for line in sys.stdin.readlines():
		#print(line)
		line = line.replace(" ", "")
		line = line.split(',')    #line is a list
		if line[0] == 'x1':
			continue
		th = point();
		th.x = [float(line[0]), float(line[1]), float(line[2])]
		th.y  = int(line[3]);     # removes \n at the end
		data.append(th);

	for th in data:
		print(th)

	return data


def gini_index(data):
	#print ("gini:")
	if len(data) == 0:
		return 0
	sigma = 0
	count = [0, 0, 0]

	for th in data:
		count[th.y] += 1;

	for cl in [0, 1, 2]:
		#print("class " + str(cl) + ":\t(" + str(count[cl]) + "/" + str(sum(count)) + ")^2")
		pi = count[cl]/sum(count)
		#print("\t\t= " + str(pi * pi))
		sigma += pi * pi;

	return 1 - sigma;



#############################

def decision_tree_split(data):

	# Compute maximum and minimum values for each feature:
	max_vals = [data[0].x[0], data[0].x[1], data[0].x[2]]
	min_vals = [data[0].x[0], data[0].x[1], data[0].x[2]]

	for point in data:
		max_vals[0] = max(max_vals[0], point.x[0]) 
		max_vals[1] = max(max_vals[1], point.x[1]) 
		max_vals[2] = max(max_vals[2], point.x[2])

		min_vals[0] = min(min_vals[0], point.x[0])
		min_vals[1] = min(min_vals[1], point.x[1])
		min_vals[2] = min(min_vals[2], point.x[2])

	# splitting t into l and r
	# improvement = i(t) - (#l/#t) * i(l) - (#r/#t) * i(r)

	best_split_feat = -1;
	best_split_val = -500;
	best_info_gain = 0;

	print("This node's Gini index is: " + str(gini_index(data)))

	for feat in range(3):
		for point in data:
			split_val = point.x[feat]
			data_l = []
			data_r = []

			#split_val = round(split_val, 1)

			for point in data:
				if point.x[feat] <= split_val:
					data_l.append(point)
				else:
					data_r.append(point)

			improvement = gini_index(data) - (len(data_l)/len(data)) * gini_index(data_l) - (len(data_r)/len(data)) * gini_index(data_r)

			#print("split on " + str(feat) + " <= " + str(split_val) + ";\tImprovement = " + str(improvement))

			if improvement > best_info_gain:
				best_split_feat = feat
				best_split_val = split_val
				best_info_gain = improvement

	print ("The best split is " + str(best_split_feat) + " <= " + str(best_split_val) + ";\tImprovement = " + str(best_info_gain))

	data_l = []
	data_r = []

	for point in data:
		if point.x[best_split_feat] <= best_split_val:
			data_l.append(point)
		else:
			data_r.append(point)
	print("1:")
	for point in data_l:
		print(point)
	print("2:")
	for point in data_r:
		print(point)

	return (data_l, data_r)


############################################


data = read_input()
decision_tree_split(data);

