import pandas as pd

if __name__ == "__main__":
    trainPath = "./Data/train.csv"
    testPath = "./Data/test.csv"

    #trainData = pd.read_csv(trainPath)
    testData = pd.read_csv(testPath)

    print(testData[0:10])