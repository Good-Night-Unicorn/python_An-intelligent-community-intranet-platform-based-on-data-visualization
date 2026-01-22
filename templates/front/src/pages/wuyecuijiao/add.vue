<template>
<div :style='{"width":"100%","padding":"40px 7%","margin":"0 auto","position":"relative","background":"none"}'>
    <el-form
      class="add-update-preview"
      ref="ruleForm"
      :model="ruleForm"
      :rules="rules"
      label-width="150px"
    >
          <el-form-item :style='{"padding":"10px","margin":"0 0 10px 0","alignItems":"center","background":"linear-gradient(90deg, rgba(238,177,238,1) 0%, rgba(165,228,222,1) 30%, rgba(165,228,222,1) 100%)","display":"flex"}'  label="月份" prop="yuefen">
            <el-select v-model="ruleForm.yuefen" placeholder="请选择月份"  >
              <el-option
                  v-for="(item,index) in yuefenOptions"
                  :key="index"
                  :label="item"
                  :value="item">
              </el-option>
            </el-select>
          </el-form-item>
          <el-form-item :style='{"padding":"10px","margin":"0 0 10px 0","alignItems":"center","background":"linear-gradient(90deg, rgba(238,177,238,1) 0%, rgba(165,228,222,1) 30%, rgba(165,228,222,1) 100%)","display":"flex"}' label="住户账号" prop="zhuhuzhanghao">
            <el-select  @change="zhuhuzhanghaoChange" v-model="ruleForm.zhuhuzhanghao" placeholder="请选择住户账号">
              <el-option
                  v-for="(item,index) in zhuhuzhanghaoOptions"
                  :key="index"
                  :label="item"
                  :value="item">
              </el-option>
            </el-select>
          </el-form-item>
          <el-form-item :style='{"padding":"10px","margin":"0 0 10px 0","alignItems":"center","background":"linear-gradient(90deg, rgba(238,177,238,1) 0%, rgba(165,228,222,1) 30%, rgba(165,228,222,1) 100%)","display":"flex"}' label="住户姓名" prop="zhuhuxingming">
            <el-input v-model="ruleForm.zhuhuxingming" 
                placeholder="住户姓名" clearable ></el-input>
          </el-form-item>
          <el-form-item :style='{"padding":"10px","margin":"0 0 10px 0","alignItems":"center","background":"linear-gradient(90deg, rgba(238,177,238,1) 0%, rgba(165,228,222,1) 30%, rgba(165,228,222,1) 100%)","display":"flex"}' label="楼栋号" prop="loudonghao">
            <el-input v-model="ruleForm.loudonghao" 
                placeholder="楼栋号" clearable ></el-input>
          </el-form-item>
          <el-form-item :style='{"padding":"10px","margin":"0 0 10px 0","alignItems":"center","background":"linear-gradient(90deg, rgba(238,177,238,1) 0%, rgba(165,228,222,1) 30%, rgba(165,228,222,1) 100%)","display":"flex"}' label="住址" prop="zhuzhi">
            <el-input v-model="ruleForm.zhuzhi" 
                placeholder="住址" clearable ></el-input>
          </el-form-item>
          <el-form-item :style='{"padding":"10px","margin":"0 0 10px 0","alignItems":"center","background":"linear-gradient(90deg, rgba(238,177,238,1) 0%, rgba(165,228,222,1) 30%, rgba(165,228,222,1) 100%)","display":"flex"}'  label="缴费类型" prop="jiaofeileixing">
            <el-select v-model="ruleForm.jiaofeileixing" placeholder="请选择缴费类型"  >
              <el-option
                  v-for="(item,index) in jiaofeileixingOptions"
                  :key="index"
                  :label="item"
                  :value="item">
              </el-option>
            </el-select>
          </el-form-item>
          <el-form-item :style='{"padding":"10px","margin":"0 0 10px 0","alignItems":"center","background":"linear-gradient(90deg, rgba(238,177,238,1) 0%, rgba(165,228,222,1) 30%, rgba(165,228,222,1) 100%)","display":"flex"}' label="费用" prop="feiyong">
            <el-input v-model="ruleForm.feiyong" 
                placeholder="费用" clearable ></el-input>
          </el-form-item>
          <el-form-item :style='{"padding":"10px","margin":"0 0 10px 0","alignItems":"center","background":"linear-gradient(90deg, rgba(238,177,238,1) 0%, rgba(165,228,222,1) 30%, rgba(165,228,222,1) 100%)","display":"flex"}' label="费用清单" v-if="type!='cross' || (type=='cross' && !ro.feiyongqingdan)" prop="feiyongqingdan">
            <file-upload
            tip="点击上传费用清单"
            action="file/upload"
            :limit="3"
            :multiple="true"
            :fileUrls="ruleForm.feiyongqingdan?ruleForm.feiyongqingdan:''"
            @change="feiyongqingdanUploadChange"
            ></file-upload>
          </el-form-item>
            <el-form-item :style='{"padding":"10px","margin":"0 0 10px 0","alignItems":"center","background":"linear-gradient(90deg, rgba(238,177,238,1) 0%, rgba(165,228,222,1) 30%, rgba(165,228,222,1) 100%)","display":"flex"}' class="upload" v-else label="费用清单" prop="feiyongqingdan">
                <img v-if="ruleForm.feiyongqingdan.substring(0,4)=='http'" class="upload-img" style="margin-right:20px;" v-bind:key="index" :src="ruleForm.feiyongqingdan.split(',')[0]" width="100" height="100">
                <img v-else class="upload-img" style="margin-right:20px;" v-bind:key="index" v-for="(item,index) in ruleForm.feiyongqingdan.split(',')" :src="baseUrl+item" width="100" height="100">
            </el-form-item>
          <el-form-item :style='{"padding":"10px","margin":"0 0 10px 0","alignItems":"center","background":"linear-gradient(90deg, rgba(238,177,238,1) 0%, rgba(165,228,222,1) 30%, rgba(165,228,222,1) 100%)","display":"flex"}' label="缴费时间" prop="jiaofeishijian" >
              <el-date-picker
                  value-format="yyyy-MM-dd HH:mm:ss"
                  v-model="ruleForm.jiaofeishijian" 
                  type="datetime"
                  placeholder="缴费时间">
              </el-date-picker>
          </el-form-item>
          <el-form-item :style='{"padding":"10px","margin":"0 0 10px 0","alignItems":"center","background":"linear-gradient(90deg, rgba(238,177,238,1) 0%, rgba(165,228,222,1) 30%, rgba(165,228,222,1) 100%)","display":"flex"}' label="截止时间" prop="jiezhishijian" >
              <el-date-picker
                  value-format="yyyy-MM-dd HH:mm:ss"
                  v-model="ruleForm.jiezhishijian" 
                  type="datetime"
                  placeholder="截止时间">
              </el-date-picker>
          </el-form-item>
          <el-form-item :style='{"padding":"10px","margin":"0 0 10px 0","alignItems":"center","background":"linear-gradient(90deg, rgba(238,177,238,1) 0%, rgba(165,228,222,1) 30%, rgba(165,228,222,1) 100%)","display":"flex"}' label="费用详情" prop="feiyongxiangqing">
            <el-input
              type="textarea"
              :rows="8"
              placeholder="费用详情"
              v-model="ruleForm.feiyongxiangqing">
            </el-input>
          </el-form-item>

      <el-form-item :style='{"padding":"0","margin":"30px 0 20px 140px"}'>
        <el-button :style='{"border":"0","cursor":"pointer","padding":"0 10px","margin":"0 10px","color":"#fff","minWidth":"140px","outline":"none","borderRadius":"10px","background":"linear-gradient(90deg, rgba(32,173,158,1) 0%, rgba(138,228,219,1) 50%, rgba(32,173,158,1) 100%),#20ad9e","width":"auto","lineHeight":"44px","fontSize":"14px","height":"44px"}'  type="primary" @click="onSubmit">提交</el-button>
        <el-button :style='{"border":"0px solid rgba(64, 158, 255, 1)","cursor":"pointer","padding":"0 15px","margin":"0 10px","color":"#fff","minWidth":"140px","outline":"none","borderRadius":"10px","background":"linear-gradient(90deg, rgba(153,153,153,1) 0%, rgba(204,204,204,1) 50%, rgba(153,153,153,1) 100%),#999","width":"auto","lineHeight":"44px","fontSize":"14px","height":"44px"}' @click="back()">返回</el-button>
      </el-form-item>
    </el-form>
</div>
</template>

<script>
  export default {
    data() {
      return {
        id: '',
        baseUrl: '',
        ro:{
            yuefen : false,
            zhuhuzhanghao : false,
            zhuhuxingming : false,
            loudonghao : false,
            zhuzhi : false,
            jiaofeileixing : false,
            feiyong : false,
            feiyongqingdan : false,
            jiaofeishijian : false,
            jiezhishijian : false,
            feiyongxiangqing : false,
            ispay : false,
        },
        type: '',
        userTableName: localStorage.getItem('UserTableName'),
        ruleForm: {
          yuefen: '',
          zhuhuzhanghao: '',
          zhuhuxingming: '',
          loudonghao: '',
          zhuzhi: '',
          jiaofeileixing: '',
          feiyong: '',
          feiyongqingdan: '',
          jiaofeishijian: '',
          jiezhishijian: '',
          feiyongxiangqing: '',
          ispay: '',
        },
        yuefenOptions: [],
        zhuhuzhanghaoOptions: [],
        jiaofeileixingOptions: [],
        rules: {
          yuefen: [
            { required: true, message: '月份不能为空', trigger: 'blur' },
          ],
          zhuhuzhanghao: [
            { required: true, message: '住户账号不能为空', trigger: 'blur' },
          ],
          zhuhuxingming: [
          ],
          loudonghao: [
          ],
          zhuzhi: [
          ],
          jiaofeileixing: [
            { required: true, message: '缴费类型不能为空', trigger: 'blur' },
          ],
          feiyong: [
            { validator: this.$validate.isNumber, trigger: 'blur' },
          ],
          feiyongqingdan: [
          ],
          jiaofeishijian: [
          ],
          jiezhishijian: [
          ],
          feiyongxiangqing: [
          ],
          ispay: [
          ],
        },
      };
    },
    computed: {



    },
    created() {
	  //this.bg();
      let type = this.$route.query.type ? this.$route.query.type : '';
      this.init(type);
      this.baseUrl = this.$config.baseUrl;
      this.ruleForm.jiaofeishijian = this.getCurDateTime()
      this.ruleForm.jiezhishijian = this.getCurDateTime()
    },
    methods: {
      getMakeZero(s) {
          return s < 10 ? '0' + s : s;
      },
      // 下载
      download(file){
        window.open(`${file}`)
      },
      // 初始化
      init(type) {
        this.type = type;
        if(type=='cross'){
          var obj = JSON.parse(localStorage.getItem('crossObj'));
          for (var o in obj){
            if(o=='yuefen'){
              this.ruleForm.yuefen = obj[o];
              this.ro.yuefen = true;
              continue;
            }
            if(o=='zhuhuzhanghao'){
              this.ruleForm.zhuhuzhanghao = obj[o];
              this.ro.zhuhuzhanghao = true;
              continue;
            }
            if(o=='zhuhuxingming'){
              this.ruleForm.zhuhuxingming = obj[o];
              this.ro.zhuhuxingming = true;
              continue;
            }
            if(o=='loudonghao'){
              this.ruleForm.loudonghao = obj[o];
              this.ro.loudonghao = true;
              continue;
            }
            if(o=='zhuzhi'){
              this.ruleForm.zhuzhi = obj[o];
              this.ro.zhuzhi = true;
              continue;
            }
            if(o=='jiaofeileixing'){
              this.ruleForm.jiaofeileixing = obj[o];
              this.ro.jiaofeileixing = true;
              continue;
            }
            if(o=='feiyong'){
              this.ruleForm.feiyong = obj[o];
              this.ro.feiyong = true;
              continue;
            }
            if(o=='feiyongqingdan'){
              this.ruleForm.feiyongqingdan = obj[o].split(",")[0];
              this.ro.feiyongqingdan = true;
              continue;
            }
            if(o=='jiaofeishijian'){
              this.ruleForm.jiaofeishijian = obj[o];
              this.ro.jiaofeishijian = true;
              continue;
            }
            if(o=='jiezhishijian'){
              this.ruleForm.jiezhishijian = obj[o];
              this.ro.jiezhishijian = true;
              continue;
            }
            if(o=='feiyongxiangqing'){
              this.ruleForm.feiyongxiangqing = obj[o];
              this.ro.feiyongxiangqing = true;
              continue;
            }
          }
        }
        // 获取用户信息
        this.$http.get(this.userTableName + '/session', {emulateJSON: true}).then(res => {
          if (res.data.code == 0) {
            var json = res.data.data;
          }
        });
        this.yuefenOptions = "一月,二月,三月,四月,五月,六月,七月,八月,九月,十月,十一月,十二月".split(',')
        this.$http.get('option/zhuhu/zhuhuzhanghao', {emulateJSON: true}).then(res => {
          if (res.data.code == 0) {
            this.zhuhuzhanghaoOptions = res.data.data;
          }
        });
        this.jiaofeileixingOptions = "水费,电费,物业费,管理费,其他费用".split(',')
      },
      // 下二随
      zhuhuzhanghaoChange () {
        this.$http.get('follow/zhuhu/zhuhuzhanghao?columnValue=' + this.ruleForm.zhuhuzhanghao, {emulateJSON: true}).then(res => {
          if (res.data.code == 0) {
            if(res.data.data.zhuhuxingming){
              this.ruleForm.zhuhuxingming = res.data.data.zhuhuxingming
            }
            if(res.data.data.loudonghao){
              this.ruleForm.loudonghao = res.data.data.loudonghao
            }
            if(res.data.data.zhuzhi){
              this.ruleForm.zhuzhi = res.data.data.zhuzhi
            }
          }
        });
      },

    // 多级联动参数
      // 多级联动参数
      info(id) {
        this.$http.get('wuyecuijiao/detail/${id}', {emulateJSON: true}).then(res => {
          if (res.data.code == 0) {
            this.ruleForm = res.data.data;
          }
        });
      },
      // 提交
      onSubmit() {

        //更新跨表属性
        var crossuserid;
        var crossrefid;
        var crossoptnum;
        this.$refs["ruleForm"].validate(valid => {
          if(valid) {
            if(this.type=='cross'){
                 var statusColumnName = localStorage.getItem('statusColumnName');
                 var statusColumnValue = localStorage.getItem('statusColumnValue');
                 if(statusColumnName && statusColumnName!='') {
                     var obj = JSON.parse(localStorage.getItem('crossObj'));
                     if(!statusColumnName.startsWith("[")) {
                         for (var o in obj){
                             if(o==statusColumnName){
                                 obj[o] = statusColumnValue;
                             }
                         }
                         var table = localStorage.getItem('crossTable');
                         this.$http.post(table+'/update', obj).then(res => {});
                     } else {
                            crossuserid=Number(localStorage.getItem('userid'));
                            crossrefid=obj['id'];
                            crossoptnum=localStorage.getItem('statusColumnName');
                            crossoptnum=crossoptnum.replace(/\[/,"").replace(/\]/,"");
                     }
                 }
            }
            if(crossrefid && crossuserid) {
                 this.ruleForm.crossuserid=crossuserid;
                 this.ruleForm.crossrefid=crossrefid;
                 var params = {
                     page: 1,
                     limit: 10,
                     crossuserid:crossuserid,
                     crossrefid:crossrefid,
                 }
                 this.$http.get('wuyecuijiao/list', {
                  params: params
                 }).then(res => {
                     if(res.data.data.total>=crossoptnum) {
                         this.$message({
                          message: localStorage.getItem('tips'),
                          type: 'success',
                          duration: 1500,
                         });
                          return false;
                     } else {
                         // 跨表计算


                          this.$http.post('wuyecuijiao/add', this.ruleForm).then(res => {
                              if (res.data.code == 0) {
                                  this.$message({
                                      message: '操作成功',
                                      type: 'success',
                                      duration: 1500,
                                      onClose: () => {
                                          this.$router.go(-1);
                                      }
                                  });
                              } else {
                                  this.$message({
                                      message: res.data.msg,
                                      type: 'error',
                                      duration: 1500
                                  });
                              }
                          });
                     }
                 });
             } else {


                  this.$http.post('wuyecuijiao/add', this.ruleForm).then(res => {
                     if (res.data.code == 0) {
                          this.$message({
                              message: '操作成功',
                              type: 'success',
                              duration: 1500,
                              onClose: () => {
                                  this.$router.go(-1);
                              }
                          });
                      } else {
                          this.$message({
                              message: res.data.msg,
                              type: 'error',
                              duration: 1500
                          });
                      }
                  });
             }
          }
        });
      },
      // 获取uuid
      getUUID () {
        return new Date().getTime();
      },
      // 返回
      back() {
        this.$router.go(-1);
      },
      feiyongqingdanUploadChange(fileUrls) {
          this.ruleForm.feiyongqingdan = fileUrls.replace(new RegExp(this.$config.baseUrl,"g"),"");;
      },
    }
  };
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
	.el-date-editor.el-input {
		width: auto;
	}
	
	.add-update-preview .el-form-item /deep/ .el-form-item__label {
	  padding: 0 15px;
	  color: #992298;
	  font-weight: 500;
	  width: 150px;
	  font-size: 15px;
	  line-height: 40px;
	  text-align: right;
	}
	
	.add-update-preview .el-form-item /deep/ .el-form-item__content {
	  margin-left: 150px;
	}
	
	.add-update-preview .el-input /deep/ .el-input__inner {
	  border: 0;
	  border-radius: 0;
	  padding: 0 10px;
	  box-shadow: 0 0 0px rgba(64, 158, 255, .5);
	  outline: none;
	  color: #333;
	  background: #fff;
	  width: 360px;
	  font-size: 14px;
	  line-height: 32px;
	  height: 32px;
	}
	
	.add-update-preview .el-select /deep/ .el-input__inner {
	  border: 0;
	  border-radius: 0;
	  padding: 0 30px 0 10px;
	  box-shadow: 0 0 0px rgba(64, 158, 255, .5);
	  outline: none;
	  color: #333;
	  background: #fff;
	  width: 320px;
	  font-size: 14px;
	  line-height: 32px;
	  height: 32px;
	}
	
	.add-update-preview .el-date-editor /deep/ .el-input__inner {
	  border: 0;
	  border-radius: 0;
	  padding: 0 10px 0 30px;
	  box-shadow: 0 0 0px rgba(64, 158, 255, .5);
	  outline: none;
	  color: #333;
	  background: #fff;
	  width: 400px;
	  font-size: 14px;
	  line-height: 32px;
	  height: 32px;
	}
	
	.add-update-preview /deep/ .el-upload--picture-card {
		background: transparent;
		border: 0;
		border-radius: 0;
		width: auto;
		height: auto;
		line-height: initial;
		vertical-align: middle;
	}
	
	.add-update-preview /deep/ .upload .upload-img {
	  border: 1px dashed #992298;
	  cursor: pointer;
	  border-radius: 6px;
	  color: #992298;
	  width: 100px;
	  font-size: 32px;
	  line-height: 100px;
	  text-align: center;
	  height: 100px;
	}
	
	.add-update-preview /deep/ .el-upload-list .el-upload-list__item {
	  border: 1px dashed #992298;
	  cursor: pointer;
	  border-radius: 6px;
	  color: #992298;
	  width: 100px;
	  font-size: 32px;
	  line-height: 100px;
	  text-align: center;
	  height: 100px;
	}
	
	.add-update-preview /deep/ .el-upload .el-icon-plus {
	  border: 1px dashed #992298;
	  cursor: pointer;
	  border-radius: 6px;
	  color: #992298;
	  width: 100px;
	  font-size: 32px;
	  line-height: 100px;
	  text-align: center;
	  height: 100px;
	}
	
	.add-update-preview .el-textarea /deep/ .el-textarea__inner {
	  border: 0;
	  border-radius: 0;
	  padding: 12px;
	  box-shadow: 0 0 0px rgba(64, 158, 255, .5);
	  outline: none;
	  color: #333;
	  width: 400px;
	  font-size: 14px;
	  height: 120px;
	}
</style>
