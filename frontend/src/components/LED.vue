<template>
    <span>
        <el-color-picker v-model="realColor"></el-color-picker>
        <p>led{{indexNum}}</p>
    </span>


</template>

<script>
    import {setled,getled} from "../api/api";

    export default {
        name: "LED",
        props:{
            indexNum:Number,
        },
        data:function () {
            return {
                realColor:"#000000",
                redNum:0,
                greenNum:0,
                blueNum:0
            }
        },
        created: function () {
            // `this` 指向 vm 实例
            const timer = setInterval(() =>{
                var a=getled(this.indexNum).then(res=>{
                    let red=Number(res.data.red).toString(16);
                    let green=Number(res.data.green).toString(16);
                    let blue=Number(res.data.blue).toString(16);
                    if(red.length==1)red="0"+red;
                    else if(red.length==0)red="00";
                    if(green.length==1)green="0"+green;
                    else if(green.length==0)green="00";
                    if(blue.length==1)blue="0"+blue;
                    else if(blue.length==0)blue="00";
                    let result="#"+red+green+blue;
                    if(result!==this.realColor){
                        this.realColor=result;
                    }
                    // console.log(red+"  "+green+"  "+blue+"  "+this.iindexNum)
                })
            }, 1000);
// 通过$once来监听定时器，在beforeDestroy钩子可以被清除。
            this.$once('hook:beforeDestroy', () => {
                clearInterval(timer);
            })
        },
        watch:{
            realColor:function(){
                this.redNum=parseInt(this.realColor.substr(1,2),16)
                this.greenNum=parseInt(this.realColor.substr(3,2),16)
                this.blueNum=parseInt(this.realColor.substr(5,2),16)
                setled(this.indexNum,this.redNum,this.greenNum,this.blueNum)
                console.log(this.realColor)
            }
        }
    }

</script>

<style scoped>

</style>