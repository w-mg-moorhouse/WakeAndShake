'''
Created on 12 May 2015

@author: will
'''
from src.configLoader import configurationHolder
from src.dto.RemoteNode import RemoteNode
from src.RemoteNodeServices import RemoteNodeServices
from src.TransmissionAPI import TransmissionService
import webbrowser 

class Entry(object):
    '''
    classdocs
    '''

    def __init__(self):
        self.confHolder = configurationHolder("resources/wands.config").getConfiguration()
        self.remote = RemoteNode(self.confHolder["ip"], self.confHolder["mac"])
    
    
    def addTorrent(self, torrent):
        ip = self.remote.getIP()
        def callback():
            TransmissionService.addToRPCQueue(ip, torrent)
        RemoteNodeServices.wakeAndCheckRemote(self.remote, callback)
    
    def turnOn(self):
        def printer():
            print("Succesfully powered up RemoteNode")
        RemoteNodeServices.wakeAndCheckRemote(self.remote, printer)
        
    def turnOnNavigateTo(self):
        def callback():
            webbrowser.open("https://plex.tv/web/app")
        RemoteNodeServices.wakeAndCheckRemote(self.remote, callback)