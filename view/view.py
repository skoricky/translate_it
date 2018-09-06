import sys
import os

from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import Qt, QObject, QThread, pyqtSignal, pyqtSlot


class MainWindow(QtWidgets.QMainWindow):

    open_project_signal = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi('.\\view\\Main.ui', self)
        self._run()

    def _run(self):
        self.pushButtonOpen.clicked.connect(self._open_project)

    @pyqtSlot()
    def _open_project(self):
        text = f'{self.lineEdit.text()}.json'
        self.open_project_signal.emit(text)

    def loads_text(self, data: dict):
        for i in data:
            print(i)
            self.textEditEn.setText(data[i][0])
            self.textEditRu.setText(data[i][1])


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
