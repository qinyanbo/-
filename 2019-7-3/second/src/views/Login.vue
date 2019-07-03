<template>
  <div class="login-wrapper">
    <div class="login-form"></div>
    <div class="login-logo"></div>
  </div>
</template>

<script>
export default {
  data() {
    return {};
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
