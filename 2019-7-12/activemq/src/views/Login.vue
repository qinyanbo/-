<template>
  <div class="login-wrapper">
    <div class="login-form">
      <h3 class="title">微型问卷系统后台管理</h3>
      <Form :rules="userRuleValidate" class="form-area" :model="userInfo" label-position="top">
        <FormItem label="用户名" prop="username">
          <Input v-model="userInfo.username"></Input>
        </FormItem>
        <FormItem label="密码" prop="password">
          <Input type="password" v-model="userInfo.password" @keyup.enter.native="login"></Input>
        </FormItem>
      </Form>
      <Button style="width:100%;margin-bottom:24px;" type="primary" @click="login">立即登录</Button>
    </div>
    <div class="login-logo"></div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      userInfo: {
        username: "",
        password: ""
      },
      userRuleValidate: {
        username: [
          {
            required: true,
            message: "请输入用户名",
            trigger: "blur"
          }
        ],
        password: [
          {
            required: true,
            message: "请输入密码",
            trigger: "blur"
          }
        ]
      }
    };
  },
  methods:{
    login(){
      this.$router.push('home');
    }
  }
};
</script>

<style scoped>
.login-wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(to bottom right, #318fce 0, #48e7ef);
}
.login-wrapper .title {
  font-size: 18px;
  font-weight: 700;
  padding-bottom: 10px;
}
.login-wrapper .form-area {
  width: 300px;
}
.login-wrapper .login-form {
  background-color: #fff;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
  border-radius: 2px;
  padding: 30px 20px;
}
.login-wrapper .login-logo {
  position: absolute;
  top: 10px;
  left: 30px;
  width: 250px;
  height: 75px;
  background: url(../assets/logo.png) no-repeat 50%;
  background-size: cover;
}
</style>
