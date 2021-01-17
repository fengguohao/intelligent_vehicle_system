from carFacility import Wheels, IR_SENSOR_ADC
import time, threading,random

wheels = Wheels.wheels
ir_sensor_adc = IR_SENSOR_ADC.ir_seneor_adc
ir_sensor_adc.start_update()
update_duty = 0.0005
speed=25

"""
start mode:向前运动
"""
isLeft = False
isRight = False
isForward = True
isWorking = False
countTime=0
lastTime=0

def auto_detect_progress():
    global isForward, isRight, isLeft,isWorking,countTime,lastTime
    print("working")
    while isWorking:
        a = ir_sensor_adc.check_side()
        if a == "NORMAL":
            countTime=0
            if not isForward:
                isForward = True
                wheels.start(speed, speed)
            if isRight:
                isRight = False
                wheels.resume_forward("LEFT")
                wheels.start(speed, speed)
            if isLeft:
                isLeft = False
                wheels.resume_forward("RIGHT")
                wheels.start(speed, speed)
        elif a == "RIGHT":
            wheels.steer_by_side("LEFT")
            isRight = True
        elif a == "LEFT":
            wheels.steer_by_side("RIGHT")
            isLeft = True
        else:
            # wheels.stop()
            # isForward = False
            countTime+=1
            print(countTime)
            if isRight:
                isRight = False
                wheels.resume_forward("LEFT")
                wheels.start(speed, speed)
            if isLeft:
                isLeft = False
                wheels.resume_forward("RIGHT")
                wheels.start(speed, speed)
            if countTime<=10:
                # 无法寻路后的调整策略
                if lastTime==1:
                    wheels.steer_by_side("RIGHT")
                    isLeft = True
                    lastTime=0
                    time.sleep(countTime * 0.003)
                else:
                    wheels.steer_by_side("LEFT")
                    isRight = True
                    lastTime=1
                    time.sleep(countTime * 0.003)
            elif countTime<=500:
                if random.random()>0.5:
                    wheels.steer_by_side("RIGHT")
                    isLeft = True
                    time.sleep(countTime*0.005)
                else:
                    wheels.steer_by_side("LEFT")
                    isRight = True
                    time.sleep(countTime * 0.005)
            else:
                wheels.stop()
        time.sleep(update_duty)
    print("thread was stopped")


def start_auto_detect(start_speed):
    global isLeft, isRight, isForward, isWorking
    if not isWorking:
        isLeft = False
        isRight = False
        isForward = True
        ir_sensor_adc.start_update()
        wheels.setDirection("FORWARD")
        wheels.start(start_speed, start_speed)
        isWorking = True
        threading.Thread(target=auto_detect_progress, args=()).start()
        print("the auto_detect progress was start at ", time.time())

def stop_auto_detect():
    global isLeft, isRight, isForward, isWorking
    if isWorking:
        isLeft = False
        isRight = False
        isForward = True
        isWorking = False
        wheels.stop()
        print("the auto_detect progress was stop at ", time.time())

if __name__ == '__main__':
    start_auto_detect(speed)