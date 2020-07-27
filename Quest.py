from useful import *
import re
import configparser
import QuestSection
import os

class Quest(object):
    def __init__(self, name, config, path):
        self.name = name
        self.config = config
        self.sections = []
        self.path = path
        for section in config.sections():
            require = {}
            actions = {}
            for key,value in config.items(section):
                key = key.strip()
                value = value.strip()
                if key.startswith("action_"):
                    actions[key[7:]] = value
                elif key.startswith("require_"):
                    require[key[8:]] = value
                else:
                    log("Unexpected config %s = %s"%(key, value))
            qs = QuestSection.QuestSection(self, section, require, actions)
            self.sections.append(qs)

    def main(self, entry):
        for section in self.sections:
            if section.main(entry):
                break
            
            
def load(filename,path):
    config = configparser.ConfigParser()
    config.read_file(open(filename))
    name = os.path.split(filename)[-1].split(".cfg")[0]
    return Quest(name, config, path)
