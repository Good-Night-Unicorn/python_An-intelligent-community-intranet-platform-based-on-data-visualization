<template>
	<div class="addEdit-block" :style='{"padding":"0px"}' style="width: 100%;">
		<el-form
			:style='{"padding":"30px","boxShadow":"0 0px 0px rgba(64, 158, 255, .3)","margin":"22px","borderRadius":"8px","background":"rgba(255,255,255,.9)"}'
			class="add-update-preview"
			ref="ruleForm"
			:model="ruleForm"
			:rules="rules"
			label-width="80px"
		>
			<template >
				<el-form-item :style='{"width":"49%","float":"left","margin":"0 0 20px 0"}' class="date" v-if="type!='info'" label="来访时间" prop="laifangshijian">
					<el-date-picker
						value-format="yyyy-MM-dd HH:mm:ss"
						v-model="ruleForm.laifangshijian" 
						type="datetime"
						:readonly="ro.laifangshijian"
						placeholder="来访时间"
					></el-date-picker>
				</el-form-item>
				<el-form-item :style='{"width":"49%","float":"left","margin":"0 0 20px 0"}' class="input" v-else-if="ruleForm.laifangshijian" label="来访时间" prop="laifangshijian">
					<el-input v-model="ruleForm.laifangshijian" placeholder="来访时间" readonly></el-input>
				</el-form-item>
				<el-form-item :style='{"width":"49%","float":"left","margin":"0 0 20px 0"}' class="input" v-if="type!='info'"  label="来访人员" prop="laifangrenyuan">
					<el-input v-model="ruleForm.laifangrenyuan" placeholder="来访人员" clearable  :readonly="ro.laifangrenyuan"></el-input>
				</el-form-item>
				<el-form-item :style='{"width":"49%","float":"left","margin":"0 0 20px 0"}' v-else class="input" label="来访人员" prop="laifangrenyuan">
					<el-input v-model="ruleForm.laifangrenyuan" placeholder="来访人员" readonly></el-input>
				</el-form-item>
				<el-form-item :style='{"width":"49%","float":"left","margin":"0 0 20px 0"}' class="input" v-if="type!='info'"  label="手机号码" prop="shoujihaoma">
					<el-input v-model="ruleForm.shoujihaoma" placeholder="手机号码" clearable  :readonly="ro.shoujihaoma"></el-input>
				</el-form-item>
				<el-form-item :style='{"width":"49%","float":"left","margin":"0 0 20px 0"}' v-else class="input" label="手机号码" prop="shoujihaoma">
					<el-input v-model="ruleForm.shoujihaoma" placeholder="手机号码" readonly></el-input>
				</el-form-item>
				<el-form-item :style='{"width":"49%","float":"left","margin":"0 0 20px 0"}' class="input" v-if="type!='info'"  label="住户账号" prop="zhuhuzhanghao">
					<el-input v-model="ruleForm.zhuhuzhanghao" placeholder="住户账号" clearable  :readonly="ro.zhuhuzhanghao"></el-input>
				</el-form-item>
				<el-form-item :style='{"width":"49%","float":"left","margin":"0 0 20px 0"}' v-else class="input" label="住户账号" prop="zhuhuzhanghao">
					<el-input v-model="ruleForm.zhuhuzhanghao" placeholder="住户账号" readonly></el-input>
				</el-form-item>
				<el-form-item :style='{"width":"49%","float":"left","margin":"0 0 20px 0"}' class="input" v-if="type!='info'"  label="住户姓名" prop="zhuhuxingming">
					<el-input v-model="ruleForm.zhuhuxingming" placeholder="住户姓名" clearable  :readonly="ro.zhuhuxingming"></el-input>
				</el-form-item>
				<el-form-item :style='{"width":"49%","float":"left","margin":"0 0 20px 0"}' v-else class="input" label="住户姓名" prop="zhuhuxingming">
					<el-input v-model="ruleForm.zhuhuxingming" placeholder="住户姓名" readonly></el-input>
				</el-form-item>
				<el-form-item :style='{"width":"49%","float":"left","margin":"0 0 20px 0"}' class="input" v-if="type!='info'"  label="楼栋号" prop="loudonghao">
					<el-input v-model="ruleForm.loudonghao" placeholder="楼栋号" clearable  :readonly="ro.loudonghao"></el-input>
				</el-form-item>
				<el-form-item :style='{"width":"49%","float":"left","margin":"0 0 20px 0"}' v-else class="input" label="楼栋号" prop="loudonghao">
					<el-input v-model="ruleForm.loudonghao" placeholder="楼栋号" readonly></el-input>
				</el-form-item>
				<el-form-item :style='{"width":"49%","float":"left","margin":"0 0 20px 0"}' class="input" v-if="type!='info'"  label="体温" prop="tiwen">
					<el-input v-model="ruleForm.tiwen" placeholder="体温" clearable  :readonly="ro.tiwen"></el-input>
				</el-form-item>
				<el-form-item :style='{"width":"49%","float":"left","margin":"0 0 20px 0"}' v-else class="input" label="体温" prop="tiwen">
					<el-input v-model="ruleForm.tiwen" placeholder="体温" readonly></el-input>
				</el-form-item>
				<el-form-item :style='{"width":"49%","float":"left","margin":"0 0 20px 0"}' class="date" v-if="type!='info'" label="进入时间" prop="jinrushijian">
					<el-date-picker
						value-format="yyyy-MM-dd HH:mm:ss"
						v-model="ruleForm.jinrushijian" 
						type="datetime"
						:readonly="ro.jinrushijian"
						placeholder="进入时间"
					></el-date-picker>
				</el-form-item>
				<el-form-item :style='{"width":"49%","float":"left","margin":"0 0 20px 0"}' class="input" v-else-if="ruleForm.jinrushijian" label="进入时间" prop="jinrushijian">
					<el-input v-model="ruleForm.jinrushijian" placeholder="进入时间" readonly></el-input>
				</el-form-item>
				<el-form-item :style='{"width":"49%","float":"left","margin":"0 0 20px 0"}' class="date" v-if="type!='info'" label="出去时间" prop="chuqushijian">
					<el-date-picker
						value-format="yyyy-MM-dd HH:mm:ss"
						v-model="ruleForm.chuqushijian" 
						type="datetime"
						:readonly="ro.chuqushijian"
						placeholder="出去时间"
					></el-date-picker>
				</el-form-item>
				<el-form-item :style='{"width":"49%","float":"left","margin":"0 0 20px 0"}' class="input" v-else-if="ruleForm.chuqushijian" label="出去时间" prop="chuqushijian">
					<el-input v-model="ruleForm.chuqushijian" placeholder="出去时间" readonly></el-input>
				</el-form-item>
				<el-form-item :style='{"width":"49%","float":"left","margin":"0 0 20px 0"}' class="input" v-if="type!='info'"  label="备注" prop="beizhu">
					<el-input v-model="ruleForm.beizhu" placeholder="备注" clearable  :readonly="ro.beizhu"></el-input>
				</el-form-item>
				<el-form-item :style='{"width":"49%","float":"left","margin":"0 0 20px 0"}' v-else class="input" label="备注" prop="beizhu">
					<el-input v-model="ruleForm.beizhu" placeholder="备注" readonly></el-input>
				</el-form-item>
			</template>
			<el-form-item :style='{"clear":"both","width":"100%","padding":"0","margin":"0"}' class="btn">
				<el-button :style='{"border":"1px solid #409eff","cursor":"pointer","padding":"0","margin":"0 20px 0 0","outline":"none","color":"rgba(255, 255, 255, 1)","borderRadius":"4px","background":"-webkit-linear-gradient(top,#7dbcfe,#409eff)","width":"128px","lineHeight":"40px","fontSize":"14px","height":"40px"}'  v-if="type!='info'" type="primary" class="btn-success" @click="onSubmit">提交</el-button>
				<el-button :style='{"border":"1px solid rgba(64, 158, 255, 1)","cursor":"pointer","padding":"0","margin":"0","outline":"none","color":"rgba(64, 158, 255, 1)","borderRadius":"4px","background":"rgba(255, 255, 255, 1)","width":"128px","lineHeight":"40px","fontSize":"14px","height":"40px"}' v-if="type!='info'" class="btn-close" @click="back()">取消</el-button>
				<el-button :style='{"border":"1px solid rgba(64, 158, 255, 1)","cursor":"pointer","padding":"0","margin":"0","outline":"none","color":"rgba(64, 158, 255, 1)","borderRadius":"4px","background":"rgba(255, 255, 255, 1)","width":"128px","lineHeight":"40px","fontSize":"14px","height":"40px"}' v-if="type=='info'" class="btn-close" @click="back()">返回</el-button>
			</el-form-item>
		</el-form>
    

  </div>
</template>
<script>
// 数字，邮件，手机，url，身份证校验
import { isNumber,isIntNumer,isEmail,isPhone, isMobile,isURL,checkIdCard } from "@/utils/validate";
export default {
	data() {
		let self = this
		var validateIdCard = (rule, value, callback) => {
			if(!value){
				callback();
			} else if (!checkIdCard(value)) {
				callback(new Error("请输入正确的身份证号码"));
			} else {
				callback();
			}
		};
		var validateUrl = (rule, value, callback) => {
			if(!value){
				callback();
			} else if (!isURL(value)) {
				callback(new Error("请输入正确的URL地址"));
			} else {
				callback();
			}
		};
		var validateMobile = (rule, value, callback) => {
			if(!value){
				callback();
			} else if (!isMobile(value)) {
				callback(new Error("请输入正确的手机号码"));
			} else {
				callback();
			}
		};
		var validatePhone = (rule, value, callback) => {
			if(!value){
				callback();
			} else if (!isPhone(value)) {
				callback(new Error("请输入正确的电话号码"));
			} else {
				callback();
			}
		};
		var validateEmail = (rule, value, callback) => {
			if(!value){
				callback();
			} else if (!isEmail(value)) {
				callback(new Error("请输入正确的邮箱地址"));
			} else {
				callback();
			}
		};
		var validateNumber = (rule, value, callback) => {
			if(!value){
				callback();
			} else if (!isNumber(value)) {
				callback(new Error("请输入数字"));
			} else {
				callback();
			}
		};
		var validateIntNumber = (rule, value, callback) => {
			if(!value){
				callback();
			} else if (!isIntNumer(value)) {
				callback(new Error("请输入整数"));
			} else {
				callback();
			}
		};
		return {
			id: '',
			type: '',
			
			
			ro:{
				laifangshijian : false,
				laifangrenyuan : false,
				shoujihaoma : false,
				zhuhuzhanghao : false,
				zhuhuxingming : false,
				loudonghao : false,
				tiwen : false,
				jinrushijian : false,
				chuqushijian : false,
				beizhu : false,
			},
			
			
			ruleForm: {
				laifangshijian: '',
				laifangrenyuan: '',
				shoujihaoma: '',
				zhuhuzhanghao: '',
				zhuhuxingming: '',
				loudonghao: '',
				tiwen: '',
				jinrushijian: '',
				chuqushijian: '',
				beizhu: '',
			},
		
			
			rules: {
				laifangshijian: [
				],
				laifangrenyuan: [
				],
				shoujihaoma: [
				],
				zhuhuzhanghao: [
				],
				zhuhuxingming: [
				],
				loudonghao: [
				],
				tiwen: [
					{ validator: validateNumber, trigger: 'blur' },
				],
				jinrushijian: [
				],
				chuqushijian: [
				],
				beizhu: [
				],
			}
		};
	},
	props: ["parent"],
	computed: {



	},
    components: {
    },
	created() {
		this.ruleForm.laifangshijian = this.getCurDateTime()
	},
	methods: {
		
		// 下载
		download(file){
			window.open(`${file}`)
		},
		// 初始化
		init(id,type) {
			if (id) {
				this.id = id;
				this.type = type;
			}
			if(this.type=='info'||this.type=='else'){
				this.info(id);
			}else if(this.type=='logistics'){
				this.logistics=false;
				this.info(id);
			}else if(this.type=='cross'){
				var obj = this.$storage.getObj('crossObj');
				for (var o in obj){
						if(o=='laifangshijian'){
							this.ruleForm.laifangshijian = obj[o];
							this.ro.laifangshijian = true;
							continue;
						}
						if(o=='laifangrenyuan'){
							this.ruleForm.laifangrenyuan = obj[o];
							this.ro.laifangrenyuan = true;
							continue;
						}
						if(o=='shoujihaoma'){
							this.ruleForm.shoujihaoma = obj[o];
							this.ro.shoujihaoma = true;
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
						if(o=='tiwen'){
							this.ruleForm.tiwen = obj[o];
							this.ro.tiwen = true;
							continue;
						}
						if(o=='jinrushijian'){
							this.ruleForm.jinrushijian = obj[o];
							this.ro.jinrushijian = true;
							continue;
						}
						if(o=='chuqushijian'){
							this.ruleForm.chuqushijian = obj[o];
							this.ro.chuqushijian = true;
							continue;
						}
						if(o=='beizhu'){
							this.ruleForm.beizhu = obj[o];
							this.ro.beizhu = true;
							continue;
						}
				}
				










			}
			
			
			// 获取用户信息
			this.$http({
				url: `${this.$storage.get('sessionTable')}/session`,
				method: "get"
			}).then(({ data }) => {
				if (data && data.code === 0) {
					
					var json = data.data;
					if(((json.zhuhuzhanghao!=''&&json.zhuhuzhanghao) || json.zhuhuzhanghao==0) && this.$storage.get("role")!="管理员"){
						this.ruleForm.zhuhuzhanghao = json.zhuhuzhanghao
						this.ro.zhuhuzhanghao = true;
					}
					if(((json.zhuhuxingming!=''&&json.zhuhuxingming) || json.zhuhuxingming==0) && this.$storage.get("role")!="管理员"){
						this.ruleForm.zhuhuxingming = json.zhuhuxingming
						this.ro.zhuhuxingming = true;
					}
					if(((json.loudonghao!=''&&json.loudonghao) || json.loudonghao==0) && this.$storage.get("role")!="管理员"){
						this.ruleForm.loudonghao = json.loudonghao
						this.ro.loudonghao = true;
					}
				} else {
					this.$message.error(data.msg);
				}
			});
			
			
		},
    // 多级联动参数

    info(id) {
      this.$http({
        url: `laifangdengji/info/${id}`,
        method: "get"
      }).then(({ data }) => {
        if (data && data.code === 0) {
        this.ruleForm = data.data;
        //解决前台上传图片后台不显示的问题
        let reg=new RegExp('../../../upload','g')//g代表全部
        } else {
          this.$message.error(data.msg);
        }
      });
    },


    // 提交
    onSubmit() {
















      if(this.ruleForm.jinrushijian>this.ruleForm.chuqushijian){
        this.$message.error("进入时间不能超过出去时间");
        return
      }





var objcross = this.$storage.getObj('crossObj');

      //更新跨表属性
       var crossuserid;
       var crossrefid;
       var crossoptnum;
       if(this.type=='cross'){
                var statusColumnName = this.$storage.get('statusColumnName');
                var statusColumnValue = this.$storage.get('statusColumnValue');
                if(statusColumnName!='') {
                        var obj = this.$storage.getObj('crossObj');
                       if(statusColumnName && !statusColumnName.startsWith("[")) {
                               for (var o in obj){
                                 if(o==statusColumnName){
                                   obj[o] = statusColumnValue;
                                 }
                               }
                               var table = this.$storage.get('crossTable');
                             this.$http({
                                 url: `${table}/update`,
                                 method: "post",
                                 data: obj
                               }).then(({ data }) => {});
                       } else {
                               crossuserid=this.$storage.get('userid');
                               crossrefid=obj['id'];
                               crossoptnum=this.$storage.get('statusColumnName');
                               crossoptnum=crossoptnum.replace(/\[/,"").replace(/\]/,"");
                        }
                }
        }
       this.$refs["ruleForm"].validate(valid => {
         if (valid) {
		 if(crossrefid && crossuserid) {
			 this.ruleForm.crossuserid = crossuserid;
			 this.ruleForm.crossrefid = crossrefid;
			let params = { 
				page: 1, 
				limit: 10, 
				crossuserid:this.ruleForm.crossuserid,
				crossrefid:this.ruleForm.crossrefid,
			} 
			this.$http({ 
				url: "laifangdengji/page", 
				method: "get", 
				params: params 
			}).then(({ 
				data 
			}) => { 
				if (data && data.code === 0) { 
				       if(data.data.total>=crossoptnum) {
					     this.$message.error(this.$storage.get('tips'));
					       return false;
				       } else {
					 this.$http({
					   url: `laifangdengji/${!this.ruleForm.id ? "save" : "update"}`,
					   method: "post",
					   data: this.ruleForm
					 }).then(({ data }) => {
					   if (data && data.code === 0) {
					     this.$message({
					       message: "操作成功",
					       type: "success",
					       duration: 1500,
					       onClose: () => {
						 this.parent.showFlag = true;
						 this.parent.addOrUpdateFlag = false;
						 this.parent.laifangdengjiCrossAddOrUpdateFlag = false;
						 this.parent.search();
						 this.parent.contentStyleChange();
					       }
					     });
					   } else {
					     this.$message.error(data.msg);
					   }
					 });

				       }
				} else { 
				} 
			});
		 } else {
			 this.$http({
			   url: `laifangdengji/${!this.ruleForm.id ? "save" : "update"}`,
			   method: "post",
			   data: this.ruleForm
			 }).then(({ data }) => {
			   if (data && data.code === 0) {
			     this.$message({
			       message: "操作成功",
			       type: "success",
			       duration: 1500,
			       onClose: () => {
				 this.parent.showFlag = true;
				 this.parent.addOrUpdateFlag = false;
				 this.parent.laifangdengjiCrossAddOrUpdateFlag = false;
				 this.parent.search();
				 this.parent.contentStyleChange();
			       }
			     });
			   } else {
			     this.$message.error(data.msg);
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
      this.parent.showFlag = true;
      this.parent.addOrUpdateFlag = false;
      this.parent.laifangdengjiCrossAddOrUpdateFlag = false;
      this.parent.contentStyleChange();
    },
  }
};
</script>
<style lang="scss" scoped>
	.amap-wrapper {
		width: 100%;
		height: 500px;
	}
	
	.search-box {
		position: absolute;
	}
	
	.el-date-editor.el-input {
		width: auto;
	}
	
	.add-update-preview .el-form-item /deep/ .el-form-item__label {
	  	  padding: 0 10px 0 0;
	  	  color: #666;
	  	  font-weight: 500;
	  	  width: 80px;
	  	  font-size: 14px;
	  	  line-height: 40px;
	  	  float: left;
	  	  text-align: right;
	  	}
	
	.add-update-preview .el-form-item /deep/ .el-form-item__content {
	  margin-left: 80px;
	}
	
	.add-update-preview .el-input /deep/ .el-input__inner {
	  	  border: 1px solid #ccc;
	  	  border-radius: 4px;
	  	  padding: 0 12px;
	  	  box-shadow: 0 0 0px rgba(64, 158, 255, .5);
	  	  outline: none;
	  	  color: #888;
	  	  width: 400px;
	  	  font-size: 14px;
	  	  height: 36px;
	  	}
	
	.add-update-preview .el-select /deep/ .el-input__inner {
	  	  border: 1px solid #ccc;
	  	  border-radius: 4px;
	  	  padding: 0 10px;
	  	  box-shadow: 0 0 0px rgba(64, 158, 255, .5);
	  	  outline: none;
	  	  color: #888;
	  	  width: auto;
	  	  font-size: 14px;
	  	  height: 40px;
	  	}
	
	.add-update-preview .el-date-editor /deep/ .el-input__inner {
	  	  border: 1px solid #ccc;
	  	  border-radius: 4px;
	  	  padding: 0 10px 0 30px;
	  	  box-shadow: 0 0 0px rgba(64, 158, 255, .5);
	  	  outline: none;
	  	  color: #888;
	  	  width: auto;
	  	  font-size: 14px;
	  	  height: 40px;
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
	  	  border: 1px solid #ccc;
	  	  cursor: pointer;
	  	  border-radius: 6px;
	  	  color: #999;
	  	  width: 200px;
	  	  font-size: 32px;
	  	  line-height: 120px;
	  	  text-align: center;
	  	  height: 120px;
	  	}
	
	.add-update-preview /deep/ .el-upload-list .el-upload-list__item {
	  	  border: 1px solid #ccc;
	  	  cursor: pointer;
	  	  border-radius: 6px;
	  	  color: #999;
	  	  width: 200px;
	  	  font-size: 32px;
	  	  line-height: 120px;
	  	  text-align: center;
	  	  height: 120px;
	  	}
	
	.add-update-preview /deep/ .el-upload .el-icon-plus {
	  	  border: 1px solid #ccc;
	  	  cursor: pointer;
	  	  border-radius: 6px;
	  	  color: #999;
	  	  width: 200px;
	  	  font-size: 32px;
	  	  line-height: 120px;
	  	  text-align: center;
	  	  height: 120px;
	  	}
	
	.add-update-preview .el-textarea /deep/ .el-textarea__inner {
	  	  border: 1px solid #ccc;
	  	  border-radius: 4px;
	  	  padding: 12px;
	  	  box-shadow: 0 0 0px rgba(64, 158, 255, .5);
	  	  outline: none;
	  	  color: #888;
	  	  width: 400px;
	  	  font-size: 14px;
	  	  min-height: 150px;
	  	  height: auto;
	  	}
</style>
