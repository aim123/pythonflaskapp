def FinallistafterChange(entityvalues,entitycategories):    
    import pickle
    FinallistofIntent=open("./FinallistofIntent.pkl",'rb')
    FinallistofIntent = pickle.load(FinallistofIntent)
    #print "FinallistofIntent",FinallistofIntent
    
    #entityvalues = [['drive','laptop','hdb','pc','box','usb','audiodevice'],['opera','chrome'],['ubuntu','windows','xp']]
    #entitycategories = ['device','browser','os']
    #cd,xfree,ubuntu, card mouse driver
#    entityvalues = [['cd','mouse','driver','card'],['ubuntu']]
#    
#    entitycategories = ['device','os']
    
   # entityvalues = [['laptop','mp3','radioclock','server','tool'],['ubuntu','window'],['alarm','app','divx','file','package','playlist','setting','time','utf'],['bed','hotel','locale','work']]
    
    #entitycategories = ['device','os','application','misc']
    #print "FinallistofIntent before name change",FinallistofIntent[1: ]
    
    for i in FinallistofIntent:
        for j in entityvalues:
            entityvalues1=i[0].split('_')
            for k in entityvalues1:
                if ((k.lower()) in j):
                    print "entityvalues.index(j)",entityvalues.index(j)
                    entityvalues1[entityvalues1.index(k)] = entitycategories[entityvalues.index(j)]
            my_lst_str = '_'.join(map(str, entityvalues1))
            i[0] =my_lst_str
            #print "my_lst_str",my_lst_str
                    
        #print "value of i",i[0]
    intentName_Utterance = [] 
    for i in FinallistofIntent:
        for j in i[2]:
            intentName_Utterance.append([j,i[0]])
            
    import pandas as pd     
    df = pd.DataFrame(intentName_Utterance,columns=['Utterance','IntentName'])
    # creating CSV file from intent list dataframe	
    df.to_csv('./IntentName_Utterance_Updated.csv', index=False)
        
    import pickle
    with open('./IntentName_Utterance_Updated_df.pkl', 'wb') as f:
        pickle.dump(df, f)
    
    
    import pickle
    with open('./FinallistofIntentafternamechange.pkl', 'wb') as f:
        pickle.dump(FinallistofIntent, f) 
        
    return FinallistofIntent          
    
    
    #print "FinallistofIntent after name change",FinallistofIntent[1: ]


