# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 20:46:11 2019

@author: bjwil
"""

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
%matplotlib inline

iris = sns.load_dataset('iris')
iris.head()



sns.set()
sns.pairplot(iris, hue='species', size=1.5)

X_iris = iris.drop('species', 1)
X_iris.shape

y_iris = iris['species']
y_iris.shape




rng = np.random.RandomState(42)
x = 10 * rng.rand(50)
y = 2 * x - 1 + rng.randn(50)
plt.scatter(x, y)

from sklearn.linear_model import LinearRegression
model = LinearRegression(fit_intercept=True)
model
X = x[:, np.newaxis]
x.shape
X.shape
model.fit(X, y)
model.coef_
model.intercept_

xfit = np.linspace(-1, 11)
xfit.shape
Xfit = xfit[:, np.newaxis]
yfit = model.predict(Xfit)

plt.scatter(x, y)
plt.plot(Xfit, yfit);

from sklearn.model_selection import train_test_split
Xtrain, Xtest, ytrain, ytest = train_test_split(X_iris, y_iris,
                                               random_state=1)
from sklearn.naive_bayes import GaussianNB
model = GaussianNB()
model.fit(Xtrain, ytrain)
y_model = model.predict(Xtest)
from sklearn.metrics import accuracy_score
accuracy_score(ytest, y_model)

# Unsupervised PCA
from sklearn.decomposition import PCA
model = PCA(n_components=2)
model.fit(X_iris)
X_2D = model.transform(X_iris)
iris[['PCA1','PCA2']] = pd.DataFrame(X_2D)
sns.lmplot('PCA1', 'PCA2', hue='species', data=iris, fit_reg=False)


# Unsupervised GMM
from sklearn.mixture import GaussianMixture
model = GaussianMixture(n_components=3)
model.fit(X_iris)
y_gmm = model.predict(X_iris)
iris['cluster'] = y_gmm
#.rename(columns={'cluser':'cluster'}, inplace=True)
sns.lmplot('PCA1', 'PCA2', hue='species', 
           data=iris, col='cluster', fit_reg=False)


#Example
from sklearn.datasets import load_digits
import sklearn
digits = load_digits()
digits.images.shape

fig, axes = plt.subplots(10, 10, figsize=(8, 8),
                         subplot_kw={'xticks':[], 'yticks':[]},
                         gridspec_kw=dict(hspace=0.1, wspace=0.1))

for i, ax in enumerate(axes.flat):
    ax.imshow(digits.images[i], cmap='binary', interpolation='nearest')
    ax.text(0.05, 0.05, str(digits.target[i]),
            transform=ax.transAxes, color='green')
    
X = digits.data
X.shape

y = digits.target
y.shape

from sklearn.manifold import Isomap
iso = Isomap()
iso.fit(X)
data_projected = iso.transform(X)
data_projected.shape


plt.scatter(data_projected[:, 0], data_projected[:, 1], c=digits.target,
            edgecolor='none', alpha=0.5,
            cmap=plt.cm.get_cmap('Spectral', 10))
plt.colorbar()
