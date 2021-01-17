<template>
    <span>
        <el-button type="primary" icon="el-icon-arrow-left" @click="setDir('LEFT',30)" circle></el-button>
        <el-button type="primary" icon="el-icon-arrow-right" @click="setDir('RIGHT',30)" circle></el-button>
        <el-button type="primary" icon="el-icon-arrow-up" @click="setDir('FORWARD',30)" circle></el-button>
        <el-button type="primary" icon="el-icon-arrow-down" @click="setDir('BACKWARD',30)" circle></el-button>
    </span>
</template>

<script>
    import {setDirCtrl} from "../api/api";
    export default {
        name: "CarDirPanel",
        methods:{
            setDir(side,speed){
                setDirCtrl(side,speed).then(res=>{console.log(res.data)})
            }
        }
    }
</script>

<style scoped>

</style>