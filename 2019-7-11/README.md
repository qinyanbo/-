### 前端权限验证和把控

- 登录成功后设置：
```
let token = success.data.token;
axios.defaults.headers.common['Authorization'] = "Token " + token;
sessionStorage.setItem('token',JSON.stringify(token));
```
- axios.js中设置：
```
axios.defaults.withCredentials = true;
let token = JSON.parse(sessionStorage.getItem('token'));
axios.defaults.headers.common['Authorization'] = "Token " + token;
```