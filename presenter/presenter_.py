# from parsertxt import ParserText


class Presenter(object):

    def __init__(self, view, model):
        self._model = model
        self._view = view
        self._view.set_text_blocks.connect(self.set_blocks)
        self._view.set_file_path.connect(self.get_blocks)

    def get_blocks(self, file_name='Hello.json'):
        self._model.file_name = file_name
        data = self._model.loads_fromjson()
        data_tuple = (data[i] for i in data.keys())
        self._view.add_text(data_tuple)

    def set_blocks(self, data, file_name='Hello.json'):
        data_dict = {}
        for idx, item in enumerate(data):
            data_dict.update({idx: item})
        self._model.data = data_dict
        self._model.file_name = file_name
        self._model.dumps_tojson()

    def set_file_path(self, path_):
        print(path_)

