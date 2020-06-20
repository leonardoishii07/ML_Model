from config.configuration import Config
from config.models import Models

n_seed = Config['seed']
datasets = Config["Datasets"]
CV = Config['CV']
n_jobs=Config['n_jobs']
test_size = Config["Test_size"]
Target_type = Config["Target_Type"]
targets = Config['Targets']
Ignore_features = Config['Ignore_Features']
model_list = [Models[Target_type].get(key) for key in Config["Models"][Target_type]]
metrics = Config['Metrics'][Target_type]
Filename_Out = Config['Filename_Out']