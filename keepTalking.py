# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 00:57:57 2021

@author: 15
"""
from tkinter import *
class ModuleFrame(Frame):
    def __init__(self, master, label, button, func, helper):
        Frame.__init__(self, master)
        self.mFrame = Frame(self)
        self.mFrame.pack()
        
        self.moduleLabel = Label(self.mFrame, text=label)
        self.moduleLabel.pack(pady=10)
        
        self.moduleInput = Entry(self.mFrame)
        self.moduleInput.pack()
        self.moduleInput.bind('<Return>', func)
        
        self.moduleButton = Button(self.mFrame, text=button)
        self.moduleButton.bind('<Button-1>', func)
        self.moduleButton.pack(side=LEFT)
        
        self.moduleHelpButton = Button(self.mFrame, text=' ? ', command=helper)
        self.moduleHelpButton.pack()

    def getInput(self):
        return self.moduleInput.get()

class KeepTalkingApp(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        # 基本信息
        self.iFrame = Frame(self)
        self.iFrame.pack()
        
        self.batteryLabel = Label(self.iFrame, text='输入电池数：')
        self.batteryLabel.pack(pady=10)
        
        self.batteryNumInput = Entry(self.iFrame)
        self.batteryNumInput.pack()
        
        self.serialNumLabel = Label(self.iFrame, text='输入序列号：')
        self.serialNumLabel.pack(pady=10)
        
        self.serialNumInput = Entry(self.iFrame)
        self.serialNumInput.pack()
        
        self.ParallelLabel = Label(self.iFrame, text='有没有Parallel接口：')
        self.ParallelLabel.pack(pady=10)
        
        self.ParallelInput = Entry(self.iFrame)
        self.ParallelInput.pack()
        
        # # 简单线路
        # self.slFrame = Frame(self)
        # self.slFrame.pack()
        
        # self.simpleLineLabel = Label(self.slFrame, text='简单线路')
        # self.simpleLineLabel.pack(pady=10)
        
        # self.simpleLineInput = Entry(self.slFrame)
        # self.simpleLineInput.pack()
        # self.simpleLineInput.bind('<Return>', self.simpleLine)
        
        # self.simpleLineButton = Button(self.slFrame, text='输入颜色序列')
        # self.simpleLineButton.bind('<Button-1>', self.simpleLine)
        # self.simpleLineButton.pack(side=LEFT)
        
        # self.simpleLineHelpButton = Button(self.slFrame, text=' ? ', command=self.simpleLineHelper)
        # self.simpleLineHelpButton.pack()
        
        self.slFrame = ModuleFrame(self, '简单线路', '输入颜色序列', self.simpleLine, self.simpleLineHelper)
        self.slFrame.pack()
        
        # 猜单词题
        self.gFrame = Frame(self)
        self.gFrame.pack()
        
        self.guessWordLabel = Label(self.gFrame, text='猜单词')
        self.guessWordLabel.pack(pady=10)
        
        self.alllettersInput = Entry(self.gFrame)
        self.alllettersInput.pack()
        self.alllettersInput.bind('<Return>', self.guessWord)
        
        self.guessButton = Button(self.gFrame, text='输入备选字母')
        self.guessButton.bind('<Button-1>', self.guessWord)
        self.guessButton.pack(side=LEFT)
        
        self.guessHelpButton = Button(self.gFrame, text=' ? ', command=self.guessWordHelper)
        self.guessHelpButton.pack()
        
        # 线和星星题
        self.lFrame = Frame(self)
        self.lFrame.pack()
        self.LEDStarAndLineLabel = Label(self.lFrame, text='灯、星星和线')
        self.LEDStarAndLineLabel.pack(pady=10)
        
        self.statesInput = Entry(self.lFrame)
        self.statesInput.pack()
        self.statesInput.bind('<Return>', self.LEDStarAndLine)
        
        self.hintButton = Button(self.lFrame, text='按顺序输入灯、星星、蓝色、红色')
        self.hintButton.bind('<Button-1>', self.LEDStarAndLine)
        self.hintButton.pack(side=LEFT)
        
        self.hintHelpButton = Button(self.lFrame, text=' ? ', command=self.LEDStarAndLineHelper)
        self.hintHelpButton.pack()

    # def hello(self):
    #     name = self.nameInput.get() or 'world'
    #     messagebox.showinfo('Message', 'Hello, %s' % name)
        
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
            elif allcolors[-1]=='w':
                return "l3-2：剪最后一根"
            elif (len(allcolors.split('b'))-1) > 1:
                return "l3-3：剪最后一根 蓝 线"
            else :
                return "l3-4：剪最后一根"
            
        def l4():
            if (len(allcolors.split('r'))-1) > 1 and int(sn[-1])%2:
                return "l4-1：剪最后一根 红 线"
            # yyby
            elif (not 'r' in allcolors) and (allcolors[-1]=='y'):
                return "l4-2：剪第 1 根"
            # ybyw
            elif (len(allcolors.split('b'))-1) == 1:
                return "l4-3：剪第 1 根"
            # yyww
            elif (len(allcolors.split('y'))-1) > 1:
                return "l4-4：剪最后一根"
            # wwww
            else :
                return "l4-5：剪第 2 根"
            
        def l5():
            if (allcolors[-1]=='k') and int(sn[-1])%2:
                return "l5-1：剪第 4 根"
            elif (len(allcolors.split('r'))-1) == 1 and (len(allcolors.split('y'))-1) > 1:
                return "l5-2：剪第 1 根"
            elif (not 'k' in allcolors):
                return "l5-3：剪第 2 根"
            else :
                return "l5-4：剪第 1 根"
            
        def l6():
            if (not 'y' in allcolors) and int(sn[-1])%2:
                return "l6-1：剪第 3 根"
            elif (len(allcolors.split('y'))-1) == 1 and (len(allcolors.split('w'))-1) > 1:
                return "l6-2：剪第 4 根"
            elif (not 'r' in allcolors):
                return "l6-3：剪最后一根"
            else :
                return "l6-4：剪第 4 根"
            
        action = {            
            3:l3,
            4:l4,
            5:l5,
            6:l6
            }
        messagebox.showinfo('操作', '%s' % action[len(allcolors)]())
        
        
    def simpleLineHelper(ev = None):
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
        allletters = self.alllettersInput.get() or 'test value'
        # self.alllettersInput.delete(0,END)
        words = ['about', 'after', 'again', 'below', 'could', 'every', 'first', 'found', 'great', 'house', 'large', 'learn', 'never', 'other', 'place', 'plant', 'point', 'right', 'small', 'sound', 'spell', 'still', 'study', 'their', 'there', 'these', 'thing', 'think', 'three', 'water', 'where', 'which', 'world', 'would', 'write']
        # allletters = 'qskxzb mcberu'
        # allletters = input('输入所有的备选字符：')
        allletters = allletters.split(' ')
        oldList = words
        newList = []
        letterNum = 0
        for letters in allletters:
            letters = list(letters)
            newList = []
            for letter in letters:
                for l in letter:
                    for w in words:
                        if w[letterNum]==l:
                            newList.append(w)
            letterNum = letterNum + 1
            newList = list(set(newList)&set(oldList))
            oldList = newList
        # print(oldList)
        messagebox.showinfo('答案', '经过分析，可能的备选项有：%s' % oldList)
    
    def guessWordHelper(ev = None):
        messagebox.showinfo('帮助', """按字母位置顺序输入备选字母，不同位置的字母用空格分开。
如果第一个位置候选有：xompwz，第二个位置候选有：zmkpar，
那么输入参数应该是：'xompwz zmkpar'""")

    # 按照灯、星星、蓝色、红色的顺序写
    # 如果灯亮，写1，如果不亮，写0；
    # 如果有星星，写1，如果无星星，写0；
    # 如果含蓝色，写1，如果不含蓝色，写0；
    # 如果含红色，写1，如果不含红色，写0。
    def LEDStarAndLine(self, event):
        states = self.statesInput.get() or '16'
        self.statesInput.delete(0,END)
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
            hint='ValueError'
        # # print(hints[hint])
        # messagebox.showinfo('提示', '%s' % hints[hint])
        
        def cutAction():
            return "C:剪"
        def dontAction():
            return "D:不剪"
        def serialNumAction():
            sn = self.serialNumInput.get() or '1'
            return ("S:不剪" if int(sn[-1])%2 else "S:剪")
        def parallelAction():
            p = int(self.ParallelInput.get() or '0')
            return ("P:剪" if p else "P:不剪")
        def batteryAction():
            bn = self.batteryNumInput.get() or '0'
            return ("B:剪" if bn>=2 else "B:不剪")
            
        action = {            
            'C':cutAction,
            'D':dontAction,
            'S':serialNumAction,
            'P':parallelAction,
            'B':batteryAction
            }
        messagebox.showinfo('操作', '%s' % action[hint]())
        
    def LEDStarAndLineHelper(ev = None):
        messagebox.showinfo('帮助', """按照灯、星星、蓝色、红色的顺序写
如果灯亮，写1，如果不亮，写0；
如果有星星，写1，如果无星星，写0；
如果含蓝色，写1，如果不含蓝色，写0；
如果含红色，写1，如果不含红色，写0。""")

app = KeepTalkingApp()
# 设置窗口标题:
app.master.title('')
def center_window(w, h):
    # 获取屏幕 宽、高
    ws = app.winfo_screenwidth()
    hs = app.winfo_screenheight()
    # 计算 x, y 位置
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    app.master.geometry('%dx%d+%d+%d' % (w, h, x, y))
center_window(350, 500)
app.update()  # 必须
# 主消息循环:
app.mainloop()









# guessWord('')


# LEDStarAndLine('')