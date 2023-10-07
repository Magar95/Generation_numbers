from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from random import randint

app = QApplication([])
main_win = QWidget()
main_win.resize(400,200)
main_win.move(300,100)
main_win.setWindowTitle('Определитель победителя')

but = QPushButton('Сгенерировать')
text = QLabel('Нажми, чтобы узнать победителя')
winner = QLabel('?')
line = QVBoxLayout()

line.addWidget(text, alignment = Qt.AlignCenter)
line.addWidget(winner, alignment = Qt.AlignCenter)
line.addWidget(but, alignment = Qt.AlignCenter)
main_win.setLayout(line)

def show_winner():
    number = randint(0, 99)
    winner.setText(str(number))
    text.setText('Победитель:')

but.clicked.connect(show_winner)


main_win.show()
app.exec_()
