# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 12:26:48 2018

@author: 509868
"""

def IntentJson(entityvalues,entitycategories):
    import json
    import pandas as pd
    myDf=pd.read_csv('./IntentName_Utterance_Updated.csv')
    data = {
	"versionId": "0.1",
	"name": "sampleJson",
	"desc": "prototype sample json",
	"culture": "en-us",}
    intents=[]
    entities=[]
    utterances=[]
    intentList=[]
    entityList=[]
    #entityvalues = [['laptop','mp3','radioclock','server','tool'],['ubuntu','window'],['alarm','app','divx','file','package','playlist','setting','time','utf'],['bed','hotel','locale','work']]
    
    #entitycategories = ['device','os','application','misc']
    for index, row in myDf.iterrows():
        if(row[1]!="IncompleteIntent"):
            intent= row[1].split("_")[0]
            intentList.append(intent) 
		
		
            entity=row[1].split("_")[1:]
            entityList.append(entity)
	
            temp_utterance={}
            temp_utterance["text"]=row[0]
            temp_utterance["intent"]=intent
            text_entity=[]
            for ent in entity:
                print("utterance :" ,row[0])
                print("ent :" ,ent)
                temp_text_entity={}
                temp_text_entity["entity"]=ent
                genericEntity_index =entitycategories.index(ent) if ent in entitycategories else None
                if(genericEntity_index==None):
                    temp_text_entity["startPos"]=row[0].lower().index(ent.lower())
                    temp_text_entity["endPos"]=row[0].lower().index(ent.lower()) + len(ent.lower()) - 1
                else:
                    print("@@ genericEntity_index :", genericEntity_index)
                    simple_entity=[i for i in entityvalues[genericEntity_index] if i in row[0].lower()][0].lower()
                    temp_text_entity["startPos"]=row[0].lower().index(simple_entity)
                    temp_text_entity["endPos"]=row[0].lower().index(simple_entity) + len(simple_entity) - 1
                text_entity.append(temp_text_entity)
                temp_utterance["entities"]=text_entity
                utterances.append(temp_utterance)
                
    for i in set(intentList):
        temp_intent={}
        temp_intent["name"]=i
        intents.append(temp_intent)
        
    for i in set([item for sublist in entityList for item in sublist]):
        temp_entity={}
        temp_entity["name"]=i
        entities.append(temp_entity)
        
    data["intents"]=intents
    data["entities"]=entities
    data["utterances"]=utterances      


    import datetime
    filename1 = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    outputfilename="./static/Output_%s.json"%(filename1)
    with open(outputfilename, 'w') as outfile:
        json.dump(data, outfile,indent = 4)
    print ("Woopie")
    return outputfilename