<template>
  <div class="home">
    <Layout style="height:100%">
      <Sider breakpoint="md" collapsible :collapsed-width="78" v-model="isCollapsed">
        <div class="home-title">微型问卷系统</div>
        <Menu :active-name="activeName" theme="dark" width="auto" :class="menuitemClasses">
          <MenuItem
            v-for="item,index in menus"
            :key="index"
            :name="item.to"
            @click.native="handleExchangeMenu(item.to)"
          >
            <Icon :type="item.icon"></Icon>
            <span>{{item.name}}</span>
          </MenuItem>
        </Menu>
        <div slot="trigger"></div>
      </Sider>
      <Layout>
        <Header class="layout-header-bar">
          <span style="float:right;">
            <a @click="logout" href="javascript:void(0);">注销 admin</a>
          </span>
        </Header>
        <Content :style="{margin: '10px', background: '#fff', minHeight: '220px'}">
          <router-view />
        </Content>
        <div class="copyright">2009-2019 © Timuwork</div>
      </Layout>
    </Layout>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from "@/components/HelloWorld.vue";

export default {
  name: "home",
  components: {
    HelloWorld
  },
  data() {
    return {
      isCollapsed: false,
      menus: [
        { name: "我的问卷", to: "myNaire", icon: "ios-paper" },
        { name: "新建问卷", to: "createNewNaire", icon: "md-create" },
        { name: "用户管理", to: "userManage", icon: "ios-person" },
        { name: "系统管理", to: "systemManage", icon: "ios-analytics" }
      ],
      activeName: ""
    };
  },
  mounted() {
    if (this.$route.name === "home") {
      this.activeName = "myNaire";
      this.$router.push({ name: this.activeName });
    } else {
      this.activeName = this.$route.name;
    }
  },
  computed: {
    menuitemClasses: function() {
      return ["menu-item", this.isCollapsed ? "collapsed-menu" : ""];
    }
  },
  methods: {
    handleExchangeMenu(to) {
      this.$router.push({ name: to });
    },
    logout() {
      this.$router.push({ name: "login" });
    }
  }
};
</script>

<style scoped>
.home {
  height: 100%;
  /* border: 1px solid #d7dde4; */
  background: #f5f7f9;
  position: relative;
  /* border-radius: 4px; */
  overflow: hidden;
}
.home-title {
  height: 64px;
  text-align: center;
  font-size: 24px;
  color: #fff;
  line-height: 64px;
}
.layout-header-bar {
  background: #fff;
  box-shadow: 0 1px 1px rgba(0, 0, 0, 0.1);
}
.menu-item span {
  display: inline-block;
  overflow: hidden;
  width: 69px;
  text-overflow: ellipsis;
  white-space: nowrap;
  vertical-align: bottom;
  transition: width 0.2s ease 0.2s;
}
.menu-item i {
  transform: translateX(0px);
  transition: font-size 0.2s ease, transform 0.2s ease;
  vertical-align: middle;
  font-size: 16px;
}
.collapsed-menu span {
  width: 0px;
  transition: width 0.2s ease;
}
.collapsed-menu i {
  transform: translateX(5px);
  transition: font-size 0.2s ease 0.2s, transform 0.2s ease 0.2s;
  vertical-align: middle;
  font-size: 22px;
}
.copyright {
  text-align: center;
  padding: 0 0 15px;
  color: #9ea7b4;
}
</style>
