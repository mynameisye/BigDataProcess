
import numpy as np
import os
import sys
import operator

def makeVector(file):
    vector = np.zeros((1, 1024))
    with open(file) as f:
        for i in range(32):
            line = f.readline()
            for j in range(32):
                vector[0, 32 * i + j] = int(line[j])
    return vector


def createDataset(dir):
    labels = []
    trainingFile = os.listdir(dir)
    m = len(trainingFile)
    matrix = np.zeros((m, 1024))

    for i in range(m):
        file = trainingFile[i]
        ans = int(file.split('_')[0])
        labels.append(ans)
        matrix[i, :] = makeVector(dir + '/' + file)

    return matrix, labels


def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis = 1)
    distances = sqDistances ** 0.5
    sortedDistIndicies = distances.argsort()
    classCount = {}

    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    sortedClassCount = sorted(classCount.items(),
        key = operator.itemgetter(1), reverse = True)
    
    return sortedClassCount[0][0]

if __name__ == '__main__':
    # trainingDir = sys.argv[1]
    # testDir = sys.argv[2]

    trainingDir = "trainingDigits"
    testDir = "testDigits"

    testFileList = os.listdir(testDir)
    tLen = len(testFileList)

    matrix, labels = createDataset(trainingDir)


    for k in range(1, 21):
        cnt = 0
        errCnt = 0

        for i in range(tLen):
            ans = int(testFileList[i].split('_')[0])
            testData = makeVector(testDir + '/' + testFileList[i])
            result = classify0(testData, matrix, labels, k)

            cnt += 1

            if ans != result:
                errCnt += 1

        print(int(errCnt / cnt * 100))