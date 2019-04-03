import os
import cPickle
import random
import numpy as np


#first, read in the pre-processed data from a folder containing the DEAP .dat files.
print("Loading EEG files")
validation_fragments = []
validation_truth = []
train_fragments = []
train_truth = []
filenames = [f for f in os.listdir("DEAP_data/")
             if (os.path.isfile("DEAP_data/" + f) and '.dat' in f)]

print("Filenames are ", filenames)

x_test = []
y_test = []
x_train = []
y_train = []

# bootstrapping test data(20%) and train data(80%)
for filename in filenames:
    with open("DEAP_data/" + filename, 'rb') as f:
        print(filename)
        array = cPickle.load(f)
        # print("array is", np.array(array))
        for datum, label in zip(list(array["data"]), list(array["labels"])):
            if random.uniform(0, 1) < .2:
                x_test.append(np.array(datum).flatten())
                y_test.append(label[0])
            else:
                x_train.append(np.array(datum).flatten())
                y_train.append(label[0])

# change list to np.array
x_test, y_test, x_train, y_train = np.array(x_test), np.array(y_test), np.array(x_train), np.array(y_train)

