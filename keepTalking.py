# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 00:57:57 2021

@author: 15

pip install fuzzywuzzy
pip install Levenshtein
"""
from tkinter import *
from tkinter import messagebox
from fuzzywuzzy import process

class ModuleFrame(Frame):
    def __init__(self, master, label, default, button, func, helper):
        Frame.__init__(self, master)
        self.iFrame = Frame(self)
        self.iFrame.pack(side=LEFT)

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

        self.default = default
        # self.idleLabel = Label(self, text='')
        # self.idleLabel.pack(pady=0)

    def getInput(self):
        return self.moduleInput.get() or self.default

    def deleteInput(self):
        self.moduleInput.delete(0, END)


class InformFrame(Frame):
    def __init__(self, master, label, default):
        Frame.__init__(self, master)
        self.iFrame = Frame(master)
        self.iFrame.pack()
        self.informLabel = Label(self.iFrame, text=label)
        self.informLabel.pack(side=LEFT, pady=2)
        
        self.informInput = Entry(self.iFrame)
        self.informInput.pack(pady=2)
        
        self.default = default

    def getInput(self):
        return self.informInput.get() or self.default

    def deleteInput(self):
        self.informInput.delete(0, END)


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

        # battery Number
        self.bFrame = InformFrame(self.iFrame,'输入电池数：', '0')
        self.bFrame.pack()
        
        # serial Num
        self.snFrame = InformFrame(self.iFrame,'输入序列号：', '0')
        self.snFrame.pack()
        
        # Parallel Port
        self.pFrame = InformFrame(self.iFrame,'Parallel接口：', '0')
        self.pFrame.pack()

        # FRK Light
        self.frkFrame = InformFrame(self.iFrame,'FRK灯亮：', '0')
        self.frkFrame.pack()
        
        self.idleLabel = Label(self.iFrame, text='')
        self.idleLabel.pack(pady=2)

        # 简单线路
        self.slFrame = ModuleFrame(self, '简单线路', 'RRRRR', '输入颜色序列',\
                                   self.simpleLine, self.simpleLineHelper)
        self.slFrame.pack()

        # 猜单词题
        self.guessFrame = ModuleFrame(self, '猜单词', 'test value', '输入备选字母',\
                                      self.guessWord, self.guessWordHelper)
        self.guessFrame.pack()

        # 线和星星题
        self.lsFrame = ModuleFrame(self, '灯、线和星星', '100000 rrbwvv 000010', '灯、颜色、星星',\
                                   self.LEDStarAndLine, self.LEDStarAndLineHelper)
        self.lsFrame.pack()

        # 顺序线路题
        self.clFrame = ModuleFrame(self, '顺序线路', 'rbrcba kakbkc ', '颜色位置',\
                                   self.complexLine, self.complexLineHelper)
        self.clFrame.pack()

        # 大按钮
        self.bbFrame = ModuleFrame(self, '大按钮', 'w anxia', '输入颜色 文字',\
                                   self.bigButton, self.bigButtonHelper)
        self.bbFrame.pack()

        # 摩斯电码
        self.mcFrame = ModuleFrame(self, '摩斯电码', '1010001010101', '输入完整的电码',\
                                   self.morseCode, self.morseCodeHelper)
        self.mcFrame.pack()


        # 迷宫
        self.mazeFrame = ModuleFrame(self, '迷宫', '12', '输入圆圈位置',\
                                     self.maze, self.mazeHelper)
        self.mazeFrame.pack()

        # 文字计算器 what's its name module
        self.nameFrame = ModuleFrame(self, '文字模块', '是', '输入文字',\
                                     self.name, self.nameHelper)
        self.nameFrame.pack()

        # 数字计算器 remember module 
        self.rmbFrame = ModuleFrame(self, '数字模块', '1', '显示、位置及数字',\
                                     self.remember, self.rememberHelper)
        self.rmbFrame.pack()


        self.otherFrame = Frame(self)
        self.otherFrame.pack()
        self.keyboardButton = Button(self.otherFrame, text='键盘模块', command=self.keyboard)
        self.keyboardButton.pack(side=LEFT)
        self.fourcolorsButton = Button(self.otherFrame, text='四色方块', command=self.fourcolors)
        self.fourcolorsButton.pack()
        
        
        # 旋钮
        self.knobFrame = ModuleFrame(self, '旋钮', '111111', '输入旋扭灯显',\
                                     self.knob, self.knobHelper)
        self.knobFrame.pack()
        
        
    def popupImage(self, imageFilepath):
        image = PhotoImage(file = imageFilepath)
        img = Toplevel()
        img.wm_title("maze")
        img.wm_attributes('-topmost',1)
    
        l = Label(img, image = image)
        l.grid(row=0, column=0)
    
        b = Button(img, text="关闭", command=img.destroy)
        
        img.bind('<Return>', lambda ev: img.destroy())
        img.bind('<space>', lambda ev: img.destroy())
        img.bind('<Button-2>', lambda ev: img.destroy())
        img.bind('<Button-3>', lambda ev: img.destroy())
        b.grid(row=1, column=0)
        img.mainloop()
        
        
    def clearAll(self, event):
        self.bFrame.deleteInput()
        self.snFrame.deleteInput()
        self.pFrame.deleteInput()
        self.frkFrame.deleteInput()
        self.slFrame.deleteInput()
        self.guessFrame.deleteInput()
        self.lsFrame.deleteInput()
        self.clFrame.deleteInput()
        self.bbFrame.deleteInput()
        self.mcFrame.deleteInput()
        self.mazeFrame.deleteInput()
        self.nameFrame.deleteInput()
        self.rmbFrame.deleteInput()
        self.knobFrame.deleteInput()

    # 按字母位置顺序输入备选字母，不同位置的字母用空格分开
    # 如果第一个位置候选有：xompwz，第二个位置候选有：zmkpar，
    # 那么输入参数应该是：'xompwz zmkpar'
    def simpleLine(self, event):
        allcolors = self.slFrame.getInput() or 'RRRRR'
        # self.alllettersInput.delete(0,END)
        allcolors = allcolors.lower()

        sn = self.snFrame.getInput() or '12345'

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
        states = self.lsFrame.getInput() or '100000 rrbwvv 000010'

        # self.lsFrame.deleteInput()

        def parserStates(states):
            sList = states.strip().split(' ')

            def led(s):
                return s

            def rgb(s):
                s1 = ''
                s2 = ''
                for a in s:
                    if a == 'r':
                        s1 = s1 + '1'
                        s2 = s2 + '0'
                    elif a == 'b':
                        s1 = s1 + '0'
                        s2 = s2 + '1'
                    elif a == 'h':
                        s1 = s1 + '1'
                        s2 = s2 + '1'
                    elif a == 'w':
                        s1 = s1 + '0'
                        s2 = s2 + '0'
                    elif a == 'v':
                        s1 = s1 + 'v'
                        s2 = s2 + 'v'
                    else:
                        s1 = s1 + 'e'
                        s2 = s2 + 'e'
                return s1, s2

            def star(s):
                return s

            sLed = led(sList[0])
            sR, sB = rgb(sList[1])
            sStar = star(sList[2])

            decodedStates = []
            for i in range(len(sLed)):
                decodedStates.append(sLed[i] + sStar[i] + sB[i] + sR[i])
            return decodedStates

        decodedStates = []
        decodedStates = parserStates(states)

        def findState(self, state):
            lookupTable = ['C', 'S', 'S', 'S', 'C', 'C', 'D', 'P', 'D', 'B', 'P', 'S', 'B', 'B', 'P', 'D']

            # hints = {
            #     'C':'剪断它',
            #     'D':'不要管，看下一根线',
            #     'S':'去看序列号末位（偶数剪断线路）',
            #     'P':'检查一下Parallel端口（存在则剪断）',
            #     'B':'数电池的数目（有大于等于2个剪断）',
            #     'ValueError':'输入数组为空或超出16种情况'
            #     }
            try:
                hint = lookupTable[int(state, 2)]
            except ValueError:
                hint = 'ValueError'

            # # print(hints[hint])
            # messagebox.showinfo('提示', '%s' % hints[hint])

            def cutAction(self):
                return "C:剪"

            def dontAction(self):
                return "D:不剪"

            def serialNumAction(self):
                sn = self.snFrame.getInput() or '1'
                return ("S:不剪" if int(sn[-1]) % 2 else "S:剪")

            def parallelAction(self):
                p = int(self.ParallelInput.get() or '0')
                return ("P:剪" if p else "P:不剪")

            def batteryAction(self):
                bn = int(self.bFrame.getInput() or '0')
                return ("B:剪" if bn >= 2 else "B:不剪")

            def errorHandler(self):
                return '输入数组为空或超出16种情况'

            action = {
                'C': cutAction,
                'D': dontAction,
                'S': serialNumAction,
                'P': parallelAction,
                'B': batteryAction,
                'ValueError': errorHandler
            }
            # messagebox.showinfo('操作', '%s' % action[hint]())
            return action[hint](self)

        action = ''
        actionOne = ''
        num = 0
        for state in decodedStates:
            fs = findState(self, state)
            if state.find('v') < 0:
                num = num + 1
                if fs.find(':剪') >= 0:
                    actionOne = actionOne + str(num) + ', '

            if state.find('e') > 0:
                fs = "输入颜色存在错误，请检查"
            action = action + fs + '\r\n'
        actionOne = '剪第 ' + actionOne[:-2] + ' 根'
        messagebox.showinfo('操作', '%s\r\n%s' % (action, actionOne))

    def LEDStarAndLineHelper(ev=None):
        messagebox.showinfo('帮助', """按照灯、线和星星的顺序写
如果灯亮，写1，如果不亮，写0；
如果线是红色，写r，如果线是蓝色，写b，如果线是蓝红，写h，如果线是白色，写w, 注意如果没线,写v；
  (r = red, b = blue, h = hybird, w = white, v=vacant)
如果有星星，写1，如果无星星，写0。

如果情况如下：
亮 暗 暗 暗 暗 暗
红 红 蓝 白 空 空
线 线 白 线     
无 无 无 无 星 无
则输入：100000 rrbwvv 000010""")

    ### sequence Line 顺序线题
    def complexLine(self, event):
        context = self.clFrame.getInput() or 'rbrcba kakbkc '
        context = context.strip()
        stageNum = len(context.split(' '))
        # '121123'
        color = ''.join(context.split(' '))[::2]
        text = ''.join(context.split(' '))[1::2]
        colorL = ''.join(context.split(' ')[-1])[::2]
        textL = ''.join(context.split(' ')[-1])[1::2]

        table = {
            'r':['C','B','A','AC','B','AC','ABC','AB','B'],
            'b':['B','AC','B','A','B','BC','C','AC','A'],
            'k':['ABC','AC','B','AC','B','BC','AB','C','C']
        }

        actionList = []
        for i in range(0,len(colorL)):
            c = colorL[i]
            t = textL[i]
            num = color[0:len(color)-len(colorL)+1+i].count(c)
            if table[c][num-1].lower().find(t)>=0 :
                actionList.append(c + '-' + str(num) + '-' +  t + ': ' + '剪')
            else:
                actionList.append(c + '-' + str(num) + '-' +  t + ': ' + '不剪')

        action = '\r\n'.join(actionList)
        messagebox.showinfo('操作', '%s' % action)

    def complexLineHelper(ev=None):
        messagebox.showinfo('帮助', """按顺序一次输入 颜色位置颜色位置, 空格后输入再次显示的线路颜色和位置：
红色-r，蓝色-b，黑色-k
例如：
第一次出现红色连a，蓝色连b，黑色连c；
第二次出现黑色连a，黑色连b，黑色连c。
则输入：rabbkc kakbrc""")

    def bigButton(self, event):
        buttonInform = (self.bbFrame.getInput() or 'w anxia').split(' ')
        buttonColor = buttonInform[0]
        buttonText = buttonInform[1]
        batteryNum = self.bFrame.getInput() or '0'
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

    def maze(self, event):
        mazeInform = (self.mazeFrame.getInput() or '12').split(' ')    
        self.popupImage( imageFilepath = ('images/%s.gif' % mazeInform[0]) )
        # messagebox._show('操作', 'maze' , _icon = image)

    def mazeHelper(ev=None):
        messagebox.showinfo('帮助', """输入靠左的圆圈坐标：
左上角为11，一行二列为21，
回车可以得到对应的迷宫图片""")

    def morseCode(self, event):
        morseCodeInform = (self.mcFrame.getInput() or '1010001010101').strip()
        morseCodeDict = {
            '10000011000'      : '3.600 MHz',
            '1000000001010111' : '3.552 MHz',
            '1000111111000000' : '3.565 MHz',
            '100011110010000'  : '3.535 MHz',
            '1000010001101'    : '3.572 MHz',
            '1000010001010101' : '3.575 MHz',
            '00100100001010101': '3.555 MHz',
            '00000101000100000': '3.515 MHz',
            '0100001101000'    : '3.542 MHz',
            '0000000001000100' : '3.505 MHz',
            '0000100001010101' : '3.522 MHz',
            '0001001101'       : '3.582 MHz',
            '00010010110'      : '3.592 MHz',
            '000101011110000'  : '3.545 MHz',
            '1010001010101'    : '3.532 MHz',
            '0001010101111010' : '3.595 MHz'
            }
        morseCodeList = list(morseCodeDict.keys())
        
        if len(morseCodeInform)<=10:
            morseCodeList2 = []
            morseCodeDict2 = {}
            for mc in morseCodeList:
                morseCodeList2.append(mc[0:len(morseCodeInform)])
                morseCodeDict2[mc[0:len(morseCodeInform)]] = mc            
            actionList = process.extract(morseCodeInform, morseCodeList2, limit=2)        
            action = morseCodeDict[morseCodeDict2[actionList[0][0]]] + '的概率为' + str(actionList[0][1]) + '%\r\n'\
                   + morseCodeDict[morseCodeDict2[actionList[1][0]]] + '的概率为' + str(actionList[1][1]) + '%'
            messagebox.showinfo('操作', '%s' % action)
        else:
            actionList = process.extract(morseCodeInform, morseCodeList, limit=2)        
            action = morseCodeDict[actionList[0][0]] + '的概率为' + str(actionList[0][1]) + '%\r\n'\
                   + morseCodeDict[actionList[1][0]] + '的概率为' + str(actionList[1][1]) + '%'
            messagebox.showinfo('操作', '%s' % action)

    def morseCodeHelper(ev=None):
        messagebox.showinfo('帮助', """输入所有听到的摩斯电码，从头开始：
0代表短，1代表长；
如果输入长度在10以内（包括10），必须从头输入，匹配将从头开始；
（输入101，将匹配到3.532 MHz，因为3.532是唯一一个以长短长开头的序列）
如果输入长度在10以上，将触发模糊匹配，匹配最相近的两个串。
（输入1000001010101，将匹配到3.532 MHz，因为和正确序列1010001010101，只差第3位。）
输出两个匹配结果及匹配度，通常只需要看第一个，因为在特殊情况下第二个并不一定是次接近的，该方案可以容忍较严格的情况下某1位的错误。""")


    def name(self, event):
        nameInform = (self.nameFrame.getInput()).strip()
        stageNum = nameInform.count(' ')+1
        stageInform = nameInform.split(' ')
        if stageNum % 2:
            # 通过不断增加便于查询的别名，提高检索速度
            nameDict = {
                'v':	'左 ← 下 ↓',
                '一':	'右方 → 上方 ↑',
                '当':	'左 ← 下 ↓',
                '灯':	'左 ← 中',
                '等':	'右方 → 下 ↓',
                '瞪':	'右方 → 中',
                '东':	'左 ← 下 ↓',
                '动':	'右方 → 中',
                '好':	'右方 → 上方 ↑',
                '空':	'右方 → 中',
                '没':	'右方 → 下 ↓',
                '没有':	'左 ← 中',
                '泥':	'右方 → 下 ↓',
                '你':	'右方 → 中',
                '你们':	'右方 → 中',
                '您':	'右方 → 中',
                '您们':	'左 ← 上方 ↑',
                '稍等':	'右方 → 下 ↓',
                '是':	'左 ← 中',
                '说':	'右方 → 下 ↓',
                '他们':	'右方 → 下 ↓',
                '他们的':'左 ← 中',
                '它们的':'左 ← 下 ↓',
                '她们的':'右方 → 中',
                '西':	'右方 → 上方 ↑',
                '喜':	'右方 → 下 ↓',
                '戏':	'右方 → 下 ↓',
                '显示':	'右方 → 下 ↓'
                }
            nickNameDict = {
                'v':	'v',
                '一':	'一',
                'y':	'一',
                '当':	'当',
                'dh':	'当',
                '灯':	'灯',
                'dgh':	'灯',
                '等':	'等',
                'dg':	'等',
                '瞪':	'瞪',
                'dgo':	'瞪',
                '东':	'东',
                'dsa':	'东',
                '动':	'动',
                'ds':	'动',
                '好':	'好',
                'hc':	'好',
                '空':	'空',
                'ks':	'空',
                '没':	'没',
                'mw':	'没',
                '没有':	'没有',
                'mwyz':	'没有',
                '泥':	'泥',
                'ni':	'泥',
                '你':	'你',
                'n':	'你',
                '你们':	'你们',
                'nimf':	'你们',
                '您':	'您',
                'nb':	'您',
                '您们':	'您们',
                'nbmf':	'您们',
                '稍等':	'稍等',
                'ucdg':	'稍等',
                '是':	'是',
                'u':	'是',
                '说':	'说',
                'uo':	'说',
                '他们':	'他们',
                'tamf':	'他们',
                '他们的':'他们的',
                'tar':'他们的',
                '它们的':'它们的',
                'tab':'它们的',
                '她们的':'她们的',
                'tan':'她们的',
                '西':	'西',
                'xia':	'西',
                '喜':	'喜',
                'xiu':	'喜',
                '戏':	'戏',
                'xiy':	'戏',
                '显示':	'显示',
                'xmui':	'显示',
                }
            action = nameDict[nickNameDict[stageInform[-1]]]
            messagebox.showinfo('操作', '查看：%s的字符' % action)
        else:
            nameDict = {
                "准备": ['是', '好', '什么', '中间', '左', '按', '预备', '空', '准备'],
                "一": ['左', '好', '是', '中间', '没', '预备', '没有', '就是', '等下', '准备', '空', '什么', '按', '一'],
                "没": ['空', '就是', '等下', '一', '什么', '准备', '预备', '是', '没有', '左', '按', '好', '没'],
                "空": ['等下', '预备', '好', '中间', '空'],
                "没有": ['就是', '预备', '好', '中间', '是', '空', '没', '按', '左', '什么', '等下', '一', '没有'],
                "是": ['好', '预备', '就是', '中间', '一', '什么', '按', '准备', '没有', '是'],
                "什么": ['就是', '什么'],
                "就是": ['准备', '没有', '左', '什么', '好', '是', '预备', '没', '按', '空', '就是'],
                "左": ['预备', '左'],
                "预备": ['是', '没有', '准备', '按', '没', '等下', '什么', '预备'],
                "中间": ['空', '准备', '好', '什么', '没有', '按', '没', '等下', '左', '中间'],
                "好": ['中间', '没', '一', '是', '就是', '没有', '等下', '好'],
                "等下": ['就是', '没', '空', '好', '是', '左', '一', '按', '什么', '等下'],
                "按": ['预备', '中间', '是', '准备', '按'],
                "你": ['没问题', '泥', '您', '你的', '下一个', '行', '您的', '稍等下', '什么？', '你'],
                "泥": ['您', '下一个', '好像', '行', '什么？', '好了', '不太对', '稍等下', '你', 'Ni', '你的', '没问题', '您的', '泥'],
                "您": ['不太对', '泥', '行', '您'],
                "你的": ['你', '你的'],
                "您的": ['好了', 'Ni', '您的'],
                "Ni": ['行', '没问题', '下一个', '什么？', '你的', '您的', '不太对', '好了', 'Ni'],
                "行": ['行'],
                "不太对": ['您的', 'Ni', '泥', '你的', '下一个', '不太对'],
                "什么？": ['你', '稍等下', '你的', '您', 'Ni', '好了', '不太对', '好像', '泥', '行', '您的', '下一个', '什么？'],
                "好了": ['没问题', '行', '下一个', '什么？', '您', '您的', '你的', '稍等下', '好像', '你', 'Ni', '泥', '不太对', '好了'],
                "下一个": ['什么？', '行', '不太对', '您', '稍等下', '没问题', '下一个'],
                "稍等下": ['泥', 'Ni', '好了', '不太对', '你', '您的', '没问题', '什么？', '你的', '下一个', '稍等下'],
                "没问题": ['泥', '好了', '好像', '你的', '你', '稍等下', '行', '您的', '没问题'],
                "好像": ['你的', '下一个', 'Ni', '您的', '稍等下', '好了', '不太对', '什么？', '行', '你', '好像']
                }
            nickNameDict = {
                "准备": "准备",
                "vybw": "准备",
                "一": "一",
                "y": "一",
                "没": "没",
                "m": "没",
                "空": "空",
                "ks": "空",
                "没有": "没有",
                "mwyz": "没有",
                "是": "是",
                "u": "是",
                "什么": "什么",
                "ufme": "什么",
                "就是": "就是",
                "jqui": "就是",
                "左": "左",
                "zo": "左",
                "预备": "预备",
                "yubw": "预备",
                "中间": "中间",
                "vsjm": "中间",
                "好": "好",
                "hc": "好",
                "等下": "等下",
                "dgxx": "等下",
                "按": "按",
                "anf": "按",
                "你": "你",
                "n": "你",
                "泥": "泥",
                "ni": "泥",
                "您": "您",
                "nb": "您",
                "你的": "你的",
                "nide": "你的",
                "您的": "您的",
                "nbde": "您的",
                "Ni": "Ni",
                "行": "行",
                "xk": "行",
                "不太对": "不太对",
                "btdv": "不太对",
                "什么？": "什么？",
                "ufme？": "什么？",
                "ufme?": "什么？",
                "好了": "好了",
                "hcle": "好了",
                "下一个": "下一个",
                "xyge": "下一个",
                "稍等下": "稍等下",
                "udxx": "稍等下",
                "没问题": "没问题",
                "mwti": "没问题",
                "好像": "好像",
                "hcxl": "好像",
                }
            action = nameDict[nickNameDict[stageInform[-1]]]
            messagebox.showinfo('操作', '按顺序阅读：%s' % action)

    def nameHelper(ev=None):
        messagebox.showinfo('帮助', """输入显示的文字：
通过查看并修改源代码，可以增加编码方式，从而便于搜索。
目前通过小鹤双拼+鹤形的方式降低重码，缩短编码。
""")


    def remember(self, event):
        # 测试案例：441 442 4a4 3
        rememberInform = (self.rmbFrame.getInput()).strip()
        stageNum = rememberInform.count(' ')
        stageInform = rememberInform.split(' ')
        for i in range(0,len(stageInform)) :
            if len(stageInform[i]) == 2:
                stageInform[i] = stageInform[i]+'n'
        table = [
            ['p2','p2','p3','p4'],
            ['n4','s1p','p1','s1p'],
            ['s2n','s1n','p3','n4'],
            ['s1p','p1','s2p','s2p'],
            ['s1n','s2n','s4n','s3n']]
        def pAction(line):
            return '位置 - 点击第 %s 个位置的按钮' % line
        def nAction(num):
            return '数字 - 点击数字为 %s 的按钮' % num
        # 假设对方没有说全位置或数字信息，有些信息不知道，通过递归可以在已知信息内进行搜索。
        # 如果是和第二给阶段的位置相同，而第二个阶段位置恰好是第1个位置的按钮，那么直接输出第一个位置。
        # 最终实现了，可以按照递归搜索，并且把递归的过程展示出来的效果。
        def sAction(hint):
            s = int(hint[0])-1
            search = table[s][int(stageInform[s][0])-1]
            hintDict = {'p':1,'n':2}
            hintDict2 = {'p':'位置','n':'数字'}
            if search[0] == 'p' and 'p' == hint[1] :
                return '和第 %s 阶段%s相同的按钮 - ' % (hint[0],hintDict2[hint[1]])+'\r\n'\
                    +pAction(search[1])
            elif search[0] == 'n' and 'n' == hint[1] :
                return '和第 %s 阶段%s相同的按钮 - ' % (hint[0],hintDict2[hint[1]])+'\r\n'\
                    +nAction(search[1])
            elif search[0] == 's' and search[2] == hint[1] :
                return '和第 %s 阶段%s相同的按钮 - ' % (hint[0],hintDict2[hint[1]])+'\r\n'\
                    +sAction(search[1:3])
            else:
                g = stageInform[int(hint[0])-1][hintDict[hint[1]]]
                return '和第 %s 阶段%s相同的按钮 - \r\n可能是%s %s' % (hint[0],hintDict2[hint[1]],hintDict2[hint[1]],g)
        rmbDict = {
            'p':pAction,
            'n':nAction,
            's':sAction
            }
        hint = table[stageNum][int(stageInform[-1][0])-1]
        action = rmbDict[hint[0]](hint[1:])
        messagebox.showinfo('操作', '%s' % action)

    def rememberHelper(ev=None):
        messagebox.showinfo('帮助', """输入显示数字、点击位置和点击数字：
如果显示屏显示1，那么输入‘1’；
如果点击的是第2个位置的1，随后显示屏显示2，那么输入‘121 2’。
程序会根据之前显示的数字、点击的位置和点击的数字进行判断。
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
            action = "未定义的情况，检查输入是否正确。"
        messagebox.showinfo('操作', '%s' % action)

    def knobHelper(ev=None):
        messagebox.showinfo('帮助', """输入第一行前三个和第二行后三个：
如果提示（■ 为LED亮，□ 为LED暗）：
□ □ ■ □ □ □
□ □ □ ■ □ □
那么输入：001100""")

    def keyboard(self, ev=None): 
        self.popupImage( imageFilepath = ('images/keyboard.gif') )

    def fourcolors(self, ev=None):
        self.popupImage( imageFilepath = ('images/fourcolors.gif') )


app = KeepTalkingApp()
# 设置窗口标题:
app.master.title('保持交流就没人爆炸-辅助工具')


def center_window(w, h):
    # 获取屏幕 宽、高
    ws = app.winfo_screenwidth()
    hs = app.winfo_screenheight()
    # 计算 x, y 位置
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    app.master.geometry('%dx%d+%d+%d' % (w, h, x, y))


center_window(350, 600)
app.update()  # 必须
# 主消息循环:
app.mainloop()

# guessWord('')


# LEDStarAndLine('')