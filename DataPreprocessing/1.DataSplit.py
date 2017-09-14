# -*- coding: utf-8 -*-

"""
Package Version(s):
    sklearn: 0.18
"""

from sklearn.datasets import load_digits

# load in datasets
datasets = load_digits()
# Print out the datashape.
print "The length of dataset is: ", datasets.data.shape
# Ans = (1797L, 64L)



# Split method 1
from sklearn.cross_validation import train_test_split
# Split the data
x_train, x_test, y_train, y_test = train_test_split( datasets.data, datasets.target, test_size = 0.25, random_state = 42 )
# Print out the datashape.
print "The length of train set is: ", y_train.shape
# Ans = (1347L,)
print "The length of test set is: ", y_test.shape
# Ans = (450L,)




# Split method 2
x_train = []
x_test = []
y_train = []
y_test = []

# Split the data
x_test = [datasets.data[i] for i in range(len(datasets.data)) if i%4 == 0]
x_train = [datasets.data[i] for i in range(len(datasets.data)) if i%4 != 0]
y_test = [datasets.target[i] for i in range(len(datasets.data)) if i%4 == 0]
y_train = [datasets.target[i] for i in range(len(datasets.data)) if i%4 != 0]

# Print out the datashape.
print "The length of train set is: ", len( y_train )
# Ans = 1347
print "The length of test set is: ", len( y_test )
# Ans = 450
