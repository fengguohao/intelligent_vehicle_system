from carFacility import Buzzer, IR_remote, IR_SENSOR, LED, DistanceDetector,Wheels,servo
import AutoDetectMode,time
"""
yfang@nju.edu.cn
提交作业邮箱
"""
dis_detect = DistanceDetector.DistanceDetector
ir_sensor= IR_SENSOR.ir_sensor
buzzer= Buzzer.buzzer
led= LED.led
wheel = Wheels.wheels
ir_remote= IR_remote.ir_remote
servo=servo.servo
ir_remote.readKey()
inAutoDetectMode=False
inRunning=False
inDirRunning=False
mode="成功启动"
def start_auto_detect_call():
    global mode
    inAutoDetectMode=True
    AutoDetectMode.start_auto_detect(10)
    mode="寻迹模式"

def stop_auto_detect_call():
    global inAutoDetectMode,mode
    inAutoDetectMode=False
    AutoDetectMode.stop_auto_detect()
    mode = "成功启动"

def runCar():
    global inRunning,inAutoDetectMode,mode
    if inAutoDetectMode:
        stop_auto_detect_call()
    wheel.start(50,50)
    inRunning=True
    mode = "前进模式"

def stopCar():
    global inRunning,inAutoDetectMode,mode
    if inAutoDetectMode:
        print("car is finding its way, it will stop now")
        stop_auto_detect_call()
        mode = "成功启动"
        return
    if inRunning:
        inRunning=False
        wheel.stop()
        mode = "成功启动"
    else:
        print("the car is not running")

def changeDir(dir,speed):
    global inRunning,inAutoDetectMode,inDirRunning
    if inRunning or inAutoDetectMode or inDirRunning:
        return "sorry its working"
    else :
        inDirRunning=True
        wheel.stop()
        wheel.resume_forward("LEFT")
        wheel.resume_forward("RIGHT")
        if dir=="LEFT":
            wheel.start(speed, speed)
            wheel.steer_by_side("RIGHT")
            print(wheel.wheel_info)
            time.sleep(0.2)
            wheel.resume_forward("RIGHT")
        elif dir=="RIGHT":
            wheel.start(speed, speed)
            wheel.steer_by_side("LEFT")
            print(wheel.wheel_info)
            time.sleep(0.2)
            wheel.resume_forward("LEFT")
        elif dir=="FORWARD":
            wheel.start(speed,speed)
            print(wheel.wheel_info)
            time.sleep(0.2)
        elif dir=="BACKWARD":
            wheel.start(speed, speed)
            wheel.steer_by_side("LEFT")
            wheel.steer_by_side("RIGHT")
            print(wheel.wheel_info)
            time.sleep(0.2)
            wheel.resume_forward("LEFT")
            wheel.resume_forward("RIGHT")
        wheel.stop()
        inDirRunning=False
        return "success"

ir_remote.bind_function("0c",led.randomColor)
ir_remote.bind_function("18",start_auto_detect_call)
ir_remote.bind_function("5e",stop_auto_detect_call)
ir_remote.bind_function("08",led.lightOff)
ir_remote.bind_function("1c",runCar)
ir_remote.bind_function("5a",stopCar)

