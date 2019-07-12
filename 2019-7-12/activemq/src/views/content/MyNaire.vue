<template>
  <div class="my-naire">
    <h1>二氧化碳的值为：{{co2_value}}</h1>
  </div>
</template>

<script>
import Stomp from 'stompjs';
  export default {
    data(){
      return {
        // ActiveMq数据开始
        client:null,
        topic:'/topic/111/real_time_data',
        server:'ws://127.0.0.1:61614',
        co2_value:''
        // ActiveMq数据结束
      }
    },
    created(){
      this.connection();
    },
    methods:{
      // ActiveMq逻辑开始
      connection(){
        this.client = Stomp.client(this.server);
        let headers = {
          login:'admin',
          passcode:'admin'
        };
        this.client.connect(
          headers,
          this.connect_callback,
          this.error_callback
        );
      },
      connect_callback(frame){
        console.log('the stomp is connected successfully');
        this.client.subscribe(
          this.topic,
          this.response_callback
        );
      },
      error_callback(frame){
        console.log('Fail:',frame);
      },
      response_callback(frame){
        // console.log('type:',typeof frame.body);
        let msg = JSON.parse(frame.body);
        console.log("active mq 接收到的消息为：",msg);
        this.co2_value = msg.co2.co2_value;
      }
      // ActiveMq逻辑开始
    }

  }
</script>

<style scoped>
</style>
