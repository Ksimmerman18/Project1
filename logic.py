from PyQt6.QtWidgets import *
from gui import *

class Logic(QMainWindow, Ui_CandidateVoting):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.push_button_submit_vote.clicked.connect(lambda: self.submit())
        self.__jane_tally = 0
        self.__john_tally = 0
        self.__jimmy_tally = 0
        self.__id_list = []

    def submit(self):
        if self.radio_button_Jane.isChecked():
            self.__jane_tally += 1
        elif self.radio_button_John.isChecked():
            self.__john_tally += 1
        elif self.radio_button_Jimmy.isChecked():
            self.__jimmy_tally += 1

