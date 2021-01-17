import RPi.GPIO as GPIO
import time
class DistanceDetector(object):
    echo_port=27
    trig_port=22
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.trig_port,GPIO.OUT)
        GPIO.setup(self.echo_port,GPIO.IN)

    """
    返回测得前方障碍物的距离
    """
    def check_distance(self):
        sleepTime=0.000015
        GPIO.output(self.trig_port,GPIO.HIGH)
        time.sleep(sleepTime)
        GPIO.output(self.trig_port,GPIO.LOW)

        channel=GPIO.wait_for_edge(self.echo_port,
                                   GPIO.RISING,
                                   timeout=1000)

        if channel is None:
            print('Check fail at this time')
            return
        else:
            t1=time.time()
        channel=None
        channel=GPIO.wait_for_edge(self.echo_port,
                                   GPIO.FALLING,
                                   timeout=1000)
        if channel is None:
            print('Check fail at this time')
            return
        else:
            t2=time.time()

        return (t2-t1)*34000/2

distanceDetector = DistanceDetector()