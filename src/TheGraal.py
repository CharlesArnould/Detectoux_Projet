from pathlib import Path
import pandas as pd
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import os
import seaborn as sns
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn import preprocessing
from sklearn.preprocessing import MinMaxScaler
from sklearn import svm
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import validation_curve
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import plot_confusion_matrix
from sklearn.model_selection import learning_curve
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv(os.path.abspath("virufy-data-main/clinical/noise_added_dataset.csv"))

# Recup mp3 a partir du csv
dfcough = df['subname']
path = os.path.abspath('virufy-data-main/clinical/segmented/modified_merged')
X0 = df.drop(columns=['corona_test', 'cough_filename', 'subname', 'date'])
X0.head()

# iterate trhough all data

maxmfcc = []
minmfcc = []
meanmfcc = []
stdmfcc = []
rangemfcc = []

maxmagspec = []
minreg = []
meanmagspec = []
meanreg = []
maxfreqmagspec = []
maxfreqreg = []
maxfreqfft = []

for i in range(len(dfcough)):
    data, sr = librosa.load(os.path.abspath(path + '/' + dfcough[i]), res_type='kaiser_fast', duration=1, mono=True)

    data_fft = np.fft.fft(data)
    magnitude_spectrum = np.abs(data_fft)
    maxmagspec.append(magnitude_spectrum.max())
    minreg.append(data.min())
    meanmagspec.append(magnitude_spectrum.mean())
    meanreg.append(data.mean())

    maxfreqmagspec.append(np.argmax(magnitude_spectrum))
    maxfreqreg.append(np.argmax(data))
    maxfreqfft.append(np.argmax(data_fft))

    # calcul du mfcc moyen sur 128 tronçons
    mfccs = np.mean(librosa.feature.mfcc(y=data, sr=sr, n_mfcc=128).T, axis=0)

    maxmfcc.append(max(mfccs))
    minmfcc.append(min(mfccs))
    meanmfcc.append(mfccs.mean())
    stdmfcc.append(np.std(mfccs))
    rangemfcc.append(max(mfccs) - min(mfccs))

d = {'maxmfcc': maxmfcc, 'minmfcc': minmfcc, 'meanmfcc': meanmfcc, 'stdmfcc': stdmfcc, 'rangemfcc': rangemfcc,
     'maxmagspec': maxmagspec, 'minreg': minreg, 'meanmagspec': meanmagspec, 'meanreg': meanreg,
     'maxfreqmagspec': maxfreqmagspec,
     'maxfreqreg': maxfreqreg, 'maxfreqfft': maxfreqfft}

df2 = pd.DataFrame(data=d)
df2.head()

X1 = pd.concat([X0, df2], axis=1)
X1 = X1.drop(columns=['has_Covid19'])

X2 = pd.concat([X0, df2], axis=1)
X2.head()

# get correlations of each features in dataset
# pensez à inclure le label au dataset
# il faut utiliser des valeurs numériques

corrmat = X2.corr()
top_corr_features = corrmat.index
print(top_corr_features)
plt.figure(figsize=(10, 10))
# plot heat map
g = sns.heatmap(X2[top_corr_features].corr(), annot=True, cmap="RdYlGn")

# X getting rid of useless parameters higly correlated to each others
X = X1.drop(columns=['minmfcc', 'meanmfcc', 'rangemfcc'])
X.head()

# transform categorical in numerical params

le = preprocessing.LabelEncoder()
X['gender'] = le.fit_transform(X['gender'])
X['smoker'] = le.fit_transform(X['smoker'])

X.head()

# replace medical history's categorical values by numeric ones
'''
none=0
Diabetes with complications=1
Asthma or chronic lung disease=2
Congestive heart failure=3
'''
for i in range(len(X['medical_history'])):
    if X['medical_history'][i] in 'Diabetes with complications,':
        X['medical_history'][i] = 1
    elif X['medical_history'][i] in 'Asthma or chronic lung disease,':
        X['medical_history'][i] = 2
    elif X['medical_history'][i] in 'Congestive heart failure,':
        X['medical_history'][i] = 3
    else:
        X['medical_history'][i] = 0

# replace patient_reported_symptoms' categorical values by numeric ones
'''
none,=0
New or worsening cough,=1
Sore throat,=2
Shortness of breath,=3
Shortness of breath, Sore throat, Body aches,=4
Shortness of breath, New or worsening cough,=5
Sore throat,Loss of taste,Loss of smell,=6
Fever, chills, or sweating,New or worsening cough,Sore throat,=7
Fever, chills, or sweating,Shortness of breath,New or worsening cough,Sore throat,Loss of taste,Loss of smell,=8
'''
for i in range(len(X['medical_history'])):
    if X['patient_reported_symptoms'][i] == 'New or worsening cough,':
        X['patient_reported_symptoms'][i] = 1
    elif X['patient_reported_symptoms'][i] == 'Sore throat,':
        X['patient_reported_symptoms'][i] = 2
    elif X['patient_reported_symptoms'][i] == 'Shortness of breath,':
        X['patient_reported_symptoms'][i] = 3
    elif X['patient_reported_symptoms'][i] == 'Shortness of breath, Sore throat, Body aches,':
        X['patient_reported_symptoms'][i] = 4
    elif X['patient_reported_symptoms'][i] == 'Shortness of breath, New or worsening cough,':
        X['patient_reported_symptoms'][i] = 5
    elif X['patient_reported_symptoms'][i] == 'Sore throat,Loss of taste,Loss of smell,':
        X['patient_reported_symptoms'][i] = 6
    elif X['patient_reported_symptoms'][i] == 'Fever, chills, or sweating,New or worsening cough,Sore throat,':
        X['patient_reported_symptoms'][i] = 7
    elif X['patient_reported_symptoms'][
        i] == 'Fever, chills, or sweating,Shortness of breath,New or worsening cough,Sore throat,Loss of taste,Loss of smell,':
        X['patient_reported_symptoms'][i] = 8
    else:
        X['patient_reported_symptoms'][i] = 0

# scaling params having negative values (meanreg, minreg) to use SelectKBest
scaler = min_max_scaler = MinMaxScaler()

X[["meanreg", "minreg"]] = min_max_scaler.fit_transform(X[["meanreg", "minreg"]])

# on va rechercher les paramètres les plus importants via la méthode SelectKBest

y = df['has_Covid19']
# apply SelectKBest class to extract top 10 best features
bestfeatures = SelectKBest(score_func=chi2, k="all")

fit = bestfeatures.fit(X, y)
dfscores = pd.DataFrame(fit.scores_)
dfcolumns = pd.DataFrame(X.columns)
# concat two dataframes for better visualization
featureScores = pd.concat([dfcolumns, dfscores], axis=1)
featureScores.columns = ['Specs', 'Score']  # naming the dataframe columns
print(featureScores.nlargest(14, 'Score'))  # print features sorted by best first

# X getting rid of non significant params in X
X_bestK = X.drop(columns=['minreg', 'meanreg', 'gender', 'age'])

# using PCA to reduce dimensions down to 5
# result is not so good so we won't use it
from sklearn.decomposition import PCA

pca = PCA(n_components=5)
data_pca = pca.fit_transform(X)

# Turn to DataFrame
Xpca = pd.DataFrame(data_pca, columns=['PC1', 'PC2', 'PC3', 'PC4', 'PC5'])

# split train/test sets
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(X_bestK, y, test_size=0.2,
                                                    random_state=78)  # test=20% of total data

# Model SVC

modelsvm = svm.NuSVC()
modelsvm.fit(x_train, y_train)
y_pred = modelsvm.predict(x_test)
print(modelsvm.score(x_train, y_train))
print(modelsvm.score(x_test, y_test))

# Model SVC crossval

SVC_cvs = cross_val_score(modelsvm, x_train, y_train, cv=10, scoring='accuracy').mean()
print(cross_val_score(modelsvm, x_train, y_train, cv=10, scoring='accuracy'))
print(SVC_cvs)

# Model Knn Classifier

modelknn = KNeighborsClassifier(n_neighbors=7, metric='euclidean')
modelknn.fit(x_train, y_train)
y_predknn = modelknn.predict(x_test)
print(modelknn.score(x_train, y_train))
print(modelknn.score(x_test, y_test))

# Model KNN crossval
KNN_cvs = cross_val_score(KNeighborsClassifier(), x_train, y_train, cv=10, scoring='accuracy').mean()
print(cross_val_score(KNeighborsClassifier(), x_train, y_train, cv=10, scoring='accuracy'))
print(KNN_cvs)

# validation curve
k = np.arange(1, 20)
train_score, val_score = validation_curve(KNeighborsClassifier(metric='euclidean'), x_train, y_train, 'n_neighbors', k,
                                          cv=10)

# visualize the best k for n_neighbors
plt.plot(k, val_score.mean(axis=1), label='validation')
plt.plot(k, train_score.mean(axis=1), label='train')
plt.ylabel('score')
plt.xlabel('n_neighbors')
plt.legend()

# gridSearchCV permet de rechercher les meilleurs hyperparamètres pour notre modèle
param_grid = {'n_neighbors': np.arange(1, 20), 'metric': ['euclidean', 'manhattan']}
grid = GridSearchCV(KNeighborsClassifier(), param_grid, cv=10)
grid.fit(x_train, y_train)
print(grid.best_score_)  # meilleur score sur les données de validation
print(grid.best_params_)  # meilleurs paramètres
modelknngrid = grid.best_estimator_  # attribuer le modèle et ses meilleurs hyperparamètres à une variable
modelknngrid.score(x_test, y_test)  # essai avec les données de test

# show confusion matrix for testset
# indépendamment du score, les erreurs de diagnostics du type false negative sont particulièrement mauvaises
plot_confusion_matrix(modelknngrid, x_test, y_test)
plt.show()

# le learning rate va nous permettre de voir s'il serait intéressant de récolter plus de données
# si nos courbes tendent vers une valeur fixe alors c'est le cas
# ici la courbe continue d'augmenter, + de données donnerait alors un modèle plus performant


N, train_score_lc, val_score_lc = learning_curve(modelknngrid, x_train, y_train, train_sizes=np.linspace(0.2, 1.0, 5),
                                                 cv=10)

print(N)
plt.plot(N, train_score_lc.mean(axis=1), label='train')
plt.plot(N, val_score_lc.mean(axis=1), label='validation')
plt.xlabel('train_sizes')
plt.legend()

# Model DecisionTreeClassfier

modeltree = DecisionTreeClassifier(max_depth=3, random_state=0)
modeltree.fit(x_train, y_train)
y_predtree = modeltree.predict(x_test)
print(modeltree.score(x_train, y_train))
print(modeltree.score(x_test, y_test))

# Model decision tree crossval
tree_cvs = cross_val_score(DecisionTreeClassifier(), x_train, y_train, cv=10, scoring='accuracy').mean()
print(cross_val_score(modeltree, x_train, y_train, cv=10, scoring='accuracy'))
print(tree_cvs)

# validation curve
k = np.arange(1, 30)
train_score, val_score = validation_curve(DecisionTreeClassifier(), x_train, y_train, 'max_depth', k, cv=10)

# visualize the best k for n_neighbors
plt.plot(k, val_score.mean(axis=1), label='validation')
plt.plot(k, train_score.mean(axis=1), label='train')
plt.ylabel('score')
plt.xlabel('max_depth')
plt.legend()

# gridSearchCV permet de rechercher les meilleurs hyperparamètres pour notre modèle
param_grid = {'max_depth': np.arange(1, 10), 'criterion': ['gini', 'entropy'], 'splitter': ['best', 'random']}
grid = GridSearchCV(DecisionTreeClassifier(), param_grid, cv=10)
grid.fit(x_train, y_train)
print(grid.best_score_)  # meilleur score sur les données de validation
print(grid.best_params_)  # meilleurs paramètres
modeltreegrid = grid.best_estimator_  # attribuer le modèle et ses meilleurs hyperparamètres à une variable
modeltreegrid.score(x_test, y_test)  # essai avec les données de test

# show confusion matrix for testset
# indépendamment du score, les erreurs de diagnostics du type false negative sont particulièrement mauvaises
plot_confusion_matrix(modeltreegrid, x_test, y_test)
plt.show()

# le learning rate va nous permettre de voir s'il serait intéressant de récolter plus de données
# si nos courbes tendent vers une valeur fixe alors c'est le cas
# ici la courbe continue d'augmenter, + de données donnerait alors un modèle plus performant

N, train_score_lc, val_score_lc = learning_curve(modeltreegrid, x_train, y_train, train_sizes=np.linspace(0.2, 1.0, 10),
                                                 cv=10)

print(N)
plt.plot(N, train_score_lc.mean(axis=1), label='train')
plt.plot(N, val_score_lc.mean(axis=1), label='validation')
plt.xlabel('train_sizes')
plt.legend()