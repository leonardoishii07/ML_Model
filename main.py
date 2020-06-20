import pandas as pd
import numpy as np
from sklearn.model_selection import cross_validate
from sklearn.model_selection import ShuffleSplit

from config import n_seed, datasets, CV, n_jobs, test_size, Target_type, targets, Ignore_features, model_list, metrics, Filename_Out

if __name__ == "__main__":
   
    df_results = pd.DataFrame()

    for dataset in datasets:
        np.random.seed(n_seed)
        for target in targets:
            df = pd.read_csv("./datasets/{}.csv".format(dataset))
            X = df.drop(targets, axis=1).drop(Ignore_features, axis=1).to_numpy()
            y = df[target].to_numpy()
            for model in model_list:
                cv = ShuffleSplit(n_splits=CV, test_size=test_size)

                results = cross_validate(model, X, y, cv=cv, scoring=metrics, error_score=1, n_jobs=n_jobs)
                results['Target'] = [target]*CV
                results['Model'] = [model]*CV
                results['Dataset'] = [dataset]*CV

                tmp = pd.DataFrame(results)
                df_results = df_results.append(tmp)

    df_results.to_csv("./Results/{}.csv".format(Filename_Out), index=False)
