from sklearn.linear_model import LinearRegression, LogisticRegression, Perceptron, RidgeClassifier, SGDClassifier, SGDRegressor,TweedieRegressor
from sklearn.svm import LinearSVC, LinearSVR
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
from sklearn.ensemble import GradientBoostingRegressor, GradientBoostingClassifier
from sklearn.neural_network import MLPClassifier, MLPRegressor


Models = {
    "Classification":{
        "BayesianRidge":RidgeClassifier(), 
        "LogisticRegression":LogisticRegression(multi_class='ovr'), 
        "SGDClassifier":SGDClassifier(), 
        "Perceptron":Perceptron(), 
        "SVM":LinearSVC(), 
        "KNN":KNeighborsClassifier(), 
        "DecisionTree":DecisionTreeClassifier(), 
        "GradientBoosting":GradientBoostingClassifier(), 
        "MLP":MLPClassifier()
    },

    "Regression":{
        "LinearRegression":LinearRegression(), 
        "LogisticRegression":LogisticRegression(), 
        "SVR":LinearSVR(), 
        "SGDRegressor":SGDRegressor(), 
        "KNN":KNeighborsRegressor(), 
        "DecisionTree":DecisionTreeRegressor(), 
        "GradientBoosting":GradientBoostingRegressor(), 
        "MLP":MLPRegressor() 
    }
}