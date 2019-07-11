<template>
  <div class="user-manage">
    <Button type="primary">新增用户</Button>
    <Table border ref="selection" :columns="columns4" :data="users">
      <template slot-scope="{ row, index }" slot="action">
        <Button type="primary" size="small" style="margin-right: 5px" @click="show(index)">View</Button>
        <Button type="error" size="small" @click="remove(row)">Delete</Button>
      </template>
    </Table>
  </div>
</template>

<script>
import axios from "@/axios.js";
export default {
  data() {
    return {
      users: [],
      columns4: [
        {
          type: "selection",
          width: 60,
          align: "center"
        },
        {
          title: "ID",
          key: "id"
        },
        {
          title: "学号",
          key: "u_number"
        },
        {
          title: "姓名",
          key: "u_name"
        },
        {
          title: "性别",
          key: "u_sex"
        },
        {
          title: "出生日期",
          key: "u_birthday"
        },
        {
          title: "QQ号",
          key: "u_identity"
        },
        {
          title: "Action",
          slot: "action",
          width: 150,
          align: "center"
        }
      ]
    };
  },
  created() {
    this.getUsers();
  },
  methods:{
    show(index){

    },
    remove(index){
      console.log(index.id);
      axios.delete("qn/Users",{data:{id:index.id+''}})
      .then(success => {
        console.log('删除成功');
        this.getUsers();
      })
      .catch(error => {
      })
      .finally(final => {
      });
    },
    getUsers(){
      axios
      .get("qn/Users")
      .then(success => {
        console.log(success.data.data);
        this.users = success.data.data;
      })
      .catch(error => {
        console.log(error);
      })
      .finally(final => {
        console.log("finally");
        console.log(final);
      });
    }
  }
};
</script>

<style scoped>
.user-manage {
  margin: 5px;
}
</style>
