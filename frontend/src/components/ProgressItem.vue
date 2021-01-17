<template>
    <span>
        <span>{{name+"  "+repeat}}</span>
        <el-button type="primary" @click="removeAction(index)">删除此项</el-button>
        <p></p>
    </span>
</template>

<script>
    export default {
        name: "ProgressItem",
        props:{
            name:String,
            repeat:Number,
            index:Number,
            removeAction:Function
        }
    }
</script>

<style scoped>

</style>