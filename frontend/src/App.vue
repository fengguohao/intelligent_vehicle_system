<template>

    <div id="app">
        <el-row :gutter="5">
            <el-col :span="14">
                <el-row :gutter="10">
                    <el-col :span="10">
                        <LEDPanel style="width: 100%"></LEDPanel>
                    </el-col>
                    <el-col :span="10">
                        <Buzzer style="width: 100%"></Buzzer>
                        <p>自动寻迹开关</p>
                        <AutoDetectCtrl></AutoDetectCtrl>
                        <p>行车控制面板</p>
                        <CarDirPanel></CarDirPanel>
                    </el-col>
                </el-row>
                <el-row :gutter="10">
                    <el-col :span="15">
                        <p></p>
                        <Video style="width: 100%"></Video>
                    </el-col>
                </el-row>
            </el-col>
            <el-col :span="6">
                当前状态：{{nowMode}}
                <KeyPanel></KeyPanel>
                <p>本系统现已经实现的功能</p>
                <p>1.LED远程管理</p>
                <p>2.远程鸣笛</p>
                <p>3.摄像头查看及控制</p>
                <p>4.寻迹</p>
                <p>5.简单避障</p>
                <p>6.运行可编程</p>
                <p>感谢您的体验</p>
            </el-col>
        </el-row>
        <br/><br/><br/>
        <ProgramPanel></ProgramPanel>
    </div>
</template>
<script>
    import LEDPanel from "./components/LEDPanel";
    import Buzzer from "./components/Buzzer";
    import Video from "./components/Video";
    import KeyPanel from "./components/KeyPanel";
    import CarDirPanel from "./components/CarDirPanel";
    import ProgramPanel from "./components/ProgramPanel";
    import {getStatus} from "./api/api";
    import AutoDetectCtrl from "./components/AutoDetectCtrl";

    export default {
        name: 'app',
        components: {
            AutoDetectCtrl,
            LEDPanel,
            Buzzer,
            Video,
            KeyPanel,
            CarDirPanel,
            ProgramPanel
        },
        data: function () {
            return {
                nowMode: "",
                keyMap: ""
            }
        },
        methods: {
            timeToGetStatus() {
                getStatus().then(res => {
                    this.nowMode = res.data
                });
            },
        },
        created: function () {
            // `this` 指向 vm 实例
            const timer = setInterval(() => {
                this.timeToGetStatus();
            }, 1000);
// 通过$once来监听定时器，在beforeDestroy钩子可以被清除。
            this.$once('hook:beforeDestroy', () => {
                clearInterval(timer);
            })
        },
    }


</script>

<style>
    #app {
        font-family: 'Avenir', Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        color: #2c3e50;
        margin-top: 60px;
    }
</style>
