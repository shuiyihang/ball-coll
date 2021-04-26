class pos:
    x,y
start=pos(0,0)
end=pos(0,0)


比较缓和的曲线<45
start.x<end.x

k=delaty/delatx
middle=0.5
step_deltay=k

cur=start

while cur.x!=end.x:
    draw_pixel()
    cur.x+=1
    if step_deltay>middle:
        cur.y+=1
        middle+=1
    step_deltay+=k
    



#改良：同时 2*delatx
k=2*delaty
middle=deltax
step_deltay=k
while cur.x!=end.x:
    draw_pixel()
    cur.x+=1
    middle-=step_deltay
    if middle<0:
        cur.y+=1
        middle+=(2*delatax)
    














k=2*delaty
middle=deltax
step_deltay=k
while cur.x!=end.x:
    draw_pixel()
    cur.x+=1
    middle=middle-step_deltay
    if middle-step_deltay<0:
        cur.y+=1
        middle+=2*delatax
    step_deltay+=k







画圆的

先只考虑1/8圆
F(x,y)=x^2+y^2-R^2=1.25-R=>1.25-R-0.25=1-R
F(a,b)<0 说明这个点是在圆内的
F(a,b)>0 在圆外




x=0
y=radius
d=1-radius


#
if d<0:
    d=d+2*x+3
else:
    d=d+2*(x-y)+5   #d=d+2*x+3-2*(y-1)
    y-=1
x+=1

#改良版
if d>=0:
    d=d-2(y-1)
    y-=1
d=d+2*x+3
x+=1
##再变
if d>=0:
    y-=1
    d=d-2*y
d=d+2*x+3
x+=1
###做改变
ddF_y =-2*radius
ddF_x=1

if d>=0:
    y-=1
    ddF_y+=2
    d=d+ddF_y
x+=1
ddF_x+=2
d=d+ddF_x






