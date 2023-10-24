from datetime import datetime
from urllib.request import urlopen
from datetime import timedelta
from dotenv import load_dotenv,find_dotenv
from pymongo import MongoClient
import math
load_dotenv(find_dotenv())
connection_string = "mongodb+srv://salmen:azerty123456@stage.g7d1vqy.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(connection_string)     
smartGarden=client.smartGarden

link="https://naturetalkers.altervista.org/C0210045/ttcloud.txt"
url= urlopen(link)

#treeListIdTTPlus=['621B0408','621B0400','62190380']
#treeListIdTTWINE=['63210025','64210015','63210030']

tree0TTPlus=smartGarden.tree0TTPlus
tree1TTPlus=smartGarden.tree1TTPlus
tree2TTPlus=smartGarden.tree2TTPlus
cloud=smartGarden.cloud
generalData=smartGarden.generalData

tree0TTWINE55=smartGarden.tree0TTWINE55
tree1TTWINE55=smartGarden.tree1TTWINE55
tree2TTWINE55=smartGarden.tree2TTWINE55

tree0TTWINE49=smartGarden.tree0TTWINE49
tree1TTWINE49=smartGarden.tree1TTWINE49
tree2TTWINE49=smartGarden.tree2TTWINE49

treedicTTPlus={'621B0408':tree0TTPlus,
               '621B0400':tree1TTPlus,
               '62190380':tree2TTPlus
}
treedicTTWine={'63210025':[tree0TTWINE55,tree0TTWINE49],
               '64210015':[tree1TTWINE55,tree1TTWINE49],
               '63210030':[tree2TTWINE55,tree2TTWINE49]
}    
#thermal diffusivity of green wood
thd={'64210015':0.0358646371824824,
     '63210025':0.063051907613087,
     '63210030':0.13898268743410033,

}       
r=0
#lastLineNum=generalData.find_one()["last line number"]
file = url.readlines()#[lastLineNum+1:]
"""tree_0.delete_many({})
tree_1.delete_many({})
tree_2.delete_many({})
cloud.delete_many({})
generalData.delete_many({})

generalData.insert_one({
    "last line number": len(file),
    "number of trees": 3,
})"""
                                  #lastLineNum+
for numLine,line in enumerate(file,1):
    new_line=line.decode().strip()
    L1=new_line.split()
    ch2=L1[1]
    L2=ch2.split(',')
    ch3=L2[1]
    L3=ch3.split(';')
    idTT=L3[0]
    sousidTT=L3[2]
    #up_line=int(L3[1],16)
    d=dict()
    time_str = L1[0].replace('.','/')+" "+L2[0]
    date_format_str = '%d/%m/%y %H:%M:%S'
    given_time = datetime.strptime(time_str, date_format_str)
    d["_id"]=numLine
    d["dateTime"]=given_time-timedelta(hours=1)
    """if idTT in treedicTTPlus:
        #63210025  , 64210015  ,63210030  TTSOL no documents     
        if sousidTT=='55':
            d["deviceType"]=L3[2]
            temperatureRef0=127.6-0.006045*int(L3[4]) + 1.26*(10**-7)*(int(L3[4]))**2 - 1.15*(10**-12)*(int(L3[4]))**3
            temperatureHeat0=127.6-0.006045*int(L3[5]) + 1.26*(10**-7)*(int(L3[5]))**2 - 1.15*(10**-12)*(int(L3[5]))**3
            temperatureRef1=127.6-0.006045*int(L3[17]) + 1.26*(10**-7)*(int(L3[17]))**2 - 1.15*(10**-12)*(int(L3[17]))**3
            temperatureHeat1=127.6-0.006045*int(L3[18]) + 1.26*(10**-7)*(int(L3[18]))**2 - 1.15*(10**-12)*(int(L3[18]))**3
            dTmax=temperatureHeat1-temperatureHeat0
            dTi=temperatureRef1-temperatureRef0
            d["tRef_0(°C)"]=temperatureRef0
            d["tHeat_0(°C)"]=temperatureHeat0
            d["tRef_1(°C)"]=temperatureRef1
            d["tHeat_1(°C)"]=temperatureHeat1
            d["sapFluxDensity(l/dm h)"]=(((dTmax-dTi)/dTmax)*10.43)-0.52
            d["airTemperature(°C)"]=float(int(L3[10])/10)
            d["airHumidity(%)"]=float(L3[9])
            d["batteryVoltage(mV)"]=((2*1100*int(L3[len(L3)-1]))/int(L3[7]))
            d["growthRate(cm)"]=((-30/45000)*float(L3[6]))+66.67
            d["AxOut(deg)"]=(float(L3[11])/1096)*(1/0.9)
            d["AyOut(deg)"]=(float(L3[13])/1096)*(1/0.9)
            d["AzOut(deg)"]=(float(L3[15])/1096)*(1/0.9)
            #(0.000000008*(float(L3[6]))**2)-(0.0016*(float(L3[6]))+89.032)/(-10)
            if idTT=='621B0400':
               tree0TTPlus.insert_one(d)
            elif idTT=='621B0408':
               tree1TTPlus.insert_one(d)
            elif idTT=='62190380':
               tree2TTPlus.insert_one(d)
    
        else:#sousidTT==49 or 4C or 4B
            d["deviceType"]=L3[2]
            d["integrationTime(ms)"]=int(L3[len(L3)-2])*2.8
            d["gain"]=float(L3[len(L3)-1])
            d["absorbedEnergy(kWh/m²)"]=((float(L3[10])*0.4562)+(float(L3[11])*0.6257)+(1.0546*float(L3[12]))+(float(L3[13])*1.0462)+(float(L3[14])*0.8654)+(float(L3[15])*0.7829)-2078.88)/28.0 
            if idTT=='621B0400':
               tree0TTPlus.insert_one(d)
            elif idTT=='621B0408':
               tree1TTPlus.insert_one(d)
            elif idTT=='62190380':
               tree2TTPlus.insert_one(d)"""

    if idTT in treedicTTWine:
        if sousidTT=='55': #4E in the document
            r+=1
            d["deviceType"]=L3[2]
            d["recordNumber"]=int(L3[1],16)
            TDownStream_0=-7*(10**-11)*(int(L3[5]))**3 + 2*(10**-6)*(int(L3[5]))**2-0.0229*int(L3[5])+117.28
            d["TDownStream_0"]=TDownStream_0
            TUpStream_0=-7*(10**-11)*(int(L3[6]))**3 + 2*(10**-6)*(int(L3[6]))**2-0.0229*int(L3[6])+117.28
            d["TUpStream_0"]=TUpStream_0
            TDownStream_1=-7*(10**-11)*(int(L3[12]))**3 + 2*(10**-6)*(int(L3[12]))**2-0.0229*int(L3[12])+117.28
            d["TDownStream_1"]=TDownStream_1
            TUpStream_1=-7*(10**-11)*(int(L3[13]))**3 + 2*(10**-6)*(int(L3[13]))**2-0.0229*int(L3[13])+117.28
            d["TUpStream_1"]=TUpStream_1
            TDownStreamAvg=-7*(10**-11)*(int(L3[15]))**3 + 2*(10**-6)*(int(L3[15]))**2-0.0229*int(L3[15])+117.28
            d["TDownStreamAvg"]=TDownStreamAvg
            TUpStreamAvg=-7*(10**-11)*(int(L3[16]))**3 + 2*(10**-6)*(int(L3[16]))**2-0.0229*int(L3[16])+117.28
            d["TUpStreamAvg"]=TUpStreamAvg
            d["TDownStreamMax"]=-7*(10**-11)*(int(L3[17]))**3 + 2*(10**-6)*(int(L3[17]))**2-0.0229*int(L3[17])+117.28
            d["TUpStreamMax"]=-7*(10**-11)*(int(L3[18]))**3 + 2*(10**-6)*(int(L3[18]))**2-0.0229*int(L3[18])+117.28
            timeTdMax=int(L3[19])*0.001
            d['timeTdMax(ms)']=int(L3[19])
            d["timeTuMax(ms)"]=int(L3[20])
            #pythagore
            ΔTd_avg=((TDownStream_0-TDownStream_1)**2+40**2)**0.5
            ΔTu_avg=((TUpStream_0-TUpStream_1)**2+40**2)**0.5 #=40 always TUpStream_1=TUpStream_0
            #(math.log2(ΔTd_avg/ΔTu_avg)/x)**2 k**2 + (4/timeTdMax) k + (0.5/timeTdMax)**2 = 0
            
            d["batteryVoltage(mV)"]= 650 +131072*(1100/int(L3[8]))
            d["dataResolution"]=int(L3[9])
            d["airRelativeHumidity(%)"]=int(L3[10])
            d["airTemperature(°C)"]=int(L3[11])*0.1
            TSoil_0=-7*(10**-11)*(int(L3[4]))**3 + 2*(10**-6)*(int(L3[4]))**2-0.0229*int(L3[4])+117.28
            TSoil_1=-7*(10**-11)*(int(L3[11]))**3 + 2*(10**-6)*(int(L3[11]))**2-0.0229*int(L3[11])+117.28
            d["TSoil_0(°C)"]=-7*(10**-11)*(int(L3[4]))**3 + 2*(10**-6)*(int(L3[4]))**2-0.0229*int(L3[4])+117.28
            d["TSoil_1(°C)"]=-7*(10**-11)*(int(L3[11]))**3 + 2*(10**-6)*(int(L3[11]))**2-0.0229*int(L3[11])+117.28
            TSoilAvg=(TSoil_0+TSoil_1)/2
            TSoilAvgC=-7*(10**-11)*(TSoilAvg)**3 + 2*(10**-6)*(TSoilAvg)**2-0.0229*TSoilAvg+117.28
            d["TSoilAvg(°C)"]=-TSoilAvg
            EcfSoil=int(L3[14])
            d["EcfSoil(Hz)"]=EcfSoil
            ECf_T=-11.282*TSoilAvgC*2467.3
            ΔECf=EcfSoil-ECf_T
            SVWCAfricanSoil=-4*(10**-12)*(ΔECf)**3+2*(10**-7)*(ΔECf)**2-0.0026*ΔECf+47.409
            SVWCloamySoil=2*(10**-12)*(ΔECf)**3+7*(10**-8)*(ΔECf)**2-0.0039*ΔECf+50.647
            d["SVWCAfricanSoil(%)"]=SVWCAfricanSoil
            d["SVWCloamySoil(%)"]=SVWCloamySoil
            if idTT=='63210025':
               d["heatVelocityMarshall_Burgess(cm/hr)"]=(thd['63210025']/0.5)*math.log2(ΔTd_avg/ΔTu_avg)
               d["heatVelocityMax(cm/hr)"]=(((0.5**2)-4*thd['63210025']*(timeTdMax/3600))**0.5)/(timeTdMax/3600)
               #tree0TTWINE55.insert_one(d)
               print(d)
            elif idTT=='63210030':
               d["heatVelocityMarshall_Burgess(cm/hr)"]=(thd['63210030']/0.5)*math.log2(ΔTd_avg/ΔTu_avg)
               d["heatVelocityMax(cm/hr)"]=(((0.5**2)-4*thd['63210030']*(timeTdMax/3600))**0.5)/(timeTdMax/3600)
               print(d)
               #tree1TTWINE55.insert_one(d)
            elif idTT=='64210015':
               d["heatVelocityMarshall_Burgess(cm/hr)"]=(thd['64210015']/0.5)*math.log2(ΔTd_avg/ΔTu_avg)
               d["heatVelocityMax(cm/hr)"]=(((0.5**2)-4*thd['64210015']*(timeTdMax/3600))**0.5)/(timeTdMax/3600)
               #tree2TTWINE55.insert_one(d)
               print(d)
            if r==2000:
               break   
            """elif sousidTT=='49':
            d["deviceType"]=L3[2]
            d["recordNumber"]=int(L3[1],16)
            d["solarEnergy"]=((float(L3[10])*0.4562)+(float(L3[11])*0.6257)+(1.0546*float(L3[12]))+(float(L3[13])*1.0462)+(float(L3[14])*0.8654)+(float(L3[15])*0.7829)-2078.88)/28.0
            d["integrationTime(ms)"]=int(L3[len(L3)-2])*2.8
            d["gain"]=float(L3[len(L3)-1])
            if idTT=='63210025':
               tree0TTWINE49.insert_one(d)
            elif idTT=='63210030':
               tree1TTWINE49.insert_one(d)
            elif idTT=='64210015':
               tree2TTWINE49.insert_one(d)
    if idTT=='C0210045': 
        if(sousidTT=='4B'): # 4C !! no document
            d["deviceType"]=L3[2]
            d["numberRecords"]=int(L3[4])
            d["dataNotSent"]=int(L3[5])
            d["countryCode"]=216
            d["mobileCountryCODE"]=int(L3[6])
            d["country"]="Tunisia"
            if(int(L3[8])==0):
                d["networkRegistration"]="NO"
            else:
                d["networkRegistration"]="YES"
            d["TTCloudSignalStrength"]=int(L3[9])
            d["batteryLevel(mV)"]=int(L3[10])
            d["firmwareVersion"]=L3[11]
            cloud.insert_one(d)
generalData.update_one({},{"$set":{"last line number":len(file)+lastLineNum}})"""
              