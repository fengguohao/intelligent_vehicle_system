<template>
    <span>
        <el-button type="primary" icon="el-icon-arrow-left" @click="setSevro('LEFT',5)" circle></el-button>
        <el-button type="primary" icon="el-icon-arrow-right" @click="setSevro('RIGHT',5)" circle></el-button>
        <el-button type="primary" icon="el-icon-arrow-up" @click="setSevro('UP',5)" circle></el-button>
        <el-button type="primary" icon="el-icon-arrow-down" @click="setSevro('DOWN',5)" circle></el-button>
    </span>
</template>

<script>
    import {sevro} from "../api/api";
    export default {
        name: "ServoPanel",
        methods:{
            setSevro(side,speed){
                sevro(side,speed).then(res=>{
                    console.log(res.data)
                });
            }
        }
    }
</script>

<style scoped>

</style>