# -*- coding: utf-8 -*-

"""
Package Version(s):
    sklearn: 0.18
"""

from sklearn.datasets import load_digits

# load in datasets
digits = load_digits()
# Print out the datashape.
print digits.data.shape
# Ans = (1797L, 64L)

from sklearn.cross_validation import train_test_split
# Split the data
x_train, x_test, y_train, y_test = train_test_split( digits.data, digits.target, test_size = 0.25, random_state = 42 )

# Print out the datashape.
print y_train.shape
# Ans = (1347L,)
print y_test.shape
# Ans = (450L,)