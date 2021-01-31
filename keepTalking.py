# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 00:57:57 2021

@author: 15
"""
from tkinter import *


class KeepTalkingApp(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        #猜单词题
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
    def guessWord(self, event):
        allletters = self.alllettersInput.get() or 'test value'
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
    def LEDStarAndLine(self):
        states = self.statesInput.get() or '16'
        lookupTable = ['C', 'S', 'S', 'S', 'C', 'C', 'D', 'P', 'D', 'B', 'P', 'S', 'B', 'P', 'B', 'D']
        
        hints = {
            'C':'剪断它',
            'D':'不要管，看下一根线',
            'S':'去看序列号末位（偶数剪断线路）',
            'P':'检查一下Parallel端口（存在则剪断）',
            'B':'数电池的数目（有大于等于2个剪断）',
            'ValueError':'输入数组为空或超出16种情况'
            }
        try:
            hint = lookupTable[int(states, 2)]
        except ValueError:
            hint='ValueError'
        # print(hints[hint])
        messagebox.showinfo('提示', '%s' % hints[hint])
        
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
center_window(350, 260)
app.update()  # 必须
# 主消息循环:
app.mainloop()









# guessWord('')


# LEDStarAndLine('')