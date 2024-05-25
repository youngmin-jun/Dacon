import pandas as pd
import category_encoders as ce
from LoadData import ld

if __name__ == "__main__":
    trainPath = "./Data/train.csv"
    testPath = "./Data/test.csv"

    l
    

    train_x = trainData.drop(columns=['ID', 'Click'])
    train_y = trainData['Click']

    test_x = testData.drop(columns=['ID'])

    for col in train_x.columns:
        if train_x[col].isnull().sum != 0:
            train_x[col].fillna(0, inplace=True)
            test_x[col].fillna(0, inplace=True)
       
    encoding_target = list(train_x.dtypes[train_x.dtypes == "object"].index)

    enc = ce.CountEncoder(col = encoding_target).fit(train_x, train_y)
    X_train_encoded = enc.transform(train_x)
    X_test_encoded = enc.transform(test_x)

    model = RandomForestRegressor()
    model.fit(X_train_encoded, train_y)

    pred = model.predict_prob(X_test_encoded)
    
    

