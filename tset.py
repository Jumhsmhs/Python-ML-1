import numpy
import scipy
import matplotlib
import sklearn  # scikit-learn library
import skimage  # scikit-image library
import h5py
import pandas
import keras
import tensorflow
import cv2  # opencv library

import numpy as np
import cv2

labels = {'dog','cat','panda'}
orig = cv2.imread('cats.jpg')
image = cv2.resize(orig, (32,32))

(width, height, channel ) = image.shape
D = int(width*heightchannel)
flatten_image = image.reshape(D,1)

K = len(labels)
W = np.random.randn(K, D)
b = np.random.randn( K, 1)

scores = W.dot(flatten_image) + b

scores = scores.T[0]

label_of_max_score = None
score_max = None
for (label, score) in zip(labels, scores):
    print('[INFO] {}: {:.2f}'.format(label,score))
    if score_max is None or score > score_max:
        score_max = score
        label_of_max_score = label

cv2.putText(orig, "Label: {:} Score: {:.2f}".format(label_of_max_score, score_max),
(10,30), cv2.FONT_HERSHEY_SIMPLEX,0.9,(0,255,0),2)

cv2.imshow("Image", orig)
cv2.waitKey(0)