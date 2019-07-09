<template>
  <div class="user-manage">
    <Button type="primary" @click="modal1 = true">新增用户</Button>
    <Table border ref="selection" :columns="columns4" :data="users">
      <template slot-scope="{ row, index }" slot="action">
        <Button type="primary" size="small" style="margin-right: 5px" @click="show(index)">View</Button>
        <Button type="error" size="small" @click="remove(row)">Delete</Button>
      </template>
    </Table>

    <!-- 弹框开始 -->
    <Modal v-model="modal1" title="添加用户" @on-ok="ok" @on-cancel="cancel">
      <Form
        ref="userFormValidate"
        :rules="userRuleValidate"
        :model="formLeft"
        label-position="left"
        :label-width="100"
      >
        <FormItem label="学号" prop="u_number">
          <Input v-model="formLeft.u_number"></Input>
        </FormItem>
        <FormItem label="姓名" prop="u_name">
          <Input v-model="formLeft.u_name"></Input>
        </FormItem>
        <FormItem label="性别" prop="u_sex">
          <!-- <Input v-model="formLeft.u_sex"></Input> -->
          <RadioGroup v-model="formLeft.u_sex">
            <Radio label="male" >男</Radio>
            <Radio label="female">女</Radio>
          </RadioGroup>
        </FormItem>
        <FormItem label="出生日期" prop="u_birthday">
          <Input v-model="formLeft.u_birthday"></Input>
        </FormItem>
        <FormItem label="QQ号" prop="u_identity">
          <Input v-model="formLeft.u_identity"></Input>
        </FormItem>
      </Form>
    </Modal>
    <!-- 弹框结束 -->
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
      ],
      modal1: false,
      formLeft: {
        u_number: "",
        u_name: "",
        u_identity: "",
        u_sex: "male",
        u_birthday: ""
      },
      userRuleValidate: {
        u_number: [
          {
            required: true,
            message: "请输入学号",
            trigger: "blur"
          }
        ],
        u_name: [
          {
            required: true,
            message: "请输入名字",
            trigger: "blur"
          }
        ],
        u_sex: [
          {
            required: true,
            message: "请输入性别",
            trigger: "blur"
          }
        ],
        u_birthday: [
          { required: true, message: "请输入生日", trigger: "blur" }
        ],
        u_identity: [
          {
            required: true,
            message: "请输入QQ号",
            trigger: "blur"
          }
        ]
      }
    };
  },
  created() {
    this.getUsers();
    this.testMethod();
  },
  methods: {
    show(index) {},
    remove(index) {
      console.log(index.id);
      axios
        .delete("qn/Users", { data: { id: index.id + "" } })
        .then(success => {
          console.log("删除成功");
          this.getUsers();
        })
        .catch(error => {})
        .finally(final => {});
    },
    getUsers() {
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
    },
    ok() {
      console.log("form:", this.formLeft);
      this.handleSubmit("userFormValidate");
    },
    cancel() {
      this.$Message.info("取消添加!");
      this.handleReset("userFormValidate");
    },
    handleSubmit(name) {
      let form = _.cloneDeep(this.formLeft);
      if(form.u_sex === 'male'){
        form.u_sex = 0;
      }else{
        form.u_sex = 1;
      }
      this.$refs[name].validate(valid => {
        if (valid) {
          axios
            .post("qn/Users", form)
            .then(success => {
              this.$Message.success("添加成功");
              this.getUsers();
            })
            .catch(error => {
              this.$Message.error("添加失败");
            })
            .finally(final => {});
        } else {
          this.$Message.error("表单校验未通过！");
          this.handleReset("userFormValidate");
        }
      });
    },
    handleReset(name) {
      this.$refs[name].resetFields();
    },
    testMethod() {
      let a = { name: "qyb", sex: "male" };
      let b = a;
      let c = _.cloneDeep(a);
      a.name = "yyb";
      console.log(a, b, c);
    }
  }
};
</script>

<style scoped>
.user-manage {
  margin: 5px;
}
</style>
