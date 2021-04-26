# 一个场景，鼠标点击创建起点和终点
# 根据鼠标点击点记录位置
# 用于测试bresenham算法



#布雷森汉姆算法
#用于计算机图形学中，显示器由像素构成这个特性来设计的算法，来实现绘制图形的近似

import tkinter as tk
import tkinter.messagebox
import copy


class pos(object):
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y

start=pos(0,0)
end=pos(0,0)
point=pos(0,0)

win=tk.Tk()
click_type=tk.IntVar()


#通过event形参来获取对应事件描述
def callback(event): 
    choose=click_type.get()
    global start,end,point
    if choose:
        x=event.x//24
        y=event.y//24
        print("callback:(%d,%d),choose:%d" %(x,y,choose))
        if choose==10:#绘制起点
            start.x=x
            start.y=y
            PlayArea.create_rectangle(x*24,y*24,(x+1)*24,(y+1)*24,fill="green",outline="black")
            PlayArea.grid()
        elif choose==20:#绘制终点
            end.x=x
            end.y=y
            PlayArea.create_rectangle(x*24,y*24,(x+1)*24,(y+1)*24,fill="red",outline="black")
            PlayArea.grid()
        elif choose==40:
            point.x=x
            point.y=y
            PlayArea.create_rectangle(x*24,y*24,(x+1)*24,(y+1)*24,fill="purple",outline="black")
            PlayArea.grid()

    else:
        tk.messagebox.showinfo(title="提示",message="请先选择类型")
        return
    print("===start:(%d,%d)" %(start.x,start.y))
    print("===end:(%d,%d)" %(end.x,end.y))




def draw_line():
    global start,end
    start_save=copy.copy(start)
    end_save=copy.copy(end)

    steep=abs(end.y-start.y)-abs(end.x-start.x)
    if steep>0:#陡的交换坐标系,>45
        start.x,start.y=start.y,start.x
        end.x,end.y=end.y,end.x
    if start.x>end.x:#180角度
        start,end=end,start
    if end.y < start.y:
        step_y=-1
    else:
        step_y=1



    deltay=abs(end.y-start.y)
    delatax=end.x-start.x
    k=2*deltay
    temp=k
    current=start
    middle=delatax
    while current.x<=end.x:

        if steep>0:
            PlayArea.create_rectangle(current.y*24,current.x*24,(current.y+1)*24,(current.x+1)*24,fill="white",outline="black")
        else:
            PlayArea.create_rectangle(current.x*24,current.y*24,(current.x+1)*24,(current.y+1)*24,fill="white",outline="black")
        PlayArea.grid()

        current.x+=1
        middle-=k
        if middle<=0:
            current.y+=step_y
            middle+=(2*delatax)

    start=start_save
    end=end_save
    # print("save__start:(%d,%d)" %(start.x,start.y))
    # print("save__end:(%d,%d)" %(end.x,end.y))


def draw_circle():
    global point
    radius=int(input_value.get())
    
    x=0
    y=radius
    d=1-radius
    ddf_x=1
    ddf_y=-2*radius

    PlayArea.create_rectangle((point.x+x)*24,(point.y+y)*24,(point.x+x+1)*24,(point.y+y+1)*24,fill="green",outline="black")
    PlayArea.create_rectangle((point.x+x)*24,(point.y-y)*24,(point.x+x+1)*24,(point.y-y+1)*24,fill="green",outline="black")
    PlayArea.create_rectangle((point.x+y)*24,(point.y+x)*24,(point.x+y+1)*24,(point.y+x+1)*24,fill="green",outline="black")
    PlayArea.create_rectangle((point.x-y)*24,(point.y+x)*24,(point.x-y+1)*24,(point.y+x+1)*24,fill="green",outline="black")
    PlayArea.grid()

    while x<y:
        if d>=0:
            y-=1
            ddf_y+=2
            d+=ddf_y
        x+=1
        ddf_x+=2
        d+=ddf_x

        PlayArea.create_rectangle((point.x+x)*24,(point.y+y)*24,(point.x+x+1)*24,(point.y+y+1)*24,fill="green",outline="black")
        PlayArea.create_rectangle((point.x-x)*24,(point.y+y)*24,(point.x-x+1)*24,(point.y+y+1)*24,fill="green",outline="black")
        PlayArea.create_rectangle((point.x+x)*24,(point.y-y)*24,(point.x+x+1)*24,(point.y-y+1)*24,fill="green",outline="black")
        PlayArea.create_rectangle((point.x-x)*24,(point.y-y)*24,(point.x-x+1)*24,(point.y-y+1)*24,fill="green",outline="black")

        PlayArea.create_rectangle((point.x+y)*24,(point.y+x)*24,(point.x+y+1)*24,(point.y+x+1)*24,fill="green",outline="black")
        PlayArea.create_rectangle((point.x-y)*24,(point.y+x)*24,(point.x-y+1)*24,(point.y+x+1)*24,fill="green",outline="black")
        PlayArea.create_rectangle((point.x+y)*24,(point.y-x)*24,(point.x+y+1)*24,(point.y-x+1)*24,fill="green",outline="black")
        PlayArea.create_rectangle((point.x-y)*24,(point.y-x)*24,(point.x-y+1)*24,(point.y-x+1)*24,fill="green",outline="black")
        PlayArea.grid()
    


def clear():
    for y in range(20):
        for x in range(20):
            PlayArea.create_rectangle(x*24,y*24,(x+1)*24,(y+1)*24,fill="gray",outline="black")
            PlayArea.grid()
    









win.geometry("720x480")
win.title("bresenham")

can_frame = tk.Frame(win,bg='blue',width=480,height=480)
can_frame.grid()

PlayArea=tk.Canvas(can_frame,width=480,height=480,bg="white")

PlayArea.bind("<Button-1>",callback)


for y in range(20):
    for x in range(20):
        PlayArea.create_rectangle(x*24,y*24,(x+1)*24,(y+1)*24,fill="gray",outline="black")
        PlayArea.grid()


maze_size_low=tk.Radiobutton(win,text="起点",variable=click_type,value=10)
maze_size_low.place(x=600,y=180)
maze_size_middle=tk.Radiobutton(win,text="终点",variable=click_type,value=20)
maze_size_middle.place(x=600,y=210)
maze_size_high=tk.Radiobutton(win,text="圆心",variable=click_type,value=40)
maze_size_high.place(x=600,y=240)
create_line_bt=tk.Button(win,text="画直线",command=draw_line,width=10,height=1)
create_line_bt.place(x=600,y=320)


create_circle_bt=tk.Button(win,text="清屏",command=clear,width=10,height=1)
create_circle_bt.place(x=600,y=120)

input_value=tk.Entry(win,text="半径")
input_value.place(x=600,y=370,width=80)
create_circle_bt=tk.Button(win,text="画圆",command=draw_circle,width=10,height=1)
create_circle_bt.place(x=600,y=400)

win.mainloop()
