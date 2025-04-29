#Functions for printing information on the iris dataset just for easie reading

def iris_keys(data):
    keys = data.keys()
    print(keys)

def iris_features(data):
    features = data['data']
    print(features)

def iris_features_shape(data):
    features_shape = data['data'].shape
    print(features_shape)

def iris_target(data):
    target = data['target']
    print(target)

def iris_shape(data):
    target_shape = data['target'].shape
    print(target_shape)

def iris_target_names(data):
    target_names = data['target_names']
    print(target_names)

def iris_features_names(data):
    features_names = data['feature_names']
    print(features_names)