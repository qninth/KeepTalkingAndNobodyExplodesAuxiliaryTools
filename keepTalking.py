# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 00:57:57 2021

@author: 15
"""
from tkinter import *
from tkinter import messagebox


class ModuleFrame(Frame):
    def __init__(self, master, label, button, func, helper):
        Frame.__init__(self, master)
        self.iFrame = Frame(self)
        self.iFrame.pack()

        self.moduleLabel = Label(self.iFrame, text=label)
        self.moduleLabel.pack(side=LEFT, pady=2)

        self.moduleInput = Entry(self.iFrame)
        self.moduleInput.pack(pady=2)
        self.moduleInput.bind('<Return>', func)

        self.mFrame = Frame(self)
        self.mFrame.pack()

        self.moduleButton = Button(self.mFrame, text=button)
        self.moduleButton.bind('<Button-1>', func)
        self.moduleButton.pack(side=LEFT, pady=2)

        self.moduleHelpButton = Button(self.mFrame, text=' ? ', command=helper)
        self.moduleHelpButton.pack(pady=2)

        self.idleLabel = Label(self, text='')
        self.idleLabel.pack(pady=0)

    def getInput(self):
        return self.moduleInput.get()

    def deleteInput(self):
        self.moduleInput.delete(0, END)


class KeepTalkingApp(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):

        self.clearAllButton = Button(self, text='清除全部输入')
        self.clearAllButton.bind('<Button-1>', self.clearAll)
        self.clearAllButton.pack(pady=2)

        # 基本信息
        self.iFrame = Frame(self)
        self.iFrame.pack()

        self.bFrame = Frame(self.iFrame)
        self.bFrame.pack()
        self.batteryLabel = Label(self.bFrame, text='输入电池数：')
        self.batteryLabel.pack(side=LEFT, pady=2)
        self.batteryNumInput = Entry(self.bFrame)
        self.batteryNumInput.pack(pady=2)

        self.snFrame = Frame(self.iFrame)
        self.snFrame.pack()
        self.serialNumLabel = Label(self.snFrame, text='输入序列号：')
        self.serialNumLabel.pack(side=LEFT, pady=2)
        self.serialNumInput = Entry(self.snFrame)
        self.serialNumInput.pack(pady=2)

        self.pFrame = Frame(self.iFrame)
        self.pFrame.pack()
        self.ParallelLabel = Label(self.pFrame, text='Parallel接口：')
        self.ParallelLabel.pack(side=LEFT, pady=2)
        self.ParallelInput = Entry(self.pFrame)
        self.ParallelInput.pack(pady=2)

        self.frkFrame = Frame(self.iFrame)
        self.frkFrame.pack()
        self.FRKLabel = Label(self.frkFrame, text='FRK灯亮：')
        self.FRKLabel.pack(side=LEFT, pady=2)
        self.FRKInput = Entry(self.frkFrame)
        self.FRKInput.pack(pady=2)

        self.idleLabel = Label(self.iFrame, text='')
        self.idleLabel.pack(pady=2)

        # 简单线路
        self.slFrame = ModuleFrame(self, '简单线路', '输入颜色序列', self.simpleLine, self.simpleLineHelper)
        self.slFrame.pack()

        # 猜单词题
        self.guessFrame = ModuleFrame(self, '猜单词', '输入备选字母', self.guessWord, self.guessWordHelper)
        self.guessFrame.pack()

        # 线和星星题
        self.lsFrame = ModuleFrame(self, '灯、星星和线', '按顺序输入灯、星星、蓝色、红色', self.LEDStarAndLine, self.LEDStarAndLineHelper)
        self.lsFrame.pack()

        # 大按钮
        self.bbFrame = ModuleFrame(self, '大按钮', '输入大按钮的颜色 文字', self.bigButton, self.bigButtonHelper)
        self.bbFrame.pack()

        # 旋钮
        self.knobFrame = ModuleFrame(self, '旋钮', '输入旋扭灯显', self.knob, self.knobHelper)
        self.knobFrame.pack()

    def clearAll(self, event):
        self.batteryNumInput.delete(0,END)
        self.serialNumInput.delete(0,END)
        self.ParallelInput.delete(0,END)
        self.FRKInput.delete(0,END)
        self.slFrame.deleteInput()
        self.guessFrame.deleteInput()
        self.lsFrame.deleteInput()
        self.bbFrame.deleteInput()
        self.knobFrame.deleteInput()

    # 按字母位置顺序输入备选字母，不同位置的字母用空格分开
    # 如果第一个位置候选有：xompwz，第二个位置候选有：zmkpar，
    # 那么输入参数应该是：'xompwz zmkpar'
    def simpleLine(self, event):
        allcolors = self.slFrame.getInput() or 'RRRRR'
        # self.alllettersInput.delete(0,END)
        allcolors = allcolors.lower()

        sn = self.serialNumInput.get() or '12345'

        def l3():
            if not 'r' in allcolors:
                return "l3-1：剪第 2 根"
            elif allcolors[-1] == 'w':
                return "l3-2：剪最后一根"
            elif (len(allcolors.split('b')) - 1) > 1:
                return "l3-3：剪最后一根 蓝 线"
            else:
                return "l3-4：剪最后一根"

        def l4():
            if (len(allcolors.split('r')) - 1) > 1 and int(sn[-1]) % 2:
                return "l4-1：剪最后一根 红 线"
            # yyby
            elif (not 'r' in allcolors) and (allcolors[-1] == 'y'):
                return "l4-2：剪第 1 根"
            # ybyw
            elif (len(allcolors.split('b')) - 1) == 1:
                return "l4-3：剪第 1 根"
            # yyww
            elif (len(allcolors.split('y')) - 1) > 1:
                return "l4-4：剪最后一根"
            # wwww
            else:
                return "l4-5：剪第 2 根"

        def l5():
            if (allcolors[-1] == 'k') and int(sn[-1]) % 2:
                return "l5-1：剪第 4 根"
            elif (len(allcolors.split('r')) - 1) == 1 and (len(allcolors.split('y')) - 1) > 1:
                return "l5-2：剪第 1 根"
            elif (not 'k' in allcolors):
                return "l5-3：剪第 2 根"
            else:
                return "l5-4：剪第 1 根"

        def l6():
            if (not 'y' in allcolors) and int(sn[-1]) % 2:
                return "l6-1：剪第 3 根"
            elif (len(allcolors.split('y')) - 1) == 1 and (len(allcolors.split('w')) - 1) > 1:
                return "l6-2：剪第 4 根"
            elif (not 'r' in allcolors):
                return "l6-3：剪最后一根"
            else:
                return "l6-4：剪第 4 根"

        action = {
            3: l3,
            4: l4,
            5: l5,
            6: l6
        }
        messagebox.showinfo('操作', '%s' % action[len(allcolors)]())

    def simpleLineHelper(ev=None):
        messagebox.showinfo('帮助', """从上到下输入颜色信息（大小写不敏感）：
红 - R；
黄 - Y；
蓝 - B；
黑 - K；
白 - W。""")

    # 按字母位置顺序输入备选字母，不同位置的字母用空格分开
    # 如果第一个位置候选有：xompwz，第二个位置候选有：zmkpar，
    # 那么输入参数应该是：'xompwz zmkpar'
    def guessWord(self, event):
        allletters = self.guessFrame.getInput() or 'test value'
        words = ['about', 'after', 'again', 'below', 'could', 'every', 'first', 'found', 'great', 'house', 'large',
                 'learn', 'never', 'other', 'place', 'plant', 'point', 'right', 'small', 'sound', 'spell', 'still',
                 'study', 'their', 'there', 'these', 'thing', 'think', 'three', 'water', 'where', 'which', 'world',
                 'would', 'write']
        allletters = allletters.strip().lower().split(' ')
        oldList = words
        newList = []
        letterNum = 0
        for letters in allletters:
            letters = list(letters)
            newList = []
            for letter in letters:
                for l in letter:
                    for w in words:
                        if w[letterNum] == l:
                            newList.append(w)
            letterNum = letterNum + 1
            newList = list(set(newList) & set(oldList))
            oldList = newList
        # print(oldList)
        messagebox.showinfo('答案', '经过分析，可能的备选项有：%s' % oldList)

    def guessWordHelper(ev=None):
        messagebox.showinfo('帮助', """按字母位置顺序输入备选字母，不同位置的字母用空格分开。
如果第一个位置候选有：xompwz，第二个位置候选有：zmkpar，
那么输入参数应该是：'xompwz zmkpar'""")

    # 按照灯、星星、蓝色、红色的顺序写
    # 如果灯亮，写1，如果不亮，写0；
    # 如果有星星，写1，如果无星星，写0；
    # 如果含蓝色，写1，如果不含蓝色，写0；
    # 如果含红色，写1，如果不含红色，写0。
    def LEDStarAndLine(self, event):
        states = self.lsFrame.getInput() or '16'
        self.lsFrame.deleteInput()
        lookupTable = ['C', 'S', 'S', 'S', 'C', 'C', 'D', 'P', 'D', 'B', 'P', 'S', 'B', 'P', 'B', 'D']

        # hints = {
        #     'C':'剪断它',
        #     'D':'不要管，看下一根线',
        #     'S':'去看序列号末位（偶数剪断线路）',
        #     'P':'检查一下Parallel端口（存在则剪断）',
        #     'B':'数电池的数目（有大于等于2个剪断）',
        #     'ValueError':'输入数组为空或超出16种情况'
        #     }
        try:
            hint = lookupTable[int(states, 2)]
        except ValueError:
            hint = 'ValueError'

        # # print(hints[hint])
        # messagebox.showinfo('提示', '%s' % hints[hint])

        def cutAction():
            return "C:剪"

        def dontAction():
            return "D:不剪"

        def serialNumAction():
            sn = self.serialNumInput.get() or '1'
            return ("S:不剪" if int(sn[-1]) % 2 else "S:剪")

        def parallelAction():
            p = int(self.ParallelInput.get() or '0')
            return ("P:剪" if p else "P:不剪")

        def batteryAction():
            bn = int(self.batteryNumInput.get()) or '0'
            return ("B:剪" if bn >= 2 else "B:不剪")

        def errorHandler():
            return '输入数组为空或超出16种情况'

        action = {
            'C': cutAction,
            'D': dontAction,
            'S': serialNumAction,
            'P': parallelAction,
            'B': batteryAction,
            'ValueError': errorHandler
        }
        messagebox.showinfo('操作', '%s' % action[hint]())

    def LEDStarAndLineHelper(ev=None):
        messagebox.showinfo('帮助', """按照灯、星星、蓝色、红色的顺序写
如果灯亮，写1，如果不亮，写0；
如果有星星，写1，如果无星星，写0；
如果含蓝色，写1，如果不含蓝色，写0；
如果含红色，写1，如果不含红色，写0。""")

    def bigButton(self, event):
        buttonInform = (self.bbFrame.getInput() or 'w anxia').split(' ')
        buttonColor = buttonInform[0]
        buttonText = buttonInform[1]
        batteryNum = self.batteryNumInput.get() or '0'
        FRK = self.FRKInput.get() or '0'
        # self.alllettersInput.delete(0,END)
        if int(batteryNum) > 1 and buttonText == 'yinbao':
            action = "l1:按一下松开"
        elif int(batteryNum) > 2 and int(FRK) == 1:
            action = "l2:按一下松开"
        elif buttonColor == 'r' and buttonText == 'anzhu':
            action = "l3:按一下松开"
        else:
            action = "按住看光条:蓝4黄5其他1"
        messagebox.showinfo('操作', '%s' % action)

    def bigButtonHelper(ev=None):
        messagebox.showinfo('帮助', """输入大按钮的颜色+空格+按钮上文字（全拼）：
颜色：红 = r 蓝 = b 黑 = k 白 = w  黄 = y
文字：引爆 = yinbao、按住 = anzhu

如果是红色引爆，则输入：k yinbao
        """)
###knob旋钮题
    def knob(self, event):
        knobInform = self.knobFrame.getInput()
        # hint = int(knobInform, 2)
        if knobInform[0:3] == '000':
            action = "向左"
        elif knobInform[3:6] == '010':
            action = "向右"
        elif knobInform == '001101' or knobInform == '101011':
            action = "向上"
        elif knobInform == '011101' or knobInform == '101001':
            action = "向下"
        else:
            action = "未定义"
        messagebox.showinfo('操作', '%s' % action)


    def knobHelper(ev=None):
        messagebox.showinfo('帮助', """输入第一行前三个和第二行后三个：
如果提示（■ 为LED亮，□ 为LED暗）：
□ □ ■ □ □ □
□ □ □ ■ □ □
那么输入：001100""")


app = KeepTalkingApp()
# 设置窗口标题:
app.master.title('')


def center_window(w, h):
    # 获取屏幕 宽、高
    ws = app.winfo_screenwidth()
    hs = app.winfo_screenheight()
    # 计算 x, y 位置
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    app.master.geometry('%dx%d+%d+%d' % (w, h, x, y))


center_window(350, 630)
app.update()  # 必须
# 主消息循环:
app.mainloop()

# guessWord('')


# LEDStarAndLine('')