# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os

from view.ui_views.mainWindow import Ui_MainWindow
from view.ui_views.info_boxes import MessageBoxes

from view.translate_api import translate


# для теста, потом убрать
# ===========================================================
a = '16 апреля 1928 года, вечером, профессор зоологии IV  государственного университета и директор зооинститута в  Москве,  Персиков,  вошел  в  свой кабинет, помещающийся в зооинституте,  что  на  улице  Герцена.  Профессор зажег верхний матовый шар и огляделся.'
b = 'лдыоврапдл форвапдлыо рвдлпофрвларплдфворап лдфоврпдлфорвап'
c = ''
ao = 'The plot of the story is rather simple. Two people, a young one and an old one, lived together. The young man helped the old man to keep the house. But with time the old man started to irritate the young. It was his pale blue eye that made him mad.  What happpened in the end you will know when you read the story.'
bo = 'Now this is the point. You think I am mad. But you should see me. You should see how wisely I started to prepare for the work! I had been very kind to the old man during the whole week before. And every night, about midnight, I opened his door— oh, so quietly! And then I put a dark lantern into the opening, all closed, closed, so that no light shone out. And then I put in my head. Oh, you would laugh to see how carefully I put my head in! I moved it slowly —very, very slowly so that I would not disturb the old man’s sleep.'
co = 'On the eighth night I was more than usually careful in opening the door. I did it so slowly that a clock minute hand moved more quickly than did mine. And I could not hide my feelings of triumph. Just imagine that I was opening the door, little by little, and he didn’t even dream of my secret thoughts. I laughed at the idea; and perhaps he heard me; for he moved on the bed suddenly. You may think that I got out — but no. It was very dark in his room, for the shutters were closed, and so I knew that he could not see me, and I kept opening the door on little by little.'

orig = [ao, bo, co, ao, bo, co, ao, bo, co, c, c, c, c, c, c]
transl = [a, b, a, b, a, b, a, b, c, a, b, c, a, b, c]
# tup = tuple(zip(orig, transl))


# =============================================================


AUTO_SAVE_TIMEOUT = 1000 * 60 * 5


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    """ Главное окно.
        Ui_MainWindow - форма для setupUi"""
    _current_block = None
    _project_changed = False  # при нажатии на save или auto-save меняется на False

    open_cur_project = QtCore.pyqtSignal(str)
    load_from_file = QtCore.pyqtSignal(str)
    set_text_blocks = QtCore.pyqtSignal(tuple)
    dump_to_file = QtCore.pyqtSignal(list, str)

    def __init__(self, paren=None):
        QtWidgets.QMainWindow.__init__(self, paren)
        self.setupUi(self)
        self.on_start()
        self.info_box = MessageBoxes(self)

        self.autosave_timer = QtCore.QTimer(self)
        self.autosave_timer.setTimerType(QtCore.Qt.VeryCoarseTimer)
        self.autosave_timer.start(AUTO_SAVE_TIMEOUT)
        self.autosave_timer.timeout.connect(self._save_project)

        self.originalListWidget.itemClicked.connect(self.original_list_click)
        self.translatedListWidget.itemClicked.connect(self.translated_list_click)

        self.originalListWidget.verticalScrollBar().valueChanged.connect(self.sync_translated_scroll)
        self.translatedListWidget.verticalScrollBar().valueChanged.connect(self.sync_original_scroll)

        self.workWithBlockPushButton.clicked.connect(self.work_with_block)
        self.saveBlockPushButton.clicked.connect(self.save_block)
        self.translateApiPushButton.clicked.connect(self.translate_word)

        self.createTrigger.triggered.connect(self.create_new_project)
        self.openTrigger.triggered.connect(self.open_project)
        self.exportTxtTrigger.triggered.connect(self.export_txt)
        self.exitToolButton.clicked.connect(self.close)
        self.saveToolButton.clicked.connect(self._save_project)
        self.saveTrigger.triggered.connect(self._save_project)

    def sync_translated_scroll(self, value):
        self.translatedListWidget.verticalScrollBar().setValue(value)

    def sync_original_scroll(self, value):
        self.originalListWidget.verticalScrollBar().setValue(value)

    # TODO: добавить сохранение при смене блока без нажатия кнопки "сохранить"/либо сделать кнопку перевести неактивной
    def work_with_block(self):
        """ Начать работу над переводом выделенного блока текста, срабатывает при нажатии кнопки 'перевести блок'. """
        self._current_block = self.translatedListWidget.currentRow()
        self.translatedPartStackedWidget.setCurrentWidget(self.editorPage)
        self.originalTextEdit.setPlainText(self.originalListWidget.currentItem().text())
        self.translatedTextEdit.setPlainText(self.translatedListWidget.currentItem().text())
        self.workWithBlockPushButton.setEnabled(False)

    def save_block(self):
        """ Сохранение измененного текста блока в item. Срабатывает при нажатии кнопки 'Сохранить блок'. """
        self.translatedListWidget.item(self._current_block).setText(self.translatedTextEdit.toPlainText())
        self.translatedPartStackedWidget.setCurrentWidget(self.listPage)
        self.workWithBlockPushButton.setEnabled(True)
        self._project_changed = True

    # TODO: изменить когда будет метод выгрузки из базы
    def add_text(self, list_of_tuples):
        for o, t in list_of_tuples:
            orig_item = QtWidgets.QListWidgetItem(o, self.originalListWidget)
            trans_item = QtWidgets.QListWidgetItem(t, self.translatedListWidget)
            self.originalListWidget.addItem(orig_item)
            self.translatedListWidget.addItem(trans_item)

    # TODO: когда будет выгрузка текста из базы - переработать под больший размер
    def align_text_blocks_height(self):
        """ Выравнивает высоту блоков текста по тексту оригинала, срабатывает при изменении размера окна"""
        for string_index in range(self.translatedListWidget.count()):
            orig_index = self.originalListWidget.model().index(string_index)
            orig_height = self.originalListWidget.visualRect(orig_index).height()
            self.translatedListWidget.item(string_index).setSizeHint(QtCore.QSize(-1, orig_height))

    @QtCore.pyqtSlot()
    def original_list_click(self):
        """ Синхронизирует выделение блоков текста по клику на блок"""
        self.translatedListWidget.setCurrentRow(self.originalListWidget.currentRow())

    def translated_list_click(self):
        """ Синхронизирует выделение блоков текста по клику на блок"""
        self.originalListWidget.setCurrentRow(self.translatedListWidget.currentRow())

    def translate_word(self):
        _PATTERN = 'оригинал: {} \n перевод: {}'
        text = self.originalTextEdit.createMimeDataFromSelection().text()
        if text:
            type_, desc_, text_ = translate(text)
            if type_ == 'info':
                self.info_box(type_, desc_, _PATTERN.format(text, text_))
                QtWidgets.QApplication.clipboard().setText(text_)
            else:
                self.info_box(type_, desc_, text_)

    def export_txt(self):
        """
        Метод экспорта в TXT
        :return: list перевода и path для сохранения
        """
        file = QtWidgets.QFileDialog.getSaveFileName(
            parent=self, caption='Экспортировать', filter='All (*);;TXT (*.txt)', initialFilter='TXT (*.txt)'
        )
        if file[0]:
            text = [self.translatedListWidget.item(i).text() for i in range(self.translatedListWidget.count())]
            self.dump_to_file.emit(text, file[0])

    # TODO: метод для теста, пока нет заливки из базы - потом убрать
    def on_start(self):
        pass
        # self.add_text(tup)

    @QtCore.pyqtSlot()
    def create_new_project(self):
        file = QtWidgets.QFileDialog.getOpenFileName(
            parent=self, caption='Новый проект', filter='All (*);;TXT (*.txt)', initialFilter='TXT (*.txt)'
        )
        # путь к файлу который нужно прочитать
        file_path = file[0]
        if file_path:
            self.load_from_file.emit(os.path.abspath(file_path))

    @QtCore.pyqtSlot()
    def open_project(self, project_name='Hello'):
        self.open_cur_project.emit(project_name)

    def resizeEvent(self, event):
        """ Переопределение метода изменения размера окна,
            запускает выравниевание высоты блоков при событии изменения окна"""
        event.accept()
        self.align_text_blocks_height()

    def closeEvent(self, event):
        if self._project_changed:
            # диалоговое окно ... подумать где создавать экземпляр
            answ = self.info_box('question', 'Выход', 'Сохранить изменения?')
            if answ == QtWidgets.QMessageBox.Cancel:
                event.ignore()

            # TODO: сюда добавить метод сохранения в базу
            elif answ == QtWidgets.QMessageBox.Yes:
                self._save_project()
                event.accept()

            elif answ == QtWidgets.QMessageBox.No:
                event.accept()
        else:
            event.accept()

    def showEvent(self, event):
        self.align_text_blocks_height()
        event.accept()

    def _save_project(self):
        text = ((self.originalListWidget.item(i).text(), self.translatedListWidget.item(i).text())
                for i in range(self.translatedListWidget.count()))

        self.set_text_blocks.emit(tuple(text))
        self._project_changed = False


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
