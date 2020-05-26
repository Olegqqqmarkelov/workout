import sys
import time
import threading
from ui_time import *
from PyQt5 import QtCore, QtGui, QtWidgets


class MyWin(QtWidgets.QMainWindow):
    global time_bool,time_bool_2
    time_bool,time_bool_2 = 0,0

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        # Вешаем на кнопку функцию PoemCheck
        self.ui.pushButton.clicked.connect(self.PushButton)
        self.ui.pushButton_2.clicked.connect(self.PushButton_2)

    def PushButton_2(self):
        global time_bool,time_bool_2
        time_bool = 1

        if time_bool_2 == 1:
            print("time_bool_2 == 1")
            time_bool,time_bool_2 = 0,0

    # Описываем функцию 
    def PushButton(self):
        def time_sleep():
            global time_bool,time_bool_2
            for i in range(0,15 + 1):
                if time_bool == 1:
                    time_bool_2 = 1
                    print("time_bool == True")

                    break
                else:
                    time.sleep(1)
                    self.ui.label.setText(str(i))

        self.t = threading.Thread(target=time_sleep, name= 'Thread1')
        self.t.start()

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())

