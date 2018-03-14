"""
Created on Wed Mar 07 13:23:39 2018

@author: 509868
"""

def pythondependency():
    import os
    import json
    import pandas as pd
    import csv 
    src = "./dependency_google/"
    
    listOfFiles = os.listdir(src)
    
    ques_list=[]
    var = 0
    
    
    for file1 in listOfFiles:
        if (var<=10000):
            try:
            #print file1
                f = open(src+'/'+file1,"r")
            #print(f.read())
                var = var+1
                print var
                
                word_details = []
                data = json.load(f)
                #print ("tokens")
                tokens=data["tokens"]
                #print ("tokens", len(data["tokens"]))
                for tk in tokens:
                    token_detail=[]
                    #print("tag: " ,tk["partOfSpeech"]["tag"])
                    #if ((tk["partOfSpeech"]["tag"] =='VERB') or (tk["partOfSpeech"]["tag"] =='NOUN')or (tk["partOfSpeech"]["label"] =='DOBJ')):
                    if ((tk["partOfSpeech"]["tag"] =='VERB') or (tk["partOfSpeech"]["tag"] =='NOUN')):
                        token_detail.append(tk["partOfSpeech"]["tag"])
                        token_detail.append(tk["dependencyEdge"]["label"])
                        token_detail.append(tk["dependencyEdge"]["headTokenIndex"])
                        #token_detail.append(tk["text"]["content"])
                        token_detail.append(tk["lemma"])
                        word_details.append(token_detail)
                        
                
                ques_list.append([data["sentences"][0]["text"]["content"],word_details])
    
            except :
                pass
    # for empty folder            
    import os, shutil
    folder = './dependency_google/'
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(e)  
            
                  
    #print ques_list            
    lst_re_aux_root = [] 
    lst_re_aux_root_pre = [] 
    
    import copy        
    for value in ques_list:
        count =0
        value_remove = copy.deepcopy(value[1])
        for valelement in value[1]:
            root_verb_index = ''
            count = count+1
            if ((valelement[0]=='VERB') and (valelement[1]=='ROOT')):
                if(valelement[3].lower() in ['can','could','may','might','do','did','must','shall','should','will','would','have','had','has','is','am','are','be']):
                    value_remove.remove(valelement)
                    root_verb_index = valelement[2]
                    #print root_verb_index
                    
            if ((valelement[0]=='VERB') and ((valelement[1]=='AUX') or (valelement[1]=='AUXPASS'))):
                value_remove.remove(valelement)
            
            if ((valelement[0]=='VERB') and (valelement[3] in ['wouldnt','can','could','do','did','may','might','must','shall','should','will','would','have','had','has','is','am','are','be'])):
                if(valelement[1] != 'ROOT' and valelement[1] != 'AUX' and valelement[1] != 'AUXPASS'):
                    value_remove.remove(valelement)
                    
            if (root_verb_index != ''):
                for valelement1 in value[1]:
                    if ((valelement1[0]=='NOUN')):
                        if (valelement1[2]==root_verb_index):
                            value_remove.remove(valelement1)
                            
        lst_re_aux_root_pre.append([value[0],value_remove])
                    
    
    
    print lst_re_aux_root_pre
    for value in lst_re_aux_root_pre:
        nsubjlist =list(row[3] for row in value[1] if row[1] =='NSUBJ')
        print "nsubjlist",len(nsubjlist)
        if (len(nsubjlist)>0):
            verblist =list(row[3] for row in value[1] if row[0] =='VERB')
            print "verblist",len(verblist)
            if (len(verblist)>1):
            
            #value_remove = copy.deepcopy(value[1])
                for valelement in value[1]:
                    root_verb_index_1=''
                    print "root_verb_index_1",root_verb_index_1
                    if ((valelement[0]=='VERB') and (valelement[1]=='ROOT')):
                        root_verb_index_1 = valelement[2]
                        print "root_verb_index_1",root_verb_index_1
                        for valelement1 in value[1]:
                            if ((valelement1[0]=='NOUN') and (valelement1[1]=='NSUBJ')):
                                print "valelement1",valelement1
                                if (valelement1[2]==root_verb_index_1):
                                    print 'valelement1',valelement1
                                    print 'valelement',valelement
                                    value[1].remove(valelement1)
                                    value[1].remove(valelement)
                    else:
                        if ((valelement[0]=='NOUN') and (valelement[1]=='NSUBJ')):
                            print "valelement1 else1",valelement
                            value[1].remove(valelement)
            
            else:
                for valelement in value[1]:
                    root_verb_index_1=''
                    print "root_verb_index_1 in else2",root_verb_index_1
                    if ((valelement[0]=='VERB') and (valelement[1]=='ROOT')):
                        root_verb_index_1 = valelement[2]
                        print "root_verb_index_1",root_verb_index_1
                        for valelement1 in value[1]:
                            if ((valelement1[0]=='NOUN') and (valelement1[1]=='NSUBJ')):
                                print "valelement1",valelement1
                                if (valelement1[2]==root_verb_index_1):
                                    print 'valelement1',valelement1
                                    print 'valelement',valelement
                                    value[1].remove(valelement1)
                    else:
                        if ((valelement[0]=='NOUN') and (valelement[1]=='NSUBJ')):
                            print "valelement1 else3",valelement
                            value[1].remove(valelement)
                        
                        
    
    
        
    
    import pickle
    with open('./intentList.pkl', 'wb') as f:
        pickle.dump(lst_re_aux_root_pre, f)          
    import pickle
    myFile=open("./intentList.pkl",'rb')
    myList1 = pickle.load(myFile)
    intent_name_and_utternace = []
    listofentities = []
    for value in myList1:
        tempList=[]
        for valelement in value[1]:
            if ((valelement[0]=='VERB') and (valelement[1]=='ROOT')):
                verb_headerindex = valelement[2]
                intent_name = valelement[3]
                
                for j in value[1]:
                     if ((j[0] =='NOUN') and (j[2] == verb_headerindex) and (j[3].lower() not in ['someone','somebody','anyone','anybody'])):
                         listofentities.append(j[3])
                         intent_name = intent_name +'_'+ j[3]

                tempList.append(([value[0],intent_name]))
                #intent_name_and_utternace.append([value[0],intent_name])
                
            if ((valelement[0]=='VERB') and (valelement[1] != 'ROOT')):
                intent_name1 = valelement[3]
                index_verb = value[1].index(valelement) +1
                #print 'index values',value[1][index_verb : ]
                for j in value[1][index_verb : ]:
                    
                    if (j[0]=='VERB'):
                        #print value[0],intent_name
                        break
                    elif ((j[0] =='NOUN') and (j[3].lower() not in ['someone','somebody','anyone','anybody'])):
                        listofentities.append(j[3])
                        intent_name1 = intent_name1 +'_'+ j[3]
                        
                #validaintent = intent_name.split('_')
                tempList.append(([value[0],intent_name1]))
                
        #print "at line 178",tempList
        import copy
        tempListcopy = copy.deepcopy(tempList)
        if(len(tempList)>1):
            for i in tempList:
                if(len(i[1].split("_"))==1):
                    #print "at line 181",i
                    tempListcopy.remove(i)
        else:
            for i in tempListcopy:
                if(len(i[1].split("_"))==1):
                    #print "at line 181",i
                    #tempListcopy.remove(i)
                    i[1] ='IncompleteIntent'
                    #print "at line 183",tempListcopy
                    
        intent_name_and_utternace.append(tempListcopy)
            
    
    # creating dataframe of intent list		
    import itertools
    chain = itertools.chain(*intent_name_and_utternace)
    intent_name_and_utternace_new = list(chain)
    
    listofintentname=list(row[1] for row in intent_name_and_utternace_new)
    
    #print "listofintentname",listofintentname
    from collections import Counter
    tupleoflistcount = Counter(listofintentname)
    
    abc = list(tupleoflistcount.items())
    
    sortedlistofIntent = sorted(abc, key=lambda tup:(-tup[1], tup[0]))
    #print "sorted ",sortedlistofIntent
    FinallistofIntent =list(list(row) for row in sortedlistofIntent)
    
    
    for i in FinallistofIntent:
        temputterancelist=[]
        for j in intent_name_and_utternace_new:
            if (i[0]==j[1]):
                temputterancelist.append(j[0])
        i.append(temputterancelist)
                
                
    print "FinallistofIntent",FinallistofIntent
    
    Finallistofentities = list(set(listofentities))
    Finallistofentities=[item.lower() for item in Finallistofentities]
    Finallistofentities = list(set(Finallistofentities))
    print "Finallistofentities",Finallistofentities
    
    import pickle
    with open('./FinallistofIntent.pkl', 'wb') as f:
        pickle.dump(FinallistofIntent, f) 
        
    df = pd.DataFrame(intent_name_and_utternace_new,columns=['Utterance','IntentName'])
    # creating CSV file from intent list dataframe	
    df.to_csv('./IntentName_Utterance.csv', index=False)
    
    
    return FinallistofIntent,Finallistofentities
    
