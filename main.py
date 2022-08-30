import os
import tkinter as tk
from tkinter import filedialog


# datain = '/Users/handyzhang/Documents/windows/Euroscope/vatprc/2207/PrfOfPRC-main/data/All/Sectoredit/ZSHA.txt'
# dataout = '/Users/handyzhang/Documents/windows/Euroscope/vatprc/2207/PrfOfPRC-main/data/All/Sectoredit/ZSHAchange.txt'
# change = "SECTORLINE:L_ZSSSAR03"
# changeto = ":test:"

# 获取文件路径
def get_path():
    filetypes = [("ese配置文件", "*.ese")]
    file_path = filedialog.askopenfilename(title='选择单个文件', filetypes=filetypes)
    print(file_path)
    textbar.insert('end', '已选择目标路径：' + file_path + '\n')
    textbar.see(end)
    path_var.set(file_path)
    global datain
    datain = file_path
    pathout(datain)


# 输出文件路径处理
def pathout(datain):
    print(datain)
    global dataout
    dataout2 = datain
    str_list = list(dataout2)
    nPos = str_list.index('.')
    str_list.insert(nPos, 'change')
    dataout = ''.join(str_list)
    print(dataout)
    textbar.insert('end', '已生成输出路径：' + dataout + '\n')
    textbar.see(end)


# 按下start处理文本信息
def start():
    global change
    change = 'SECTORLINE:L_' + var_change.get()
    print(change)
    textbar.insert('end', '已生成关键词：' + change + '\n')
    textbar.see(end)
    global changeto
    changeto = ':' + var_changeto.get() + ':'
    print(changeto)
    textbar.insert('end', '已生成插入词：' + changeto + '\n')
    textbar.see(end)
    changestart()


# 替换执行
def changestart():
    textbar.insert('end', '开始执行\n')
    textbar.see(end)
    count = -1
    countchange = 0
    textbar.see(end)
    for count, linecount in enumerate(open(datain, 'r')):
        pass
    count += 1
    f = open(datain, 'r')
    line = f.readline()
    num = 1
    while num <= count:
        if change in line:
            print(line)
            textbar.insert('end', '找到关键词：' + line + '\n')
            textbar.see(end)
            while 1:
                if "OWNER" in line:
                    print(line)
                    textbar.insert('end', '原：' + line + '\n')
                    textbar.see(end)
                    u1, u2 = line.split(':', 1)
                    print(u1)
                    print(u2)
                    line = line.replace(line, u1 + changeto + u2)
                    f_w = open(dataout, 'a')
                    f_w.write(line)
                    f_w.close()
                    print(line)
                    textbar.insert('end', '改：' + line + '\n')
                    textbar.see(end)
                    num = num + 1
                    countchange = countchange + 1
                    textbar.see(end)
                    break
                else:
                    f_w = open(dataout, 'a')
                    f_w.write(line)
                    f_w.close()
                    num = num + 1
                line = f.readline()
        else:
            f_w = open(dataout, 'a')
            f_w.write(line)
            f_w.close()
            num = num + 1
        line = f.readline()

    f.close()
    os.remove(datain)
    os.rename(dataout, datain)
    textbar.insert('end', '已完成' + str(count) + '行扫描，共更改' + str(countchange) + '行数据\n')
    textbar.see(end)


# 初始化图形界面
end = 10000.0
window = tk.Tk()
window.title('ese编辑器')
window.geometry('500x400')
# 欢迎使用
l = tk.Label(window, text="你好，欢迎使用", font=('Arial', 16), width=30, height=2)
l.pack()
# 提示信息
tk.Label(window, text="请选择txt文件", font=('Arial', 14)).place(x=10, y=80)
tk.Label(window, text='涉及扇区编号', font=('Arial', 14)).place(x=10, y=120)
tk.Label(window, text='example: ZSSSAR03', font=('Arial', 10)).place(x=300, y=120)
tk.Label(window, text='新增扇区缩写', font=('Arial', 14)).place(x=10, y=160)
tk.Label(window, text='example: STC', font=('Arial', 10)).place(x=300, y=160)
# 路径显示框
path_var = tk.StringVar()
entry = tk.Entry(window, textvariable=path_var, font=('Arial', 14))
entry.place(x=120, y=80, anchor='nw')
# 路径选择按钮
tk.Button(window, text='...', command=get_path).place(x=300, y=80, anchor='nw')
# 涉及扇区编号
var_change = tk.StringVar()
entry_change = tk.Entry(window, textvariable=var_change, font=('Arial', 14))
entry_change.place(x=120, y=120)
# 新增扇区缩写
var_changeto = tk.StringVar()
entry_changeto = tk.Entry(window, textvariable=var_changeto, font=('Arial', 14))
entry_changeto.place(x=120, y=160)
# start按钮
btn_start = tk.Button(window, text='Start!', command=start)
btn_start.place(x=120, y=200)
# 运行状态更新
textbar = tk.Text(window, height=6, width=59, font=('Arial', 10))
textbar.place(x=10, y=250, anchor='nw')
# 页面loop显示
window.mainloop()
