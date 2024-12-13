from PyQt6.QtWidgets import *
from gui import *
import csv

class Logic(QMainWindow, Ui_CandidateVoting):
    """
    Logic class that handles the voting process and displays results.

    Inherits from QMainWindow and Ui_CandidateVoting to set up the
    user interface and manage the voting logic.
    """
    def __init__(self) -> None:
        """
        Initializes the Logic class and sets up the UI components, hides the
        results display and connects the buttons to their respective functions.
        """
        super().__init__()
        self.setupUi(self)
        self.plain_text_edit_results.hide()
        self.push_button_submit_vote.clicked.connect(lambda: self.submit())
        self.push_button_results.clicked.connect(lambda: self.results())
        self.__jane_tally: int = 0
        self.__john_tally: int = 0
        self.__jimmy_tally: int = 0
        self.__id_list: list[int] = []


    def submit(self) -> None:
        """
        Submits votes, updates the tally for the candidate selected, also has
        multiple exceptions to make sure a valid vote is cast. Resets inputs
        when a successful vote is submitted.
        """
        try:
            id_num: int = int(self.ID_input.text())
            if id_num in self.__id_list:
                raise TypeError
            else:
                self.__id_list.append(int(self.ID_input.text()))
                self.ID_already_voted_lable.setText('')
            if self.radio_button_Jane.isChecked():
                self.__jane_tally += 1
            elif self.radio_button_John.isChecked():
                self.__john_tally += 1
            elif self.radio_button_Jimmy.isChecked():
                self.__jimmy_tally += 1
            self.ID_error_label.setText('')
            self.ID_input.setText('')
            self.buttonGroup.setExclusive(False)
            self.radio_button_John.setChecked(False)
            self.radio_button_Jimmy.setChecked(False)
            self.radio_button_Jane.setChecked(False)
            self.buttonGroup.setExclusive(True)
        except ValueError:
            self.ID_already_voted_lable.setText('')
            self.ID_error_label.setText('Numbers only please')
        except TypeError:
            self.ID_error_label.setText('')
            self.ID_already_voted_lable.setText('ALREADY VOTED')


    def results(self) -> None:
        """
        Displays the results of the vote, writes the results of the vote to
        a CSV file that displays the candidates and how many votes each one got
        along with the winner. Handles outcomes where there is a tie for the winner
        forcing another vote to be cast.
        """
        try:
            if (self.__jane_tally >= self.__john_tally and self.__jane_tally == self.__jimmy_tally) or (self.__jane_tally >= self.__jimmy_tally and self.__jane_tally == self.__john_tally) or (self.__john_tally >= self.__jane_tally and self.__john_tally == self.__jimmy_tally) or (self.__john_tally >= self.__jimmy_tally and self.__john_tally == self.__jane_tally) or (self.__jimmy_tally >= self.__john_tally and self.__jimmy_tally == self.__jane_tally) or (self.__jimmy_tally >= self.__jane_tally and self.__jimmy_tally == self.__john_tally):
                raise TypeError
            else:
                self.plain_text_edit_results.show()
                self.radio_button_Jane.hide()
                self.radio_button_Jimmy.hide()
                self.radio_button_John.hide()
                self.Candidates_lable.hide()
                self.ID_error_label.hide()
                self.ID_input.setText('')
                self.ID_already_voted_lable.setText('')
                if self.__jane_tally > self.__john_tally and self.__jane_tally > self.__jimmy_tally:
                    winner: str = 'Jane'
                elif self.__john_tally > self.__jane_tally and self.__john_tally > self.__jimmy_tally:
                    winner = 'John'
                elif self.__jimmy_tally > self.__john_tally and self.__jimmy_tally > self.__jane_tally:
                    winner = "Jimmy"
                self.plain_text_edit_results.setPlainText(f'The winner of the vote is {winner}\nJane had {self.__jane_tally} vote(s)\nJohn had {self.__john_tally} vote(s)\nJimmy had {self.__jimmy_tally} vote(s)')
                header_list: list[str] = [f'{"Jane Total Votes": ^20}',f'{"John Total Votes": ^20}', f'{"Jimmy Total Votes": ^20}', f'{"Winner": ^10}']
                votes_list: list[str] = [f'{self.__jane_tally: ^20}',f'{self.__john_tally: ^20}', f'{self.__jimmy_tally: ^20}', f'{winner: ^10}']
                self.ID_input.setEnabled(False)
                self.push_button_submit_vote.setEnabled(False)
                self.push_button_results.setEnabled(False)
                with open('candidate_results.csv', 'w', newline='') as csvfile:
                    content = csv.writer(csvfile)
                    content.writerow(header_list)
                    content.writerow(votes_list)
        except TypeError:
            self.ID_error_label.setText('')
            self.ID_already_voted_lable.setText('TIE NEED ANOTHER VOTE')

