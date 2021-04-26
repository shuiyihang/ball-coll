
import tkinter as tk
from queue import Queue
import random
import time
circle_buff = Queue(maxsize=0)

class spirit(object):
    def __init__(self,x=280,y=480,r=30,dir_x=1,dir_y=1,speed_x=2,speed_y=2):
        self.x=x
        self.y=y
        self.r=r
        self.dir_x=dir_x
        self.dir_y=dir_y
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
    instance.x+=(instance.dir_x*instance.speed_x)
    if (instance.x+instance.r)>=720 or (instance.x-instance.r)<=0:
        if (instance.x+instance.r)>=720:
            instance.x=720-instance.r
        else:
            instance.x=instance.r
        instance.dir_x=-instance.dir_x

    instance.y+=(instance.dir_y*instance.speed_y)
    if (instance.y+instance.r)>=720 or (instance.y-instance.r)<=0:

        if (instance.y+instance.r)>=720:
            instance.y=720-instance.r
        else:
            instance.y=instance.r
        instance.dir_y=-instance.dir_y
def coll_speed(body1,body2):
    body1.speed_x = ((body1.r-body2.r)*body1.speed_x + 2*body2.r*body2.speed_x)/(body1.r+body2.r)
    body1.speed_y = ((body1.r-body2.r)*body1.speed_y + 2*body2.r*body2.speed_y)/(body1.r+body2.r)
    body2.speed_x = ((body2.r-body1.r)*body2.speed_x + 2*body1.r*body1.speed_x)/(body1.r+body2.r)
    body2.speed_y = ((body2.r-body1.r)*body2.speed_y + 2*body1.r*body1.speed_y)/(body1.r+body2.r)

def hit_body_detect(body1,body2):

    delta_x=abs((body1.x+(body1.dir_x*body1.speed_x))-(body2.x+(body2.dir_x*body2.speed_x)))
    delta_y=abs((body1.y+(body1.dir_y*body1.speed_y))-(body2.y+(body2.dir_y*body2.speed_y)))
    if (delta_x**2+delta_y**2)<(body1.r+body2.r+80)**2:
        draw_line(body1.x,body1.y,body2.x,body2.y,"red")
    if (delta_x**2+delta_y**2)<=((body1.r+body2.r)**2):#碰撞了
        
        # 怎么做能让他不穿透呢???
        if body1.dir_x !=body2.dir_x:
            if body1.dir_y != body2.dir_y:#x,y方向都不相同

                body1.dir_x=-body1.dir_x
                body1.dir_y=-body1.dir_y
                body2.dir_x=-body2.dir_x
                body2.dir_y=-body2.dir_y
            else:#  x方向不同，y方向相同
                if body1.dir_y>0:#此时都是向下走的
                    if body1.y<body2.y:#说明是body1撞了body2,那么对body1做方向取反
                        #需要对被撞球做一个速度合成，改变x方向，改变x,y速度
                        if body2.speed_x<body1.speed_x:
                            body2.dir_x=-body2.dir_x#方向取反
                        #     body2.speed_x=body1.speed_x-body2.speed_x
                        # else:
                        #     body2.speed_x-=body1.speed_x

                        #碰撞之后没速度了
                        # if body2.speed_x==0:
                        #     body2.speed_x=1
                        # body2.speed_y=body1.speed_y#######被撞球的速度分量获取撞他的速度

                        body1.dir_x=-body1.dir_x
                        body1.dir_y=-body1.dir_y
                    else:#body2撞了test_spirt
                        if body1.speed_x<body2.speed_x:
                            body1.dir_x=-body1.dir_x#方向取反
                        #     body1.speed_x=body2.speed_x-body1.speed_x
                        # else:
                        #     body1.speed_x-=body2.speed_x
                        #碰撞之后没速度了
                        # if body1.speed_x==0:
                        #     body1.speed_x=1
                        # body1.speed_y=body2.speed_y

                        body2.dir_x=-body2.dir_x
                        body2.dir_y=-body2.dir_y
                else:#都是向上走的
                    if body1.y<body2.y:#body2撞了test
                        if body1.speed_x<body2.speed_x:#判断一下x方向的分量
                            body1.dir_x=-body1.dir_x
                        #     body1.speed_x=body2.speed_x-body1.speed_x
                        # else:
                        #     body1.speed_x-=body2.speed_x
                        #碰撞之后没速度了
                        # if body1.speed_x==0:
                        #     body1.speed_x=1
                        # body1.speed_y=body2.speed_y

                        body2.dir_x=-body2.dir_x
                        body2.dir_y=-body2.dir_y
                    else:
                        if body2.speed_x<body1.speed_x:
                            body2.dir_x=-body2.dir_x#方向取反
                        #     body2.speed_x=body1.speed_x-body2.speed_x
                        # else:
                        #     body2.speed_x-=body1.speed_x
                        #碰撞之后没速度了
                        # if body2.speed_x==0:
                        #     body2.speed_x=1
                        # body2.speed_y=body1.speed_y#######被撞球的速度分量获取撞他的速度

                        body1.dir_x=-body1.dir_x
                        body1.dir_y=-body1.dir_y


        elif body1.dir_y != body2.dir_y:#x方向相同，y方向不同

            if body1.dir_x>0:#都是向右走
                if body1.x<body2.x:#说明是body1撞了body2,那么对body1做方向取反
                    #需要对被撞球做一个速度合成，改变x方向，改变x,y速度
                    if body2.speed_y<body1.speed_y:
                        body2.dir_y=-body2.dir_y#方向取反
                    #     body2.speed_y=body1.speed_y-body2.speed_y
                    # else:
                    #     body2.speed_y-=body1.speed_y
                    
                    #碰撞之后没速度了
                    # if body2.speed_y==0:
                    #     body2.speed_y=1
                    # body2.speed_x=body1.speed_x#######被撞球的速度分量获取撞他的速度

                    body1.dir_x=-body1.dir_x
                    body1.dir_y=-body1.dir_y
                else:#body2撞了test_spirt
                    if body1.speed_y<body2.speed_y:#判断一下x方向的分量
                        body1.dir_y=-body1.dir_y
                    #     body1.speed_y=body2.speed_y-body1.speed_y
                    # else:
                    #     body1.speed_y-=body2.speed_y
                    #碰撞之后没速度了
                    # if body1.speed_y==0:
                    #     body1.speed_y=1
                    # body1.speed_x=body2.speed_x

                    body2.dir_x=-body2.dir_x
                    body2.dir_y=-body2.dir_y
            else:#都是向左走
                if body1.x<body2.x:#body2撞了test
                    if body1.speed_y<body2.speed_y:#判断一下x方向的分量
                        body1.dir_y=-body1.dir_y
                    #     body1.speed_y=body2.speed_y-body1.speed_y
                    # else:
                    #     body1.speed_y-=body2.speed_y
                    #碰撞之后没速度了
                    # if body1.speed_y==0:
                    #     body1.speed_y=1
                    # body1.speed_x=body2.speed_x

                    body2.dir_x=-body2.dir_x
                    body2.dir_y=-body2.dir_y
                else:#test撞了body2
                    if body2.speed_y<body1.speed_y:
                        body2.dir_y=-body2.dir_y#方向取反
                    #     body2.speed_y=body1.speed_y-body2.speed_y
                    # else:
                    #     body2.speed_y-=body1.speed_y
                    #碰撞之后没速度了
                    # if body2.speed_y==0:
                    #     body2.speed_y=1
                    # body2.speed_x=body1.speed_x#######被撞球的速度分量获取撞他的速度

                    body1.dir_x=-body1.dir_x
                    body1.dir_y=-body1.dir_y


        else:#方向都是相同的
            if body1.dir_y>0:
                if body1.y>body2.y:#body2撞了test
                    body2.dir_x=-body2.dir_x
                    body2.dir_y=-body2.dir_y
                    # if body1.speed_x<body2.speed_x:
                    #     body1.speed_x=body2.speed_x
                    # if body1.speed_y<body2.speed_y:
                    #     body1.speed_y=body2.speed_y
                else:
                    body1.dir_x=-body1.dir_x
                    body1.dir_y=-body1.dir_y

                    # if body2.speed_x<body1.speed_x:
                    #     body2.speed_x=body1.speed_x
                    # if body2.speed_y<body1.speed_y:
                    #     body2.speed_y=body1.speed_y
            else:
                if body1.y>body2.y:#test撞了body2
                    body1.dir_x=-body1.dir_x
                    body1.dir_y=-body1.dir_y

                    # if body2.speed_x<body1.speed_x:
                    #     body2.speed_x=body1.speed_x
                    # if body2.speed_y<body1.speed_y:
                    #     body2.speed_y=body1.speed_y

                else:#body2撞了test
                    body2.dir_x=-body2.dir_x
                    body2.dir_y=-body2.dir_y
                    # if body1.speed_x<body2.speed_x:
                    #     body1.speed_x=body2.speed_x
                    # if body1.speed_y<body2.speed_y:
                    #     body1.speed_y=body2.speed_y
        coll_speed(body1,body2)

def rand_init_speed(ins_zero):
    ins_zero.speed_x=random.randint(1,5)
    ins_zero.speed_y=random.randint(1,5)
    ins_zero.r=random.randint(10,20)

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

    spirit_list=[ins_one,ins_two,ins_three,ins_four,ins_five,ins_six,ins_seven,ins_eight,ins_nine,ins_ten]#ins_three,ins_four,ins_five
    cnt=0
    while 1:
        for i in spirit_list:
            hit_wall_detect(i)

        PlayArea.delete("all")

        for i in spirit_list:
            draw_circle(i.x,i.y,i.r,"red")
        
        

        if cnt>10:
            for i in range(len(spirit_list)):
                for j in range(i+1,len(spirit_list)):
                    hit_body_detect(spirit_list[i],spirit_list[j])
        else:
            cnt+=1
        time.sleep(0.02)
    

    

    # for i in range(6):
    #     _new_k=random.randint(0,90)
    #     _new_r=random.randint(0,20)
    #     _new_dir=random.randint(0,2)
    #     circle_buff.put(spirit(k=_new_k,r=_new_r,dir=_new_dir))

    # while not circle_buff.empty():

    #     temp_spirit=circle_buff.get()

        
    #     if temp_spirit.dir==0:
    #         spirit.x+=1
    #     else:
    #         spirit-=1
    #     if sp





    #     if spirit.x>720 or spirit<0:


    

    win.mainloop()






