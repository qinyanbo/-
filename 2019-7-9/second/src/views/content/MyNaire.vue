<template>
  <div class="my-naire">
    <h1>我的问卷页面</h1>
    <div class="my-chart" ref="chart1"></div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      myChart1:{},
      option: {
        xAxis: {
          type: "category",
          data: ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        },
        yAxis: {
          type: "value"
        },
        series: [
          {
            data: [820, 932, 901, 934, 1290, 1330, 1320],
            type: "line"
          }
        ]
      }
    };
  },
  
  mounted(){
    this.setEchart();
  },
  methods: {
    //图表的绘制
    setEchart() {
      //$refs 可以减少获取dom 节点的消耗,只要在相关元素中绑定ref属性="值"的方式,
      //就可以通过this.$refs.###进行操作了
      let dom1 = this.$refs.chart1;
      this.myChart1 = this.$echarts.init(dom1);
      this.myChart1.setOption(this.option);
      // let myChart1 = this.myChart1;
      //图形自适应窗口
      window.addEventListener("resize", () => {
        // alert("窗口大小改变")
        this.myChart1.resize();
      });
    }
  }
};
</script>

<style scoped>
.my-chart {
  width: 400px;
  height: 400px;
}
</style>
