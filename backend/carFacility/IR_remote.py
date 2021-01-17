import threading
import time
key_mapper={"45":"CH-","46":"CH","47":"CH+","44":"|<<","40":">>|","43":">||",
            "07":"-","15":"+","09":"EQ","16":"0","19":"100+","0d":"200+",
            "0c":"1","18":"2","5e":"3","08":"4","1c":"5","5a":"6","42":"7","52":"8","4a":"9"}



class IR_remote(object):
    def __init__(self):
        self.data=open('/dev/input/event0','rb')
        self.cache=None
        self.func_dirc={}
        self.cache_time=0

    def read(self):
        d=self.data.read(48)
        key=d.hex()[40:42]
        return key

    def readNoTwice(self):
        while True:
            temp=self.read()
            if temp!=None:
                temptime = time.time()
                if temptime - self.cache_time > 0.1:
                    print(temptime,self.cache_time)
                    self.cache=temp
                    print(key_mapper[temp])
                    self.cache_time=temptime
                    try:
                        if self.func_dirc[temp]!=None:
                            self.func_dirc[temp]()
                    except:
                        print("no function bind")
                    temp=None

    """
    使用此方法来启动按键读取，如果不使用，bind function将会没有作用
    """
    def readKey(self):
        try:
            threading.Thread(target=self.readNoTwice,args=()).start()
        except:
            print("fail")

    """
    为某一特定按键绑定事件
    key:按键键值，func:按键响应方法
    """
    def bind_function(self,key,func):
        self.func_dirc[key]=func

ir_remote=IR_remote()

if __name__ == '__main__':
    ir_remote.readKey()
    def print45():
        print("45 was touched")
    ir_remote.bind_function("45",print45)
    while True:
        continue
