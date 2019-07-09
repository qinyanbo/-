### 弹框利用表单提交数据

- 表单校验

### echarts在vue项目中使用:
1. 安装: cnpm i -S echarts
2. 在main.js中导入：
   import echarts from 'echarts'
   Vue.prototype.$echarts = echarts
3. 在组件中使用：
   1. 先在html页面中插入一个div
      ```
      <div class="top-body-chart1" ref="chart1"></div>
      ```
      该div必须有宽高(这样才能显示绘制的图表)
      ```
      .top-body-chart1{
        width: 300px;
        height: 300px;
      }
      ```
   2. 在js代码中准备echarts图表的图表绘制对象myChart1和图标绘制参数option，将其放在data里：
      ```
      data() {
        return {
          myChart1:{},
          option1: {
            ...
          }
        };
      },
      ```
   3. 在methods中定义绘制方法    setEchart：
      ```
      methods: {
        //图表的绘制
        setEchart() {
          //$refs 可以减少获取dom 节点的消耗,只要在相关元素中绑定ref属性="值"的方式,
          //就可以通过this.$refs.###进行操作了
          let dom1 = this.$refs.chart1;
          this.myChart1 = this.$echarts.init(dom1);
          this.myChart1.setOption(this.option1);
          // let myChart1 = this.myChart1;
          //图形自适应窗口
          window.addEventListener("resize", () => {
            // alert("窗口大小改变")
            this.myChart1.resize();
          });
        }
      }
      ```
   4. 在vue实例加载的时候绘制(在mounted方法中调用)：
      ```
      mounted() {
        this.setEchart();
      },
      ```