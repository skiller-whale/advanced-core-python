import csv
import io
import json

from utils import fake_requests as requests
from utils.utils import load_document


class DocumentLoader:
    def __init__(self, location):
        self.location = location

    def read(self):
        with open(self.location) as file:
            return file.read()

    def parse(self, item):
        return item  # This method exists to be extended by subclasses.

    def load(self):
        load_document(
            {
                'location': str(self.location),
                'contents': self.parse(self.read()),
            }
        )


class LocalJsonLoader(DocumentLoader):
    def parse(self, data):
        parsed_data = json.loads(data)
        return parsed_data['data']


class LocalCsvLoader(DocumentLoader):
    def parse(self, data):
        file_data = io.StringIO(data)
        reader = csv.DictReader(file_data)
        return list(reader)


class RemoteJsonLoader(DocumentLoader):
    def read(self):
        return requests.get(self.location)

    def parse(self, data):
        parsed_data = json.loads(data)
        return parsed_data['values']


class RemoteCsvLoader(DocumentLoader):
    def read(self):
        return requests.get(self.location)

    def parse(self, data):
        file_data = io.StringIO(data)
        reader = csv.DictReader(file_data)
        return list(reader)


# ------------------------------------------------------------------------------
# DON'T EDIT BELOW HERE - it's just to check that your code is working
# ------------------------------------------------------------------------------

import pathlib
data_dir = pathlib.Path(__file__).parent / 'data'

print("\nExample Cases")
DocumentLoader(data_dir / 'demo_txt.txt').load()
LocalJsonLoader(data_dir / 'demo_json.json').load()
LocalCsvLoader(data_dir / 'demo_csv.csv').load()
RemoteJsonLoader("http://fake-json-source.com").load()
RemoteCsvLoader("http://fake-csv-source.com").load()
