<template>
    <el-switch
            v-model="inAutoDetect"
            active-text="开始寻迹"
            inactive-text="停止寻迹">
    </el-switch>
</template>

<script>
    import {startAutoDetect,stopAutoDetect} from "../api/api";

    export default {
        name: "AutoDetectCtrl",
        data() {
            return {
                inAutoDetect: false,
            }
        },
        watch:{
            inAutoDetect(){
                if(this.inAutoDetect==true){
                    startAutoDetect().then(res=>{
                        console.log(res.data)
                        if(res.data=="True"){
                            this.inAutoDetect=true;
                        }
                        else{
                            this.inAutoDetect=false;
                        }
                    })
                }else{
                    stopAutoDetect().then(res=>{
                        console.log(res.data)
                        if(res.data=="True"){
                            this.inAutoDetect=true;
                        }
                        else{
                            this.inAutoDetect=false;
                        }
                    })
                }
            }
        }
    }
</script>

<style scoped>

</style>