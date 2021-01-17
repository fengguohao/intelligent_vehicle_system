<template>
    <el-card class="box-card">
        <div slot="header" class="clearfix">
            <span>LED</span>
            <el-button style="float: right; padding: 3px 0" type="text" @click="closeAll">关闭全部</el-button>
        </div>
        <el-row :gutter="20">
            <el-col :span="6"><LED :index-num="indexList[0]"></LED></el-col>
            <el-col :span="6"><LED :index-num="indexList[1]"></LED></el-col>
            <el-col :span="6"><LED :index-num="indexList[2]"></LED></el-col>
            <el-col :span="6"><LED :index-num="indexList[3]"></LED></el-col>
        </el-row>
    </el-card>
</template>

<script>
    import LED from "./LED";
    import {setled} from "../api/api";
    export default {
        name: "LEDPanel",
        components:{LED},
        data(){
            return{
                indexList:[0,1,2,3]
            }
        },
        methods:{
            closeAll(){
                for(var i=0;i<4;i++){
                    setled(i,0,0,0)
                }
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

    LED{
        width:40px;
        height:40px;
        display: inline;
    }
</style>