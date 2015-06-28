'''
Created on 10 May 2015

@author: will
'''

class RemoteNode(object):
    '''
    classdocs
    '''

    def __init__(self, ip, mac):
        self.ip = ip
        self.mac = mac
        '''
        Constructor
        '''
        
    def getIP(self):
        return self.ip
    
    def getMAC(self):
        return self.mac