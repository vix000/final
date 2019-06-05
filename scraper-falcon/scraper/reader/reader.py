import json
from scraper.scraper import AbstractWrapper


class Reader(AbstractWrapper):
    DIRECTORY = '/Users/vix/Desktop/STUFF/scraper/scraper-script/proj_zesp'

    def __init__(self, filename):
        self.filename = filename
        self.json_string = {}
        
    @property
    def read_file(self):
        with open(f'{self.DIRECTORY}/{self.FILE}', "r+") as f:
            data = json.load(f)
        return json.dumps(data)
