# -*- coding: utf-8 -*-
"""
Created on Mon Mar 05 11:16:46 2018

@author: 509868
"""

def findIntent():
    import csv
    from itertools import chain
    import httplib2
    from oauth2client.client import GoogleCredentials
    from googleapiclient import discovery
    import os
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./BankerChat-e66b473d6e85.json"
    DISCOVERY_URL = ('https://language.googleapis.com/$discovery/rest?version=v1')
    import re
    from nltk.tokenize import sent_tokenize
    emoticons = [
		":-(", ":(", ":-|", 
		";-(", ";-<", "|-{",
		":-)",":)", ":o)",
		":-}", ";-}", ":->",
		";-)",
		":(", ":(", ":|", 
		";(", ";<", "|{", ":o)",
		":}", ";}", ":>",
		";)","&amp;","pls","lol","->","<-",":"]
            
    ques_keywords=['what','when', 'how','where', 'which','why','who']
    def remove_junk(text):
        for word in text.split(' '):
            if word in emoticons:
				#print "found"
                text=text.replace(word, " ")
                
        line = re.sub('\.\.+', '.', text)
        sent_tokenize_list = sent_tokenize(line)
        sent_tokenize_list = list(set(sent_tokenize_list))
        return sent_tokenize_list
        
    def get_questions(text_list):
        question_sent=[]
        for i in text_list:
            sent_list=i.split(' ')
            if any(word in sent_list for word in ques_keywords) or any(word=='?' for word in i):
                question_sent.append(i)
                
        return question_sent
        
    def getSyntax(text):
        http = httplib2.Http()
		
        credentials = GoogleCredentials.get_application_default().create_scoped(
			['https://www.googleapis.com/auth/cloud-platform'])
		
        http=httplib2.Http()
        credentials.authorize(http)
		#print("Authorization done!!")
        service = discovery.build('language', 'v1',
								http=http, discoveryServiceUrl=DISCOVERY_URL)
        service_request = service.documents().analyzeSyntax(
		body={
			'document': {
				'type': 'PLAIN_TEXT',
				'content': text
			}
		})
  
        response = service_request.execute()
        import time
        timestr = time.strftime("%Y%m%d-%H%M%S")
        print ("------------------ Question :", text)
        import json
        with open("./dependency_google/"+timestr+'.json', 'w') as outfile:
            json.dump(response, outfile)

	
    with open('./Questions10000.csv', 'r') as f:
		
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            print "len row",len(row)
            for column in row[0:5000]:
                #print (column,'------------')
                try:
                    sent_tokenize_list=remove_junk(column)
				    #print "sent_tokenize_list",sent_tokenize_list
                    final_list= get_questions(sent_tokenize_list)
                    print "final_list",final_list

                    for i in final_list:
                        #i = re.sub(r"http\S+", "", i)
                        question=i.split(' ')
                        if any(word in question for word in ques_keywords) or any(word=='?' for word in i):
                            getSyntax(i)                         

                except:
                    pass
