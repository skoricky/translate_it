import sys
from PyQt5 import QtCore, QtGui, QtWidgets

from parsertxt import ParserText
from main_window import MainWindow


class Presenter(object):

    __slots__ = ['_model', '_view']

    def __init__(self, view, model):
        self._model = model
        self._view = view
        # self._view.set_file_path.connect(self.set_file_path)
        # self.main()

    def get_blocks(self):
        pass

    def set_blocks(self):
        pass

    def set_file_path(self, path_):
        print(path_)

    def main(self):
        prs = ParserText('Привет тебе, противный мир\n Как же я не люблю тебя!')
        print(prs.get())


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    pr = Presenter(win, None)
    win.set_file_path.connect(pr.set_file_path)
    win.show()
    sys.exit(app.exec_())
