#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, svm, cross_validation
from sklearn.datasets import load_svmlight_file
import csv
import urllib

my_file = open('data01.csv', 'r')
dataset = np.loadtxt(my_file, delimiter=",")
my_file.close()

target = dataset[:,0]
data = dataset[:,1:3]

np.random.shuffle(dataset)
X_train, X_test, y_train, y_test = data[50:],data[:50],target[50:],target[:50]

print X_train
C = 1.0  # SVM regularization parameterd
X = X_train
y = y_train

h = .02  # step size in the mesh

svc = svm.SVC(kernel='linear', C=C).fit(X, y)
rbf_svc = svm.SVC(kernel='rbf', gamma=0.7, C=C).fit(X, y)
poly_svc = svm.SVC(kernel='poly', degree=2, C=C).fit(X, y)

# title for the plots
titles = ['SVM con kernel lineal',
          'SVM con kernel RBF',
          'SVM con kernel poligonal (grado 2)']

for i, clf in enumerate((svc, rbf_svc, poly_svc)):
	result = clf.predict(X_test)
	print "#####################################"
	print ""
	print titles[i]
	print ""
	#print "Result:\n %s" %(result)
	#print "Target:\n %s" %(y_test)

	score = 0.0
	j = 0
	positivo = 0
	falsos_positivos = 0
	for sample in result:
		if (y_test[j] == 0 and sample == 1):
			falsos_positivos+=1
		if(sample == y_test[j]):
			score+=1.0
			if (y_test[j] == 1):
				positivo+=1
		j = j + 1
	
	print "Score: %s, Sample_set: %s, " %(score, len(result))
	print "Porcentaje acertadas: %s" %((float(score)/len(result)) * 100)
	print "-------------------------------------"
	print "Verdaderos positivos: %s " %(positivo)
	print "Falsos positivos: %s" %(falsos_positivos)
	print "Falsos negativos: %s " %(100 - positivo)
	print "Verdaderos negativos: %s" %(100 - falsos_positivos)
	print ""

"""
# create a mesh to plot in
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                     np.arange(y_min, y_max, h))
                     

for i, clf in enumerate((svc, rbf_svc, poly_svc)):
    # Plot the decision boundary. For that, we will assign a color to each
    # point in the mesh [x_min, m_max]x[y_min, y_max].
    plt.subplot(2, 2, i + 1)
    plt.subplots_adjust(wspace=0.4, hspace=0.4)

    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

    # Put the result into a color plot
    Z = Z.reshape(xx.shape)
    plt.contourf(xx, yy, Z, cmap=plt.cm.Paired, alpha=0.8)

    # Plot also the training points
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Paired)
    plt.xlabel(' Mayusculas ')
    plt.ylabel(' Uso de signos ')
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())
    plt.xticks(())
    plt.yticks(())
    plt.title(titles[i])

plt.show()
"""