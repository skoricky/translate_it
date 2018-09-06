from parsertxt import ParserText


class Presenter(object):
    def __init__(self, view, model):
        self.view = view
        self.model = model
        self.config = None

    def _open_project(self, file_name):
        print(file_name)
        self.model.file_name = file_name
        data = self.model.loads_fromjson()
        print(data)
        self.view.loads_text(data)

