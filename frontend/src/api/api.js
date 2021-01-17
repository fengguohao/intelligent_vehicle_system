import request from "@/utils/requests"

//const loginURL="/api/user/login";
// export function login(data) {
//     return request({
//         url:loginURL,
//         method:'post',
//         data
//     })
// }
const buzzerURL="/buzzer";
export function buzzer() {
    return request({
        url:buzzerURL,
        method:'get',
    })
}

const setledURL="/setLed";
export function setled(index,red,green,blue) {
    return request({
        url:setledURL+"?index="+index+"&red="+red+"&green="+green+"&blue="+blue,
        method:'get',
    })
}

const getledURL="/ledInfo";
export function getled(index) {
    return request({
        url:getledURL+"?index="+index,
        method:'get',
    })
}

const setSevro="/setSevro";
export function sevro(side,speed) {
    return request({
        url:setSevro+"?side="+side+"&speed="+speed,
        method:'get',
    })
}

const Status="/status";
export function getStatus() {
    return request({
        url:Status,
        method:'get',
    })
}

const keyList="/keyBind";
export function keyBind() {
    return request({
        url:keyList,
        method:'get',
    })
}

const dirCtrl="/runCar";
export function setDirCtrl(dir,speed) {
    return request({
        url:dirCtrl+"?dir="+dir+"&speed="+speed,
        method:'get',
    })
}

const start="/startAutoDetect";
export function startAutoDetect() {
    return request({
        url:start,
        method:'get',
    })
}

const stop="/stopAutoDetect";
export function stopAutoDetect(dir,speed) {
    return request({
        url:stop,
        method:'get',
    })
}


const programRunStr="/programRun";
export function programRun(data) {
    return request({
        url:programRunStr,
        method:'post',
        data
    })
}