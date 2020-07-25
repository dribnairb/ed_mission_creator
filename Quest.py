from useful import *
import re
import configparser
import QuestSection

class Quest(object):
    def __init__(self, config):
        self.config = config
        self.sections = []
        for section in config.sections():
            require = {}
            actions = {}
            for key,value in config.items(section):
                if key.startswith("action_"):
                    actions[key[7:]] = value
                elif key.startswith("require_"):
                    require[key[8:]] = value
                else:
                    log("Unexpected config %s = %s"%(key, value))
            qs = QuestSection.QuestSection(require, actions)
            self.sections.append(qs)

    def main(self, entry):
        for section in self.sections:
            section.main(entry)
            
            
def load(filename):
    config = configparser.ConfigParser()
    config.read_file(open(filename))
    return Quest(config)
    
