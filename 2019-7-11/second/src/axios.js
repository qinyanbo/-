import axios from 'axios';

// axios.defaults.baseURL = 'http://47.106.101.129:9999/';

axios.defaults.baseURL = 'http://www.brotherbo.cn:9999/';
axios.defaults.withCredentials = true;

let token = JSON.parse(sessionStorage.getItem('token'));
axios.defaults.headers.common['Authorization'] = "Token " + token;

export default axios;