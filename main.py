import sys
import os
from PySide6.QtWidgets import QApplication, QMainWindow
from falcon import Ui_MainWindow

def nyny():
    from vyvod import f
    f = str(f)
    return(f)
    file = open('vyvod.py','w')
    file.close()
def get_OTV_print(entry, spin):
    file = open('vyvod.py', 'w')
    file.write('def convert_base(num, to_base='+str(spin)+', from_base=7):\n'
               '    if isinstance(num, str):\n'
               '        n = int(num, from_base)\n'
               '    else:\n'
               '        n = int(num)\n'
               '    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"\n'
               '    if n < to_base:\n'
               '        return alphabet[n]\n'
               '    else:\n'
               '        return convert_base(n // to_base, to_base) + alphabet[n % to_base]\n'
               '\n'
               'otv = '+ entry +'#\n'
               'f = convert_base(otv)')
    file.close()


class Calculator(QMainWindow):
    def __init__(self):
        super(Calculator, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_0.clicked.connect(lambda: self.add_digit('0'))
        self.ui.btn_1.clicked.connect(lambda: self.add_digit('1'))
        self.ui.btn_2.clicked.connect(lambda: self.add_digit('2'))
        self.ui.btn_3.clicked.connect(lambda: self.add_digit('3'))
        self.ui.btn_4.clicked.connect(lambda: self.add_digit('4'))
        self.ui.btn_5.clicked.connect(lambda: self.add_digit('5'))
        self.ui.btn_6.clicked.connect(lambda: self.add_digit('6'))
        self.ui.btn_7.clicked.connect(lambda: self.add_digit('7'))
        self.ui.btn_8.clicked.connect(lambda: self.add_digit('8'))
        self.ui.btn_9.clicked.connect(lambda: self.add_digit('9'))
        self.ui.btn_stepen.clicked.connect(lambda: self.add_digit('^'))
        self.ui.btn_delenie.clicked.connect(lambda: self.add_digit('/'))
        self.ui.btn_x.clicked.connect(lambda: self.add_digit('x'))
        self.ui.btn_minus.clicked.connect(lambda: self.add_digit('-'))
        self.ui.btn_plus.clicked.connect(lambda: self.add_digit('+'))
        self.ui.btn_otv.clicked.connect(lambda: self.get_entry_num())
        self.ui.btn_otv.clicked.connect(lambda: self.add_temp())
        self.ui.btn_CE.clicked.connect(self.clear_all)
        self.ui.btn_C.clicked.connect(self.clear_entry)

    def add_digit(self, btn_text: str) -> None:
        if self.ui.YPAVNENIE.text() == '0':
            self.ui.YPAVNENIE.setText(btn_text)
        else:
            self.ui.YPAVNENIE.setText(self.ui.YPAVNENIE.text() + btn_text)

    def clear_all(self) -> None:
        self.ui.YPAVNENIE.setText('0')
        self.ui.OTVET.clear()

    def clear_entry(self) -> None:
        self.ui.YPAVNENIE.setText('0')


    def get_entry_num(self):
        entry = self.ui.YPAVNENIE.text()
        entry = entry.replace('^', '**')
        entry = entry.replace('x', '*')
        spin = self.ui.spinBox.value()
        get_OTV_print(entry, spin)

    def add_temp(self) -> None:
        btn = self.sender()
        coc = nyny()
        coc = str(coc)
        self.ui.OTVET.setText(' кол-во 0 : '+ str(coc.count('0'))+'     кол-во A : ' + str(coc.count('A'))+'\n'
                              ' кол-во 1 : '+ str(coc.count('1'))+'     кол-во B : '+ str(coc.count('B'))+'\n'
                              ' кол-во 2 : '+ str(coc.count('2'))+'     кол-во C : '+ str(coc.count('C'))+'\n'
                              ' кол-во 3 : '+ str(coc.count('3'))+'     кол-во D : '+ str(coc.count('D'))+'\n'
                              ' кол-во 4 : '+ str(coc.count('4'))+'     кол-во E : '+ str(coc.count('E'))+'\n'
                              ' кол-во 5 : '+ str(coc.count('5'))+'     кол-во F : '+ str(coc.count('F'))+'\n'
                              ' кол-во 6 : '+ str(coc.count('6'))+'\n'
                              ' кол-во 7 : '+ str(coc.count('7'))+'\n'
                              ' кол-во 8 : '+ str(coc.count('8'))+'\n'
                              ' кол-во 9 : '+ str(coc.count('9'))+'\n'
                              ' сумма цифр числа : ' + str(sum(map(int,coc))))








if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Calculator()
    window.show()

    sys.exit(app.exec())
