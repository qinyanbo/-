<template>
  <div id="app">
    <!-- <img alt="Vue logo" src="./assets/logo.png"> -->
    <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
    <p :title="message1" :class="{colorStyle:isStatus,'text-danger':isDangerStatus}">{{message1}}</p>
    <!-- <p>{{msg}}</p>
    <span>啦啦啦2</span>
    <span>啦啦啦3</span>
    <p v-if="seen">{{message1}}</p>
    <ul>
      <li v-for="item,index in todos" :key="index" >{{item}}</li>
    </ul>
    <button @click="handleClick">反转</button>
    <input type="text" v-model="message1">
    <ol>
      <TodoItem v-for="item,index in todos" :key="index" :name="item"></TodoItem>
    </ol>
    <p>{{count+1}}</p> -->
    <!-- 'seen' 'not seen' 'not very seen' -->
    <!-- <p>{{seen?'seen':'not seen'}}</p>
    <p>{{see == '1'?'seen':(see == '2'?'not seen':'not very seen')}}</p> -->

    <!-- <p>{{reverseMessage}}</p> -->
    <!-- <p>{{reverseString(message1)}}</p> -->
    <p>{{user}}</p>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import TodoItem from '@/components/TodoItem.vue'
export default {
  name: 'app',
  components: {
    HelloWorld,
    TodoItem
  },
  data(){
    return {
      message1:'我是一条小青龙！',
      msg:'啦啦啦',
      seen:false,
      todos:[
        'a','b','c'
      ],
      count:0,
      see:'1', //'1','2','3' 
      user:{
        firstName:'yb',
        lastName:'Qin'
      },
      isStatus:false,
      isDangerStatus:false

    }
    
  },

  watch:{
    user(){
      console.log('user is modified');
      this.handleClick();
    },
    'user.firstName':function () {
      this.handleClick();
    }

  },
  // computed:{
  //   reverseMessage(){
  //     return this.message1 = this.message1.split('').reverse().join('');
  //   },
  //   reverseString(){
  //     return function (string) {
  //       return string.split('').reverse().join('');
  //     }
  //   }
  // },
  methods:{
    handleClick(){
      this.message1 = this.message1.split('').reverse().join('');
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
.colorStyle{
  color: red;
}
.text-danger{
  font-size: 30px;
}
</style>
