'''
Created on 10 May 2015

@author: will
'''
import threading
import time

from wakeonlan import wol

import subprocess


class RemoteNodeServices(object):
    
    '''
    classdocs
    '''
    @staticmethod
    def __wakeNode(remoteNode):
        try:
            wol.send_magic_packet(remoteNode.getMAC())
        except (AttributeError, TypeError):
            raise AssertionError('Input variables should be strings')
    
    @staticmethod
    def __isAwake(ip, tries=1, sleep=0):
        while tries > 0:
            if RemoteNodeServices.__pingRemote(ip) == 0:
                tries = tries - 1
                time.sleep(sleep)
            else:
                return 1
        return 0
    
    @staticmethod
    def __pingRemote(ip):
        try:
            # bash equivalent: ping -c 1 > /dev/null
            subprocess.check_call(["ping", "-c 1", ip], stdin=None, stdout=None, stderr=None)
            print("ping to " + ip + " OK")
            return 1
        except subprocess.CalledProcessError:
            print("no response from " + ip)
            return 0
    
    @staticmethod
    def __checkRemoteWakeStatus(ip, callback):
        if RemoteNodeServices.__isAwake(ip,100,1) == 1:
        #try:
            callback()
        #except Exception:
        #print("LOG: callback failure")
        else:
            print("LOG: host failed to respond in allowed time")
    
    @staticmethod
    def wakeAndCheckRemote(remoteNode, callback):
        ip = remoteNode.getIP()
        if RemoteNodeServices.__isAwake(ip) == 0:
            RemoteNodeServices.__wakeNode(remoteNode)
        t = threading.Thread(target=RemoteNodeServices.__checkRemoteWakeStatus, args=(ip, callback))
        t.start()
    
    @staticmethod
    def sendRemoteToSleep(remoteNode, callback):
        pass
    
