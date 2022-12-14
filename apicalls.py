import requests
import os
import json


#Specify a URL that resolves to your workspace
URL = "http://127.0.0.1:8000/"


with open('config.json','r') as f:
    config = json.load(f) 

model_path = os.path.join(config['output_model_path']) 
test_data_path = os.path.join(config['test_data_path'])


#Call each API endpoint and store the responses

response1 = requests.post(URL+'/prediction', json={'filepath': os.getcwd()+'/'+test_data_path+'/'+'testdata.csv'}).content
response2 = requests.get(URL+'scoring').content
response3 = requests.get(URL+'summarystats').content
response4 = requests.get(URL+'diagnostics').content
res1 = json.loads(response1)
res3 = json.loads(response3)
res4 = json.loads(response4)

#combine all API responses
#responses = #combine reponses here

with open(os.getcwd()+'/'+model_path+'/'+'apireturns.txt', 'w+') as f:
    f.write("API Responses\n")
    f.write('------------------------------------------------\n')
    f.write("Data predictions\n")
    f.write(str(res1))
    f.write('\n------------------------------------------------\n')

    f.write("F1 score\n")
    f.write(response2)
    f.write('\n------------------------------------------------\n')
 
    f.write("Summary for each feature\n")
    f.write("Feature: \t\t Mean \t\t Median \t Std\n")
    for row in res3:
        for i in range(len(row)):
            f.write(str(row[i]) + "\t")
        f.write("\n")
    f.write('\n------------------------------------------------\n')


    f.write("Missing data\n")
    for row in res4['missing_percentage']:
        for i in range(len(row)):
            f.write(str(row[i]) + " ")
        f.write("\n")
    f.write('\n------------------------------------------------\n')

    f.write("Execution time\n")
    for row in res4['execution_time']:
        for i in range(len(row)):
            f.write(str(row[i]) + " ")
        f.write("\n")
    f.write('\n------------------------------------------------\n')

    f.write("Outdated packages: package name - installed version - newest version\n")
    for row in res4['outdated_packages']:
        for i in range(len(row)):
            f.write(str(row[i]))
        f.write("\n")

    f.write('\n------------------------------------------------\n')





