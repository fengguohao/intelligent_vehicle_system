import axios from 'axios';
const service = axios.create({
    baseURL: process.env.VUE_APP_BASE_API, // api 的 base_url
    timeout: 5000 // request timeout
})

service.interceptors.request.use(
    config => {
        return config;
    },
    err => Promise.reject(err)
)

export default service