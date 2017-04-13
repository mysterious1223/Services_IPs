import os
import subprocess
import sys

count = 0
serviceObjects = []


class service_obj:
    servicename=""
    datastring=""
    def __init__ (self,service,data):
        self.servicename = service
        self.datastring = data



def getServices(count):
    _services = []
    for line in services.split("\n"):
        if "?" not in line:
            if len(line)>0:
                #print line[8::]
                count +=1
                _services.append(line[8::])

    return _services
def getNetStuff(service):
    cmd = "netstat -plant | grep "+service
    try:
        netstuff = subprocess.check_output(cmd, stderr=subprocess.STDOUT,shell=True)
    except:
        netstuff="NULL"
    return netstuff
def create_objects(count):
    #get services into array
    myServices = []
    myServices = getServices(count)

    for service in myServices:
        stuff = getNetStuff(service)
        obj = service_obj(service, stuff)
        serviceObjects.append(obj)
        print "-------------------------------------------------\n["+obj.servicename + "]:\n" +obj.datastring + "\n\n"





#if len(sys.argv) < 2:
 #   print "[NO ARGUMENTS SUPPLIED]: LIVE |NOTLIVE"
#elif len(sys.argv) == 2:
    #check
 #  if str(sys.argv[1]) == "LIVE":
  #     print "ALL LIVE CONNECTIONS"
   #if str(sys.argv[1]) == "NOTLIVE":
    #   print "ALL NOT LIVE CONNECTIONS"



services = subprocess.check_output("service --status-all | grep '+'",stderr=subprocess.STDOUT,shell=True)
#print services

#getServices(count)


create_objects(count)
#objects have been created
