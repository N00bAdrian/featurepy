from featurepy.parametric_features import parse_feature_args

print(parse_feature_args("basicGraph"))
print(parse_feature_args("basicGraph()"))
print(parse_feature_args("basicGraph('q', 1)"))
print(parse_feature_args("basicGraph('q', 1, ['b'], d={'a': 2})"))
