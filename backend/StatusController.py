from flask import Flask,request
from flask_cors import *
import Main,json,time
from carFacility import IR_remote
app = Flask(__name__)

CORS(app)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/status',methods=['GET'])
def getStatus():
    return Main.mode

@app.route('/keyBind',methods=['GET'])
def getKeyList():
    keylist=Main.ir_remote.func_dirc
    ans={"keys":[]}
    for i in keylist:
        ans["keys"].append({"key":IR_remote.key_mapper[i],"method":keylist[i].__name__})
    return json.dumps(ans)

@app.route('/ledInfo',methods=['GET'])
def getColor():
    index = request.args.get("index")
    colorList=Main.led.colorList[index]
    return colorList

@app.route("/carSpeed",methods=['GET'])
def getCarSpeed():
    speedList=Main.wheel.wheel_info
    return speedList

@app.route("/buzzer",methods=['GET'])
def getBuzzer():
    Main.buzzer.doBim(1)
    return "success"

@app.route("/setLed",methods=['GET'])
def setColor():
    index=request.args.get("index")
    red = request.args.get("red")
    green = request.args.get("green")
    blue = request.args.get("blue")
    Main.led.lightOn(int(index),int(red),int(green),int(blue))
    return "success in setting led index="+index+"  color: r:"+red+"  g:"+green+"  b:"+blue

@app.route("/setSevro",methods=['GET'])
def setSevro():
    dataBefore=Main.servo.degree
    side=request.args.get("side")
    speed= request.args.get("speed")
    Main.servo.change(side,int(speed))
    dataAfter=Main.servo.degree
    return "success  "+str(dataBefore)+"  "+str(dataAfter)


@app.route("/runCar",methods=['GET'])
def runCar():
    dir=request.args.get("dir")
    speed= request.args.get("speed")
    return Main.changeDir(dir,int(speed))

@app.route("/startAutoDetect",methods=['GET'])
def start_auto():
    Main.start_auto_detect_call()
    return Main.inAutoDetectMode

@app.route("/stopAutoDetect",methods=['GET'])
def stop_auto():
    Main.stop_auto_detect_call()
    return Main.inAutoDetectMode

@app.route("/programRun",methods=['POST'])
def programRun():
    rawdata=request.data
    actions=json.loads(rawdata)
    print(actions)
    for action in actions["data"]:
        for i in range(int(action["repeat"])):
            if action["name"]=="LIGHTON":
                Main.led.randomColor()
            elif action["name"]=="LIGHTOFF":
                Main.led.lightOff()
            elif action["name"]=="BUZZER":
                Main.buzzer.doBim(1)
                time.sleep(1)
            elif action["name"]=="SLEEP":
                time.sleep(0.2)
            else:
                Main.changeDir(action["name"],20)

    return "success"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
