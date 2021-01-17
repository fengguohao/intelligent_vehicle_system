<template>
<!--    key_mapper={"45":"CH-","46":"CH","47":"CH+","44":"|<<","40":">>|","43":">||",
            "07":"-","15":"+","09":"EQ","16":"0","19":"100+","0d":"200+",
            "0c":"1","18":"2","5e":"3","08":"4","1c":"5","5a":"6","42":"7","52":"8","4a":"9"}-->
    <span>
        <p>遥控器方法列表：总方法数{{keyMap.length}}</p>
        <p>正与车端实时同步</p>
        <el-table
                :data="keyMap"
                style="width: 100%">
        <el-table-column
                prop="key"
                label="key"
                width="180">
        </el-table-column>
        <el-table-column
                prop="method"
                label="method"
                width="180">
        </el-table-column>
    </el-table>
    </span>

</template>

<script>
    import {keyBind} from "../api/api";

    export default {
        name: "KeyPanel",
        data:function () {
            return{
                keyMap:[]
            }
        },
        methods:{
            timeToGetKeyMap(){
                keyBind().then(res=>{
                    this.keyMap=new Array();
                    for(var i in res.data.keys){
                        this.keyMap.push(res.data.keys[i])
                    }
                });
            }
        },
        created: function () {
            // `this` 指向 vm 实例
            const timer = setInterval(() =>{
                this.timeToGetKeyMap();
            }, 1000);
            // 通过$once来监听定时器，在beforeDestroy钩子可以被清除。
            this.$once('hook:beforeDestroy', () => {
                clearInterval(timer);
            })
        },
    }
</script>

<style scoped>

</style>