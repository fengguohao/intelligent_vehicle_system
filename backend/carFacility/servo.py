import Adafruit_PCA9685
import time
class Servo(object):
    pwm=None
    degree=[60,60]
    def __init__(self):
        self.pwm=Adafruit_PCA9685.PCA9685()
        self.pwm.set_pwm_freq(50)
        self.set_servo_angle(0,self.degree[0])
        self.set_servo_angle(1, self.degree[1])

    """
    channel:0左右旋转，1上下旋转
    """
    def set_servo_angle(self,channel,angle):
        value=4095*(angle*11+500)/20000
        print(value)
        self.pwm.set_pwm(channel,0,int(value))

    def change(self,side,speed):
        channel=1
        sign=-1
        if side=="LEFT" or side=="RIGHT":
            channel=0
        if side=="RIGHT" or side=="DOWN":
            sign=1
        changed=self.degree[channel]+sign*speed
        if (changed<100 and changed>30 and channel==0) or (changed<150 and changed>10 and channel==1):
            self.degree[channel]=changed
        self.set_servo_angle(channel,self.degree[channel])

servo=Servo()

if __name__ == '__main__':

    for angle in range(30,145):
        servo.set_servo_angle(1,angle)
        time.sleep(0.01)