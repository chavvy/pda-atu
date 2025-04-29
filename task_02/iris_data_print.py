#Functions for printing information on the iris dataset just for easie reading

def iris_keys(data):
    keys = data.keys()
    print(keys)

def iris_features(data):
    features = data['data']
    print(f"\nFeatures of the data:")
    print(features)

def iris_features_shape(data):
    features_shape = data['data'].shape
    print(f"\nShape of the data:")
    print(features_shape)

def iris_target(data):
    target = data['target']
    print(f"\nTarget of the data:")
    print(target)

def iris_shape(data):
    target_shape = data['target'].shape
    print(f"\nTarget shape of the data:")
    print(target_shape)

def iris_target_names(data):
    target_names = data['target_names']
    print(f"\nTarget names of the data:")
    print(target_names)

def iris_features_names(data):
    features_names = data['feature_names']
    print(f"\nFeature names of the data:")
    print(features_names)

def iris_firstrow_data(data, n=5):
    features = data['data']
    print(f"\nFirst {n} rows of data:")
    print(features[:n])

def iris_lastrow_data(data, n=5):
    features = data['data']
    print(f"\nLast {n} rows of data:")
    print(features[-n:])