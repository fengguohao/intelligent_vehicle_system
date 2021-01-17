import RPi.GPIO as GPIO
class IR_SENSOR(object):
    IR_SENSOR_R = 19
    IR_SENSOR_L = 16
    def __init__(self):
        GPIO.setup(self.IR_SENSOR_L, GPIO.IN)
        GPIO.setup(self.IR_SENSOR_R, GPIO.IN)

    """
    检测前方是否有障碍物
    side:"LEFT","RIGHT",表示选择读取的传感器侧
    """
    def detect(self,side):
        if side=="LEFT":
            return GPIO.input(self.IR_SENSOR_L)
        elif side=="RIGHT":
            return GPIO.input(self.IR_SENSOR_R)


    """
    检测前方是否安全
    """
    def safeBefore(self):
        if self.detect("LEFT")==0 or self.detect("LEFT")==0:
            return False
        else:
            return True

    def getUnsafeSide(self):
        if self.detect("LEFT") == 0 and self.detect("RIGHT") == 0:
            return "BOTH"
        elif self.detect("LEFT")==0:
            return "LEFT"
        elif self.detect("RIGHT")==0:
            return "RIGHT"

ir_sensor = IR_SENSOR()