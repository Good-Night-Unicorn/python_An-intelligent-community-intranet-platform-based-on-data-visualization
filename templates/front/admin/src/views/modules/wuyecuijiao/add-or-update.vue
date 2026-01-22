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
				<el-form-item :style='{"width":"49%","float":"left","margin":"0 0 20px 0"}' class="select" v-if="type!='info'"  label="月份" prop="yuefen">
					<el-select :disabled="ro.yuefen" v-model="ruleForm.yuefen" placeholder="请选择月份" >
						<el-option
							v-for="(item,index) in yuefenOptions"
							v-bind:key="index"
							:label="item"
							:value="item">
						</el-option>
					</el-select>
				</el-form-item>
				<el-form-item :style='{"width":"49%","float":"left","margin":"0 0 20px 0"}' v-else class="input" label="月份" prop="yuefen">
					<el-input v-model="ruleForm.yuefen"
						placeholder="月份" readonly></el-input>
				</el-form-item>
				<el-form-item :style='{"width":"49%","float":"left","margin":"0 0 20px 0"}' class="select" v-if="type!='info'" label="住户账号" prop="zhuhuzhanghao">
					<el-select :disabled="ro.zhuhuzhanghao" @change="zhuhuzhanghaoChange" v-model="ruleForm.zhuhuzhanghao" placeholder="请选择住户账号">
						<el-option
							v-for="(item,index) in zhuhuzhanghaoOptions"
							v-bind:key="index"
							:label="item"
							:value="item">
						</el-option>
					</el-select>
				</el-form-item>
				<el-form-item :style='{"width":"49%","float":"left","margin":"0 0 20px 0"}' class="input" v-else-if="ruleForm.zhuhuzhanghao" label="住户账号" prop="zhuhuzhanghao">
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
				<el-form-item :style='{"width":"49%","float":"left","margin":"0 0 20px 0"}' class="input" v-if="type!='info'"  label="住址" prop="zhuzhi">
					<el-input v-model="ruleForm.zhuzhi" placeholder="住址" clearable  :readonly="ro.zhuzhi"></el-input>
				</el-form-item>
				<el-form-item :style='{"width":"49%","float":"left","margin":"0 0 20px 0"}' v-else class="input" label="住址" prop="zhuzhi">
					<el-input v-model="ruleForm.zhuzhi" placeholder="住址" readonly></el-input>
				</el-form-item>
				<el-form-item :style='{"width":"49%","float":"left","margin":"0 0 20px 0"}' class="select" v-if="type!='info'"  label="缴费类型" prop="jiaofeileixing">
					<el-select :disabled="ro.jiaofeileixing" v-model="ruleForm.jiaofeileixing" placeholder="请选择缴费类型" >
						<el-option
							v-for="(item,index) in jiaofeileixingOptions"
							v-bind:key="index"
							:label="item"
							:value="item">
						</el-option>
					</el-select>
				</el-form-item>
				<el-form-item :style='{"width":"49%","float":"left","margin":"0 0 20px 0"}' v-else class="input" label="缴费类型" prop="jiaofeileixing">
					<el-input v-model="ruleForm.jiaofeileixing"
						placeholder="缴费类型" readonly></el-input>
				</el-form-item>
				<el-form-item :style='{"width":"49%","float":"left","margin":"0 0 20px 0"}' class="input" v-if="type!='info'"  label="费用" prop="feiyong">
					<el-input v-model="ruleForm.feiyong" placeholder="费用" clearable  :readonly="ro.feiyong"></el-input>
				</el-form-item>
				<el-form-item :style='{"width":"49%","float":"left","margin":"0 0 20px 0"}' v-else class="input" label="费用" prop="feiyong">
					<el-input v-model="ruleForm.feiyong" placeholder="费用" readonly></el-input>
				</el-form-item>
				<el-form-item :style='{"width":"49%","float":"left","margin":"0 0 20px 0"}' class="upload" v-if="type!='info' && !ro.feiyongqingdan" label="费用清单" prop="feiyongqingdan">
					<file-upload
						tip="点击上传费用清单"
						action="file/upload"
						:limit="3"
						:multiple="true"
						:fileUrls="ruleForm.feiyongqingdan?ruleForm.feiyongqingdan:''"
						@change="feiyongqingdanUploadChange"
					></file-upload>
				</el-form-item>
				<el-form-item :style='{"width":"49%","float":"left","margin":"0 0 20px 0"}' class="upload" v-else-if="ruleForm.feiyongqingdan" label="费用清单" prop="feiyongqingdan">
					<img v-if="ruleForm.feiyongqingdan.substring(0,4)=='http'" class="upload-img" style="margin-right:20px;" v-bind:key="index" :src="ruleForm.feiyongqingdan.split(',')[0]" width="100" height="100">
					<img v-else class="upload-img" style="margin-right:20px;" v-bind:key="index" v-for="(item,index) in ruleForm.feiyongqingdan.split(',')" :src="$base.url+item" width="100" height="100">
				</el-form-item>
				<el-form-item :style='{"width":"49%","float":"left","margin":"0 0 20px 0"}' class="date" v-if="type!='info'" label="缴费时间" prop="jiaofeishijian">
					<el-date-picker
						value-format="yyyy-MM-dd HH:mm:ss"
						v-model="ruleForm.jiaofeishijian" 
						type="datetime"
						:readonly="ro.jiaofeishijian"
						placeholder="缴费时间"
					></el-date-picker>
				</el-form-item>
				<el-form-item :style='{"width":"49%","float":"left","margin":"0 0 20px 0"}' class="input" v-else-if="ruleForm.jiaofeishijian" label="缴费时间" prop="jiaofeishijian">
					<el-input v-model="ruleForm.jiaofeishijian" placeholder="缴费时间" readonly></el-input>
				</el-form-item>
				<el-form-item :style='{"width":"49%","float":"left","margin":"0 0 20px 0"}' class="date" v-if="type!='info'" label="截止时间" prop="jiezhishijian">
					<el-date-picker
						value-format="yyyy-MM-dd HH:mm:ss"
						v-model="ruleForm.jiezhishijian" 
						type="datetime"
						:readonly="ro.jiezhishijian"
						placeholder="截止时间"
					></el-date-picker>
				</el-form-item>
				<el-form-item :style='{"width":"49%","float":"left","margin":"0 0 20px 0"}' class="input" v-else-if="ruleForm.jiezhishijian" label="截止时间" prop="jiezhishijian">
					<el-input v-model="ruleForm.jiezhishijian" placeholder="截止时间" readonly></el-input>
				</el-form-item>
			</template>
				<el-form-item :style='{"width":"49%","float":"left","margin":"0 0 20px 0"}' class="textarea" v-if="type!='info'" label="费用详情" prop="feiyongxiangqing">
					<el-input
					  style="min-width: 200px; max-width: 600px;"
					  type="textarea"
					  :rows="8"
					  placeholder="费用详情"
					  v-model="ruleForm.feiyongxiangqing" >
					</el-input>
				</el-form-item>
				<el-form-item :style='{"width":"49%","float":"left","margin":"0 0 20px 0"}' v-else-if="ruleForm.feiyongxiangqing" label="费用详情" prop="feiyongxiangqing">
					<span :style='{"fontSize":"14px","lineHeight":"24px","color":"#888","fontWeight":"500","display":"inline-block"}'>{{ruleForm.feiyongxiangqing}}</span>
				</el-form-item>
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
					{ validator: validateNumber, trigger: 'blur' },
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
			}
		};
	},
	props: ["parent"],
	computed: {



	},
    components: {
    },
	created() {
		this.ruleForm.jiaofeishijian = this.getCurDateTime()
		this.ruleForm.jiezhishijian = this.getCurDateTime()
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
							this.ruleForm.feiyongqingdan = obj[o];
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
			this.$http({
				url: `${this.$storage.get('sessionTable')}/session`,
				method: "get"
			}).then(({ data }) => {
				if (data && data.code === 0) {
					
					var json = data.data;
				} else {
					this.$message.error(data.msg);
				}
			});
			
            this.yuefenOptions = "一月,二月,三月,四月,五月,六月,七月,八月,九月,十月,十一月,十二月".split(',')
            this.$http({
				url: `option/zhuhu/zhuhuzhanghao`,
				method: "get"
            }).then(({ data }) => {
				if (data && data.code === 0) {
					this.zhuhuzhanghaoOptions = data.data;
				} else {
					this.$message.error(data.msg);
				}
            });
            this.jiaofeileixingOptions = "水费,电费,物业费,管理费,其他费用".split(',')
			
		},
			// 下二随
			zhuhuzhanghaoChange () {
				this.$http({
					url: `follow/zhuhu/zhuhuzhanghao?columnValue=`+ this.ruleForm.zhuhuzhanghao,
					method: "get"
				}).then(({ data }) => {
					if (data && data.code === 0) {
						if(data.data.zhuhuxingming){
							this.ruleForm.zhuhuxingming = data.data.zhuhuxingming
						}
						if(data.data.loudonghao){
							this.ruleForm.loudonghao = data.data.loudonghao
						}
						if(data.data.zhuzhi){
							this.ruleForm.zhuzhi = data.data.zhuzhi
						}
					} else {
						this.$message.error(data.msg);
					}
				});
			},
    // 多级联动参数

    info(id) {
      this.$http({
        url: `wuyecuijiao/info/${id}`,
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
















	if(this.ruleForm.feiyongqingdan!=null) {
		this.ruleForm.feiyongqingdan = this.ruleForm.feiyongqingdan.replace(new RegExp(this.$base.url,"g"),"");
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
				url: "wuyecuijiao/page", 
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
					   url: `wuyecuijiao/${!this.ruleForm.id ? "save" : "update"}`,
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
						 this.parent.wuyecuijiaoCrossAddOrUpdateFlag = false;
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
			   url: `wuyecuijiao/${!this.ruleForm.id ? "save" : "update"}`,
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
				 this.parent.wuyecuijiaoCrossAddOrUpdateFlag = false;
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
      this.parent.wuyecuijiaoCrossAddOrUpdateFlag = false;
      this.parent.contentStyleChange();
    },
    feiyongqingdanUploadChange(fileUrls) {
	    this.ruleForm.feiyongqingdan = fileUrls;
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
