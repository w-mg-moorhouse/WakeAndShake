
class configurationHolder(object):

    def __init__(self, configLoader):
        self.configuration = {}
        self.configLoader(configLoader)
    
    def addToConfiguration(self, key, value):
        self.configuration[key.rstrip()] = value.rstrip()
        
    def getConfiguration(self):
        return self.configuration

    def configLoader(self, configLocation):
        config = open(configLocation, 'r')
        for line in config:
            if "=" in line:
                values = line.split("=")
                if len(values) == 2:
                    self.addToConfiguration(values[0], values[1])
