'''
Created on 10 May 2015

@author: will
'''

import transmissionrpc

class TransmissionService(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        pass
    
    @staticmethod
    def addToRPCQueue(ip, torrent):
        tc = transmissionrpc.Client(ip, port=9091)
        tc.add_torrent(torrent)
        print("Torrent successfully added")