import numpy as np
import pandas as pd

def distEclud(A,B):
    return np.sqrt(sum(np.power(A-B,2)))

def randCent(dataSet,k):
    n=np.shape(dataSet)[1]
    centId=np.mat(np.zeros(k,n))
    for i in range(n):
        minI=np.min(dataSet[:,i])
        maxI=np.max(dataSet[:,i])
        rangeI=maxI-minI
        centId=minI+rangeI*np.random.rand(k,1)
    return centId

def kMeans(dataSet,k,distMean=distEclud,creatCent=randCent):
    sam_s=np.shape(dataSet)[0]
    clusterArray=np.mat(np.zeros(m,2))
    centId=creatCent(dataSet,k)
    clusterAlt=True
    while clusterAlt:
        clusterAlt=False
        for i in range(sam_s):
            minDist=np.inf
            minIndex=-1
            for j in range(k):
                distJI=distMean(centId[j,:],data[i,:])
                if distJI<minDist:
                    minDist=distJI
                    minIndex=j
            if clusterArray[i,0] !=minIndex:
                clusterAlt=Y=True
            clusterArray[i,:]=minIndex,minDist**2
        for cent in range(k):
            ifInClust=dataSet(np.nonzero(clusterArray[:,0].A==cent)[0])
            centId=np.mean(ifInClust,axis=0)
    return centId,clusterArray
    
