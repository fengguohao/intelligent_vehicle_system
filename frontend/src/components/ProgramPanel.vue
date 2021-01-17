<template>
    <span>
        <el-row :gutter=20>
            <el-col :span=10>
                <p>已编程列表&emsp13;&emsp13;&emsp13;&emsp13;<el-button @click="deleteAll" :disabled="executing" type="danger">全部删除</el-button></p>
                <el-table :data="progress">
                    <el-table-column prop="name" label="执行任务名"></el-table-column>
                    <el-table-column prop="repeat" label="重复次数"></el-table-column>
                    <el-table-column
                            fixed="right"
                            label="删除"
                            width="120">
                      <template slot-scope="scope">
                        <el-button
                                @click="remove(scope.$index)"
                                type="text"
                                size="small">
                          移除
                        </el-button>
                      </template>
                    </el-table-column>
                </el-table>
                <el-button type="primary" @click="onExecute" :disabled="executing">开始执行</el-button>
            </el-col>
            <el-col :span=10>
                <p>在此处添加任务</p>
                <el-form ref="form" :model="form" label-width="80px">
                    <el-form-item label="任务名称">
                        <el-select v-model="form.name" placeholder="请选择要执行的任务">
                          <el-option label="左转" value="LEFT"></el-option>
                          <el-option label="右转" value="RIGHT"></el-option>
                          <el-option label="向前" value="FORWARD"></el-option>
                          <el-option label="向后" value="BACKWARD"></el-option>
                          <el-option label="鸣笛" value="BUZZER"></el-option>
                          <el-option label="随机亮灯（仅可选1次）" value="LIGHTON"></el-option>
                          <el-option label="关灯（仅可选1次）" value="LIGHTOFF"></el-option>
                            <el-option label="休眠0.2s" value="SLEEP"></el-option>
                        </el-select>
                    </el-form-item>
                  <el-form-item label="重复次数">
                    <el-input type="age" v-model.number="form.repeat" autocomplete="off"></el-input>
                  </el-form-item>
                  <el-form-item>
                    <el-button type="primary" @click="onSubmit" :disabled="executing">添加</el-button>
                    <el-button>取消</el-button>
                  </el-form-item>
                </el-form>
            </el-col>
        </el-row>

    </span>


</template>

<script>
    import ProgressItem from "./ProgressItem";
    import {programRun} from "../api/api";

    export default {
        name: "ProgramPanel",
        components:{
            ProgressItem
        },
        data:function () {
            return {
                progress:[{name:"LEFT",repeat:1},{name:"FORWARD",repeat:3}],
                form:{
                    name:"",
                    repeat:0
                },
                executing:false
            }
        },
        methods:{
            remove(index){
                this.progress.splice(index,1);
            },
            onSubmit(){
                if(this.form.name!=""&&this.form.repeat>0){
                    this.progress.push({name:this.form.name,repeat:this.form.repeat})
                    this.form.name="";
                    this.form.repeat=0;
                }
            },
            onExecute(){
                if(this.progress.length>0){
                    this.executing=true;
                    programRun({data:this.progress}).then(res=>{
                        if(res.data=="success"){
                            this.executing=false;
                        }
                    })
                }
            },
            deleteAll(){
                this.progress=[]
            }
        }
    }
</script>

<style scoped>

</style>