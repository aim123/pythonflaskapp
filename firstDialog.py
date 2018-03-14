def Dialog():
    import os, subprocess
    src = "./dialogs/"
    dst_can = "./f6/"
    import pickle
    listOfFiles = os.listdir(src)
    import pandas as pd
    import csv
    
    df = pd.DataFrame() 
    ques_list=[]
    df_temp = []
    var = 0
    column_names = ['time','sender','reciever','message']
    for folder in listOfFiles:
        for file1 in os.listdir(src+'/'+folder):
        	if (var<=100):
        	    try:
        	    	#print file1
        	    	f = open(src+'/'+folder+'/'+file1,"r")
        	    	#print(f.read())
        	    	var = var+1
        	    	print var
        	    	df_temp=pd.read_csv((src+'/'+folder+'/'+file1), sep='\t', lineterminator='\n', encoding='utf-8',names = column_names)
        	    	no_reciever = df_temp[df_temp['reciever'].isnull()]  
        	    	ques=no_reciever['message']
        	    	ques=list(ques)
        	    	res = ". ".join(ques)
        	    	ques_list.append(res)
        	    	df=df.append(df_temp,ignore_index=True)
        	    
        	    except :
                     pass
                
    
    
    with open("./Questions10000.csv", 'wb') as myfile:
    	wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    	wr.writerow([unicode(s).encode("utf-8") for s in ques_list])
    
    with open('questions10000.pkl', 'wb') as f:
        pickle.dump(ques_list, f)
        
    #print "df_temp",df_temp
    print "first doc values",[df_temp['time'].iloc[0],df_temp['sender'].iloc[0],df_temp['reciever'].iloc[0],df_temp['message'].iloc[0]]
    return [df_temp['time'].iloc[0],df_temp['sender'].iloc[0],df_temp['reciever'].iloc[0],df_temp['message'].iloc[0]]