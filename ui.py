import sys

from PyQt5.QtWidgets import (
    QApplication, 
    QWidget, 
    QHBoxLayout, 
    QVBoxLayout, 
    QPushButton,
    QLabel,
    QLineEdit,
    QListWidget
)

from core import Core

class Button(QPushButton):
    def __init__(self, text) -> None:
        super().__init__(text)
        self.setFixedSize(200,60)
        self.setStyleSheet('background: green; font-size: 25px')


class Dic(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Menu")
        self.setFixedSize(400,500)

        self.v_box = QVBoxLayout()
        self.h_box = QHBoxLayout()

        self.btn_add_new_word = Button('Add new word')
        self.btn_list_of_words = Button('List of words')
        self.btn_search_word = Button('Search word')
        self.btn_exit = Button('Exit')

        self.v_box.addStretch()
        self.v_box.addWidget(self.btn_add_new_word)
        self.v_box.addWidget(self.btn_list_of_words)
        self.v_box.addWidget(self.btn_search_word)
        self.v_box.addWidget(self.btn_exit)
        self.v_box.addStretch()

        self.h_box.addStretch()
        self.h_box.addLayout(self.v_box)
        self.h_box.addStretch()

        self.setLayout(self.h_box)

        self.show()


class AddWord(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.core = Core()
        self.setWindowTitle("Add new word")
        self.setFixedSize(400,500)

        self.v_box = QVBoxLayout()

        self.v_box_edit = QVBoxLayout()
        self.h_box_send = QHBoxLayout()
        self.h_box_btns = QHBoxLayout()

        self.edit_eng = QLineEdit()
        self.edit_eng.setPlaceholderText("English...")

        self.edit_uzb = QLineEdit()
        self.edit_uzb.setPlaceholderText("Uzbek...")

        self.btn_send = QPushButton("Send")
        self.btn_menu = QPushButton("Menu")
        self.btn_list_of_words = QPushButton("List of words")
        self.btn_search = QPushButton("Search")

        self.v_box_edit.addWidget(self.edit_eng)
        self.v_box_edit.addWidget(self.edit_uzb)

        self.h_box_send.addLayout(self.v_box_edit)
        self.h_box_send.addWidget(self.btn_send)

        self.h_box_btns.addWidget(self.btn_menu)
        self.h_box_btns.addWidget(self.btn_list_of_words)
        self.h_box_btns.addWidget(self.btn_search)

        self.v_box.addLayout(self.h_box_send)
        self.v_box.addStretch()
        self.v_box.addLayout(self.h_box_btns)

        self.btn_send.clicked.connect(self.save_word)

        self.setLayout(self.v_box)

        self.show()

    def __clear_edit(self):
        self.edit_eng.clear()
        self.edit_uzb.clear()

    def save_word(self):
        eng = self.edit_eng.text()
        uzb = self.edit_uzb.text()
        if not '' in (eng, uzb):
            self.core.insert(eng, uzb)
            self.__clear_edit()



class ListOfWords(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.core = Core()
        self.setWindowTitle("List of words")
        self.setFixedSize(400,500)

        self.v_box = QVBoxLayout()

        self.v_box_eng = QVBoxLayout()
        self.v_box_uzb = QVBoxLayout()
        self.h_box_lang = QHBoxLayout()
        self.h_box_btns = QHBoxLayout()

        self.label_eng = QLabel("English")
        self.list_eng = QListWidget()

        self.label_uzb = QLabel("Uzbek")
        self.list_uzb = QListWidget()

        self.btn_menu = QPushButton("Menu")
        self.btn_add_word = QPushButton("Add new words")
        self.btn_search = QPushButton("Search")

        self.v_box_eng.addWidget(self.label_eng)
        self.v_box_eng.addWidget(self.list_eng)

        self.v_box_uzb.addWidget(self.label_uzb)
        self.v_box_uzb.addWidget(self.list_uzb)

        self.h_box_lang.addLayout(self.v_box_eng)
        self.h_box_lang.addLayout(self.v_box_uzb)

        self.h_box_btns.addWidget(self.btn_menu)
        self.h_box_btns.addWidget(self.btn_add_word)
        self.h_box_btns.addWidget(self.btn_search)

        self.v_box.addLayout(self.h_box_lang)
        self.v_box.addLayout(self.h_box_btns)

        self.scroll_bar1 = self.list_eng.verticalScrollBar()
        self.scroll_bar2 = self.list_uzb.verticalScrollBar()

        self.scroll_bar1.valueChanged.connect(self.scrollBarValueChanged1)
        self.scroll_bar2.valueChanged.connect(self.scrollBarValueChanged2)

        self.setLayout(self.v_box)
        self.show_all_words()

        self.show()

    def show_all_words(self):
        words = self.core.get_words()
        for eng, uzb in words:
            self.list_eng.addItem(eng)
            self.list_uzb.addItem(uzb)


    def scrollBarValueChanged1(self, value):
        self.scroll_bar2 = self.list_uzb.verticalScrollBar()
        self.scroll_bar2.setValue(value)
    
    def scrollBarValueChanged2(self, value):
        self.scroll_bar1 = self.list_eng.verticalScrollBar()
        self.scroll_bar1.setValue(value)

class SearchWord(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Search word")
        self.setFixedSize(400,500)

        self.v_box = QVBoxLayout()

        self.h_box_search = QHBoxLayout()
        self.h_box_btns = QHBoxLayout()

        self.edit_search = QLineEdit()
        self.btn_search = QPushButton('search')

        self.list_words = QListWidget()

        self.btn_menu = QPushButton("Menu")
        self.btn_add_word = QPushButton("Add new words")
        self.btn_list_words = QPushButton("List of words")

        self.h_box_search.addWidget(self.edit_search)
        self.h_box_search.addWidget(self.btn_search)

        self.h_box_btns.addWidget(self.btn_menu)
        self.h_box_btns.addWidget(self.btn_add_word)
        self.h_box_btns.addWidget(self.btn_list_words)

        self.v_box.addLayout(self.h_box_search)
        self.v_box.addWidget(self.list_words)
        self.v_box.addLayout(self.h_box_btns)

        self.setLayout(self.v_box)

        self.show()



app = QApplication(sys.argv)
win = Dic()
# win2 = AddWord()
win3 = ListOfWords()
# win4 = SearchWord()
sys.exit    (app.exec_())

