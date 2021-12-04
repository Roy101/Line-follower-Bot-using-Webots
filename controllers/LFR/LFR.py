from controller import Robot

robot = Robot()
timestep = 32

lm=robot.getMotor("left_motor")
rm=robot.getMotor("right_motor")

lm.setPosition(float('inf'))
lm.setVelocity(0.0)

rm.setPosition(float('inf'))
rm.setVelocity(0.0)

sensors=[]
names=["IR_1","IR_2","IR_3","IR_4","IR_5","IR_6","IR_7","IR_8"]
reading=[0,0,0,0,0,0,0,0]

previous_error=0.0
kp=1
kd=0.5 
ki=0.0
Integral=0.0

for i in range (0,8):
    sensors.append(robot.getDistanceSensor(names[i]))
    sensors[i].enable(timestep)
def getReading():
    for i in range (0,8):
        if int(sensors[i].getValue())>512:
            reading[i]=0
        else:
            reading[i]=1
def PID():
    error=0
    coefficient=[-4000,-3000,-2000,-1000,1000,2000,3000,4000]
 
    for i in range(0,8):
        error+=coefficient[i]*reading[i]
    P=kp*error
    I=Integral+(ki*error)
    D=kd*(error-previous_error)    
    correction=(P+I+D)/1000
    l_speed=10+correction
    r_speed=10-correction   
   
    if l_speed<0.0  : 
        l_speed=0
    if l_speed>10.0 : 
        l_speed=10.0
    if r_speed<0.0  : 
        r_speed=0
    if r_speed>10.0 : 
        r_speed=10.0

    lm.setVelocity(l_speed)

    rm.setVelocity(r_speed)

    print(l_speed,r_speed,reading)
    return I,error

while (robot.step(timestep) != -1):
    getReading()
    print(kp, kd, ki)
    Integral,previous_error=PID()
    pass