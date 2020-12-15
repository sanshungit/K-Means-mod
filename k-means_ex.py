import numpy as np
import pandas as pd


def readData(iopath):
    print('正在读取数据...')
    ioData=pd.read_excel(iopath,
                         names=['srid','srstate','srtype','srtitle','custom','ata','isrnum',
                                'overtime','firstimeval','prio','descri','answer','flightid',
                                'creatime','subtime','apprtime','anstime','reqanstime']
                        )
    print('数据读取完成！')
    return ioData

def distEclud(A,B):
    return np.abs(A-B)

def randCent(dataSet,k):#以随机的方式生成k个初始点
    centId=np.mat(np.zeros((k,1)))
    minI=np.min(dataSet[:])
    maxI=np.max(dataSet[:])
    rangeI=maxI-minI
    centId=minI+rangeI*np.random.rand(k,1)
    return centId

def kMeans(dataSet,k,distMean=distEclud,creatCent=randCent):
    sam_s=np.shape(dataSet)[1]
    clusterArray=np.mat(np.zeros((sam_s,2)))
    centId=np.array([[4],[48],[72],[120],[240],[480]])#指定k=6个初始点
    clusterAlt=True
    while clusterAlt:
        clusterAlt=False
        for i in range(sam_s):
            minDist=np.inf
            minIndex=-1
            for j in range(k):
                distJI=distMean(centId[j,0],dataSet[0,i])
                if distJI<=minDist:
                    minDist=distJI
                    minIndex=j
            if clusterArray[i,0] !=minIndex:
                clusterAlt==True
            clusterArray[i,:]=minIndex,minDist**2
        for cent in range(k):
            ifInClust=dataSet[0,np.nonzero(clusterArray[:,0].A==cent)[0]]
            centId[cent,:]=np.mean(ifInClust,axis=1)
    return centId,clusterArray
    
if __name__=='__main__':
    ioPath='./Data/input_sr.xlsx'
    ioData=readData(ioPath)
    for colname in ['creatime','subtime','apprtime','anstime','reqanstime'] :
        ioData[colname]=pd.to_datetime(ioData[colname])
    timeVal=ioData['anstime']-ioData['creatime']
    newtimeVal=np.mat(timeVal.apply(lambda x:x.total_seconds()/3600)) #转换时间单位为Hour
    fiCenterId,fiClusterArr=kMeans(newtimeVal,6)
    print(fiCenterId)
