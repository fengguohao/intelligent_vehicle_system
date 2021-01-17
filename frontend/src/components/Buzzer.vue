<template>
    <el-card class="box-card">
        <div slot="header" class="clearfix">
            <span>鸣笛</span>
        </div>
        <el-button type="primary" @click="onClickBuzzer()" :disabled="notAllowClick">鸣笛</el-button>
    </el-card>
</template>

<script>
    import {buzzer} from "../api/api";

    export default {
        name: "Buzzer",
        data:function(){
            return{
                notAllowClick:false
            }
        },
        methods:{
            onClickBuzzer:function () {
                this.notAllowClick=true;
                console.log(this.notAllowClick);
                buzzer().then(res=>{}).catch(error=>{consloe.log(error)});
                setTimeout(()=>{this.notAllowClick=false;},1000);
            }
        }
    }
</script>

<style scoped>
    .clearfix:before,
    .clearfix:after {
        display: table;
        content: "";
    }
    .clearfix:after {
        clear: both
    }

    .box-card {
        width: 480px;
    }
</style>