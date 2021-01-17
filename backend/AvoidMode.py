from carFacility import Wheels, IR_SENSOR
import time

ir_sensor=IR_SENSOR.ir_sensor
wheel=Wheels.wheels

isStop=False
isWorking=False
leftTurning=True
rightTurning=True

def startAvoid():
    global isStop,isWorking,leftTurning,rightTurning
    wheel.start(10,10)
    isWorking=True
    while isWorking:
        if not ir_sensor.safeBefore():
            safeState = ir_sensor.getUnsafeSide()
            print(safeState)
            if safeState == "BOTH" or safeState=="RIGHT":
                wheel.steer_by_side("LEFT")
                time.sleep(0.2)
                wheel.resume_forward("RIGHT")
            elif safeState=="LEFT":
                wheel.steer_by_side("RIGHT")
                time.sleep(0.2)
                wheel.resume_forward("LEFT")
        else:
            wheel.start(10, 10)
            wheel.resume_forward("LEFT")
            wheel.resume_forward("RIGHT")
    wheel.stop()

if __name__ == '__main__':
    startAvoid()
