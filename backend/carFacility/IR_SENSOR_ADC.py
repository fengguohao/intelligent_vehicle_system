"""
精度1024 约为5mV
"""
import RPi.GPIO as GPIO
import time
import threading
CS = 5
CLOCK = 25
ADDRESS = 24
DATAOUT = 23
DIFF= -120
GPIO.setmode(GPIO.BCM)
GPIO.setup((CS,CLOCK,ADDRESS),GPIO.OUT)
GPIO.setup(DATAOUT,GPIO.IN,GPIO.PUD_UP)
class IR_SENSOR_ADC(object):
    value=[0]*6
    working = False
    def AnalogRead(self):
        val=[0]*6
        for j in range(6):
            GPIO.output(CS,GPIO.LOW)
            for i in range(10):
                if i < 4:
                    bit = (((j)>>(3-i)) & 0x01)
                    GPIO.output(ADDRESS,bit)
                val[j]<<=1
                val[j]|=GPIO.input(DATAOUT)
                GPIO.output(CLOCK, GPIO.HIGH)
                GPIO.output(CLOCK,GPIO.LOW)
            GPIO.output(CS,GPIO.HIGH)
            time.sleep(0.0001)
        average = (val[1]+val[2]+val[3]+val[4]+val[5])/5
        for i in range(1,6):
            val[i]=val[i]-average
        self.value=val.copy()

    def check_analog(self):
        while True:
            if self.working:
                self.AnalogRead()


    """
    调用此方法启动检测
    """
    def start_update(self):
        self.working = True


    def stop_update(self):
        self.working = False

    def check_distance(self,port):
        return self.value[port]

    """
    LEFT:小车向左偏离线路
    RIGHT:小车向右偏离线路
    NORMAL:正常运行
    """
    def check_side(self):
        if self.check_distance(3)>DIFF:
            if self.check_distance(1)>DIFF and self.check_distance(2)>DIFF:
                if self.check_distance(4)<DIFF or self.check_distance(5)<DIFF:
                    return "LEFT"
                elif self.check_distance(4)>DIFF or self.check_distance(5)>DIFF:
                    return "ABNORMAL"
            else:
                if self.check_distance(4)>DIFF and self.check_distance(5)>DIFF:
                    return "RIGHT"
                else:
                    return "ABNORMAL"
        else:
            return "NORMAL"

    def __init__(self):
        self.t = threading.Thread(target=self.check_analog, args=())
        self.t.start()

ir_seneor_adc = IR_SENSOR_ADC()