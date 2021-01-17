这是嵌入式作业——智能车控制系统的后端代码，项目结构如下

```
─carFacility（基础设施层）
    │  Buzzer.py
    │  DistanceDetector.py
    │  IR_remote.py
    │  IR_SENSOR.py
    │  IR_SENSOR_ADC.py
    │  LED.py
    │  servo.py
    │  Wheels.py
    └---
     |-- AutoDetectMode.py（自动寻迹）
     |-- AvoidMode.py（避障）
     |-- Main.py（服务集成）
     |-- README.md
     |--start.sh
     |--StatusController.py（web服务）
```

您可以通过执行start.sh运行程序

您也可以将

```bash
modprobe -v i2c-bcm2835
modprobe -v i2c-dev
$PROJECT_PATH/start.sh
```

这三条代码添加到/etc/rc.d/rc.conf中来使得项目自启动

感谢您的浏览阅读

