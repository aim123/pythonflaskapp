# -*- coding: utf-8 -*-

import json
import string 
import os
from os.path import join, dirname 
from os import environ 
from flask import Flask, render_template,request
import pandas as pd
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import csv
import itertools
import pickle
import findingIntents
import firstDialog
#filelist=[]
#firstDialog.Dialog()
#findingIntents.findIntent()

 
app = Flask(__name__)


@app.route('/')
def index():
  print "I am in root"  
  return render_template('page1.html')
  
  
@app.route('/upload', methods=['POST']) 
def visualRecog():
  print "in upload"
  if request.method == 'POST':
      for f in request.files.getlist('file'):
      
            f.save(os.path.join("/home/cts565637/intentDetection/IntentDetectionModularcode/code_Flask_server_12_3/dialogs/101/", f.filename))
      
      listofsamplevalue =[]
      listofsamplevalue = firstDialog.Dialog()

  return render_template('page2.html',output=listofsamplevalue)
  
  

@app.route('/visualRecog', methods=['POST'])
def my_link():
    print "in visual Recog"
    #if request.method == 'POST':
    import json
    import string 
    import os
    from os.path import join, dirname 
    from os import environ 
    from flask import Flask, render_template,request
    import pandas as pd
    from nltk.stem import WordNetLemmatizer
    lemmatizer = WordNetLemmatizer()
    import csv
    import itertools
    import pickle
    import findingIntents
    import firstDialog
    firstDialog.Dialog()
    findingIntents.findIntent()
    import python_dependency

    FinallistofIntent,Finallistofentities = python_dependency.pythondependency()
    
    print "total number of Intents detected:",len(FinallistofIntent)
    print "total number of entities detected:",len(Finallistofentities)
    import os, shutil
    folder = '/home/cts565637/intentDetection/IntentDetectionModularcode/code_Flask_server_12_3/dialogs/101/'
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(e)
    
    ## manually doing taxonomy
    
    return render_template('page4.html',objlistintent=FinallistofIntent,objentities=Finallistofentities);


@app.route('/uploadafterchange', methods=['POST']) 
def visualRecoguploadafterchange():
  print "in uploadafterchange"
  if request.method == 'POST':
      entityvalues =[]
      entitycategories = request.form.getlist('entity_cname')
      for i in entitycategories:
          entityvalues_temp =[]
          entityvalues_temp = request.form.getlist(i)
          entityvalues.append(entityvalues_temp)
          
      print "entitycategories in intent server",entitycategories
      print "entityvalues in intent server",entityvalues
      #print "form values" ,request.form
      #print "entity array",request.form.getlist("entity_cname");
      #print "example :",request.form.getlist("tools");
      import pythontestforpage4
      FinallistIntent = pythontestforpage4.FinallistafterChange(entityvalues,entitycategories)
      #print "FinallistIntent in server",FinallistIntent
      import IntentJsonCreation
      outputfilename=IntentJsonCreation.IntentJson(entityvalues,entitycategories)
      outputfilename = outputfilename.split("/")[2] 
      
      print "outputfilename in server",outputfilename
      
  return render_template('page5.html',output1=FinallistIntent, output2=outputfilename)

if __name__ == '__main__':
  #app.run(debug=True)
  app.run(host= '0.0.0.0',port='5612')
