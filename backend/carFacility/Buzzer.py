import RPi.GPIO as GPIO
import _thread
import time
class Buzzer(object):
    BUZZER = 4
    BUZZER_PWM = None
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.BUZZER, GPIO.OUT)
        self.BUZZER_PWM = GPIO.PWM(self.BUZZER, 300)

    def startBuzzer(self):
        self.BUZZER_PWM.start(50)

    def setDutyCycle(self,cycle):
        self.BUZZER_PWM.ChangeDutyCycle(cycle)

    def setFreq(self,freq):
        self.BUZZER_PWM.ChangeFrequency(freq)

    def bimb(self,timeDuty):
        self.BUZZER_PWM.start(50)
        time.sleep(timeDuty)
        self.BUZZER_PWM.stop()

    """
    发出蜂鸣信号
    参数：timeDuty:蜂鸣时长，单位为秒（s）
    """
    def doBim(self,timeDuty):
        try:
            _thread.start_new_thread(self.bimb,(timeDuty,))
        except:
            print("fail")

buzzer = Buzzer()