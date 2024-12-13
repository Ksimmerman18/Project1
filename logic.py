from PyQt6.QtWidgets import *
from gui import *
import csv

class Logic(QMainWindow, Ui_Grades):
    """
    Logic class that handles the grading process and displays results.

    Inherits from QMainWindow and Ui_Grades to set up the user
    interface and manage the grading logic.
    """
    def __init__(self) -> None:
        """
        Initializes the Logic class and sets up the UI components,
        hides the score displays initially and connects the buttons
        to their respective functions.
        """
        super().__init__()
        self.setupUi(self)
        Logic.hide(self)
        self.push_button_attempts_submit.clicked.connect(lambda: self.attempts_submit())
        self.submit_button.clicked.connect(lambda: self.submit())
        self.clear_button.clicked.connect(lambda: self.clear())
        self.submit_button.setEnabled(False)
        self.__student_list: list[str] = []
        header: list[str] = [f'{"Name": ^10}',f'{"Score 1": ^10}', f'{"score 2": ^10}', f'{"score 3": ^10}', f'{"score 4": ^10}', f'{"Average Score": ^10}']
        with open('scores_file.csv', 'w', newline='') as csvfile:
            content = csv.writer(csvfile)
            content.writerow(header)

    def hide(self) -> None:
        """
        Hides the score inputs and labels, as well as clears
        the text in input fields.
        """
        self.score_lable1.hide()
        self.score_lable2.hide()
        self.score_lable3.hide()
        self.score_lable4.hide()
        self.score_line_edit1.hide()
        self.score_line_edit2.hide()
        self.score_line_edit3.hide()
        self.score_line_edit4.hide()
        self.line_edit_attempts_error.hide()
        self.score_line_edit1.setText('')
        self.score_line_edit2.setText('')
        self.score_line_edit3.setText('')
        self.score_line_edit4.setText('')
        self.line_edit_attempts_error.setText('')

    def attempts_submit(self) -> None:
        """
        Handles the submit action for the number of attempts and
        updates the UI based on how many attempts are entered, as
        well as checks to see if the name of the student has already
        been submitted. Raises exception for invalid inputs.
        """
        try:
            self.score_input_error_lable.setText('')
            student: str = self.student_line_edit.text()
            if student in self.__student_list:
                raise TypeError
            else:
                self.line_edit_attempts_error.setText('')
            attempts: int = int(self.attempts_line_edit.text())
            if attempts == 1:
                self.submit_button.setEnabled(True)
                self.score_lable1.show()
                self.score_line_edit1.show()
                self.line_edit_attempts_error.hide()
                self.score_line_edit2.hide()
                self.score_line_edit3.hide()
                self.score_line_edit4.hide()
                self.score_lable2.hide()
                self.score_lable3.hide()
                self.score_lable4.hide()
                self.score_line_edit2.setText('')
                self.score_line_edit3.setText('')
                self.score_line_edit4.setText('')
            elif attempts == 2:
                self.submit_button.setEnabled(True)
                self.score_lable1.show()
                self.score_line_edit1.show()
                self.score_lable2.show()
                self.score_line_edit2.show()
                self.line_edit_attempts_error.hide()
                self.score_line_edit3.hide()
                self.score_line_edit4.hide()
                self.score_lable3.hide()
                self.score_lable4.hide()
                self.score_line_edit3.setText('')
                self.score_line_edit4.setText('')
            elif attempts == 3:
                self.submit_button.setEnabled(True)
                self.score_lable1.show()
                self.score_line_edit1.show()
                self.score_lable2.show()
                self.score_line_edit2.show()
                self.score_lable3.show()
                self.score_line_edit3.show()
                self.line_edit_attempts_error.hide()
                self.score_line_edit4.hide()
                self.score_lable4.hide()
                self.score_line_edit4.setText('')
            elif attempts == 4:
                self.submit_button.setEnabled(True)
                self.score_lable1.show()
                self.score_line_edit1.show()
                self.score_lable2.show()
                self.score_line_edit2.show()
                self.score_lable3.show()
                self.score_line_edit3.show()
                self.score_lable4.show()
                self.score_line_edit4.show()
                self.line_edit_attempts_error.hide()
            else:
                raise ValueError
        except ValueError:
            Logic.hide(self)
            self.line_edit_attempts_error.show()
            self.line_edit_attempts_error.setText('Numbers 1-4 only')
            self.submit_button.setEnabled(False)
        except TypeError:
            Logic.hide(self)
            self.line_edit_attempts_error.show()
            self.line_edit_attempts_error.setText('Student Entered')
            self.submit_button.setEnabled(False)

    def submit(self) -> None:
        """
        Submits the scores, calculates the average, and
        appends the results to a CSV file. Raises exceptions
        for invalid score inputs and updates the UI accordingly.
        """
        try:
            file_list: list[str] = []
            file_list.append(f'{self.student_line_edit.text(): ^10}')
            if self.score_line_edit1.text() == '':
                score1: int = 0
            elif int(self.score_line_edit1.text()) > 100 or int(self.score_line_edit1.text()) < 0:
                raise ValueError
            else:
                score1 = int(self.score_line_edit1.text())
            if self.score_line_edit2.text() == '':
                score2: int = 0
            elif int(self.score_line_edit2.text()) > 100 or int(self.score_line_edit2.text()) < 0:
                raise ValueError
            else:
                score2 = int(self.score_line_edit2.text())
            if self.score_line_edit3.text() == '':
                score3: int = 0
            elif int(self.score_line_edit3.text()) > 100 or int(self.score_line_edit3.text()) < 0:
                raise ValueError
            else:
                score3 = int(self.score_line_edit3.text())
            if self.score_line_edit4.text() == '':
                score4: int = 0
            elif int(self.score_line_edit4.text()) > 100 or int(self.score_line_edit4.text()) < 0:
                raise ValueError
            else:
                score4 = int(self.score_line_edit4.text())
            file_list.append(f'{score1: ^10}')
            file_list.append(f'{score2: ^10}')
            file_list.append(f'{score3: ^10}')
            file_list.append(f'{score4: ^10}')
            final_score: float = (score1 + score2 + score3 + score4) / 4
            file_list.append(f'{final_score: ^10}')
            self.__student_list.append(self.student_line_edit.text())
            with open ('scores_file.csv', 'a', newline='') as csvfile:
                content = csv.writer(csvfile)
                content.writerow(file_list)
            Logic.clear(self)
            self.submit_button.setEnabled(False)
        except ValueError:
            self.score_input_error_lable.setText('Score needs to be 0-100 or no input')

    def clear(self) -> None:
        """
        Clears all input fields and hides the score inputs and labels.
        """
        Logic.hide(self)
        self.attempts_line_edit.setText('')
        self.student_line_edit.setText('')
        self.score_input_error_lable.setText('')
        self.submit_button.setEnabled(False)