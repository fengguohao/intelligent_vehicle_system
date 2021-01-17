<template>
    <span>
        <iframe src="http://192.168.88.1:8081" style="width: 640px;height: 480px" scrolling="no"></iframe>
        <ServoPanel></ServoPanel>
    </span>

</template>

<script>
    import ServoPanel from "./ServoPanel";
    export default {
        name: "Video",
        components:{
            ServoPanel
        }
    }
</script>

<style scoped>

</style>