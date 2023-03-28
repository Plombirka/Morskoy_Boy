from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon
from tkinter import *
from tkinter import messagebox as mb
import sys
import time
import random

class Ui_Element_Uprav(object):
    def setupUi(self, Element_Uprav):
        Element_Uprav.setObjectName("Element_Uprav")
        self.label = QtWidgets.QLabel(Element_Uprav)
        self.label.setGeometry(QtCore.QRect(220, 10, 285, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.btn_GLmenu = QtWidgets.QPushButton(Element_Uprav)
        self.btn_GLmenu.setGeometry(QtCore.QRect(0, 0, 75, 51))
        self.btn_GLmenu.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("d:\\Projeck\\Proect/Стрелка влево.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_GLmenu.setIcon(icon)
        self.btn_GLmenu.setIconSize(QtCore.QSize(40, 40))
        self.btn_GLmenu.setObjectName("btn_GLmenu")
        self.label_3 = QtWidgets.QLabel(Element_Uprav)
        self.label_3.setGeometry(QtCore.QRect(160, 160, 401, 201))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)  
        font.setWeight(75)
        self.label_3.setStyleSheet("")
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(Element_Uprav)
        self.label_2.setGeometry(QtCore.QRect(36, 160, 131, 201))
        self.label_2.setStyleSheet("")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("d:\\Projeck\\Proect/Клик мыши.ico"))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Element_Uprav)
        QtCore.QMetaObject.connectSlotsByName(Element_Uprav)

    def retranslateUi(self, Element_Uprav):
        _translate = QtCore.QCoreApplication.translate
        Element_Uprav.setWindowTitle(_translate("Element_Uprav", "Морской бой"))
        self.label.setText(_translate("Element_Uprav", "Элементы управления"))
        self.label_3.setText(_translate("Element_Uprav", "- Стрельба"))

class Ui_Rule_Play(object):
    def setupUi(self, Rule_Play):
        Rule_Play.setObjectName("Rule_Play")
        self.label = QtWidgets.QLabel(parent=Rule_Play)
        self.label.setGeometry(QtCore.QRect(260, 10, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.btn_GLmenu = QtWidgets.QPushButton(parent=Rule_Play)
        self.btn_GLmenu.setGeometry(QtCore.QRect(0, 0, 75, 51))
        self.btn_GLmenu.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("d:\\Projeck\\Proect/Стрелка влево.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_GLmenu.setIcon(icon)
        self.btn_GLmenu.setIconSize(QtCore.QSize(40, 40))
        self.btn_GLmenu.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(parent=Rule_Play)
        self.label_2.setEnabled(True)
        self.label_2.setGeometry(QtCore.QRect(0, 170, 711, 351))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setItalic(False)
        font.setUnderline(False)
        self.label_2.setFont(font)
        self.label_2.setMouseTracking(False)
        self.label_2.setTabletTracking(False)
        self.label_2.setAcceptDrops(False)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet("")
        self.label_2.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.label_2.setLineWidth(3)
        self.label_2.setMidLineWidth(2)
        self.label_2.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label_2.setScaledContents(False)
        self.label_2.setWordWrap(True)
        self.label_2.setOpenExternalLinks(False)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Rule_Play)
        QtCore.QMetaObject.connectSlotsByName(Rule_Play)

    def retranslateUi(self, Rule_Play):
        _translate = QtCore.QCoreApplication.translate
        Rule_Play.setWindowTitle(_translate("Rule_Play", "Морской бой"))
        self.label.setText(_translate("Rule_Play", "Правила игры"))
        self.label_2.setText(_translate("Rule_Play", "Принцип «Морского боя» очень прост — Случайным образом расставляются корабли на вашем поле, в зависимости от сложности, Easy - 12х12, Medium - 15x15, Hard - 18x18 и поле оппонента. Далее вы по очереди делаете «выстрелы», нажимая на те или иные клетки на поле оппонента — если попадаете по короблю оппонента на клетке, на которую вы нажали появляется крестик с соответствующим цветом корабля, розовый – однопалубный корабль, синий – двухпалубный корабль, зелёный – трёхпалубный корабль, жёлтый – четырёхпалубный корабль(в начале игры эта функция отключена, включить её можно поставив галочку которая находиться в самом низу посередине экрана), если вы промахнулись на клетке, на которую вы нажали появляется кружочек чёрного цвета. Игра длиться до тех пор, пока кто-нибудь из игроков не подобьёт все корабли оппонента."))

class Ui_Slosnost(object):
    def setupUi(self, Slosnost):
        Slosnost.setObjectName("Slosnost")
        self.btn_Easy = QtWidgets.QPushButton(Slosnost)
        self.btn_Easy.setGeometry(QtCore.QRect(310, 230, 111, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_Easy.setFont(font)
        self.btn_Easy.setObjectName("btn_Easy")
        self.btn_Medium = QtWidgets.QPushButton(Slosnost)
        self.btn_Medium.setGeometry(QtCore.QRect(310, 270, 111, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_Medium.setFont(font)
        self.btn_Medium.setObjectName("btn_Medium")
        self.btn_Hard = QtWidgets.QPushButton(Slosnost)
        self.btn_Hard.setGeometry(QtCore.QRect(310, 310, 111, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_Hard.setFont(font)
        self.btn_Hard.setObjectName("btn_Hard")
        self.label = QtWidgets.QLabel(Slosnost)
        self.label.setGeometry(QtCore.QRect(260, 20, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.btn_GLmenu = QtWidgets.QPushButton(Slosnost)
        self.btn_GLmenu.setGeometry(QtCore.QRect(0, 0, 75, 51))
        self.btn_GLmenu.setStyleSheet("")
        self.btn_GLmenu.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("d:\\Projeck\\Proect/Стрелка влево"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_GLmenu.setIcon(icon)
        self.btn_GLmenu.setIconSize(QtCore.QSize(40, 40))
        self.btn_GLmenu.setObjectName("btn_GLmenu")

        self.retranslateUi(Slosnost)
        QtCore.QMetaObject.connectSlotsByName(Slosnost)

    def retranslateUi(self, Slosnost):
        _translate = QtCore.QCoreApplication.translate
        Slosnost.setWindowTitle(_translate("Slosnost", "Морсокй бой"))
        self.btn_Easy.setText(_translate("Slosnost", "Easy"))
        self.btn_Hard.setText(_translate("Slosnost", "Hard"))
        self.btn_Medium.setText(_translate("Slosnost", "Medium"))
        self.label.setText(_translate("Slosnost", "Сложности Игры"))

class Ui_GLMenu(object):
    def setupUi(self, GLMenu):
        GLMenu.setObjectName("GLMenu")
        self.label = QtWidgets.QLabel(parent=GLMenu)
        self.label.setGeometry(QtCore.QRect(220, 10, 240, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.btn_Igra = QtWidgets.QPushButton(GLMenu)
        self.btn_Igra.setGeometry(QtCore.QRect(270, 200, 151, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_Igra.setFont(font)
        self.btn_Igra.setObjectName("btn_Igra")
        self.btn_Rule_Play = QtWidgets.QPushButton(GLMenu)
        self.btn_Rule_Play.setGeometry(QtCore.QRect(270, 240, 151, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_Rule_Play.setFont(font)
        self.btn_Rule_Play.setObjectName("brt_Rule_Play")
        self.btn_Element_Uprav = QtWidgets.QPushButton(GLMenu)
        self.btn_Element_Uprav.setGeometry(QtCore.QRect(270, 280, 151, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_Element_Uprav.setFont(font)
        self.btn_Element_Uprav.setObjectName("btn_Element_Uprav")
        self.btn_Exit = QtWidgets.QPushButton(GLMenu)
        self.btn_Exit.setGeometry(QtCore.QRect(640, 0, 75, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.btn_Exit.setFont(font)
        self.btn_Exit.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.btn_Exit.setObjectName("btn_Exit")

        self.retranslateUi(GLMenu)
        QtCore.QMetaObject.connectSlotsByName(GLMenu)

    def retranslateUi(self, GLMenu):
        _translate = QtCore.QCoreApplication.translate
        GLMenu.setWindowTitle(_translate("GLMenu", "Морской бой"))
        self.label.setText(_translate("Rule_Play", "Игра Морской бой"))
        self.btn_Igra.setText(_translate("GLMenu", "Играть"))
        self.btn_Rule_Play.setText(_translate("GLMenu", "Правила игры"))
        self.btn_Element_Uprav.setText(_translate("GLMenu", "Элементы управления"))
        self.btn_Exit.setText(_translate("GLMenu", "Exit"))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    GLMenu = QMainWindow()
    GLMenu.setFixedSize(711, 592)
    ui = Ui_GLMenu()
    ui.setupUi(GLMenu)
    GLMenu.show()

    def openIgra():
        global Slosnost
        Slosnost = QMainWindow()
        Slosnost.setFixedSize(711, 592)
        ui = Ui_Slosnost()
        ui.setupUi(Slosnost)
        GLMenu.close()
        Slosnost.show()

        def returnGLmenu():
            Slosnost.close()
            GLMenu.show()
        
        def openPlayEasy():
            global Exit
            Exit = False
            Slosnost.close()
            GLMenu.show()
            GLMenu.hide()
            def poles(number_rectengle):
                global running, hod_igroka, size_wn_x, size_wn_y, s_x, s_y, step_x, step_y, ship, ship_1, ship_2, ship_3, ship_4, enemy_ships_1, enemy_ships_2, enemy_ships_3, enemy_ships_4, enemy_ships1, enemy_ships2, menu_x, menu_y, list_ids, Clik_String1, Clik_String2, boom

                tk = Tk()
                running=True

                size_wn_x= 600
                size_wn_y= 600
                s_x=s_y=number_rectengle #размер поля
                step_x=size_wn_x//s_x #шаг по горизонтали
                step_y=size_wn_y//s_y #шаг по вертекали
                size_wn_x = step_x * s_x
                size_wn_y = step_y * s_y
                #общее количество кораблей
                ship = 10
                #размеры кораблей
                ship_1 = 1
                ship_2 = 2
                ship_3 = 3
                ship_4 = 4
                #колличество кораблей
                enemy_ships_1= 4
                enemy_ships_2 = 3
                enemy_ships_3 = 2
                enemy_ships_4 = 1
                enemy_ships1 = [[0 for i in range(s_y+1)] for i in range(s_x+1)]
                enemy_ships2 = [[0 for i in range(s_y+1)] for i in range(s_x+1)]
                menu_x= step_x*6
                menu_y = 40
                list_ids=[] #список объектов
                Clik_String1 = [[-1 for i in range(s_y)] for i in range(s_x)] #список куда мы кликнули
                Clik_String2 = [[-1 for i in range(s_y)] for i in range(s_x)] #список куда мы кликнули
                boom = [[0 for i in range(s_y)] for i in range(s_x)] #список попаданей по короблям

                photo = PhotoImage(file='D:\Projeck\Proect\Sea_warr.png')
                tk.iconphoto(False, photo)

                #Истина - 2 игрок, ложно - 1 игрок
                hod_igroka=False

                def settings():
                    global var, Helper
                    Helper=False
                    var = IntVar(tk)
                    Btn_Check = Checkbutton(text="Включить обозначения размера корабля?",
                                            variable=var,
                                            command=print_value)
                    Btn_Check.pack(side='bottom')

                def print_value():
                    global Helper
                    print(var.get())
                    if var.get() == 1:
                        Helper=True
                    else:
                        Helper=False

                settings()

                def closing():
                    global running, Exit
                    if mb.askokcancel("Выход из игры", "Хотите выйти из игры?"):
                        running=False
                        Exit = True
                        tk.destroy()

                tk.protocol("WM_DELETE_WINDOW", closing)
                tk.title("Морской бой")
                tk.resizable(0,0)
                tk.wm_attributes("-topmost", 1)
                pole = Canvas(tk, width=size_wn_x+menu_x + size_wn_x, height=size_wn_y+ menu_y, bd=0, highlightthickness=0)
                pole.create_rectangle(0,0,size_wn_x, size_wn_y, fill="white")
                pole.create_rectangle(size_wn_x+menu_x,0,size_wn_x+menu_x + size_wn_x, size_wn_y, fill="white")
                pole.pack()
                tk.update()
                
                
                Pink_rectangle=Label(tk,text="",background="pink")
                Pink_rectangle.place(x=size_wn_x+menu_x//5,y=step_y*8,width=15,height=15)
                one_palub=Label(tk,text="- Однопалубный корабль")
                one_palub.place(x=size_wn_x+menu_x//5+20,y=step_y*8)
                Blue_rectangle=Label(tk,text="",background="blue")
                Blue_rectangle.place(x=size_wn_x+menu_x//5,y=step_y*9,width=15,height=15)
                two_palub=Label(tk,text="- Двухпалубный корабль")
                two_palub.place(x=size_wn_x+menu_x//5+20,y=step_y*9)
                Green_rectangle=Label(tk,text="",background="green")
                Green_rectangle.place(x=size_wn_x+menu_x//5,y=step_y*10,width=15,height=15)
                three_palub=Label(tk,text="- Трёхпалубный корабль")
                three_palub.place(x=size_wn_x+menu_x//5+20,y=step_y*10)
                Yellow_rectangle=Label(tk,text="",background="yellow")
                Yellow_rectangle.place(x=size_wn_x+menu_x//5,y=step_y*11,width=15,height=15)
                four_palub=Label(tk,text="- Четырёхпалубный корабль")
                four_palub.place(x=size_wn_x+menu_x//5+20,y=step_y*11)
                
                def Pole(offset_x=0):
                    for i in range(s_x+1):
                        pole.create_line(offset_x + step_x * i,0,offset_x + step_x * i,size_wn_y)
                    for i in range(s_y+1):
                        pole.create_line(offset_x,step_y * i ,offset_x + size_wn_x, step_y * i)

                Pole()
                Pole(size_wn_x+menu_x)

                lbl1 = Label(tk, text= 'Игрок №1', font=('Helvetica', 16))
                lbl1.place(x = size_wn_x //2 - lbl1.winfo_reqwidth() //2 , y = size_wn_y+3)
                lbl2 = Label(tk, text= 'Игрок №2', font=('Helvetica', 16))
                lbl2.place(x = size_wn_x + menu_x + size_wn_x //2 - lbl2.winfo_reqwidth() //2 , y = size_wn_y+3)
                lbl3 = Label(tk, text= '', font=('Helvetica', 16))
                lbl3.place(x = size_wn_x + step_x+20, y = 12*step_y)

                def mark_igrok(igrok_mark):
                    if igrok_mark:
                        lbl1.configure(bg='red')
                        lbl2.configure(bg='#f0f0f0')
                        lbl3.configure(text='Ход Игрока №2')
                    else:
                        lbl2.configure(bg='red')
                        lbl1.configure(bg='#f0f0f0')
                        lbl3.configure(text='Ход Игрока №1')
                mark_igrok(hod_igroka)

                def GLmenu():
                    global running
                    running=False
                    tk.destroy()

                btn_GLmenu = Button(tk,text="Главное меню", command=GLmenu)
                btn_GLmenu.place(x=size_wn_x + menu_x//3, y = 30)

                def Play_return():
                    global list_ids, Clik_String1, Clik_String2, boom, enemy_ships1, enemy_ships2
                    for el in list_ids:
                        pole.delete(el)
                    list_ids =[]
                    Clik_String1 = [[-1 for i in range(s_y)] for i in range(s_x)]
                    Clik_String2 = [[-1 for i in range(s_y)] for i in range(s_x)]
                    boom = [[0 for i in range(s_y)] for i in range(s_x)]
                    enemy_ships1 = generate_enemy_ships()
                    enemy_ships2 = generate_enemy_ships()

                btn_return = Button(tk, text="Начать заново!", command=Play_return)
                btn_return.place(x=size_wn_x + menu_x//3, y=70)

                def show_enemy1():
                    for i in range (0, s_x):
                        for j in range(0, s_y):
                            if enemy_ships1[j][i] > 0:
                                color = "red"
                                if Clik_String1[j][i] != -1:
                                    color = "green"
                                _id = pole.create_rectangle(i*step_x,j*step_y,i*step_x+step_x,j*step_y+step_y,fill=color)
                                list_ids.append(_id)

                btn_ships_play1 = Button(tk, text="Показать корабли Игрока №1", command=show_enemy1)
                btn_ships_play1.place(x=size_wn_x + menu_x //4-15, y=110)

                def show_enemy2():
                    for i in range (0, s_x):
                        for j in range(0, s_y):
                            if enemy_ships2[j][i] > 0:
                                color = "red"
                                if Clik_String2[j][i] != -1:
                                    color = "green"
                                _id = pole.create_rectangle(size_wn_x+menu_x + i*step_x,j*step_y,size_wn_x+menu_x + i*step_x+step_x,j*step_y+step_y,fill=color)
                                list_ids.append(_id)

                btn_ships_play2 = Button(tk, text="Показать корабли Игрока №2", command=show_enemy2)
                btn_ships_play2.place(x=size_wn_x + menu_x //4-15, y=150)

                def draw_point(x,y):
                    global hod_igroka
                    print(enemy_ships1[y][x])
                    if Helper:
                        if enemy_ships1[y][x] == 0:
                            color = 'black'
                            id1 = pole.create_oval(x*step_x+step_x//3,y*step_y+step_y//3,x*step_x+step_x - step_y//3,y*step_y+step_y-step_y//3,fill=color)
                            list_ids.append(id1)
                            hod_igroka = False
                        if enemy_ships1[y][x] > 0 and enemy_ships1[y][x] <= 4:
                            color1 = 'pink'
                            id2 = pole.create_rectangle(x * step_x, y * step_y + step_y // 2 - step_y // 10, x * step_x + step_x,y * step_y + step_y // 2 + step_y // 10, fill=color1)
                            id3= pole.create_rectangle(x * step_x + step_x // 2 - step_x // 10, y * step_y, x * step_x + step_x // 2 + step_x // 10, y * step_y + step_y, fill=color1)
                            list_ids.append(id2)
                            list_ids.append(id3)
                        if enemy_ships1[y][x] > 4 and enemy_ships1[y][x] <= 7:
                            color2 = 'blue'
                            id4 = pole.create_rectangle(x * step_x, y * step_y + step_y // 2 - step_y // 10, x * step_x + step_x,y * step_y + step_y // 2 + step_y // 10, fill=color2)
                            id5= pole.create_rectangle(x * step_x + step_x // 2 - step_x // 10, y * step_y, x * step_x + step_x // 2 + step_x // 10, y * step_y + step_y, fill=color2)
                            list_ids.append(id4)
                            list_ids.append(id5)
                        if enemy_ships1[y][x] == 8 or enemy_ships1[y][x] == 9:
                            color3 = 'green'
                            id6 = pole.create_rectangle(x * step_x, y * step_y + step_y // 2 - step_y // 10, x * step_x + step_x,y * step_y + step_y // 2 + step_y // 10, fill=color3)
                            id7= pole.create_rectangle(x * step_x + step_x // 2 - step_x // 10, y * step_y, x * step_x + step_x // 2 + step_x // 10, y * step_y + step_y, fill=color3)
                            list_ids.append(id6)
                            list_ids.append(id7)
                        if enemy_ships1[y][x] == 10:
                            color4 = 'yellow'
                            id8 = pole.create_rectangle(x * step_x, y * step_y + step_y // 2 - step_y // 10, x * step_x + step_x,y * step_y + step_y // 2 + step_y // 10, fill=color4)
                            id9= pole.create_rectangle(x * step_x + step_x // 2 - step_x // 10, y * step_y, x * step_x + step_x // 2 + step_x // 10, y * step_y + step_y, fill=color4)
                            list_ids.append(id8)
                            list_ids.append(id9)
                    else:
                        if enemy_ships1[y][x] == 0:
                            color = 'black'
                            id1 = pole.create_oval(x*step_x+step_x//3,y*step_y+step_y//3,x*step_x+step_x - step_y//3,y*step_y+step_y-step_y//3,fill=color)
                            list_ids.append(id1)
                            hod_igroka = False
                        if enemy_ships1[y][x] > 0:
                            color1 = 'grey'
                            id2 = pole.create_rectangle(x * step_x, y * step_y + step_y // 2 - step_y // 10, x * step_x + step_x,y * step_y + step_y // 2 + step_y // 10, fill=color1)
                            id3= pole.create_rectangle(x * step_x + step_x // 2 - step_x // 10, y * step_y, x * step_x + step_x // 2 + step_x // 10, y * step_y + step_y, fill=color1)
                            list_ids.append(id2)
                            list_ids.append(id3)

                def draw_point2(x,y, offset_x=size_wn_x + menu_x): 
                    global hod_igroka
                    print(enemy_ships2[y][x])
                    if Helper:
                        if enemy_ships2[y][x] == 0:
                            color = 'black'
                            id10 = pole.create_oval(offset_x + x*step_x+step_x//3,y*step_y+step_y//3,offset_x + x*step_x+step_x - step_y//3,y*step_y+step_y-step_y//3,fill=color)
                            list_ids.append(id10)
                            hod_igroka =True
                        if enemy_ships2[y][x] > 0 and enemy_ships2[y][x] <= 4:
                            color1 = 'pink'
                            id11 = pole.create_rectangle(offset_x + x * step_x, y * step_y + step_y // 2 - step_y // 10, offset_x + x * step_x + step_x,y * step_y + step_y // 2 + step_y // 10, fill=color1)
                            id12= pole.create_rectangle(offset_x + x * step_x + step_x // 2 - step_x // 10, y * step_y,offset_x + x * step_x + step_x // 2 + step_x // 10, y * step_y + step_y, fill=color1)
                            list_ids.append(id11)
                            list_ids.append(id12)
                        if enemy_ships2[y][x] >= 5 and enemy_ships2[y][x] <= 7:
                            color2 = 'blue'
                            id13 = pole.create_rectangle(offset_x + x * step_x, y * step_y + step_y // 2 - step_y // 10,offset_x + x * step_x + step_x,y * step_y + step_y // 2 + step_y // 10, fill=color2)
                            id14 = pole.create_rectangle(offset_x + x * step_x + step_x // 2 - step_x // 10, y * step_y,offset_x + x * step_x + step_x // 2 + step_x // 10, y * step_y + step_y, fill=color2)
                            list_ids.append(id13)
                            list_ids.append(id14)
                        if enemy_ships2[y][x] == 8 or enemy_ships2[y][x] == 9:
                            color3 = 'green'
                            id15 = pole.create_rectangle(offset_x + x * step_x, y * step_y + step_y // 2 - step_y // 10,offset_x + x * step_x + step_x,y * step_y + step_y // 2 + step_y // 10, fill=color3)
                            id16 = pole.create_rectangle(offset_x + x * step_x + step_x // 2 - step_x // 10, y * step_y,offset_x + x * step_x + step_x // 2 + step_x // 10, y * step_y + step_y, fill=color3)
                            list_ids.append(id15)
                            list_ids.append(id16)
                        if enemy_ships2[y][x] == 10:
                            color4 = 'yellow'
                            id17 = pole.create_rectangle(offset_x + x * step_x, y * step_y + step_y // 2 - step_y // 10,offset_x + x * step_x + step_x,y * step_y + step_y // 2 + step_y // 10, fill=color4)
                            id18= pole.create_rectangle(offset_x + x * step_x + step_x // 2 - step_x // 10, y * step_y,offset_x + x * step_x + step_x // 2 + step_x // 10, y * step_y + step_y, fill=color4)
                            list_ids.append(id17)
                            list_ids.append(id18)
                    else:
                        if enemy_ships2[y][x] == 0:
                            color = 'black'
                            id10 = pole.create_oval(offset_x + x*step_x+step_x//3,y*step_y+step_y//3,offset_x + x*step_x+step_x - step_y//3,y*step_y+step_y-step_y//3,fill=color)
                            list_ids.append(id10)
                            hod_igroka = True
                        if enemy_ships2[y][x] > 0:
                            color1 = 'grey'
                            id11 = pole.create_rectangle(offset_x + x * step_x, y * step_y + step_y // 2 - step_y // 10, offset_x + x * step_x + step_x,y * step_y + step_y // 2 + step_y // 10, fill=color1)
                            id12= pole.create_rectangle(offset_x + x * step_x + step_x // 2 - step_x // 10, y * step_y,offset_x + x * step_x + step_x // 2 + step_x // 10, y * step_y + step_y, fill=color1)
                            list_ids.append(id11)
                            list_ids.append(id12)
                        
                def check_winer1():
                    win = True
                    for i in range(0,s_x):
                            for j in range(0, s_x):
                                if enemy_ships1[i][j] > 0:
                                    if Clik_String1[i][j] == -1:
                                        win = False
                    return win
                
                def check_winer2():
                    win = True
                    for i in range(0,s_x):
                            for j in range(0, s_x):
                                if enemy_ships2[i][j] > 0:
                                    if Clik_String2[i][j] == -1:
                                        win = False
                    return win

                def add_to_all(event):
                    global Clik_String1, Clik_String2, hod_igroka
                    _type=0
                    mouse_x=pole.winfo_pointerx() - pole.winfo_rootx()
                    mouse_y=pole.winfo_pointery() - pole.winfo_rooty()
                    ip_x=mouse_x//step_x
                    ip_y=mouse_y//step_y
                    if ip_x < s_x and ip_y < s_y and hod_igroka: #первое игровое поле
                        if Clik_String1[ip_y][ip_x] == -1:
                            Clik_String1[ip_y][ip_x] = _type
                            draw_point(ip_x,ip_y)
                            if check_winer1():
                                Clik_String1 = [[10 for i in range(s_y)] for i in range(s_x)]
                                Clik_String2 = [[10 for i in range(s_y)] for i in range(s_x)]
                                winner = "Победа Игрока №2 (Все корабли Игрока №1 подбиты)!!!"
                                mb.showinfo(title='Победа', message=winner)

                    if ip_x >= s_x + 6 and ip_x <= s_x + s_x + 6 and ip_y < s_y and not hod_igroka: # второе игровое поле
                        if Clik_String2[ip_y][ip_x - s_x - 6] == -1:
                            Clik_String2[ip_y][ip_x - s_x - 6] = _type
                            draw_point2(ip_x - s_x - 6,ip_y)
                            if check_winer2():
                                Clik_String1 = [[10 for i in range(s_y)] for i in range(s_x)]
                                Clik_String2 = [[10 for i in range(s_y)] for i in range(s_x)]
                                winner = "Победа Игрока №1 (Все корабли Игрока №2 подбиты)!!!"
                                mb.showinfo(title='Победа', message=winner)
                    mark_igrok(hod_igroka)    

                pole.bind_all("<Button-1>", add_to_all)

                def generate_enemy_ships():
                    near_ships = []
                    ships_list = []
                    #Добавление кораблей в список
                    for i in range(enemy_ships_1):
                        ships_list.append(ship_1) 
                    for i in range(enemy_ships_2):
                        ships_list.append(ship_2) 
                    for i in range(enemy_ships_3):
                        ships_list.append(ship_3) 
                    for i in range(enemy_ships_4):
                        ships_list.append(ship_4) 
                    sum_enemy_ships = sum(ships_list)
                    sum_enemy=0
                    while sum_enemy != sum_enemy_ships:
                        near_ships=[[0 for i in range(s_y+1)] for i in range(s_x+1)] 

                        for i in range(ship): 
                            len = ships_list[i]
                            horizont_vertikal = random.randrange(1,3)

                            primerno_x = random.randrange(0, s_x)
                            if primerno_x + len > s_x:
                                primerno_x = primerno_x - len
                            
                            primerno_y = random.randrange(0, s_y)
                            if primerno_y + len > s_y:
                                primerno_y - primerno_y - len

                            if horizont_vertikal == 1:
                                if primerno_x + len <= s_x:
                                    for j in range(0, len):
                                        try:
                                            #Проверка есть ли корабль рядом
                                            check_ships = near_ships[primerno_y][primerno_x - 1] + \
                                                                near_ships[primerno_y][primerno_x + j] + \
                                                                near_ships[primerno_y][primerno_x + j + 1] + \
                                                                near_ships[primerno_y + 1][primerno_x + j + 1] + \
                                                                near_ships[primerno_y - 1][primerno_x + j + 1] + \
                                                                near_ships[primerno_y + 1][primerno_x + j] + \
                                                                near_ships[primerno_y - 1][primerno_x + j] + \
                                                                near_ships[primerno_y + 1][primerno_x + 1] + \
                                                                near_ships[primerno_y - 1][primerno_x - 1] + \
                                                                near_ships[primerno_y - 1][primerno_x + 1] + \
                                                                near_ships[primerno_y + 1][primerno_x - 1]
                                            if check_ships == 0:
                                                near_ships[primerno_y][primerno_x + j] = i + 1
                                        except Exception:
                                            pass
                            if horizont_vertikal == 2:
                                if primerno_y + len <= s_y:
                                    for j in range(0, len):
                                        try:
                                            #Проверка есть ли корабль рядом
                                            check_ships = near_ships[primerno_x - 1][primerno_y] + \
                                                                near_ships[primerno_x + j][primerno_y] + \
                                                                near_ships[primerno_x + j + 1][primerno_y] + \
                                                                near_ships[primerno_x + j + 1][primerno_y + 1] + \
                                                                near_ships[primerno_x + j + 1][primerno_y - 1] + \
                                                                near_ships[primerno_x + j][primerno_y + 1] + \
                                                                near_ships[primerno_x + j][primerno_y - 1] + \
                                                                near_ships[primerno_x + 1][primerno_y + 1] + \
                                                                near_ships[primerno_x - 1][primerno_y - 1] + \
                                                                near_ships[primerno_x + 1][primerno_y - 1] + \
                                                                near_ships[primerno_x - 1][primerno_y + 1]
                                            if check_ships == 0:
                                                near_ships[primerno_x+j][primerno_y] = i + 1
                                        except Exception:
                                            pass
                        sum_enemy = 0
                        for i in range(0,s_x):
                            for j in range(0, s_x):
                                if near_ships[i][j] > 0:
                                    sum_enemy = sum_enemy + 1
                    return near_ships

                enemy_ships1 = generate_enemy_ships()
                enemy_ships2 = generate_enemy_ships()
                
                while running:
                    if running:
                        tk.update_idletasks()
                        tk.update()
                    time.sleep(0.005)
            poles(12)
            if Exit:
                exit()
            GLMenu.show()

        def openPlayMedium():
            global Exit
            Exit = False
            Slosnost.close()
            GLMenu.show()
            GLMenu.hide()
            def poles(number_rectengle):
                global running, hod_igroka, size_wn_x, size_wn_y, s_x, s_y, step_x, step_y, ship, ship_1, ship_2, ship_3, ship_4, enemy_ships_1, enemy_ships_2, enemy_ships_3, enemy_ships_4, enemy_ships1, enemy_ships2, menu_x, menu_y, list_ids, Clik_String1, Clik_String2, boom
                
                tk = Tk()
                running=True

                size_wn_x= 600
                size_wn_y= 600
                s_x=s_y=number_rectengle #размер поля
                step_x=size_wn_x//s_x #шаг по горизонтали
                step_y=size_wn_y//s_y #шаг по вертекали
                size_wn_x = step_x * s_x
                size_wn_y = step_y * s_y
                #общее количество кораблей
                ship = 10
                #размеры кораблей
                ship_1 = 1
                ship_2 = 2
                ship_3 = 3
                ship_4 = 4
                #колличество кораблей
                enemy_ships_1= 4
                enemy_ships_2 = 3
                enemy_ships_3 = 2
                enemy_ships_4 = 1
                enemy_ships1 = [[0 for i in range(s_y+1)] for i in range(s_x+1)]
                enemy_ships2 = [[0 for i in range(s_y+1)] for i in range(s_x+1)]
                menu_x= step_x*7
                menu_y = 40
                list_ids=[] #список объектов
                Clik_String1 = [[-1 for i in range(s_y)] for i in range(s_x)] #список куда мы кликнули
                Clik_String2 = [[-1 for i in range(s_y)] for i in range(s_x)] #список куда мы кликнули
                boom = [[0 for i in range(s_y)] for i in range(s_x)] #список попаданей по короблям

                photo = PhotoImage(file='D:\Projeck\Proect\Sea_warr.png')
                tk.iconphoto(False, photo)

                #Истина - 2 игрок, ложно - 1 игрок
                hod_igroka=False

                def settings():
                    global var, Helper
                    Helper=False
                    var = IntVar(tk)
                    Btn_Check = Checkbutton(text="Включить обозначения размера корабля?",
                                            variable=var,
                                            command=print_value)
                    Btn_Check.pack(side='bottom')

                def print_value():
                    global Helper
                    print(var.get())
                    if var.get() == 1:
                        Helper=True
                    else:
                        Helper=False

                settings()

                def closing():
                    global running, Exit
                    if mb.askokcancel("Выход из игры", "Хотите выйти из игры?"):
                        running=False
                        Exit = True
                        tk.destroy()

                tk.protocol("WM_DELETE_WINDOW", closing)
                tk.title("Морской бой")
                tk.resizable(0,0)
                tk.wm_attributes("-topmost", 1)
                pole = Canvas(tk, width=size_wn_x+menu_x + size_wn_x, height=size_wn_y+ menu_y, bd=0, highlightthickness=0)
                pole.create_rectangle(0,0,size_wn_x, size_wn_y, fill="white")
                pole.create_rectangle(size_wn_x+menu_x,0,size_wn_x+menu_x + size_wn_x, size_wn_y, fill="white")
                pole.pack()
                tk.update()

                Pink=Label(tk,text="",background="pink")
                Pink.place(x=size_wn_x+menu_x//5,y=step_y*11,width=15,height=15)
                one_palub=Label(tk,text="- Однопалубный корабль")
                one_palub.place(x=size_wn_x+menu_x//5+20,y=step_y*11)
                Blue=Label(tk,text="",background="blue")
                Blue.place(x=size_wn_x+menu_x//5,y=step_y*12,width=15,height=15)
                two_palub=Label(tk,text="- Двухпалубный корабль")
                two_palub.place(x=size_wn_x+menu_x//5+20,y=step_y*12)
                Green=Label(tk,text="",background="green")
                Green.place(x=size_wn_x+menu_x//5,y=step_y*13,width=15,height=15)
                three_palub=Label(tk,text="- Трёхпалубный корабль")
                three_palub.place(x=size_wn_x+menu_x//5+20,y=step_y*13)
                Yellow=Label(tk,text="",background="yellow")
                Yellow.place(x=size_wn_x+menu_x//5,y=step_y*14,width=15,height=15)
                four_palub=Label(tk,text="- Четырёхпалубный корабль")
                four_palub.place(x=size_wn_x+menu_x//5+20,y=step_y*14)

                def Pole(offset_x=0):
                    for i in range(s_x+1):
                        pole.create_line(offset_x + step_x * i,0,offset_x + step_x * i,size_wn_y)
                    for i in range(s_y+1):
                        pole.create_line(offset_x,step_y * i ,offset_x + size_wn_x, step_y * i)

                Pole()
                Pole(size_wn_x+menu_x)

                lbl1 = Label(tk, text= 'Игрок №1', font=('Helvetica', 16))
                lbl1.place(x = size_wn_x //2 - lbl1.winfo_reqwidth() //2 , y = size_wn_y+3)
                lbl2 = Label(tk, text= 'Игрок №2', font=('Helvetica', 16))
                lbl2.place(x = size_wn_x + menu_x + size_wn_x //2 - lbl2.winfo_reqwidth() //2 , y = size_wn_y+3)
                lbl3 = Label(tk, text= '', font=('Helvetica', 16))
                lbl3.place(x = size_wn_x + step_x+15, y = 15*step_y)

                def mark_igrok(igrok_mark):
                    if igrok_mark:
                        lbl1.configure(bg='red')
                        lbl2.configure(bg='#f0f0f0')
                        lbl3.configure(text='Ход Игрока №2')
                    else:
                        lbl2.configure(bg='red')
                        lbl1.configure(bg='#f0f0f0')
                        lbl3.configure(text='Ход Игрока №1')
                mark_igrok(hod_igroka)

                def GLmenu():
                    global running
                    running=False
                    tk.destroy()

                btn_GLmenu = Button(tk,text="Главное меню", command=GLmenu)
                btn_GLmenu.place(x=size_wn_x + menu_x//3, y = 30)

                def Play_return():
                    global list_ids, Clik_String1, Clik_String2, boom, enemy_ships1, enemy_ships2
                    for el in list_ids:
                        pole.delete(el)
                    list_ids =[]
                    Clik_String1 = [[-1 for i in range(s_y)] for i in range(s_x)]
                    Clik_String2 = [[-1 for i in range(s_y)] for i in range(s_x)]
                    boom = [[0 for i in range(s_y)] for i in range(s_x)]
                    enemy_ships1 = generate_enemy_ships()
                    enemy_ships2 = generate_enemy_ships()

                btn_return = Button(tk, text="Начать заново!", command=Play_return)
                btn_return.place(x=size_wn_x + menu_x//3, y=70)

                def show_enemy1():
                    for i in range (0, s_x):
                        for j in range(0, s_y):
                            if enemy_ships1[j][i] > 0:
                                color = "red"
                                if Clik_String1[j][i] != -1:
                                    color = "green"
                                _id = pole.create_rectangle(i*step_x,j*step_y,i*step_x+step_x,j*step_y+step_y,fill=color)
                                list_ids.append(_id)

                btn_ships_play1 = Button(tk, text="Показать корабли Игрока №1", command=show_enemy1)
                btn_ships_play1.place(x=size_wn_x + menu_x //4-15, y=110)

                def show_enemy2():
                    for i in range (0, s_x):
                        for j in range(0, s_y):
                            if enemy_ships2[j][i] > 0:
                                color = "red"
                                if Clik_String2[j][i] != -1:
                                    color = "green"
                                _id = pole.create_rectangle(size_wn_x+menu_x + i*step_x,j*step_y,size_wn_x+menu_x + i*step_x+step_x,j*step_y+step_y,fill=color)
                                list_ids.append(_id)

                btn_ships_play2 = Button(tk, text="Показать корабли Игрока №2", command=show_enemy2)
                btn_ships_play2.place(x=size_wn_x + menu_x //4-15, y=150)

                def draw_point(x,y):
                    global hod_igroka
                    print(enemy_ships1[y][x])
                    if Helper:
                        if enemy_ships1[y][x] == 0:
                            color = 'black'
                            id1 = pole.create_oval(x*step_x+step_x//3,y*step_y+step_y//3,x*step_x+step_x - step_y//3,y*step_y+step_y-step_y//3,fill=color)
                            list_ids.append(id1)
                            hod_igroka = False
                        if enemy_ships1[y][x] > 0 and enemy_ships1[y][x] <= 4:
                            color1 = 'pink'
                            id2 = pole.create_rectangle(x * step_x, y * step_y + step_y // 2 - step_y // 10, x * step_x + step_x,y * step_y + step_y // 2 + step_y // 10, fill=color1)
                            id3= pole.create_rectangle(x * step_x + step_x // 2 - step_x // 10, y * step_y, x * step_x + step_x // 2 + step_x // 10, y * step_y + step_y, fill=color1)
                            list_ids.append(id2)
                            list_ids.append(id3)
                        if enemy_ships1[y][x] > 4 and enemy_ships1[y][x] <= 7:
                            color2 = 'blue'
                            id4 = pole.create_rectangle(x * step_x, y * step_y + step_y // 2 - step_y // 10, x * step_x + step_x,y * step_y + step_y // 2 + step_y // 10, fill=color2)
                            id5= pole.create_rectangle(x * step_x + step_x // 2 - step_x // 10, y * step_y, x * step_x + step_x // 2 + step_x // 10, y * step_y + step_y, fill=color2)
                            list_ids.append(id4)
                            list_ids.append(id5)
                        if enemy_ships1[y][x] == 8 or enemy_ships1[y][x] == 9:
                            color3 = 'green'
                            id6 = pole.create_rectangle(x * step_x, y * step_y + step_y // 2 - step_y // 10, x * step_x + step_x,y * step_y + step_y // 2 + step_y // 10, fill=color3)
                            id7= pole.create_rectangle(x * step_x + step_x // 2 - step_x // 10, y * step_y, x * step_x + step_x // 2 + step_x // 10, y * step_y + step_y, fill=color3)
                            list_ids.append(id6)
                            list_ids.append(id7)
                        if enemy_ships1[y][x] == 10:
                            color4 = 'yellow'
                            id8 = pole.create_rectangle(x * step_x, y * step_y + step_y // 2 - step_y // 10, x * step_x + step_x,y * step_y + step_y // 2 + step_y // 10, fill=color4)
                            id9= pole.create_rectangle(x * step_x + step_x // 2 - step_x // 10, y * step_y, x * step_x + step_x // 2 + step_x // 10, y * step_y + step_y, fill=color4)
                            list_ids.append(id8)
                            list_ids.append(id9)
                    else:
                        if enemy_ships1[y][x] == 0:
                            color = 'black'
                            id1 = pole.create_oval(x*step_x+step_x//3,y*step_y+step_y//3,x*step_x+step_x - step_y//3,y*step_y+step_y-step_y//3,fill=color)
                            list_ids.append(id1)
                            hod_igroka = False
                        if enemy_ships1[y][x] > 0:
                            color1 = 'grey'
                            id2 = pole.create_rectangle(x * step_x, y * step_y + step_y // 2 - step_y // 10, x * step_x + step_x,y * step_y + step_y // 2 + step_y // 10, fill=color1)
                            id3= pole.create_rectangle(x * step_x + step_x // 2 - step_x // 10, y * step_y, x * step_x + step_x // 2 + step_x // 10, y * step_y + step_y, fill=color1)
                            list_ids.append(id2)
                            list_ids.append(id3)

                def draw_point2(x,y, offset_x=size_wn_x + menu_x):
                    global hod_igroka
                    print(enemy_ships2[y][x])
                    if Helper:
                        if enemy_ships2[y][x] == 0:
                            color = 'black'
                            id10 = pole.create_oval(offset_x + x*step_x+step_x//3,y*step_y+step_y//3,offset_x + x*step_x+step_x - step_y//3,y*step_y+step_y-step_y//3,fill=color)
                            list_ids.append(id10)
                            hod_igroka =True
                        if enemy_ships2[y][x] > 0 and enemy_ships2[y][x] <= 4:
                            color1 = 'pink'
                            id11 = pole.create_rectangle(offset_x + x * step_x, y * step_y + step_y // 2 - step_y // 10, offset_x + x * step_x + step_x,y * step_y + step_y // 2 + step_y // 10, fill=color1)
                            id12= pole.create_rectangle(offset_x + x * step_x + step_x // 2 - step_x // 10, y * step_y,offset_x + x * step_x + step_x // 2 + step_x // 10, y * step_y + step_y, fill=color1)
                            list_ids.append(id11)
                            list_ids.append(id12)
                        if enemy_ships2[y][x] >= 5 and enemy_ships2[y][x] <= 7:
                            color2 = 'blue'
                            id13 = pole.create_rectangle(offset_x + x * step_x, y * step_y + step_y // 2 - step_y // 10,offset_x + x * step_x + step_x,y * step_y + step_y // 2 + step_y // 10, fill=color2)
                            id14 = pole.create_rectangle(offset_x + x * step_x + step_x // 2 - step_x // 10, y * step_y,offset_x + x * step_x + step_x // 2 + step_x // 10, y * step_y + step_y, fill=color2)
                            list_ids.append(id13)
                            list_ids.append(id14)
                        if enemy_ships2[y][x] == 8 or enemy_ships2[y][x] == 9:
                            color3 = 'green'
                            id15 = pole.create_rectangle(offset_x + x * step_x, y * step_y + step_y // 2 - step_y // 10,offset_x + x * step_x + step_x,y * step_y + step_y // 2 + step_y // 10, fill=color3)
                            id16 = pole.create_rectangle(offset_x + x * step_x + step_x // 2 - step_x // 10, y * step_y,offset_x + x * step_x + step_x // 2 + step_x // 10, y * step_y + step_y, fill=color3)
                            list_ids.append(id15)
                            list_ids.append(id16)
                        if enemy_ships2[y][x] == 10:
                            color4 = 'yellow'
                            id17 = pole.create_rectangle(offset_x + x * step_x, y * step_y + step_y // 2 - step_y // 10,offset_x + x * step_x + step_x,y * step_y + step_y // 2 + step_y // 10, fill=color4)
                            id18= pole.create_rectangle(offset_x + x * step_x + step_x // 2 - step_x // 10, y * step_y,offset_x + x * step_x + step_x // 2 + step_x // 10, y * step_y + step_y, fill=color4)
                            list_ids.append(id17)
                            list_ids.append(id18)
                    else:
                        if enemy_ships2[y][x] == 0:
                            color = 'black'
                            id10 = pole.create_oval(offset_x + x*step_x+step_x//3,y*step_y+step_y//3,offset_x + x*step_x+step_x - step_y//3,y*step_y+step_y-step_y//3,fill=color)
                            list_ids.append(id10)
                            hod_igroka = True
                        if enemy_ships2[y][x] > 0:
                            color1 = 'grey'
                            id11 = pole.create_rectangle(offset_x + x * step_x, y * step_y + step_y // 2 - step_y // 10, offset_x + x * step_x + step_x,y * step_y + step_y // 2 + step_y // 10, fill=color1)
                            id12= pole.create_rectangle(offset_x + x * step_x + step_x // 2 - step_x // 10, y * step_y,offset_x + x * step_x + step_x // 2 + step_x // 10, y * step_y + step_y, fill=color1)
                            list_ids.append(id11)
                            list_ids.append(id12)
                        
                def check_winer1():
                    win = True
                    for i in range(0,s_x):
                            for j in range(0, s_x):
                                if enemy_ships1[i][j] > 0:
                                    if Clik_String1[i][j] == -1:
                                        win = False
                    return win
                
                def check_winer2():
                    win = True
                    for i in range(0,s_x):
                            for j in range(0, s_x):
                                if enemy_ships2[i][j] > 0:
                                    if Clik_String2[i][j] == -1:
                                        win = False
                    return win

                def add_to_all(event):
                    global Clik_String1, Clik_String2, hod_igroka
                    _type=0
                    mouse_x=pole.winfo_pointerx() - pole.winfo_rootx()
                    mouse_y=pole.winfo_pointery() - pole.winfo_rooty()
                    ip_x=mouse_x//step_x
                    ip_y=mouse_y//step_y
                    if ip_x < s_x and ip_y < s_y and hod_igroka: #первое игровое поле
                        if Clik_String1[ip_y][ip_x] == -1:
                            Clik_String1[ip_y][ip_x] = _type
                            draw_point(ip_x,ip_y)
                            if check_winer1():
                                Clik_String1 = [[10 for i in range(s_y)] for i in range(s_x)]
                                Clik_String2 = [[10 for i in range(s_y)] for i in range(s_x)]
                                winner = "Победа Игрока №2(Все корабли Игрока №1 подбиты)!!!"
                                mb.showinfo(title='Победа', message=winner)

                    if ip_x >= s_x + 7 and ip_x <= s_x + s_x + 7 and ip_y < s_y and not hod_igroka: # второе игровое поле
                        if Clik_String2[ip_y][ip_x - s_x - 7] == -1:
                            Clik_String2[ip_y][ip_x - s_x - 7] = _type
                            draw_point2(ip_x - s_x - 7,ip_y)
                            if check_winer2():
                                Clik_String1 = [[10 for i in range(s_y)] for i in range(s_x)]
                                Clik_String2 = [[10 for i in range(s_y)] for i in range(s_x)]
                                winner = "Победа Игрока №1 (Все корабли Игрока №2 подбиты)!!!"
                                mb.showinfo(title='Победа', message=winner)
                    mark_igrok(hod_igroka)    

                pole.bind_all("<Button-1>", add_to_all)

                def generate_enemy_ships():
                    near_ships = []
                    ships_list = []
                    #Добавление кораблей в список
                    for i in range(enemy_ships_1):
                        ships_list.append(ship_1) 
                    for i in range(enemy_ships_2):
                        ships_list.append(ship_2) 
                    for i in range(enemy_ships_3):
                        ships_list.append(ship_3) 
                    for i in range(enemy_ships_4):
                        ships_list.append(ship_4) 
                    sum_enemy_ships = sum(ships_list)
                    sum_enemy=0
                    while sum_enemy != sum_enemy_ships:
                        near_ships=[[0 for i in range(s_y+1)] for i in range(s_x+1)] 

                        for i in range(ship): 
                            len = ships_list[i]
                            horizont_vertikal = random.randrange(1,3)

                            primerno_x = random.randrange(0, s_x)
                            if primerno_x + len > s_x:
                                primerno_x = primerno_x - len
                            
                            primerno_y = random.randrange(0, s_y)
                            if primerno_y + len > s_y:
                                primerno_y - primerno_y - len

                            if horizont_vertikal == 1:
                                if primerno_x + len <= s_x:
                                    for j in range(0, len):
                                        try:
                                            #Проверка есть ли корабль рядом
                                            check_ships = near_ships[primerno_y][primerno_x - 1] + \
                                                                near_ships[primerno_y][primerno_x + j] + \
                                                                near_ships[primerno_y][primerno_x + j + 1] + \
                                                                near_ships[primerno_y + 1][primerno_x + j + 1] + \
                                                                near_ships[primerno_y - 1][primerno_x + j + 1] + \
                                                                near_ships[primerno_y + 1][primerno_x + j] + \
                                                                near_ships[primerno_y - 1][primerno_x + j] + \
                                                                near_ships[primerno_y + 1][primerno_x + 1] + \
                                                                near_ships[primerno_y - 1][primerno_x - 1] + \
                                                                near_ships[primerno_y - 1][primerno_x + 1] + \
                                                                near_ships[primerno_y + 1][primerno_x - 1]
                                            if check_ships == 0:
                                                near_ships[primerno_y][primerno_x + j] = i + 1
                                        except Exception:
                                            pass
                            if horizont_vertikal == 2:
                                if primerno_y + len <= s_y:
                                    for j in range(0, len):
                                        try:
                                            #Проверка есть ли корабль рядом
                                            check_ships = near_ships[primerno_x - 1][primerno_y] + \
                                                                near_ships[primerno_x + j][primerno_y] + \
                                                                near_ships[primerno_x + j + 1][primerno_y] + \
                                                                near_ships[primerno_x + j + 1][primerno_y + 1] + \
                                                                near_ships[primerno_x + j + 1][primerno_y - 1] + \
                                                                near_ships[primerno_x + j][primerno_y + 1] + \
                                                                near_ships[primerno_x + j][primerno_y - 1] + \
                                                                near_ships[primerno_x + 1][primerno_y + 1] + \
                                                                near_ships[primerno_x - 1][primerno_y - 1] + \
                                                                near_ships[primerno_x + 1][primerno_y - 1] + \
                                                                near_ships[primerno_x - 1][primerno_y + 1]
                                            if check_ships == 0:
                                                near_ships[primerno_x+j][primerno_y] = i + 1
                                        except Exception:
                                            pass
                        sum_enemy = 0
                        for i in range(0,s_x):
                            for j in range(0, s_x):
                                if near_ships[i][j] > 0:
                                    sum_enemy = sum_enemy + 1
                    return near_ships

                enemy_ships1 = generate_enemy_ships()
                enemy_ships2 = generate_enemy_ships()

                while running:
                    if running:
                        tk.update_idletasks()
                        tk.update()
                    time.sleep(0.005)
            poles(15)
            if Exit:
                exit()
            GLMenu.show()

        def openPlayHard():
            global Exit
            Exit = False
            Slosnost.close()
            GLMenu.show()
            GLMenu.hide()
            def poles(number_rectengle):
                global running, hod_igroka, size_wn_x, size_wn_y, s_x, s_y, step_x, step_y, ship, ship_1, ship_2, ship_3, ship_4, enemy_ships_1, enemy_ships_2, enemy_ships_3, enemy_ships_4, enemy_ships1, enemy_ships2, menu_x, menu_y, list_ids, Clik_String1, Clik_String2, boom
                
                tk = Tk()
                running=True

                size_wn_x= 600
                size_wn_y= 600
                s_x=s_y=number_rectengle #размер поля
                step_x=size_wn_x//s_x #шаг по горизонтали
                step_y=size_wn_y//s_y #шаг по вертекали
                size_wn_x = step_x * s_x
                size_wn_y = step_y * s_y
                #общее количество кораблей
                ship = 10
                #размеры кораблей
                ship_1 = 1
                ship_2 = 2
                ship_3 = 3
                ship_4 = 4
                #колличество кораблей
                enemy_ships_1= 4
                enemy_ships_2 = 3
                enemy_ships_3 = 2
                enemy_ships_4 = 1
                enemy_ships1 = [[0 for i in range(s_y+1)] for i in range(s_x+1)]
                enemy_ships2 = [[0 for i in range(s_y+1)] for i in range(s_x+1)]
                menu_x= step_x*8
                menu_y = 40
                list_ids=[] #список объектов
                Clik_String1 = [[-1 for i in range(s_y)] for i in range(s_x)] #список куда мы кликнули
                Clik_String2 = [[-1 for i in range(s_y)] for i in range(s_x)] #список куда мы кликнули
                boom = [[0 for i in range(s_y)] for i in range(s_x)] #список попаданей по короблям

                photo = PhotoImage(file='D:\Projeck\Proect\Sea_warr.png')
                tk.iconphoto(False, photo)

                #Истина - 2 игрок, ложно - 1 игрок
                hod_igroka=False

                def settings():
                    global var, Helper
                    Helper=False
                    var = IntVar(tk)
                    Btn_Check = Checkbutton(text="Включить обозначения размера корабля?",
                                            variable=var,
                                            command=print_value)
                    Btn_Check.pack(side='bottom')

                def print_value():
                    global Helper
                    print(var.get())
                    if var.get() == 1:
                        Helper=True
                    else:
                        Helper=False

                settings()

                def closing():
                    global running, Exit
                    if mb.askokcancel("Выход из игры", "Хотите выйти из игры?"):
                        running=False
                        Exit = True
                        tk.destroy()

                tk.protocol("WM_DELETE_WINDOW", closing)
                tk.title("Морской бой")
                tk.resizable(0,0)
                tk.wm_attributes("-topmost", 1)
                pole = Canvas(tk, width=size_wn_x+menu_x + size_wn_x, height=size_wn_y+ menu_y, bd=0, highlightthickness=0)
                pole.create_rectangle(0,0,size_wn_x, size_wn_y, fill="white")
                pole.create_rectangle(size_wn_x+menu_x,0,size_wn_x+menu_x + size_wn_x, size_wn_y, fill="white")
                pole.pack()
                tk.update()

                Pink=Label(tk,text="",background="pink")
                Pink.place(x=size_wn_x+menu_x//5,y=step_y*14,width=15,height=15)
                one_palub=Label(tk,text="- Однопалубный корабль")
                one_palub.place(x=size_wn_x+menu_x//5+20,y=step_y*14)
                Blue=Label(tk,text="",background="blue")
                Blue.place(x=size_wn_x+menu_x//5,y=step_y*15,width=15,height=15)
                two_palub=Label(tk,text="- Двухпалубный корабль")
                two_palub.place(x=size_wn_x+menu_x//5+20,y=step_y*15)
                Green=Label(tk,text="",background="green")
                Green.place(x=size_wn_x+menu_x//5,y=step_y*16,width=15,height=15)
                three_palub=Label(tk,text="- Трёхпалубный корабль")
                three_palub.place(x=size_wn_x+menu_x//5+20,y=step_y*16)
                Yellow=Label(tk,text="",background="yellow")
                Yellow.place(x=size_wn_x+menu_x//5,y=step_y*17,width=15,height=15)
                four_palub=Label(tk,text="- Четырёхпалубный корабль")
                four_palub.place(x=size_wn_x+menu_x//5+20,y=step_y*17)

                def Pole(offset_x=0):
                    for i in range(s_x+1):
                        pole.create_line(offset_x + step_x * i,0,offset_x + step_x * i,size_wn_y)
                    for i in range(s_y+1):
                        pole.create_line(offset_x,step_y * i ,offset_x + size_wn_x, step_y * i)

                Pole()
                Pole(size_wn_x+menu_x)

                lbl1 = Label(tk, text= 'Игрок №1', font=('Helvetica', 16))
                lbl1.place(x = size_wn_x //2 - lbl1.winfo_reqwidth() //2 , y = size_wn_y+3)
                lbl2 = Label(tk, text= 'Игрок №2', font=('Helvetica', 16))
                lbl2.place(x = size_wn_x + menu_x + size_wn_x //2 - lbl2.winfo_reqwidth() //2 , y = size_wn_y+3)
                lbl3 = Label(tk, text= '', font=('Helvetica', 16))
                lbl3.place(x = size_wn_x + step_x+15, y = 18*step_y)

                def mark_igrok(igrok_mark):
                    if igrok_mark:
                        lbl1.configure(bg='red')
                        lbl2.configure(bg='#f0f0f0')
                        lbl3.configure(text='Ход Игрока №2')
                    else:
                        lbl2.configure(bg='red')
                        lbl1.configure(bg='#f0f0f0')
                        lbl3.configure(text='Ход Игрока №1')
                mark_igrok(hod_igroka)

                def GLmenu():
                    global running
                    running=False
                    tk.destroy()

                btn_GLmenu = Button(tk,text="Главное меню", command=GLmenu)
                btn_GLmenu.place(x=size_wn_x + menu_x//3, y = 30)

                def Play_return():
                    global list_ids, Clik_String1, Clik_String2, boom, enemy_ships1, enemy_ships2
                    for el in list_ids:
                        pole.delete(el)
                    list_ids =[]
                    Clik_String1 = [[-1 for i in range(s_y)] for i in range(s_x)]
                    Clik_String2 = [[-1 for i in range(s_y)] for i in range(s_x)]
                    boom = [[0 for i in range(s_y)] for i in range(s_x)]
                    enemy_ships1 = generate_enemy_ships()
                    enemy_ships2 = generate_enemy_ships()

                btn_return = Button(tk, text="Начать заново!", command=Play_return)
                btn_return.place(x=size_wn_x + menu_x//3, y=70)

                def show_enemy1():
                    for i in range (0, s_x):
                        for j in range(0, s_y):
                            if enemy_ships1[j][i] > 0:
                                color = "red"
                                if Clik_String1[j][i] != -1:
                                    color = "green"
                                _id = pole.create_rectangle(i*step_x,j*step_y,i*step_x+step_x,j*step_y+step_y,fill=color)
                                list_ids.append(_id)

                btn_ships_play1 = Button(tk, text="Показать корабли Игрока №1", command=show_enemy1)
                btn_ships_play1.place(x=size_wn_x + menu_x //4-15, y=110)

                def show_enemy2():
                    for i in range (0, s_x):
                        for j in range(0, s_y):
                            if enemy_ships2[j][i] > 0:
                                color = "red"
                                if Clik_String2[j][i] != -1:
                                    color = "green"
                                _id = pole.create_rectangle(size_wn_x+menu_x + i*step_x,j*step_y,size_wn_x+menu_x + i*step_x+step_x,j*step_y+step_y,fill=color)
                                list_ids.append(_id)

                btn_ships_play2 = Button(tk, text="Показать корабли Игрока №2", command=show_enemy2)
                btn_ships_play2.place(x=size_wn_x + menu_x //4-15, y=150)

                def draw_point(x,y):
                    global hod_igroka
                    print(enemy_ships1[y][x])
                    if Helper:
                        if enemy_ships1[y][x] == 0:
                            color = 'black'
                            id1 = pole.create_oval(x*step_x+step_x//3,y*step_y+step_y//3,x*step_x+step_x - step_y//3,y*step_y+step_y-step_y//3,fill=color)
                            list_ids.append(id1)
                            hod_igroka = False
                        if enemy_ships1[y][x] > 0 and enemy_ships1[y][x] <= 4:
                            color1 = 'pink'
                            id2 = pole.create_rectangle(x * step_x, y * step_y + step_y // 2 - step_y // 10, x * step_x + step_x,y * step_y + step_y // 2 + step_y // 10, fill=color1)
                            id3= pole.create_rectangle(x * step_x + step_x // 2 - step_x // 10, y * step_y, x * step_x + step_x // 2 + step_x // 10, y * step_y + step_y, fill=color1)
                            list_ids.append(id2)
                            list_ids.append(id3)
                        if enemy_ships1[y][x] > 4 and enemy_ships1[y][x] <= 7:
                            color2 = 'blue'
                            id4 = pole.create_rectangle(x * step_x, y * step_y + step_y // 2 - step_y // 10, x * step_x + step_x,y * step_y + step_y // 2 + step_y // 10, fill=color2)
                            id5= pole.create_rectangle(x * step_x + step_x // 2 - step_x // 10, y * step_y, x * step_x + step_x // 2 + step_x // 10, y * step_y + step_y, fill=color2)
                            list_ids.append(id4)
                            list_ids.append(id5)
                        if enemy_ships1[y][x] == 8 or enemy_ships1[y][x] == 9:
                            color3 = 'green'
                            id6 = pole.create_rectangle(x * step_x, y * step_y + step_y // 2 - step_y // 10, x * step_x + step_x,y * step_y + step_y // 2 + step_y // 10, fill=color3)
                            id7= pole.create_rectangle(x * step_x + step_x // 2 - step_x // 10, y * step_y, x * step_x + step_x // 2 + step_x // 10, y * step_y + step_y, fill=color3)
                            list_ids.append(id6)
                            list_ids.append(id7)
                        if enemy_ships1[y][x] == 10:
                            color4 = 'yellow'
                            id8 = pole.create_rectangle(x * step_x, y * step_y + step_y // 2 - step_y // 10, x * step_x + step_x,y * step_y + step_y // 2 + step_y // 10, fill=color4)
                            id9= pole.create_rectangle(x * step_x + step_x // 2 - step_x // 10, y * step_y, x * step_x + step_x // 2 + step_x // 10, y * step_y + step_y, fill=color4)
                            list_ids.append(id8)
                            list_ids.append(id9)
                    else:
                        if enemy_ships1[y][x] == 0:
                            color = 'black'
                            id1 = pole.create_oval(x*step_x+step_x//3,y*step_y+step_y//3,x*step_x+step_x - step_y//3,y*step_y+step_y-step_y//3,fill=color)
                            list_ids.append(id1)
                            hod_igroka = False
                        if enemy_ships1[y][x] > 0:
                            color1 = 'grey'
                            id2 = pole.create_rectangle(x * step_x, y * step_y + step_y // 2 - step_y // 10, x * step_x + step_x,y * step_y + step_y // 2 + step_y // 10, fill=color1)
                            id3= pole.create_rectangle(x * step_x + step_x // 2 - step_x // 10, y * step_y, x * step_x + step_x // 2 + step_x // 10, y * step_y + step_y, fill=color1)
                            list_ids.append(id2)
                            list_ids.append(id3)

                def draw_point2(x,y, offset_x=size_wn_x + menu_x): 
                    global hod_igroka
                    print(enemy_ships2[y][x])
                    if Helper:
                        if enemy_ships2[y][x] == 0:
                            color = 'black'
                            id10 = pole.create_oval(offset_x + x*step_x+step_x//3,y*step_y+step_y//3,offset_x + x*step_x+step_x - step_y//3,y*step_y+step_y-step_y//3,fill=color)
                            list_ids.append(id10)
                            hod_igroka =True
                        if enemy_ships2[y][x] > 0 and enemy_ships2[y][x] <= 4:
                            color1 = 'pink'
                            id11 = pole.create_rectangle(offset_x + x * step_x, y * step_y + step_y // 2 - step_y // 10, offset_x + x * step_x + step_x,y * step_y + step_y // 2 + step_y // 10, fill=color1)
                            id12= pole.create_rectangle(offset_x + x * step_x + step_x // 2 - step_x // 10, y * step_y,offset_x + x * step_x + step_x // 2 + step_x // 10, y * step_y + step_y, fill=color1)
                            list_ids.append(id11)
                            list_ids.append(id12)
                        if enemy_ships2[y][x] >= 5 and enemy_ships2[y][x] <= 7:
                            color2 = 'blue'
                            id13 = pole.create_rectangle(offset_x + x * step_x, y * step_y + step_y // 2 - step_y // 10,offset_x + x * step_x + step_x,y * step_y + step_y // 2 + step_y // 10, fill=color2)
                            id14 = pole.create_rectangle(offset_x + x * step_x + step_x // 2 - step_x // 10, y * step_y,offset_x + x * step_x + step_x // 2 + step_x // 10, y * step_y + step_y, fill=color2)
                            list_ids.append(id13)
                            list_ids.append(id14)
                        if enemy_ships2[y][x] == 8 or enemy_ships2[y][x] == 9:
                            color3 = 'green'
                            id15 = pole.create_rectangle(offset_x + x * step_x, y * step_y + step_y // 2 - step_y // 10,offset_x + x * step_x + step_x,y * step_y + step_y // 2 + step_y // 10, fill=color3)
                            id16 = pole.create_rectangle(offset_x + x * step_x + step_x // 2 - step_x // 10, y * step_y,offset_x + x * step_x + step_x // 2 + step_x // 10, y * step_y + step_y, fill=color3)
                            list_ids.append(id15)
                            list_ids.append(id16)
                        if enemy_ships2[y][x] == 10:
                            color4 = 'yellow'
                            id17 = pole.create_rectangle(offset_x + x * step_x, y * step_y + step_y // 2 - step_y // 10,offset_x + x * step_x + step_x,y * step_y + step_y // 2 + step_y // 10, fill=color4)
                            id18= pole.create_rectangle(offset_x + x * step_x + step_x // 2 - step_x // 10, y * step_y,offset_x + x * step_x + step_x // 2 + step_x // 10, y * step_y + step_y, fill=color4)
                            list_ids.append(id17)
                            list_ids.append(id18)
                    else:
                        if enemy_ships2[y][x] == 0:
                            color = 'black'
                            id10 = pole.create_oval(offset_x + x*step_x+step_x//3,y*step_y+step_y//3,offset_x + x*step_x+step_x - step_y//3,y*step_y+step_y-step_y//3,fill=color)
                            list_ids.append(id10)
                            hod_igroka = True
                        if enemy_ships2[y][x] > 0:
                            color1 = 'grey'
                            id11 = pole.create_rectangle(offset_x + x * step_x, y * step_y + step_y // 2 - step_y // 10, offset_x + x * step_x + step_x,y * step_y + step_y // 2 + step_y // 10, fill=color1)
                            id12= pole.create_rectangle(offset_x + x * step_x + step_x // 2 - step_x // 10, y * step_y,offset_x + x * step_x + step_x // 2 + step_x // 10, y * step_y + step_y, fill=color1)
                            list_ids.append(id11)
                            list_ids.append(id12)
                        
                def check_winer1():
                    win = True
                    for i in range(0,s_x):
                            for j in range(0, s_x):
                                if enemy_ships1[i][j] > 0:
                                    if Clik_String1[i][j] == -1:
                                        win = False
                    return win
                
                def check_winer2():
                    win = True
                    for i in range(0,s_x):
                            for j in range(0, s_x):
                                if enemy_ships2[i][j] > 0:
                                    if Clik_String2[i][j] == -1:
                                        win = False
                    return win

                def add_to_all(event):
                    global Clik_String1, Clik_String2, hod_igroka
                    _type=0
                    mouse_x=pole.winfo_pointerx() - pole.winfo_rootx()
                    mouse_y=pole.winfo_pointery() - pole.winfo_rooty()
                    ip_x=mouse_x//step_x
                    ip_y=mouse_y//step_y
                    if ip_x < s_x and ip_y < s_y and hod_igroka: #первое игровое поле
                        if Clik_String1[ip_y][ip_x] == -1:
                            Clik_String1[ip_y][ip_x] = _type
                            draw_point(ip_x,ip_y)
                            if check_winer1():
                                Clik_String1 = [[10 for i in range(s_y)] for i in range(s_x)]
                                Clik_String2 = [[10 for i in range(s_y)] for i in range(s_x)]
                                winner = "Победа Игрока №2 (Все корабли Игрока №1 подбиты)!!!"
                                mb.showinfo(title='Победа', message=winner)

                    if ip_x >= s_x + 8 and ip_x <= s_x + s_x + 8 and ip_y < s_y and not hod_igroka: # второе игровое поле
                        if Clik_String2[ip_y][ip_x - s_x - 8] == -1:
                            Clik_String2[ip_y][ip_x - s_x - 8] = _type
                            draw_point2(ip_x - s_x - 8,ip_y)
                            if check_winer2():
                                Clik_String1 = [[10 for i in range(s_y)] for i in range(s_x)]
                                Clik_String2 = [[10 for i in range(s_y)] for i in range(s_x)]
                                winner = "Победа Игрока №1 (Все корабли Игрока №2 подбиты)!!!"
                                mb.showinfo(title='Победа', message=winner)
                    mark_igrok(hod_igroka)    

                pole.bind_all("<Button-1>", add_to_all)

                def generate_enemy_ships():
                    near_ships = []
                    ships_list = []
                    #добавление кораблей в строку
                    for i in range(enemy_ships_1):
                        ships_list.append(ship_1) 
                    for i in range(enemy_ships_2):
                        ships_list.append(ship_2) 
                    for i in range(enemy_ships_3):
                        ships_list.append(ship_3) 
                    for i in range(enemy_ships_4):
                        ships_list.append(ship_4) 
                    sum_enemy_ships = sum(ships_list)
                    sum_enemy=0
                    while sum_enemy != sum_enemy_ships:
                        near_ships=[[0 for i in range(s_y+1)] for i in range(s_x+1)] 

                        for i in range(ship): 
                            len = ships_list[i]
                            horizont_vertikal = random.randrange(1,3)

                            primerno_x = random.randrange(0, s_x)
                            if primerno_x + len > s_x:
                                primerno_x = primerno_x - len
                            
                            primerno_y = random.randrange(0, s_y)
                            if primerno_y + len > s_y:
                                primerno_y - primerno_y - len

                            if horizont_vertikal == 1:
                                if primerno_x + len <= s_x:
                                    for j in range(0, len):
                                        try:
                                            #Проверка есть ли корабль рядом
                                            check_ships = near_ships[primerno_y][primerno_x - 1] + \
                                                                near_ships[primerno_y][primerno_x + j] + \
                                                                near_ships[primerno_y][primerno_x + j + 1] + \
                                                                near_ships[primerno_y + 1][primerno_x + j + 1] + \
                                                                near_ships[primerno_y - 1][primerno_x + j + 1] + \
                                                                near_ships[primerno_y + 1][primerno_x + j] + \
                                                                near_ships[primerno_y - 1][primerno_x + j] + \
                                                                near_ships[primerno_y + 1][primerno_x + 1] + \
                                                                near_ships[primerno_y - 1][primerno_x - 1] + \
                                                                near_ships[primerno_y - 1][primerno_x + 1] + \
                                                                near_ships[primerno_y + 1][primerno_x - 1]
                                            if check_ships == 0:
                                                near_ships[primerno_y][primerno_x + j] = i + 1
                                        except Exception:
                                            pass
                            if horizont_vertikal == 2:
                                if primerno_y + len <= s_y:
                                    for j in range(0, len):
                                        try:
                                            #Проверка есть ли корабль рядом
                                            check_ships = near_ships[primerno_x - 1][primerno_y] + \
                                                                near_ships[primerno_x + j][primerno_y] + \
                                                                near_ships[primerno_x + j + 1][primerno_y] + \
                                                                near_ships[primerno_x + j + 1][primerno_y + 1] + \
                                                                near_ships[primerno_x + j + 1][primerno_y - 1] + \
                                                                near_ships[primerno_x + j][primerno_y + 1] + \
                                                                near_ships[primerno_x + j][primerno_y - 1] + \
                                                                near_ships[primerno_x + 1][primerno_y + 1] + \
                                                                near_ships[primerno_x - 1][primerno_y - 1] + \
                                                                near_ships[primerno_x + 1][primerno_y - 1] + \
                                                                near_ships[primerno_x - 1][primerno_y + 1]
                                            if check_ships == 0:
                                                near_ships[primerno_x+j][primerno_y] = i + 1
                                        except Exception:
                                            pass
                        sum_enemy = 0
                        for i in range(0,s_x):
                            for j in range(0, s_x):
                                if near_ships[i][j] > 0:
                                    sum_enemy = sum_enemy + 1
                    return near_ships

                enemy_ships1 = generate_enemy_ships()
                enemy_ships2 = generate_enemy_ships()

                while running:
                    if running:
                        tk.update_idletasks()
                        tk.update()
                    time.sleep(0.005)
            poles(18)
            if Exit:
                exit()
            GLMenu.show()

        ui.btn_Easy.clicked.connect(openPlayEasy)
        ui.btn_Medium.clicked.connect(openPlayMedium)
        ui.btn_Hard.clicked.connect(openPlayHard)
        ui.btn_GLmenu.clicked.connect(returnGLmenu)

    def openRulePlay():
        global Rule_Play
        Rule_Play = QMainWindow()
        Rule_Play.setFixedSize(711, 592)
        ui = Ui_Rule_Play()
        ui.setupUi(Rule_Play)
        GLMenu.close()
        Rule_Play.show()
        
        def returnGLmenu():
            Rule_Play.close()
            GLMenu.show()

        ui.btn_GLmenu.clicked.connect(returnGLmenu)

    def openElementUprav():
        global Element_Uprav
        Element_Uprav = QMainWindow()
        Element_Uprav.setFixedSize(711, 592)
        ui = Ui_Element_Uprav()
        ui.setupUi(Element_Uprav)
        GLMenu.close()
        Element_Uprav.show()
        
        def returnGLmenu():
            Element_Uprav.close()
            GLMenu.show()

        ui.btn_GLmenu.clicked.connect(returnGLmenu)

    ui.btn_Exit.clicked.connect(GLMenu.close)
    ui.btn_Igra.clicked.connect(openIgra)
    ui.btn_Rule_Play.clicked.connect(openRulePlay)
    ui.btn_Element_Uprav.clicked.connect(openElementUprav)

    sys.exit(app.exec_())