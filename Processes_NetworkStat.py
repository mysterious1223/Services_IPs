import os
import sys
import subprocess

procs = []

def getIP_PORT(pid):
    ipport="NO NET"
    try:
        ipport=subprocess.check_output("netstat -plant | grep "+pid,stderr=subprocess.STDOUT,shell=True)
    except:
        return ipport
    return ipport
def getpname(path):
    name=subprocess.check_output("head -n 1 "+path+"/status",stderr=subprocess.STDOUT,shell=True)
    return name[5::]

for f in os.listdir("/proc/"):
    if os.path.isdir("/proc/"+f):
        if f.isdigit():
            procs.append("/proc/"+f)

for p in procs:
    print p + " - " + getpname(p)
    pid = p[6::]
    print getIP_PORT(pid)
    
