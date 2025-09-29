import numpy as np
import matplotlib.pyplot as plt
from tkinter import *

ad = False
global width
width = 600
global height
height = 400

global width2
width2 = 1500
global height2
height2 = 800

screenResolution = str(width)+'x'+str(height)
screenResolution2 = str(width2)+'x'+str(height2)
print(screenResolution)
print(screenResolution2)



def progression(x1,x2):

    n = 5
    y = [180,181.8,183.618,185.454,187.309]
    x1_2 = 0
    x2_2 = 0
    x1_x2 = 0
    x1_y = 0
    x2_y = 0
    for i in range(0,5):
        x1_2 += x1[i]*x1[i]
        x2_2 += x2[i]*x2[i]
        x1_x2 += x1[i]*x2[i]
        x1_y += x1[i]*y[i]
        x2_y += x2[i]*y[i]
    A = [[n             ,sum(x1)       ,sum(x2)]
        ,[sum(x1)      ,x1_2           ,x1_x2]
        ,[sum(x2)      ,x1_x2          ,x2_2]]

    D = np.linalg.det(A)
    D_0 = np.linalg.det([[sum(y)        ,sum(x1)       ,sum(x2)]
                        ,[x1_y          ,x1_2          ,x1_x2]
                        ,[x2_y          ,x1_x2         ,x2_2]])/D
    D_1 = np.linalg.det([[n             ,sum(y)       ,sum(x2)],
                         [sum(x1),       x1_y,         x1_x2]
                        ,[sum(x2),       x2_y,         x2_2]])/D
    D_2 = np.linalg.det([[n             ,sum(x1)       ,sum(y)],
                         [sum(x1),          x1_2,           x1_y]
                        ,[sum(x2),          x1_x2,          x2_y]])/D
    print("y = (",D_2,")x2 + (",D_1,")x1 + (",D_0,")\n")

    r_x1_y= np.corrcoef(x1,y,)
    r_x1_y = r_x1_y[0][1]
    r_x2_y = np.corrcoef(x2, y,)
    r_x2_y = r_x2_y[0][1]
    r_x1_x2 = np.corrcoef(x1, x2,)
    r_x1_x2 = r_x1_x2[0][1]

    R_x1_x2_y = np.sqrt( ( (r_x1_y * r_x1_y) + (r_x2_y * r_x2_y) - 2 * r_x1_y * r_x2_y * r_x1_x2 ) / (1 - (r_x1_x2 * r_x1_x2)) )
    print("Множественная R:", R_x1_x2_y)
    R2 = R_x1_x2_y * R_x1_x2_y
    print("Квадрат R:", R2)
    R2_correct = 1 - (1 - R2) * ((n - 1) / (n - 3))
    print("Скорректированная R:", R2_correct)

    print("Таким образом,", R2 * 100,"% вариации признака-результата обусловлены признаками-факторами\n")

    x1_sr = sum(x1)/n
    x2_sr = sum(x2)/n
    y_sr = sum(y)/n

    S_x1 = np.std(x1)
    S_x2 = np.std(x2)
    S_y = np.std(y)

    t1 = ((S_y * np.sqrt(1 - R2)) / (S_x1 * np.sqrt(1 - (r_x1_x2 * r_x1_x2)))) * (1 / np.sqrt(n - 3))
    t2 = ((S_y * np.sqrt(1 - R2)) / (S_x2 * np.sqrt(1 - (r_x1_x2 * r_x1_x2)))) * (1 / np.sqrt(n - 3))

    t = ((D_1 / t1) + (D_2 / t2)) / 2

    print("Стандартаная ошибка:", t)

    F = R2 / (1 - R2) * (n - 3) / 2

    print("Наблюдаемость:", F)


    str1 = "y = ("+str(round(D_2,3))+")x2 + ("+str(round(D_1,3))+")x1 + ("+str(round(D_0,3))+")\n"
    str2 = "Множественная R:" + str(round(R_x1_x2_y,3))
    str3 = "Квадрат R:" + str(round(R2,3))
    str4 = "Скорректированная R:" + str(round(R2_correct,3))
    str5 = "Таким образом," + str(round(R2 * 100,3)) + "% вариации признака-результата обусловлены признаками-факторами\n"
    str6 = "Стандартаная ошибка:" + str(round(t,3))
    str7 = "Наблюдаемость:" + str(round(F,3))

    titleFont = 18
    font = 14
    window = Tk()
    window.columnconfigure(0, weight=1, minsize=75)
    window.rowconfigure([0, 1], weight=1, minsize=50)
    window.geometry(screenResolution)
    window.minsize(width+400, height)
    window.maxsize(width + 800, height)
    window.title("Регрессия")
    frame = Frame(master=window, borderwidth=10, relief=border_effects["ridge"])
    frame.grid()
    lbl1_0 = Label(master=frame, text="Результат:", font=("Arial Bold", titleFont), background='blue',
                foreground='white', padx=5, pady=5)
    lbl1_1 = Label(master=frame, text=str1, font=("Arial Bold", font), background='blue',
                foreground='white', padx=5, pady=5)
    lbl1_2 = Label(master=frame, text=str2, font=("Arial Bold", font), background='blue',
                foreground='white', padx=5, pady=5)
    lbl1_3 = Label(master=frame, text=str3, font=("Arial Bold", font), background='blue',
                foreground='white', padx=5, pady=5)
    lbl1_4 = Label(master=frame, text=str4, font=("Arial Bold", font), background='blue',
                foreground='white', padx=5, pady=5)
    lbl1_5= Label(master=frame, text=str5, font=("Arial Bold", font), background='blue',
                foreground='white', padx=5, pady=5)
    lbl1_6 = Label(master=frame, text=str6, font=("Arial Bold", font), background='blue',
                foreground='white', padx=5, pady=5)
    lbl1_7 = Label(master=frame, text=str7, font=("Arial Bold", font), background='blue',
                foreground='white', padx=5, pady=5)

    lbl1_0.grid(column=0, row=0)
    lbl1_1.grid(column=0 , row=1)
    lbl1_2.grid(column=0, row=2)
    lbl1_3.grid(column=0, row=3)
    lbl1_4.grid(column=0, row=4)
    lbl1_5.grid(column=0, row=5)
    lbl1_6.grid(column=0, row=6)
    lbl1_7.grid(column=0, row=7)

def grafika(expr, way):

    dateUsl = [-2, -1, 0, 1, 2]
    export = expr
    for i in range(0,5):
        export[i] = export[i]*way

    expA1 = 0
    for i in range(0,5):
        expA1 = expA1 + export[i]
    expA1 = float(expA1/5)

    dateValSum = 0
    expA21 = []
    for i in range(0, 5):
        expA21.append(export[i] * dateUsl[i])
    expA2 = 0
    for i in range(0,5):
        dateValSum = dateValSum + dateUsl[i] * dateUsl[i]
        expA2 = expA2 + expA21[i]
    expA2 = float(expA2/dateValSum)

    progExport = []
    trendExport = []

    dateUslFuture = [2, 3, 4, 5, 6]

    for i in range(0, 5):
        progExport.append(expA1 + expA2 * dateUslFuture[i])
        trendExport.append(expA1 + expA2 * dateUsl[i])
    for i in range(5, 15):
        dateUslFuture.append(i+2)
        progExport.append(expA1 + expA2 * dateUslFuture[i])

    fig, ax = plt.subplots()
    line, = ax.plot([], label="реальные данные", color='yellow', marker='o', markerfacecolor="w", markersize=7, linewidth=2)
    prognoz, = ax.plot([], label="прогноз", color='blue', marker='o', markerfacecolor="w", markersize=7, linewidth=1)
    trend, = ax.plot([], label="тренд", color='red', marker='o', markerfacecolor="w", markersize=7, linewidth=1)
    plt.xlabel('скоротечное время')
    plt.ylabel('количественные единицы')
    plt.legend()
    plt.grid()

    ax.set_xlim(2015, 2037)
    ax.set_ylim(0, expA21[4]*2)

    curTime = []
    curTime2 = []
    curTrend = []
    curProg = []
    curExp = []
    firstTC = -1
    secTC = -1

    for i in range(2019,2036):
        if i >= 2023:
            secTC += 1
            curTime2.append(i)
            curProg.append(progExport[secTC])
            prognoz.set_data(curTime2, curProg)
            plt.pause(0.1)
            if i == 2023:
                firstTC += 1
                curTime.append(i)
                curExp.append(export[firstTC])
                curTrend.append(trendExport[firstTC])
                trend.set_data(curTime, curTrend)
                line.set_data(curTime, curExp)
                plt.fill_between(curTime, curExp, color='cyan')
                print(export[firstTC])
                plt.pause(0.1)
            if i >= 2024:
                curTime.append(i)
                curExp.append(progExport[secTC])
                line.set_data(curTime, curExp)
                print(export[firstTC])
                plt.fill_between(curTime, curExp, color='cyan')
                plt.pause(0.1)
        else:
            firstTC += 1
            curTime.append(i)
            curExp.append(export[firstTC])
            curTrend.append(trendExport[firstTC])
            trend.set_data(curTime, curTrend)
            line.set_data(curTime, curExp)
            plt.fill_between(curTime, curExp, color='cyan')
            print(export[firstTC])
            plt.pause(0.1)
        print("мы вышли")
    plt.show()
    print("END")

border_effects = {
    "flat": FLAT,
    "sunken": SUNKEN,
    "raised": RAISED,
    "groove": GROOVE,
    "ridge": RIDGE,
}


def clicked(who):
    dataOfTrend = \
        {
            "input1": [],
            "input2": [],
            "input3": []
        }
    dataOfTrend["input1"].append(int(txt1_1.get()))
    dataOfTrend["input1"].append(int(txt1_2.get()))
    dataOfTrend["input1"].append(int(txt1_3.get()))
    dataOfTrend["input1"].append(int(txt1_4.get()))
    dataOfTrend["input1"].append(int(txt1_5.get()))

    dataOfTrend["input2"].append(int(txt2_1.get()))
    dataOfTrend["input2"].append(int(txt2_2.get()))
    dataOfTrend["input2"].append(int(txt2_3.get()))
    dataOfTrend["input2"].append(int(txt2_4.get()))
    dataOfTrend["input2"].append(int(txt2_5.get()))

    dataOfTrend["input3"].append(int(txt3_1.get()))
    dataOfTrend["input3"].append(int(txt3_2.get()))
    dataOfTrend["input3"].append(int(txt3_3.get()))
    dataOfTrend["input3"].append(int(txt3_4.get()))
    dataOfTrend["input3"].append(int(txt3_5.get()))

    print(dataOfTrend)
    if(who == 1):
        modeGraph = 0
        tempVar = int(var2.get())
        if tempVar == 0:
            modeGraph = 0.90
        elif tempVar == 1:
            modeGraph = 1
        elif tempVar == 2:
            modeGraph = 1.15

        modeGraph2 = 0
        tempVar2 = int(var.get())
        if tempVar2 == 0:
            grafika(dataOfTrend["input1"], modeGraph)
        elif tempVar2 == 1:
            grafika(dataOfTrend["input2"], modeGraph)
        elif tempVar2 == 2:
            grafika(dataOfTrend["input3"], modeGraph)

        print("modeGraph2: ")
        print(modeGraph2)

        print("modeGraph: ")
        print(modeGraph)
    else:
        progression(dataOfTrend["input1"],dataOfTrend["input3"])

border_effects = {
    "flat": FLAT,
    "sunken": SUNKEN,
    "raised": RAISED,
    "groove": GROOVE,
    "ridge": RIDGE,
}

window = Tk()
window.columnconfigure(0, weight=1, minsize=75)
window.rowconfigure([0, 1], weight=1, minsize=50)
window.geometry(screenResolution)
window.minsize(width, height)
window.maxsize(width + 200, height + 200)
window.title("Прогноз")


def mul():
    global ad
    ad = True
    print("Значение в функции:", ad)
    window.destroy()


varMain = IntVar()
varMain.set(0)
while (ad == False):
    frameTitle = Frame(master=window, borderwidth=10, relief=border_effects["ridge"])
    frame = Frame(master=window, borderwidth=10, relief=border_effects["ridge"])
    frameButton = Frame(master=window, borderwidth=10, relief=border_effects["ridge"])
    lbl = Label(master=frameTitle, text="Выберите что будем считать", font=("Arial Bold", 24), background='blue',
                foreground='white')
    frameTitle.grid(column=0, row=0, padx=(20, 20), pady=(20, 20))
    frame.grid(column=0, row=1, padx=(20, 20), pady=(20, 20))
    frameButton.grid(column=0, row=2, padx=(20, 20), pady=(20, 20))
    lbl.grid(column=0, row=0, sticky='w', padx=(20, 20), pady=(20, 20))
    firstInputMainScreen = Radiobutton(master=frame, text="Тренд", variable=varMain, value=0)
    secondInputMainScreen = Radiobutton(master=frame, text="Регрессия", variable=varMain, value=1)

    firstInputMainScreen.grid(column=0, row=1, padx=5, pady=5)
    secondInputMainScreen.grid(column=2, row=1, padx=5, pady=5)

    btn = Button(master=frameButton, text="CLICK!", command=(lambda: mul()), font=("Arial Bold", 20))
    btn.grid(column=0, row=0, sticky='e')
    print("Значение вне функции:", ad)
    window.mainloop()
print("Значение вне функции и цикла:", ad)

print("varMain:::")
print(varMain.get())

if (int(varMain.get()) == 0):
    print("FIRST")
    window = Tk()
    window.columnconfigure(0, weight=1, minsize=75)
    window.rowconfigure([0, 1], weight=1, minsize=50)
    window.geometry(screenResolution2)
    window.minsize(width2, height2)
    window.maxsize(width2 + 200, height2 + 200)
    window.title("Прогноз")
    frame = Frame(master=window, borderwidth=10, relief=border_effects["ridge"])
    frameTitle = Frame(master=frame, borderwidth=10, relief=border_effects["ridge"])
    frameForm = Frame(master=frame, borderwidth=10, relief=border_effects["ridge"])
    frameFormYears0 = Frame(master=frameForm, borderwidth=10, relief=border_effects["ridge"])
    frameFormYears1 = Frame(master=frameForm, borderwidth=10, relief=border_effects["ridge"])
    frameFormYears2 = Frame(master=frameForm, borderwidth=10, relief=border_effects["ridge"])
    frameFormYears3 = Frame(master=frameForm, borderwidth=10, relief=border_effects["ridge"])
    frameFormYears4 = Frame(master=frameForm, borderwidth=10, relief=border_effects["ridge"])
    frameFormYears5 = Frame(master=frameForm, borderwidth=10, relief=border_effects["ridge"])
    frame.grid()
    frameTitle.grid(column=0, row=0)
    frameForm.grid(column=0, row=1)
    frameFormYears0.grid(column=0, row=1, padx=(10, 10), pady=(10, 10))
    frameFormYears1.grid(column=1, row=1, padx=(10, 10), pady=(10, 10))
    frameFormYears2.grid(column=2, row=1, padx=(10, 10), pady=(10, 10))
    frameFormYears3.grid(column=3, row=1, padx=(10, 10), pady=(10, 10))
    frameFormYears4.grid(column=4, row=1, padx=(10, 10), pady=(10, 10))
    frameFormYears5.grid(column=5, row=1, padx=(10, 10), pady=(10, 10))

    lbl = Label(master=frameTitle, text="Тренды", font=("Arial Bold", 24), background='blue',
                foreground='white')
    lbl1_1 = Label(master=frameForm, text="Input data", font=("Arial Bold", 20), background='blue', foreground='white',
                   justify="right", padx=10, pady=10)
    lbl1_2 = Label(master=frameForm, text="Input data 2", font=("Arial Bold", 24), background='blue',
                   foreground='white')
    lbl1_3 = Label(master=frameForm, text="Input data 3", font=("Arial Bold", 24), background='blue',
                   foreground='white')
    lbl1_4 = Label(master=frameForm, text="Input data 3", font=("Arial Bold", 24), background='blue',
                   foreground='white')
    lbl1_5 = Label(master=frameForm, text="Input data 3", font=("Arial Bold", 24), background='blue',
                   foreground='white')

    lbl2_1 = Label(master=frameForm, text="Какая cтрана?", font=("Arial Bold", 18), background='blue',
                   foreground='white', padx=5, pady=5)

    lbl5 = Label(master=frameFormYears0, text="Количественный показатель", font=("Arial Bold", 20), background='blue',
                 foreground='white', padx=20, pady=10)
    lbl6 = Label(master=frameFormYears1, text="2019", font=("Arial Bold", 20), background='blue', foreground='white',
                 padx=20, pady=10)
    lbl7 = Label(master=frameFormYears2, text="2020", font=("Arial Bold", 20), background='blue', foreground='white',
                 padx=20, pady=10)
    lbl8 = Label(master=frameFormYears3, text="2021", font=("Arial Bold", 20), background='blue', foreground='white',
                 padx=20, pady=10)
    lbl9 = Label(master=frameFormYears4, text="2022", font=("Arial Bold", 20), background='blue', foreground='white',
                 padx=20, pady=10)
    lbl10 = Label(master=frameFormYears5, text="2023", font=("Arial Bold", 20), background='blue', foreground='white',
                  padx=20, pady=10)

    lbl.grid(column=0, row=0, sticky='w', padx=(20, 20), pady=(20, 20))
    lbl5.grid(column=0, row=1, sticky='w')
    lbl6.grid(column=1, row=1, sticky='w')
    lbl7.grid(column=2, row=1, sticky='w')
    lbl8.grid(column=3, row=1, sticky='w')
    lbl9.grid(column=4, row=1, sticky='w')
    lbl10.grid(column=5, row=1, sticky='w')

    lbl2_1.grid(column=2, row=8, sticky='w', padx=(20, 20), pady=(20, 20))

    txt0_1 = Entry(master=frameForm, font=("Arial Bold", 20), width=10)
    txt0_1.grid(column=2, row=9, sticky='w', padx=10, pady=10)

    txt1_1 = Entry(master=frameForm, font=("Arial Bold", 24), width=10)
    txt1_1.grid(column=1, row=2, sticky='w', padx=5, pady=5)
    txt1_2 = Entry(master=frameForm, font=("Arial Bold", 24), width=10)
    txt1_2.grid(column=2, row=2, sticky='w', padx=5, pady=5)
    txt1_3 = Entry(master=frameForm, font=("Arial Bold", 24), width=10)
    txt1_3.grid(column=3, row=2, sticky='w', padx=5, pady=5)
    txt1_4 = Entry(master=frameForm, font=("Arial Bold", 24), width=10)
    txt1_4.grid(column=4, row=2, sticky='w', padx=5, pady=5)
    txt1_5 = Entry(master=frameForm, font=("Arial Bold", 24), width=10)
    txt1_5.grid(column=5, row=2, sticky='w', padx=5, pady=5)

    txt1_1.insert(0, "7")
    txt1_2.insert(0, "5")
    txt1_3.insert(0, "15")
    txt1_4.insert(0, "28")
    txt1_5.insert(0, "80")

    lbl1_1.grid(column=0, row=2, sticky='w', padx=(100, 0), pady=(20, 20))
    lbl1_2.grid(column=0, row=3, sticky='w', padx=(100, 0), pady=(20, 20))
    lbl1_3.grid(column=0, row=4, sticky='w', padx=(100, 0), pady=(20, 20))

    txt2_1 = Entry(master=frameForm, font=("Arial Bold", 24), width=10)
    txt2_1.grid(column=1, row=3, sticky='w', padx=5, pady=5)
    txt2_2 = Entry(master=frameForm, font=("Arial Bold", 24), width=10)
    txt2_2.grid(column=2, row=3, sticky='w', padx=5, pady=5)
    txt2_3 = Entry(master=frameForm, font=("Arial Bold", 24), width=10)
    txt2_3.grid(column=3, row=3, sticky='w', padx=5, pady=5)
    txt2_4 = Entry(master=frameForm, font=("Arial Bold", 24), width=10)
    txt2_4.grid(column=4, row=3, sticky='w', padx=5, pady=5)
    txt2_5 = Entry(master=frameForm, font=("Arial Bold", 24), width=10)
    txt2_5.grid(column=5, row=3, sticky='w', padx=5, pady=5)

    txt2_1.insert(0, "10")
    txt2_2.insert(0, "8")
    txt2_3.insert(0, "11")
    txt2_4.insert(0, "13")
    txt2_5.insert(0, "15")

    txt3_1 = Entry(master=frameForm, font=("Arial Bold", 24), width=10)
    txt3_1.grid(column=1, row=4, sticky='w', padx=5, pady=5)
    txt3_2 = Entry(master=frameForm, font=("Arial Bold", 24), width=10)
    txt3_2.grid(column=2, row=4, sticky='w', padx=5, pady=5)
    txt3_3 = Entry(master=frameForm, font=("Arial Bold", 24), width=10)
    txt3_3.grid(column=3, row=4, sticky='w', padx=5, pady=5)
    txt3_4 = Entry(master=frameForm, font=("Arial Bold", 24), width=10)
    txt3_4.grid(column=4, row=4, sticky='w', padx=5, pady=5)
    txt3_5 = Entry(master=frameForm, font=("Arial Bold", 24), width=10)
    txt3_5.grid(column=5, row=4, sticky='w', padx=5, pady=5)

    txt3_1.insert(0, "3")
    txt3_2.insert(0, "2")
    txt3_3.insert(0, "2")
    txt3_4.insert(0, "6")
    txt3_5.insert(0, "5")

    var = IntVar()
    var.set(0)
    firstInput = Radiobutton(master=frameForm, text="Рассчитать первую пачку", variable=var, value=0)
    secondInput = Radiobutton(master=frameForm, text="Рассчитать вторую пачку", variable=var, value=1)
    thirdInput = Radiobutton(master=frameForm, text="Рассчитать третью пачку", variable=var, value=2)

    firstInput.grid(column=1, row=5, padx=5, pady=5)
    secondInput.grid(column=2, row=5, padx=5, pady=5)
    thirdInput.grid(column=3, row=5, padx=5, pady=5)

    var2 = IntVar()
    var2.set(0)
    negative = Radiobutton(master=frameForm, text="Негатив", variable=var2, value=0)
    baza = Radiobutton(master=frameForm, text="База", variable=var2, value=1)
    positive = Radiobutton(master=frameForm, text="Позитив", variable=var2, value=2)

    negative.grid(column=1, row=6, padx=5, pady=5)
    baza.grid(column=2, row=6, padx=5, pady=5)
    positive.grid(column=3, row=6, padx=5, pady=5)

    btn = Button(master=frameForm, text="Рассчитать!", command=(lambda: clicked(1)), font=("Arial Bold", 20))
    btn.grid(column=2, row=7, sticky='e')

else:
    print("SECOND")
    window = Tk()
    window.columnconfigure(0, weight=1, minsize=75)
    window.rowconfigure([0, 1], weight=1, minsize=50)
    window.geometry(screenResolution2)
    window.minsize(width2, height2)
    window.maxsize(width2 + 200, height2 + 200)
    window.title("Регрессия")
    frame = Frame(master=window, borderwidth=10, relief=border_effects["ridge"])
    frameTitle = Frame(master=frame, borderwidth=10, relief=border_effects["ridge"])
    frameForm = Frame(master=frame, borderwidth=10, relief=border_effects["ridge"])
    frameFormYears0 = Frame(master=frameForm, borderwidth=10, relief=border_effects["ridge"])
    frameFormYears1 = Frame(master=frameForm, borderwidth=10, relief=border_effects["ridge"])
    frameFormYears2 = Frame(master=frameForm, borderwidth=10, relief=border_effects["ridge"])
    frameFormYears3 = Frame(master=frameForm, borderwidth=10, relief=border_effects["ridge"])
    frameFormYears4 = Frame(master=frameForm, borderwidth=10, relief=border_effects["ridge"])
    frameFormYears5 = Frame(master=frameForm, borderwidth=10, relief=border_effects["ridge"])
    frame.grid()
    frameTitle.grid(column=0, row=0)
    frameForm.grid(column=0, row=1)
    frameFormYears0.grid(column=0, row=1, padx=(10, 10), pady=(10, 10))
    frameFormYears1.grid(column=1, row=1, padx=(10, 10), pady=(10, 10))
    frameFormYears2.grid(column=2, row=1, padx=(10, 10), pady=(10, 10))
    frameFormYears3.grid(column=3, row=1, padx=(10, 10), pady=(10, 10))
    frameFormYears4.grid(column=4, row=1, padx=(10, 10), pady=(10, 10))
    frameFormYears5.grid(column=5, row=1, padx=(10, 10), pady=(10, 10))

    lbl = Label(master=frameTitle, text="Регрессия", font=("Arial Bold", 24), background='blue',
                foreground='white')
    lbl1_1 = Label(master=frameForm, text="Input data", font=("Arial Bold", 20), background='blue', foreground='white',
                   justify="right", padx=10, pady=10)
    lbl1_2 = Label(master=frameForm, text="Input data 2", font=("Arial Bold", 24), background='blue',
                   foreground='white')
    lbl1_3 = Label(master=frameForm, text="Input data 3", font=("Arial Bold", 24), background='blue',
                   foreground='white')
    lbl1_4 = Label(master=frameForm, text="Input data 3", font=("Arial Bold", 24), background='blue',
                   foreground='white')
    lbl1_5 = Label(master=frameForm, text="Input data 3", font=("Arial Bold", 24), background='blue',
                   foreground='white')

    lbl2_1 = Label(master=frameForm, text="Какая cтрана?", font=("Arial Bold", 18), background='blue',
                   foreground='white', padx=5, pady=5)

    lbl5 = Label(master=frameFormYears0, text="Количественный показатель", font=("Arial Bold", 20), background='blue',
                 foreground='white', padx=20, pady=10)
    lbl6 = Label(master=frameFormYears1, text="2019", font=("Arial Bold", 20), background='blue', foreground='white',
                 padx=20, pady=10)
    lbl7 = Label(master=frameFormYears2, text="2020", font=("Arial Bold", 20), background='blue', foreground='white',
                 padx=20, pady=10)
    lbl8 = Label(master=frameFormYears3, text="2021", font=("Arial Bold", 20), background='blue', foreground='white',
                 padx=20, pady=10)
    lbl9 = Label(master=frameFormYears4, text="2022", font=("Arial Bold", 20), background='blue', foreground='white',
                 padx=20, pady=10)
    lbl10 = Label(master=frameFormYears5, text="2023", font=("Arial Bold", 20), background='blue', foreground='white',
                  padx=20, pady=10)

    lbl.grid(column=0, row=0, sticky='w', padx=(20, 20), pady=(20, 20))
    lbl5.grid(column=0, row=1, sticky='w')
    lbl6.grid(column=1, row=1, sticky='w')
    lbl7.grid(column=2, row=1, sticky='w')
    lbl8.grid(column=3, row=1, sticky='w')
    lbl9.grid(column=4, row=1, sticky='w')
    lbl10.grid(column=5, row=1, sticky='w')

    lbl2_1.grid(column=2, row=8, sticky='w', padx=(20, 20), pady=(20, 20))

    txt0_1 = Entry(master=frameForm, font=("Arial Bold", 20), width=10)
    txt0_1.grid(column=2, row=9, sticky='w', padx=10, pady=10)

    txt1_1 = Entry(master=frameForm, font=("Arial Bold", 24), width=10)
    txt1_1.grid(column=1, row=2, sticky='w', padx=5, pady=5)
    txt1_2 = Entry(master=frameForm, font=("Arial Bold", 24), width=10)
    txt1_2.grid(column=2, row=2, sticky='w', padx=5, pady=5)
    txt1_3 = Entry(master=frameForm, font=("Arial Bold", 24), width=10)
    txt1_3.grid(column=3, row=2, sticky='w', padx=5, pady=5)
    txt1_4 = Entry(master=frameForm, font=("Arial Bold", 24), width=10)
    txt1_4.grid(column=4, row=2, sticky='w', padx=5, pady=5)
    txt1_5 = Entry(master=frameForm, font=("Arial Bold", 24), width=10)
    txt1_5.grid(column=5, row=2, sticky='w', padx=5, pady=5)

    txt1_1.insert(0, "7")
    txt1_2.insert(0, "5")
    txt1_3.insert(0, "15")
    txt1_4.insert(0, "28")
    txt1_5.insert(0, "80")

    lbl1_1.grid(column=0, row=2, sticky='w', padx=(100, 0), pady=(20, 20))
    lbl1_2.grid(column=0, row=3, sticky='w', padx=(100, 0), pady=(20, 20))
    lbl1_3.grid(column=0, row=4, sticky='w', padx=(100, 0), pady=(20, 20))

    txt2_1 = Entry(master=frameForm, font=("Arial Bold", 24), width=10)
    txt2_1.grid(column=1, row=3, sticky='w', padx=5, pady=5)
    txt2_2 = Entry(master=frameForm, font=("Arial Bold", 24), width=10)
    txt2_2.grid(column=2, row=3, sticky='w', padx=5, pady=5)
    txt2_3 = Entry(master=frameForm, font=("Arial Bold", 24), width=10)
    txt2_3.grid(column=3, row=3, sticky='w', padx=5, pady=5)
    txt2_4 = Entry(master=frameForm, font=("Arial Bold", 24), width=10)
    txt2_4.grid(column=4, row=3, sticky='w', padx=5, pady=5)
    txt2_5 = Entry(master=frameForm, font=("Arial Bold", 24), width=10)
    txt2_5.grid(column=5, row=3, sticky='w', padx=5, pady=5)

    txt2_1.insert(0, "10")
    txt2_2.insert(0, "8")
    txt2_3.insert(0, "11")
    txt2_4.insert(0, "13")
    txt2_5.insert(0, "15")

    txt3_1 = Entry(master=frameForm, font=("Arial Bold", 24), width=10)
    txt3_1.grid(column=1, row=4, sticky='w', padx=5, pady=5)
    txt3_2 = Entry(master=frameForm, font=("Arial Bold", 24), width=10)
    txt3_2.grid(column=2, row=4, sticky='w', padx=5, pady=5)
    txt3_3 = Entry(master=frameForm, font=("Arial Bold", 24), width=10)
    txt3_3.grid(column=3, row=4, sticky='w', padx=5, pady=5)
    txt3_4 = Entry(master=frameForm, font=("Arial Bold", 24), width=10)
    txt3_4.grid(column=4, row=4, sticky='w', padx=5, pady=5)
    txt3_5 = Entry(master=frameForm, font=("Arial Bold", 24), width=10)
    txt3_5.grid(column=5, row=4, sticky='w', padx=5, pady=5)

    txt3_1.insert(0, "3")
    txt3_2.insert(0, "2")
    txt3_3.insert(0, "2")
    txt3_4.insert(0, "6")
    txt3_5.insert(0, "5")

    var = IntVar()
    var.set(0)
    firstInput = Radiobutton(master=frameForm, text="Рассчитать первую пачку", variable=var, value=0)
    secondInput = Radiobutton(master=frameForm, text="Рассчитать вторую пачку", variable=var, value=1)
    thirdInput = Radiobutton(master=frameForm, text="Рассчитать третью пачку", variable=var, value=2)

    firstInput.grid(column=1, row=5, padx=5, pady=5)
    secondInput.grid(column=2, row=5, padx=5, pady=5)
    thirdInput.grid(column=3, row=5, padx=5, pady=5)

    btn = Button(master=frameForm, text="Рассчитать!", command=(lambda: clicked(0)), font=("Arial Bold", 20))
    btn.grid(column=2, row=6, sticky='e')
window.mainloop()