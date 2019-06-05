from subprocess import Popen
import os
import json
from abc import ABC


class AbstractWrapper(ABC):
    BIN_DIRECTORY = '/Users/vix/Desktop/STUFF/scraper/scraper-script/.env/bin/'
    DIRECTORY = '/Users/vix/Desktop/STUFF/scraper/scraper-script/proj_zesp'
    FILE = 'results.json'

    def __str__(self):
        return f'{self.__class__.__name__} class at {id(self)}'

    def __repr__(self):
        return self.__str__()


class Scraper(AbstractWrapper):


    def __init__(self, category, lookup_string):
        self.category = category
        self.lookup_string = lookup_string
        os.chdir(self.DIRECTORY)


    @property
    def run(self):
        system_call_string = self.prepare_system_call_string()
        os.system(system_call_string)

    def prepare_system_call_string(self):
        return f'{self.BIN_DIRECTORY}scrapy crawl {self.category} -a tag="{self.lookup_string}" -o {self.FILE}'

