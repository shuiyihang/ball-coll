
import tkinter as tk
from queue import Queue
import random
import time
circle_buff = Queue(maxsize=0)

class spirit(object):
    def __init__(self,x=280,y=480,r=30,speed_x=2,speed_y=2):
        self.x=x
        self.y=y
        self.r=r
        self.speed_x=speed_x
        self.speed_y=speed_y




def draw_line(start_x,start_y,end_x,end_y,color):
    PlayArea.create_line(start_x,start_y,end_x,end_y,fill=color)
    PlayArea.grid()
    PlayArea.update()

def draw_circle(x,y,r,color):
    PlayArea.create_oval(x-r,y-r,x+r,y+r)
    PlayArea.grid()
    PlayArea.update()


def draw_clear():
    PlayArea.create_rectangle(0,0,720,720,fill="white")
    PlayArea.grid()

def hit_wall_detect(instance):
    instance.x+=instance.speed_x
    if (instance.x+instance.r)>=720 or (instance.x-instance.r)<=0:
        if (instance.x+instance.r)>=720:
            instance.x=720-instance.r
        else:
            instance.x=instance.r
        instance.speed_x=-instance.speed_x

    instance.y+=instance.speed_y
    if (instance.y+instance.r)>=720 or (instance.y-instance.r)<=0:

        if (instance.y+instance.r)>=720:
            instance.y=720-instance.r
        else:
            instance.y=instance.r
        instance.speed_y=-instance.speed_y
def coll_speed(body1,body2):
    print("before<%d,%d>,m1:%d,<%d,%d>,m2:%d"%(body1.speed_x,body1.speed_y,body1.r,body2.speed_x,body2.speed_y,body2.r))
    temp_value1 = ((body1.r-body2.r)*body1.speed_x + 2*body2.r*body2.speed_x)//(body1.r+body2.r)
    temp_value2 = ((body1.r-body2.r)*body1.speed_y + 2*body2.r*body2.speed_y)//(body1.r+body2.r)
    temp_value3 = ((body2.r-body1.r)*body2.speed_x + 2*body1.r*body1.speed_x)//(body1.r+body2.r)
    temp_value4 = ((body2.r-body1.r)*body2.speed_y + 2*body1.r*body1.speed_y)//(body1.r+body2.r)
    body1.speed_x = temp_value1
    body1.speed_y = temp_value2
    body2.speed_x = temp_value3
    body2.speed_y = temp_value4
    print("after:<%d,%d>,<%d,%d>"%(body1.speed_x,body1.speed_y,body2.speed_x,body2.speed_y))

def hit_body_detect(body1,body2):

    delta_x=abs((body1.x+body1.speed_x)-(body2.x+body2.speed_x))
    delta_y=abs((body1.y+body1.speed_y)-(body2.y+body2.speed_y))
    if (delta_x**2+delta_y**2)<(body1.r+body2.r+80)**2:
        draw_line(body1.x,body1.y,body2.x,body2.y,"red")
    if (delta_x**2+delta_y**2)<=((body1.r+body2.r)**2):#碰撞了
        print("coll!!")
        coll_speed(body1,body2)
        
        
        
        

def rand_init_speed(ins_zero):
    ins_zero.speed_x=5-random.randint(0,11)
    ins_zero.speed_y=5-random.randint(0,11)
    ins_zero.r=random.randint(10,50)

if __name__=="__main__":
    win=tk.Tk()
    win.geometry("720x720")
    win.title("showUI")
    PlayArea=tk.Canvas(win,width=720,height=720,bg="white")


    
    ins_one = spirit(x=210,y=480)
    ins_two = spirit(x=480,y=590,r=40)
    ins_three = spirit(x=420,y=500,r=40)
    ins_four = spirit(x=330,y=590,r=40)
    ins_five = spirit(x=110,y=330,r=40)

    ins_six = spirit(x=0,y=280)
    ins_seven = spirit(x=480,y=90)
    ins_eight = spirit(x=180,y=500)
    ins_nine = spirit(x=330,y=90)
    ins_ten = spirit(x=100,y=330)
    
    rand_init_speed(ins_one)
    rand_init_speed(ins_two)
    rand_init_speed(ins_three)
    rand_init_speed(ins_four)
    rand_init_speed(ins_five)

    rand_init_speed(ins_six)
    rand_init_speed(ins_seven)
    rand_init_speed(ins_eight)
    rand_init_speed(ins_nine)
    rand_init_speed(ins_ten)

    spirit_list=[ins_one,ins_two,ins_three,ins_four,ins_five,ins_six,ins_seven,ins_eight,ins_nine,ins_ten]#ins_three,ins_four,ins_five,ins_six,ins_seven,ins_eight,ins_nine,ins_ten
    cnt=0
    while 1:
        for i in spirit_list:
            hit_wall_detect(i)

        PlayArea.delete("all")

        for i in spirit_list:
            draw_circle(i.x,i.y,i.r,"red")
        
        

        if cnt>20:
            for i in range(len(spirit_list)):
                for j in range(i+1,len(spirit_list)):
                    hit_body_detect(spirit_list[i],spirit_list[j])
        else:
            cnt+=1
        time.sleep(0.02)
    



    

    win.mainloop()






