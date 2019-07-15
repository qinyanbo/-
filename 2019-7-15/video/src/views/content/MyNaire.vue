<template>
  <div class="my-naire">
    <div id="runtimePlayers">
      <div
        id="vxg_media_player1"
        class="vxgplayer"
        :url="url1"
        aspect-ratio
        latency="3000000"
        autostart
        controls
        avsync
      ></div>
    </div>
  </div>
</template>

<script>
import "@/assets/vxgplayer/vxgplayer-1.8.51.min.js";
export default {
  data() {
    return {
      url1: "rtsp://briup_iots:briup2018@www.briup.cn:10010",
      url2: "rtsp://briup_iots:briup2018@www.briup.cn:10020"
    };
  },
  created() {
   let flag = 1;
   
   if(!sessionStorage.getItem('flag')){
     sessionStorage.setItem('flag',JSON.stringify(flag));
   }
   if(JSON.parse(sessionStorage.getItem('flag')) == 1){
     location.reload();
     flag += 1;
     sessionStorage.setItem('flag',JSON.stringify(flag));
   }
   
   
  },
  mounted(){
    
  },
  methods: {
    
  }
};
</script>

<style scoped>
@import url("../../assets/vxgplayer/vxgplayer-1.8.51.min.css");
.my-naire {
  width: 100%;
  height: 100%;
}

</style>
