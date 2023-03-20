from tkinter import *
from tkinter import messagebox as mb
import time
import random

tk=Tk()
app_running = True

def poles():
    global hod_igroka, size_wn_x, size_wn_y, s_x, s_y, step_x, step_y, ship, ship_1, ship_2, ship_3, ship_4, enemy_ships_1, enemy_ships_2, enemy_ships_3, enemy_ships_4, enemy_ships1, enemy_ships2, menu_x, menu_y, list_ids, points1, points2, boom

    size_wn_x= 600
    size_wn_y= 600
    s_x=s_y=12 #размер поля
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
    menu_x= step_x*5
    menu_y = 40
    list_ids=[] #список объектов
    points1 = [[-1 for i in range(s_y)] for i in range(s_x)] #список куда мы кликнули первое поле
    points2 = [[-1 for i in range(s_y)] for i in range(s_x)] #список куда мы кликнули второе поле
    boom = [[0 for i in range(s_y)] for i in range(s_x)] #список попаданей по короблям

    photo = PhotoImage(file='D:\Projeck\Proect\Sea_warr.png')
    tk.iconphoto(False, photo)

    #Истина - 2 игрок, ложно - 1 игрок
    hod_igroka=False

    
    def settings():
        global var
        var = IntVar(tk)
        cb = Checkbutton(text="Включить обозначения размера корабля?",
                                 variable=var,
                                 command=print_value)
        cb.pack(side='bottom')

    def print_value():
        global Helper
        print(var.get())
        if var.get() == 1:
            Helper=True
        else:
            Helper=False

    settings()

    def closing():
        global app_running
        if mb.askokcancel("Выход из игры", "Хотите выйти из игры?"):
            app_running=False
            tk.destroy()

    tk.protocol("WM_DELETE_WINDOW", closing)
    tk.title("Морской бой")
    tk.resizable(0,0)
    tk.wm_attributes("-topmost", 1)
    tk.geometry("1450x640+200+200")
    pole = Canvas(tk, width=size_wn_x+menu_x + size_wn_x, height=size_wn_y+ menu_y, bd=0, highlightthickness=0)
    pole.create_rectangle(0,0,size_wn_x, size_wn_y, fill="white")
    pole.create_rectangle(size_wn_x+menu_x,0,size_wn_x+menu_x + size_wn_x, size_wn_y, fill="white")
    pole.pack()
    tk.update()

    mb.showinfo(title="Производится расстановка", message="Подождите пожалуйста, производится расстановка кораблей")

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
    lbl3.place(x = size_wn_x + step_x+10, y = 10*step_y)

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
        global app_running
        app_running=False
        tk.destroy()

    btn = Button(tk,text="Главное меню", command=GLmenu)
    btn.place(x=size_wn_x + menu_x//3, y = 30)

    def Play_return():
        global list_ids, points1, points2, boom, enemy_ships1, enemy_ships2
        for el in list_ids:
            pole.delete(el)
        list_ids =[]
        points1 = [[-1 for i in range(s_y)] for i in range(s_x)]
        points2 = [[-1 for i in range(s_y)] for i in range(s_x)]
        boom = [[0 for i in range(s_y)] for i in range(s_x)]
        enemy_ships1 = generate_enemy_ships()
        enemy_ships2 = generate_enemy_ships()

    btn1 = Button(tk, text="Начать заново!", command=Play_return)
    btn1.place(x=size_wn_x + menu_x//3, y=70)

    def show_enemy1():
        for i in range (0, s_x):
            for j in range(0, s_y):
                if enemy_ships1[j][i] > 0:
                    color = "red"
                    if points1[j][i] != -1:
                        color = "green"
                    _id = pole.create_rectangle(i*step_x,j*step_y,i*step_x+step_x,j*step_y+step_y,fill=color)
                    list_ids.append(_id)

    btn2 = Button(tk, text="Показать корабли Игрока №1", command=show_enemy1)
    btn2.place(x=size_wn_x + menu_x //4-15, y=110)

    def show_enemy2():
        for i in range (0, s_x):
            for j in range(0, s_y):
                if enemy_ships2[j][i] > 0:
                    color = "red"
                    if points2[j][i] != -1:
                        color = "green"
                    _id = pole.create_rectangle(size_wn_x+menu_x + i*step_x,j*step_y,size_wn_x+menu_x + i*step_x+step_x,j*step_y+step_y,fill=color)
                    list_ids.append(_id)

    btn3 = Button(tk, text="Показать корабли Игрока №2", command=show_enemy2)
    btn3.place(x=size_wn_x + menu_x //4-15, y=150)

    def draw_point(x,y):
        global hod_igroka
        if Helper:
            print(enemy_ships1[y][x])
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
            if enemy_ships1[y][x] > 4 and enemy_ships2[y][x] <= 7:
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
        if Helper:
            print(enemy_ships2[y][x])
            if enemy_ships2[y][x] == 0:
                color = 'black'
                id10 = pole.create_oval(offset_x + x*step_x+step_x//3,y*step_y+step_y//3,offset_x + x*step_x+step_x - step_y//3,y*step_y+step_y-step_y//3,fill=color)
                list_ids.append(id10)
                hod_igroka = True
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
                        if points1[i][j] == -1:
                            win = False
        return win
    
    def check_winer2():
        win = True
        for i in range(0,s_x):
                for j in range(0, s_x):
                    if enemy_ships2[i][j] > 0:
                        if points2[i][j] == -1:
                            win = False
        return win

    def add_to_all(event):
        global points1, points2, hod_igroka
        _type=0
        mouse_x=pole.winfo_pointerx() - pole.winfo_rootx()
        mouse_y=pole.winfo_pointery() - pole.winfo_rooty()
        ip_x=mouse_x//step_x
        ip_y=mouse_y//step_y
        if ip_x < s_x and ip_y < s_y and hod_igroka: #первое игровое поле
            if points1[ip_y][ip_x] == -1:
                points1[ip_y][ip_x] = _type
                draw_point(ip_x,ip_y)
                if check_winer1():
                    winner = "Победа Игрока №2"
                    winner_add = "(Все корабли противника Игрока №1 подбиты)!!!"
                    points1 = [[10 for i in range(s_y)] for i in range(s_x)]
                    points2 = [[10 for i in range(s_y)] for i in range(s_x)]
                    id19 = pole.create_rectangle(step_x*3,step_y*3,size_wn_x + menu_x + size_wn_x-step_x*3, size_wn_y-step_y, fill="blue")
                    list_ids.append(id19)
                    id20 = pole.create_rectangle(step_x*3+step_x//2,step_y*3+step_x//2,size_wn_x + menu_x + size_wn_x-step_x*3-step_x//2, size_wn_y-step_y-step_x//2, fill="yellow")
                    list_ids.append(id20)
                    id21=pole.create_text(step_x*12,step_y*5, text=winner, font=('Arial',50), justify=CENTER)
                    id22=pole.create_text(step_x*12,step_y*6, text=winner_add, font=('Arial',20), justify=CENTER)
                    list_ids.append(id21)
                    list_ids.append(id22)

        if ip_x >= s_x + 5 and ip_x <= s_x + s_x + 5 and ip_y < s_y and not hod_igroka: # второе игровое поле
            if points2[ip_y][ip_x - s_x - 5] == -1:
                points2[ip_y][ip_x - s_x - 5] = _type
                draw_point2(ip_x - s_x - 5,ip_y)
                if check_winer2():
                    winner = "Победа Игрока №1"
                    winner_add = "(Все корабли противника Игрока №2 подбиты)!!!"
                    points1 = [[10 for i in range(s_y)] for i in range(s_x)]
                    points2 = [[10 for i in range(s_y)] for i in range(s_x)]
                    id23 = pole.create_rectangle(step_x*3,step_y*3,size_wn_x + menu_x + size_wn_x-step_x*3, size_wn_y-step_y, fill="blue")
                    list_ids.append(id23)
                    id24 = pole.create_rectangle(step_x*3+step_x//2,step_y*3+step_x//2,size_wn_x + menu_x + size_wn_x-step_x*3-step_x//2, size_wn_y-step_y-step_x//2, fill="yellow")
                    list_ids.append(id24)
                    id25=pole.create_text(step_x*12,step_y*5, text=winner, font=('Arial',50), justify=CENTER)
                    id26=pole.create_text(step_x*12,step_y*6, text=winner_add, font=('Arial',20), justify=CENTER)
                    list_ids.append(id25)
                    list_ids.append(id26)
        mark_igrok(hod_igroka)    

    pole.bind_all("<Button-1>", add_to_all)

    def generate_enemy_ships():
        enemy_ships = []
        ships_list = []
        for i in range(enemy_ships_1):
            ships_list.append(ship_1) 
        for i in range(enemy_ships_2):
            ships_list.append(ship_2) 
        for i in range(enemy_ships_3):
            ships_list.append(ship_3) 
        for i in range(enemy_ships_4):
            ships_list.append(ship_4)
        print(ships_list) 
        sum_enemy_ships = sum(ships_list)
        sum_enemy=0
        while sum_enemy != sum_enemy_ships:
            enemy_ships=[[0 for i in range(s_y+1)] for i in range(s_x+1)] 

            for i in range(ship): 
                len = ships_list[i]
                horizont_vertikal = random.randint(1,3)

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
                                check_near_ships = enemy_ships[primerno_y][primerno_x - 1] + \
                                                    enemy_ships[primerno_y][primerno_x + j] + \
                                                    enemy_ships[primerno_y][primerno_x + j + 1] + \
                                                    enemy_ships[primerno_y + 1][primerno_x + j + 1] + \
                                                    enemy_ships[primerno_y - 1][primerno_x + j + 1] + \
                                                    enemy_ships[primerno_y + 1][primerno_x + j] + \
                                                    enemy_ships[primerno_y - 1][primerno_x + j] + \
                                                    enemy_ships[primerno_y + 1][primerno_x + 1] + \
                                                    enemy_ships[primerno_y - 1][primerno_x - 1] + \
                                                    enemy_ships[primerno_y - 1][primerno_x + 1] + \
                                                    enemy_ships[primerno_y + 1][primerno_x - 1]
                                if check_near_ships == 0:
                                    enemy_ships[primerno_y][primerno_x + j] = i + 1
                            except Exception:
                                pass
                            
                elif horizont_vertikal == 2:
                    if primerno_y + len <= s_y:
                        for j in range(0, len):
                            try:
                                check_near_ships = enemy_ships[primerno_x - 1][primerno_y] + \
                                                    enemy_ships[primerno_x + j][primerno_y] + \
                                                    enemy_ships[primerno_x + j + 1][primerno_y] + \
                                                    enemy_ships[primerno_x + j + 1][primerno_y + 1] + \
                                                    enemy_ships[primerno_x + j + 1][primerno_y - 1] + \
                                                    enemy_ships[primerno_x + j][primerno_y + 1] + \
                                                    enemy_ships[primerno_x + j][primerno_y - 1] + \
                                                    enemy_ships[primerno_x + 1][primerno_y + 1] + \
                                                    enemy_ships[primerno_x - 1][primerno_y - 1] + \
                                                    enemy_ships[primerno_x + 1][primerno_y - 1] + \
                                                    enemy_ships[primerno_x - 1][primerno_y + 1]
                                if check_near_ships == 0:
                                    enemy_ships[primerno_x+j][primerno_y] = i + 1
                            except Exception:
                                pass
            sum_enemy = 0
            for i in range(0,s_x):
                for j in range(0, s_x):
                    if enemy_ships[i][j] > 0:
                        sum_enemy = sum_enemy + 1
        return enemy_ships

    enemy_ships1 = generate_enemy_ships()
    enemy_ships2 = generate_enemy_ships()
    
    mb.showinfo(title="Расстановка кораблей прошла успешно",message="Корабли расставлены \n Приятной игры")
    
    while app_running:
        if app_running:
            tk.update_idletasks()
            tk.update()
        time.sleep(0.005)
poles()