import csv
import random
import math
def loadcsv(filename):
    lines=csv.reader(open(filename,'r'))
    dataset=list(lines)
    for i in range(len(dataset)):
        dataset[i]=[float(x) for x in dataset[i]]
    return dataset

def splitDataset(dataset,splitratio):
    trainsize=int (len(dataset)*splitratio)
    trainset=[]
    copy=list(dataset)
    while len(trainset)< trainsize:
        index=random.randrange(len(copy))
        trainset.append(copy.pop(index))
    return [trainset,copy]

def seperateByClass(dataset):
    seperated={}
    for i in range(len(dataset)):
        vector=dataset[i]
        if(vector[-1] not in seperated):
            seperated[vector[-1]]=[]
        seperated[vector[-1]].append(vector)
    return seperated

def mean(numbers):
    return sum(numbers)/float(len(numbers))

def stdev(numbers):
    avg=mean(numbers)
    variance=sum([pow(x-avg,2) for x in numbers])/float(len(numbers))
    return math.sqrt(variance)

def summarize(dataset):
    summaries=[(mean(attribute),stdev(attribute)) for attribute in zip(*dataset)]
    del summaries[-1]
    return summaries

def summarizeByClass(dataset):
    seperated=seperateByClass(dataset) 
    summaries={}
    for classValue,instances in seperated.items():
        summaries[classValue]=summarize(instances)
    return summaries

def calculateProbability(x,mean,stdev):
    exponent=math.exp(-(math.pow(x-mean,2)/(2*math.pow(stdev,2))))
    return(1/(math.sqrt(2*math.pi)*stdev))*exponent

def calculateClassProbability(summaries,inputVector):
    probabilities={}
    for classValue,classSummaries in summaries.items():
        probabilities[classValue]=1
        for i in range(len(classSummaries)):
            mean,stdev=classSummaries[i]
            x=inputVector[i]
            probabilities[classValue]*=calculateProbability(x,mean,stdev)
    return probabilities

def predict(summaries,inputVector):
    probabilities=calculateClassProbability(summaries,inputVector)
    bestLabel,bestProb=None,-1
    for classValue,probability in probabilities.items():
        if bestLabel is None or probability>bestProb:
            bestProb=probability
            bestLabel=classValue
    return bestLabel

def getPredictions(summaries,testset):
    predictions=[]
    for i in range(len(testset)):
        result=predict(summaries,testset[i])
        predictions.append(result)
    return predictions

def getAccuracy(testset,predictions):
    correct=0
    for i in range(len(testset)):
        if(testset[i][-1]==predictions[i]):
            correct+=1
    return(correct/float(len(testset)))*100.0

def main():
    filename='naviebayes.csv'
    splitratio=0.99
    dataset=loadcsv(filename)
    trainingset,testset=splitDataset(dataset,splitratio)
    #trainingset=dataset
    #testset=[[8.0,1830,64.0,0.0,0.0,2.3,3.0,672,32.0]]
           
    print('split {0} rows into train={1} and test={2} rows'.format(len(dataset), len(trainingset), len(testset)))
    summaries=summarizeByClass(trainingset)
    predictions=getPredictions(summaries,testset)
    accuracy=getAccuracy(testset,predictions)
    print('accuracy:{0}%',format(accuracy))
    print('prediction:{0}%',format(predictions))
main()