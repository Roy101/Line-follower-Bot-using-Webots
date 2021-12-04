from controller import Robot

robot = Robot()
timestep = 64
max_speed=6.28

lm= robot.getMotor("left_motor")
rm= robot.getMotor("right_motor")

lm.setPosition(float('inf'))
lm.setVelocity(0.0)
rm.setPosition(float('inf'))
rm.setVelocity(0.0)

#IR=robot.getDistanceSensor("IR_1")
#IR.enable(timestep)
sensors=[]
names=["IR_1","IR_2","IR_3","IR_4","IR_5","IR_6","IR_7","IR_8"]
panel=[0,0,0,0,0,0,0,0]

for i in range (0,8):
    sensors.append(robot.getDistanceSensor(names[i]))
    sensors[i].enable(timestep)

while (robot.step(timestep) != -1):
    lm.setVelocity(6.28*0.5)
    rm.setVelocity(6.28*0.3)
    
    #k=IR.getValue();
    #print(k)
    for i in range(0,8):
        panel[i]=sensors[i].getValue()
    print(panel)
    pass