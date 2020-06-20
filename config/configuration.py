Config = {

    "seed":137,

    "CV":3,

    "n_jobs":-1,

    "Test_size":.3,

    "Datasets":[
        "creditcard"
    ],

    "Filename_Out":"Results",

    "Ignore_Features":[

        ],

    "Targets":[
        "Class"
    ],

    "Target_Type":"Classification", # Classification or Regression

    "Models":{
        "Classification":[
            "BayesianRidge", 
            "LogisticRegression", 
            "SGDClassifier", 
            "Perceptron", 
            "SVM", 
            "KNN", 
            "DecisionTree", 
            "GradientBoosting", 
            "MLP"
        ],

        "Regression":[
            "LinearRegression",
            "LogisticRegression", 
            "SVR",
            "SGDRegressor",
            "KNN",
            "DecisionTree",
            "GradientBoosting",
            "MLP"
        ]
    },

    "Metrics":{
        "Classification":[
            "accuracy",
            "balanced_accuracy",
            "average_precision",
            #"neg_brier_score", # predict_proba: can't use this metric with some models (BayesianRidge, LogisticRegression)
            "f1",
            "f1_micro",
            "f1_macro",
            "f1_weighted",
            #"neg_log_loss", #predict_proba: can't use this metric with some models
            "precision",
            "recall",
            #"roc_auc" #predict_proba: can't use this metric with some models
        ],

        "Regression":[
            "explained_variance",
            "max_error",
            "neg_mean_absolute_error",
            "neg_mean_squared_error",
            "neg_root_mean_squared_error",
            #"neg_mean_squared_log_error", # Mean Squared Logarithmic Error cannot be used when targets contain negative values.
            "neg_median_absolute_error",
            "r2",
            #"neg_mean_poisson_deviance", #Mean Tweedie deviance error with power=1 can only be used on non-negative y and strictly positive y_pred.
            #"neg_mean_gamma_deviance"  #Mean Tweedie deviance error with power=1 can only be used on non-negative y and strictly positive y_pred.
        ]
    }
    

    

}