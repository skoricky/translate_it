import json


class TempRepository:

    __slots__ = ['file_name', 'data']

    def __init__(self, file_name, data):
        self.file_name = file_name
        self.data = data

    def dumps_tojson(self):
        try:
            with open(self.file_name, 'w') as file:
                file.write(json.dumps(self.data))
            print('done')
        except Exception as e:
            print('Error (so bad):', e)

    def loads_fromjson(self):
        try:
            with open(self.file_name, 'r') as file:
                data = dict(json.loads(file.read(), encoding='utf-8'))
            print('done')
            return data
        except Exception as e:
            print('Error (so bad):', e)


class Repository(TempRepository):

    __slots__ = ['file_name', 'data']

    def __init__(self, file_name=None, data=None):
        super().__init__(file_name, data)
