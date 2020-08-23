# from boom.boom import load,calc_stats
# from datetime import datetime



# count =100
# domain  =  "https://b-api.ir/testspeed/path"
# print('domain:::::::::',domain)
# t1 = datetime.now()
# res = load(domain, int(count), 10, 0, 'GET', None, 'text/plain', None) #quiet=True
# print('errors : ',res.errors)
# totalTime = datetime.now() - t1
# data =calc_stats(res)
# print(data)
# print('Total time :',totalTime)


import subprocess
import re
from pprint import pprint
import  json
from datetime import datetime

def CleanLine(line):
    cleanLine = re.sub(r"\s+", "",line)
    splitLine = cleanLine.split(":")
    return splitLine[1]

def RemoveWord(data):
    words=["bytes","[#/sec](mean)","[Kbytes/sec]received","seconds",'[K/sec]received']
    removedata = data 
    for word in words:
        if word in removedata:
            removedata = data.replace(word,'')
    return removedata

def NumberDetect(data):
    matchNumber = []
    regex = r"[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?"
    matches = re.finditer(regex, data)  
    for matchNum, match in enumerate(matches, start=1):
        matchNumber.append(float(match.group()))
    return matchNumber

finalResult ={}
result = subprocess.run(["ab", "-n","10","-c","10","https://b-api.ir/testspeed/path"],stdout=subprocess.PIPE)
lines = str(result.stdout).split("\\n")
print("hi")
for line in lines:
        print(line)
        if "Server Software" in line:
            finalResult['webServer'] = CleanLine(line)
        elif "Server Hostname" in line: 
            finalResult['hostName'] = CleanLine(line)
        elif "Server Port" in line:
            finalResult['port'] = CleanLine(line)
        elif "Document Path" in line:
            finalResult['path'] = CleanLine(line)
        elif "Document Length" in line :
            data = CleanLine(line)
            finalResult['length'] = float(RemoveWord(data))
        elif "Concurrency Level" in line:
            finalResult['concurrency'] = CleanLine(line)
        elif "Time taken for tests" in line: 
            data = CleanLine(line)
            finalResult['totalTime'] = float(RemoveWord(data))
        elif "Complete requests" in line : 
            finalResult['completeReq'] = int(CleanLine(line))
        elif "Failed requests" in line : 
            finalResult['failedReq'] = int(CleanLine(line))
        elif "Total transferred" in line :
            data = CleanLine(line)
            finalResult['totalTransfer'] = float(RemoveWord(data))

        elif "HTML transferred" in line :
            data = CleanLine(line)
            finalResult['htmlTransfer'] = float(RemoveWord(data))
            
        elif "Requests per second" in line :
            finalResult['rps'] = float(RemoveWord(CleanLine(line)))

        elif "Transfer rate" in line:
            data = CleanLine(line)
            finalResult['transferRate'] = float(data.replace('[Kbytes/sec]received',''))
        elif "Connect:" in line : 
            data = line.split(":")
            # print(data)
            finalResult['CTconnect'] = NumberDetect(data[1])
        elif "Processing" in line : 
            data = line.split(":")
            finalResult['CTprocessing'] = NumberDetect(data[1])
        elif "Waiting" in line : 
            data = line.split(":")
            finalResult['CTwaiting'] = NumberDetect(data[1])
        elif "Total" in line : 
            data = line.split(":")
            finalResult['CTtotal'] = NumberDetect(data[1])
        elif "50%" in line : 
            data = line.split("%")
            finalResult['p50'] =NumberDetect(data[1])
        elif "66%" in line : 
            data = line.split("%")
            finalResult['p66'] =NumberDetect(data[1])
        elif "75%" in line : 
            data = line.split("%")
            finalResult['p75'] =NumberDetect(data[1])
        elif "80%" in line : 
            data = line.split("%")
            finalResult['p80'] =NumberDetect(data[1])
        elif "90%" in line : 
            data = line.split("%")
            finalResult['p90'] =NumberDetect(data[1])
        elif "100%" in line : 
            data = line.split("%")
            finalResult['p100'] =NumberDetect(data[1])


jsonData ={
    'date' : datetime.now(),
    'result' : finalResult
}
#TODO : Insert to database
# with open('boOom.json','a+') as json_file:
#     data = json.load(json_file.readlines())
#     data.update(jsonData)
#     json_file.write(data)

    





pprint(jsonData)