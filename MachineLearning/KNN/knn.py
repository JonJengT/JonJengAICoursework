import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from collections import Counter

iris = load_iris()
full_dataset = list(zip(iris.data, iris.target))

def distance(p1, p2):
    
    squared_diff = (p1-p2)*(p1-p2)

    summed_square_diff = np.sum(squared_diff)

    sqrt_summed_square_diff = np.sqrt(summed_square_diff)

    return sqrt_summed_square_diff

def kNN(item, dataset, k):
    distances = []

    for x, y in dataset:
        d = distance(x,item)
        distances.append((d, y))

    distances.sort(key= lambda x: x[0])

    k_nearest = distances[:k]

    #We want to find the most common occurence of distance

    occurences = dict()
    for item in k_nearest:
        if item[1] not in occurences:
            occurences[item[1]] = 1
        else:
            occurences[item[1]] += 1

    #We created a dictionary data structure to count the number of occurences

    max_occur_label = None
    max_occur_val = 0

    for label in occurences:
        if occurences[label] > max_occur_val:
            max_occur_label = label
            max_occur_val = occurences[label]

    return dataset[0][1]

sample_item, true_label = full_dataset[2][0], full_dataset[2][1]
predicted_label = kNN(sample_item, full_dataset, k=3)

print(f"Predicted: {iris.target_names[predicted_label]}")
print(f"Actual:    {iris.target_names[true_label]}")