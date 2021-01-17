import RPi.GPIO as GPIO
import time,threading

class Wheels(object):
    wheel_left = {"A": 13, "B": 12, "CTRL": 6}
    wheel_right = {"A": 21, "B": 20, "CTRL": 26}
    wheel_info={"LEFT":{"speed":0,"dir":None},"RIGHT":{"speed":0,"dir":None}}
    left_pwm = None
    right_pwm = None
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup([self.wheel_left["A"],self.wheel_left["B"],self.wheel_left["CTRL"]],GPIO.OUT)
        GPIO.setup([self.wheel_right["A"], self.wheel_right["B"], self.wheel_right["CTRL"]], GPIO.OUT)
        GPIO.output((self.wheel_left["A"], self.wheel_left["B"]), (GPIO.LOW, GPIO.HIGH))
        GPIO.output((self.wheel_right["A"], self.wheel_right["B"]), (GPIO.LOW, GPIO.HIGH))
        self.left_pwm = GPIO.PWM(self.wheel_left["CTRL"], 1000)
        self.right_pwm = GPIO.PWM(self.wheel_right["CTRL"], 1000)
        # self.getInfo()

    def setDirectionBySide(self,dir,side):
        self.wheel_info[side]["dir"] = dir
        if side=="LEFT":
            if dir=="BACKWARD":
                GPIO.output((self.wheel_left["A"], self.wheel_left["B"]), (GPIO.LOW, GPIO.HIGH))
            elif dir=="FORWARD":
                GPIO.output((self.wheel_left["A"], self.wheel_left["B"]), (GPIO.HIGH, GPIO.LOW))
        elif side=="RIGHT":
            if dir == "BACKWARD":
                GPIO.output((self.wheel_right["A"], self.wheel_right["B"]), (GPIO.LOW, GPIO.HIGH))
            elif dir == "FORWARD":
                GPIO.output((self.wheel_right["A"], self.wheel_right["B"]), (GPIO.HIGH, GPIO.LOW))
    '''
    allowed args:dir=["FORWARD","BACKWARD"]
    control the direction
    '''
    def setDirection(self,dir):
        self.wheel_info["LEFT"]["dir"] = dir
        self.wheel_info["RIGHT"]["dir"] = dir
        self.setDirectionBySide(dir,"LEFT")
        self.setDirectionBySide(dir, "RIGHT")

    def setSpeed(self,dir,speed):
        self.wheel_info[dir]["speed"] = speed
        if dir=="LEFT":
            self.left_pwm.ChangeDutyCycle(speed)
        elif dir=="RIGHT":
            self.right_pwm.ChangeDutyCycle(speed)

    """
    dypercated
    """
    def steer(self,degree,baseSpeed,delta):
        slow_side=baseSpeed-abs(degree)/90*delta
        fast_side = baseSpeed + abs(degree) / 90 * delta
        if degree<0:
            self.changeSpeedBySide("LEFT",slow_side)
            self.changeSpeedBySide("RIGHT", fast_side)
        elif degree>0:
            self.changeSpeedBySide("LEFT", fast_side)
            self.changeSpeedBySide("RIGHT", slow_side)


    def steer_by_side(self,dir,speed=30):
        # self.changeSpeedBySide("LEFT", 0)
        # self.changeSpeedBySide("RIGHT", speed)
        # time.sleep(0.30*(30/speed))
        # self.run(afterspeed)
        self.wheel_info["LEFT"]["speed"] = speed
        self.wheel_info["RIGHT"]["speed"] = speed
        self.setDirectionBySide("BACKWARD",dir)
        self.changeSpeedBySide("LEFT", speed)
        self.changeSpeedBySide("RIGHT", speed)
        # time.sleep(1.15)
        # self.setDirectionBySide("FORWARD", "LEFT")
        # self.run(afterspeed)

    def resume_forward(self,dir):
        self.setDirectionBySide("FORWARD", dir)

    def left_round(self,speed=10,afterspeed=30):
        # self.changeSpeedBySide("LEFT", 0)
        # self.changeSpeedBySide("RIGHT", speed)
        # time.sleep(0.30*(30/speed))
        # self.run(afterspeed)
        self.setDirectionBySide("BACKWARD","LEFT")
        self.changeSpeedBySide("LEFT", speed)
        self.changeSpeedBySide("RIGHT", speed)


    def right_steer(self,speed):
        self.changeSpeedBySide("RIGHT", 0)
        self.changeSpeedBySide("LEFT", speed)
        time.sleep(0.30*(30/speed))
        self.run(speed)

    def changeSpeedBySide(self,side,speed):
        self.wheel_info[side]["speed"] = speed
        if side=="LEFT":
            self.left_pwm.ChangeDutyCycle(speed)
        elif side=="RIGHT":
            self.right_pwm.ChangeDutyCycle(speed)


    def startRun(self, speed , side):
        self.wheel_info[side]["speed"] = speed
        if side=="LEFT":
            self.left_pwm.start(speed)
        elif side=="RIGHT":
            self.right_pwm.start(speed)

    def run(self,speed):
        self.changeSpeedBySide("LEFT",speed)
        self.changeSpeedBySide("RIGHT", speed)

    def start(self,leftSpeed=50,rightSpeed=50):
        self.setDirection("FORWARD")
        self.startRun(leftSpeed,"LEFT")
        self.startRun(rightSpeed,"RIGHT")

    def stopRun(self,side):
        self.wheel_info[side]["speed"] = 0
        if side=="LEFT":
            self.left_pwm.stop()
        elif side=="RIGHT":
            self.right_pwm.stop()

    def stop(self):
        self.stopRun("LEFT")
        self.stopRun("RIGHT")

    def getDetails(self):
        while True:
            print(self.wheel_info)
            time.sleep(0.1)

    def getInfo(self):
        threading.Thread(target=self.getDetails,args=()).start()


wheels = Wheels()




