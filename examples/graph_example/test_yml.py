from yaml import safe_load
import json
from featurepy.model_constraints import *
import os

with open('feature_model.yml') as fp:
    yml = safe_load(fp)

# print(get_features(yml))
print(json.dumps(yml))
