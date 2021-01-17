from neopixel import *
import time
import random
class LED(object):
    LED_COUNT=4
    LED_PIN=18
    LED_FREQ_HZ=800000
    LED_DMA=10
    LED_BRIGHTNESS=255
    LED_INVERT=False
    LED_CHANNEL=0
    LED_STRIP=ws.WS2812_STRIP

    red=255
    green=0
    blue=0
    colorList={"0":{"red":0,"green":0,"blue":0},"1":{"red":0,"green":0,"blue":0},"2":{"red":0,"green":0,"blue":0},"3":{"red":0,"green":0,"blue":0},"4":{"red":0,"green":0,"blue":0}}
    strip=None

    def __init__(self):
        self.strip = Adafruit_NeoPixel(self.LED_COUNT,
                                       self.LED_PIN,
                                       self.LED_FREQ_HZ,
                                       self.LED_DMA,
                                       self.LED_INVERT,
                                       self.LED_BRIGHTNESS,
                                       self.LED_CHANNEL)
        self.strip.begin()

    def lightOn(self,index,red=255,green=0,blue=0):
        self.colorList[str(index)]["red"]=red
        self.colorList[str(index)]["green"] = green
        self.colorList[str(index)]["blue"] = blue
        self.strip.setPixelColor(index,(red<<16|green<<8|blue))
        self.strip.show()

    """
    车上LED光源随机颜色亮起
    """
    def randomColor(self):
        for i in range(0, 4):
            self.lightOn(i, int(random.random() * 255), int(random.random() * 255), int(random.random() * 255))

    def lightOff(self):
        for i in range(0,4):
            self.lightOn(i, 0,0,0)

led = LED()

if __name__ == '__main__':
    for i in range(4):
        led.strip.setPixelColor(i, (0 << 16 | 0 << 8 | 0))
        time.sleep(0.2)
        led.strip.show()
