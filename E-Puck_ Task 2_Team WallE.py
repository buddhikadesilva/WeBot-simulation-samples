
from controller import Robot, DistanceSensor, Motor

def run_robot(robot):
    time_step=32
    max_speed=5
    left_speed=0
    right_speed=0
    
    isNeedRotate= 0;
    isNeedToPark=0;
    stopMotors=0;
    countFoward=0;
    speedLevel=1.2;
    
    left_motor = robot.getDevice('left wheel motor')
    right_motor = robot.getDevice('right wheel motor')
    left_motor.setPosition(float('inf'))
    right_motor.setPosition(float('inf'))
    left_motor.setVelocity(0.0)
    right_motor.setVelocity(0.0)
    
    left_ir = robot.getDevice('gs0')
    left_ir.enable(time_step)
    
    middle_ir = robot.getDevice('gs1')
    middle_ir.enable(time_step)
    
    right_ir = robot.getDevice('gs2')
    right_ir.enable(time_step) 
    
    while robot.step(time_step) != -1:
    
        left_ir_value = left_ir.getValue()
        middle_ir_value = middle_ir.getValue()
        right_ir_value = right_ir.getValue()
        
        print('left: {} middle: {} right: {}'.format(left_ir_value,middle_ir_value,right_ir_value))
        
        if(isNeedRotate==1):
            left_speed = 5
            right_speed = -5
            if(left_ir_value<400 and middle_ir_value<400 and right_ir_value<400):
                print('0 1 0')
                left_speed = 0
                right_speed = 0
                isNeedRotate=0
                stopMotors=1
        elif(isNeedToPark==1):
            left_speed =-5
            right_speed=5
            countFoward=countFoward+1
            if (countFoward>50):
                left_speed =5
                right_speed=5
                if (countFoward>60):                
                    left_speed =-6
                    right_speed=6
                    stopMotors=1
            
        else:
            if((left_ir_value>800 and left_ir_value<820)  and (middle_ir_value>800 and middle_ir_value<820) and (right_ir_value>800 and right_ir_value<820)):
                print('0 0 0 - dead-end')
                # isNeedRotate=1
                isNeedToPark=1
                
            if((left_ir_value>820 and middle_ir_value>820 and right_ir_value>820)):
                print('0 0 0')
                left_speed = 3
                right_speed = -3
                countFoward=0
                
            if(left_ir_value<400 and middle_ir_value<400 and right_ir_value<400):
                print('1 1 1')
                countFoward=countFoward+1
                if(countFoward>50):
                    isNeedToPark=1
                    countFoward=0
                    stopMotors=1
                else:
                    left_speed = 2
                    right_speed = 0  
                
            if(left_ir_value>820 and middle_ir_value<400 and right_ir_value>820):
                print('0 1 0')
                left_speed = 6
                right_speed = 6
                countFoward=0
                
                
            if(left_ir_value<400 and middle_ir_value<400 and right_ir_value>820):
                print('1 1 0')
                left_speed = -6
                right_speed = 6
                countFoward=0
                
            if(left_ir_value>820 and middle_ir_value<400 and right_ir_value<400):
                print('0 1 1')
                left_speed = 5
                right_speed = 0
                countFoward=0
                
            if(left_ir_value<400 and middle_ir_value>820 and right_ir_value>820):
                print('1 0 0')
                left_speed = -6
                right_speed = 6
                countFoward=0
                
            if(left_ir_value>820 and middle_ir_value>820 and right_ir_value<400):
                print('0 0 1')
                left_speed = 5
                right_speed = 0
                countFoward=0
            
        if(stopMotors==1):       
            left_motor.setVelocity(0)
            right_motor.setVelocity(0)
        else:
            left_motor.setVelocity(left_speed)
            right_motor.setVelocity(right_speed)            
    

if __name__ == '__main__':
    my_robot = Robot()
    run_robot(my_robot)