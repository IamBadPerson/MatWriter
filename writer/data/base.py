from tinydb_base import DatabaseBase
from os.path import dirname, abspath, join

class Data(DatabaseBase):

    def __init__(self, table: str = ..., requiredKeys='title:str', test=False):
        file = join(dirname(abspath('Pipfile')), 'data.json')
        if test:
            file = join(dirname(abspath('Pipfile')), 'data.dev.json')
        super().__init__(file, table, requiredKeys)