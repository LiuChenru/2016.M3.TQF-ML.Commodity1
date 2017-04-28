# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 11:00:00 2017

@author: Angelina
"""

def getCount(begin_dt,end_dt,SplInfo):
    
    SplInfo1=SplInfo[SplInfo['time']<end_dt]
    SplInfo1=SplInfo1[SplInfo1['time']>begin_dt]
    
    if(len(SplInfo1)>0):
        SplInfo1=SplInfo1.sort_values(by=['user_id','sku_id','type'])
        SplGroup=SplInfo1.groupby(['user_id','sku_id','type'])
        SplCount=SplGroup.apply(len)
        SplCount=SplCount.unstack(level=2)
        SplCount=SplCount.fillna(0)
        return SplCount
    else:
        print('no data')

        
        os.chdir(folder_proc)
"""
Mon='Mar'
time='5'
csvName=Mon+time+"weight.csv"
"""
def getPinfo(Mon, time, csvName):
    
    os.chdir(folder_proc)    
    OriDF=pd.read_csv(csvName)
    del OriDF['Unnamed: 0']
    OriDF['PIntNum']=OriDF['Num1']+OriDF['Num2']+OriDF['Num3']+OriDF['Num4']+OriDF['Num5']+OriDF['Num6']
    
    tempDF=OriDF.copy()
    del tempDF['UID']
    
    ##只交互过一次，两次，三次的用户
    tempDF['PInt1']=(tempDF['PIntNum']==1)
    tempDF['PInt2']=(tempDF['PIntNum']==2)
    tempDF['PInt3']=(tempDF['PIntNum']==3)
    tempDF['buyUNum']=(tempDF['Num4']>0)
    
    #只点击过一次的用户
    tempDF['PClick1']=(tempDF['Num6']==1)
    tempDF['activeUNum']=(tempDF['Num6']>=3)
    
    ##买过一次，两次的用户
    tempDF['buyUNum']=(tempDF['Num4']>0)
    tempDF['buyMoreNum']=(tempDF['Num4']>1)
    #访问的人数
    tempDF['visitUNum']=(tempDF['Num1']>0)
    
    PGroup=tempDF.groupby('PID')
    Pinfo1=PGroup.apply(sum,axis=0)
    del Pinfo1['PID']
    Pinfo2=PGroup.apply(len)
    Pinfo2=pd.DataFrame(Pinfo2,columns=['PUNum'])
    Pinfo=pd.merge(Pinfo1,Pinfo2,left_index=True,right_index=True)
    
    ###人均点击次数----
    Pinfo['Num1PP']=Pinfo['Num1']/Pinfo['PUNum']
    Pinfo['Num2PP']=Pinfo['Num2']/Pinfo['PUNum']
    Pinfo['Num3PP']=Pinfo['Num3']/Pinfo['PUNum']
    Pinfo['Num4PP']=Pinfo['Num4']/Pinfo['PUNum']
    Pinfo['Num5PP']=Pinfo['Num5']/Pinfo['PUNum']
    Pinfo['Num6PP']=Pinfo['Num6']/Pinfo['PUNum']
    Pinfo['IntPP']=Pinfo['PIntNum']/Pinfo['PUNum']
    Pinfo['activeUR']=Pinfo['activeUNum']/Pinfo['PUNum']
    
    
    #各种转化率，比如购买一次需要的点击数，对于每个商品
    Pinfo['1to4PR']=Pinfo['Num4']/Pinfo['Num1']
    Pinfo['2to4PR']=Pinfo['Num4']/Pinfo['Num2']
    Pinfo['3to4PR']=Pinfo['Num4']/Pinfo['Num3']
    Pinfo['5to4PR']=Pinfo['Num4']/Pinfo['Num5']
    Pinfo['6to4PR']=Pinfo['Num4']/Pinfo['Num6']
    
    #返客率
    Pinfo['BuyMoreR']=Pinfo['buyMoreNum']/Pinfo['Num4']
    
    
    
    inVars=['Num%d' %num for num in np.arange(1,7)]
    Pinfo=Pinfo.rename(columns={invar:invar+'TP' for invar in inVars})
    #del Pinfo['PID']
    Pinfo.to_csv(Mon+time+'weightPinfo.csv')       
    return Pinfo
    
"""
Mon='Mar'
time='30'
csvName=Mon+time+"weight.csv"
"""
def getUinfo(Mon,time,csvName):
    os.chdir(folder_proc)
    OriDF=pd.read_csv(csvName)
    del OriDF['Unnamed: 0']
    OriDF.fillna(0)
    OriDF['UIntNum']=OriDF['Num1']+OriDF['Num2']+OriDF['Num3']+OriDF['Num4']+OriDF['Num5']+OriDF['Num6']
    
    tempDF=OriDF.copy()
    del tempDF['PID']
    
    ##只交互过一次，两次，三次的商品
    tempDF['UInt1']=(tempDF['UIntNum']==1)
    tempDF['UInt2']=(tempDF['UIntNum']==2)
    tempDF['UInt3']=(tempDF['UIntNum']==3)
    
    #只点击过一次的商品
    tempDF['UClick1']=(tempDF['Num6']==1)
    
    UGroup=tempDF.groupby('UID')
    Uinfo1=UGroup.apply(sum,axis=0)
    del Uinfo1['UID']
    Uinfo2=UGroup.apply(len)
    Uinfo2=pd.DataFrame(Uinfo2,columns=['UPNum'])
    Uinfo=pd.merge(Uinfo1,Uinfo2,left_index=True,right_index=True)
    
    ###每个人点击商品的平均次数
    Uinfo['Num1PU']=Uinfo['Num1']/Uinfo['UPNum']
    Uinfo['Num2PU']=Uinfo['Num2']/Uinfo['UPNum']
    Uinfo['Num3PU']=Uinfo['Num3']/Uinfo['UPNum']
    Uinfo['Num4PU']=Uinfo['Num4']/Uinfo['UPNum']
    Uinfo['Num5PU']=Uinfo['Num5']/Uinfo['UPNum']
    Uinfo['Num6PU']=Uinfo['Num6']/Uinfo['UPNum']
    Uinfo['IntPU']=Uinfo['UIntNum']/Uinfo['UPNum']
    #Uinfo['UID']=Uinfo.index
    
    #各种转化率，比如购买一次需要的点击数,对于每个人来说
    Uinfo['1to4UR']=Uinfo['Num4']/Uinfo['Num1']
    Uinfo['2to4UR']=Uinfo['Num4']/Uinfo['Num2']
    Uinfo['3to4UR']=Uinfo['Num4']/Uinfo['Num3']
    Uinfo['5to4UR']=Uinfo['Num4']/Uinfo['Num5']
    Uinfo['6to4UR']=Uinfo['Num4']/Uinfo['Num6']
    
    inVars=['Num%d' %num for num in np.arange(1,7)]
    Uinfo=Uinfo.rename(columns={invar:invar+'TU' for invar in inVars})
    
    Uinfo.to_csv(Mon+time+'weightUinfo.csv')
    return Uinfo   
    

Mon='Feb'
def getPUTinfo(Mon,begin_dt,end_dt,hold_time):

    os.chdir(folder_action)
    SplInfo=pd.read_csv('Spl%sInfo.csv' %Mon)
    del SplInfo['Unnamed: 0']
        
    os.chdir(folder_proc)
    SplInfo1=SplInfo[(SplInfo['time']<end_dt)&(SplInfo['time']>begin_dt)]
    
    SplInfo1=SplInfo1.sort_values(by=['user_id','sku_id','type'])
    SplInfoGroup=SplInfo1.groupby(['user_id','sku_id','type'])
    
    def getLastTime(Data):
        temp=Data.sort_values(by='time',ascending=False)
        return temp['time'].iloc[0]
    
    def getFirstTime(Data):
        temp=Data.sort_values(by='time')
        return temp['time'].iloc[0]
    
    
    
    LastDF=SplInfoGroup.apply(getLastTime)
    Day=LastDF.apply(lambda x:x[8:10])
    
    lastDF=LastDF.unstack(level=2)
    lastDF.to_csv('Feb%dlastTime.csv' %hold_time) 

    DayDF=Day.unstack(level=2)
    DayDF.to_csv('Feb%dlastDay.csv'%hold_time)
    
    FirstDF=SplInfoGroup.apply(getFirstTime)
    Day=FirstDF.apply(lambda x:x[8:10])
    
    FirstDF=FirstDF.unstack(level=2)
    FirstDF.to_csv('Feb%dFirstTime.csv' %hold_time) 

    DayDF=Day.unstack(level=2)
    DayDF.to_csv('Feb%dFirstDay.csv'%hold_time)

"""
os.chdir(folder_action)
Mon='Mar'
time=5
begin_dt='2016-03-27'
end_dt='2016-04-02'
"""
def getPUInterInfo(Mon,time,begin_dt,end_dt):

    cvsName='Spl%sInfo.csv' %Mon
    SplInfo1=pd.read_csv(folder_action+cvsName)
    del SplInfo1['Unnamed: 0']
     
    SplInfo=SplInfo1[(SplInfo1['time']<end_dt)&(SplInfo1['time']>begin_dt)]
    SplInfo['day']=SplInfo['time'].apply(lambda x:x[8:10])
    
    del SplInfo1
    
    os.chdir(folder_proc)
    
    SplDay=SplInfo[['user_id','sku_id','day']]
    SplDay=SplDay.sort_values(['user_id','sku_id'])
    SplInfoGroup=SplDay.groupby(by=['user_id','sku_id'])
    del SplDay
    
    InterDays=SplInfoGroup.apply(lambda x:len(x['day'].unique()))
    InterDays1=pd.DataFrame(InterDays,columns=['InterDays'])
    InterDays1['ItDayR']=InterDays1['InterDays']/time
      
    del SplInfoGroup
             
           
    del SplInfo['time']
    SplInfo=SplInfo.sort_values(['user_id','sku_id'])
    SplGroup=SplInfo.groupby(['user_id','sku_id','type'])
    DayInfo=SplGroup.apply(lambda x:len(x['day'].unique()))
    DayInfo=DayInfo.unstack(level=2)
    DayInfo=pd.merge(DayInfo,InterDays1,left_index=True,right_index=True,how='outer')
    DayInfo['It2BuyR']=DayInfo[4]/DayInfo['InterDays']
    
    os.chdir(folder_proc)
    DayInfo.to_csv('%s%dActiveDay.csv' %(Mon,time))
    
    del InterDays
    del SplInfo
    del UCol
    del PCol
    del index
    
    
    
