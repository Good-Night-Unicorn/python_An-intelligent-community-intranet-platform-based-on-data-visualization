<template>
<div class="content" :style='{"padding":"30px"}'>
	<div class="text" :style='{"margin":"20px auto","fontSize":"32px","color":"#333","textAlign":"center","fontWeight":"bold"}'>欢迎使用 {{this.$project.projectName}}</div>
    <div class="cardView">
        <div class="cards" :style='{"margin":"0 0 20px 0","alignItems":"center","justifyContent":"center","display":"flex"}'>
			<div :style='{"border":"0px solid #ccc","boxShadow":"0 0px 0px rgba(0,0,0,.3)","margin":"0 10px","borderRadius":"4px","display":"flex"}' v-if="isAuth('zhuhu','首页总数')">
				<div :style='{"borderColor":"#eee","borderRadius":"4px 0px 0px 4px","background":"url(http://codegen.caihongy.cn/20230303/7d7b3d6dd8c54d79b5cbd44a635ecab6.jpg) no-repeat center center / 60% auto","borderWidth":"1px","width":"100px","borderStyle":"solid","height":"100px"}'></div>
				<div :style='{"borderColor":"#eee","alignItems":"center","borderRadius":"0px 4px 4px 0px","flexDirection":"column","background":"#fff","borderWidth":"1px 1px 1px 0","display":"flex","width":"160px","borderStyle":"solid","justifyContent":"center"}'>
					<div :style='{"margin":"5px 0","lineHeight":"24px","fontSize":"20px","color":"#333","fontWeight":"bold","height":"24px"}'>{{zhuhuCount}}</div>
					<div :style='{"margin":"5px 0","lineHeight":"24px","fontSize":"16px","color":"#666","height":"24px"}'>住户总数</div>
				</div>
			</div>
			<div :style='{"border":"0px solid #ccc","boxShadow":"0 0px 0px rgba(0,0,0,.3)","margin":"0 10px","borderRadius":"4px","display":"flex"}' v-if="isAuth('laifangdengji','首页总数')">
				<div :style='{"borderColor":"#eee","borderRadius":"4px 0px 0px 4px","background":"url(http://codegen.caihongy.cn/20230303/7d7b3d6dd8c54d79b5cbd44a635ecab6.jpg) no-repeat center center / 60% auto","borderWidth":"1px","width":"100px","borderStyle":"solid","height":"100px"}'></div>
				<div :style='{"borderColor":"#eee","alignItems":"center","borderRadius":"0px 4px 4px 0px","flexDirection":"column","background":"#fff","borderWidth":"1px 1px 1px 0","display":"flex","width":"160px","borderStyle":"solid","justifyContent":"center"}'>
					<div :style='{"margin":"5px 0","lineHeight":"24px","fontSize":"20px","color":"#333","fontWeight":"bold","height":"24px"}'>{{laifangdengjiCount}}</div>
					<div :style='{"margin":"5px 0","lineHeight":"24px","fontSize":"16px","color":"#666","height":"24px"}'>来访登记总数</div>
				</div>
			</div>
			<div :style='{"border":"0px solid #ccc","boxShadow":"0 0px 0px rgba(0,0,0,.3)","margin":"0 10px","borderRadius":"4px","display":"flex"}' v-if="isAuth('churudengji','首页总数')">
				<div :style='{"borderColor":"#eee","borderRadius":"4px 0px 0px 4px","background":"url(http://codegen.caihongy.cn/20230303/7d7b3d6dd8c54d79b5cbd44a635ecab6.jpg) no-repeat center center / 60% auto","borderWidth":"1px","width":"100px","borderStyle":"solid","height":"100px"}'></div>
				<div :style='{"borderColor":"#eee","alignItems":"center","borderRadius":"0px 4px 4px 0px","flexDirection":"column","background":"#fff","borderWidth":"1px 1px 1px 0","display":"flex","width":"160px","borderStyle":"solid","justifyContent":"center"}'>
					<div :style='{"margin":"5px 0","lineHeight":"24px","fontSize":"20px","color":"#333","fontWeight":"bold","height":"24px"}'>{{churudengjiCount}}</div>
					<div :style='{"margin":"5px 0","lineHeight":"24px","fontSize":"16px","color":"#666","height":"24px"}'>出入登记总数</div>
				</div>
			</div>
			<div :style='{"border":"0px solid #ccc","boxShadow":"0 0px 0px rgba(0,0,0,.3)","margin":"0 10px","borderRadius":"4px","display":"flex"}' v-if="isAuth('gaoweiloudong','首页总数')">
				<div :style='{"borderColor":"#eee","borderRadius":"4px 0px 0px 4px","background":"url(http://codegen.caihongy.cn/20230303/7d7b3d6dd8c54d79b5cbd44a635ecab6.jpg) no-repeat center center / 60% auto","borderWidth":"1px","width":"100px","borderStyle":"solid","height":"100px"}'></div>
				<div :style='{"borderColor":"#eee","alignItems":"center","borderRadius":"0px 4px 4px 0px","flexDirection":"column","background":"#fff","borderWidth":"1px 1px 1px 0","display":"flex","width":"160px","borderStyle":"solid","justifyContent":"center"}'>
					<div :style='{"margin":"5px 0","lineHeight":"24px","fontSize":"20px","color":"#333","fontWeight":"bold","height":"24px"}'>{{gaoweiloudongCount}}</div>
					<div :style='{"margin":"5px 0","lineHeight":"24px","fontSize":"16px","color":"#666","height":"24px"}'>高危楼栋总数</div>
				</div>
			</div>
        </div>
        <div style="display: flex;align-items: center;width: 100%;margin-bottom: 10px;">
            <el-card style="width: 20%;margin: 0 10px;" v-if="isAuth('zhuhu','首页统计')">
                <div id="zhuhuChart1" style="width:100%;height:400px;"></div>
            </el-card>
            <el-card style="width: 20%;margin: 0 10px;" v-if="isAuth('zhuhu','首页统计')">
                <div id="zhuhuChart2" style="width:100%;height:400px;"></div>
            </el-card>
            <el-card style="width: 20%;margin: 0 10px;" v-if="isAuth('laifangdengji','首页统计')">
                <div id="laifangdengjiChart1" style="width:100%;height:400px;"></div>
            </el-card>
            <el-card style="width: 20%;margin: 0 10px;" v-if="isAuth('churudengji','首页统计')">
                <div id="churudengjiChart1" style="width:100%;height:400px;"></div>
            </el-card>
            <el-card style="width: 20%;margin: 0 10px;" v-if="isAuth('gaoweiloudong','首页统计')">
                <div id="gaoweiloudongChart1" style="width:100%;height:400px;"></div>
            </el-card>
        </div>
    </div>
</div>
</template>
<script>
//5
import router from '@/router/router-static'
import * as echarts from 'echarts'
export default {
	data() {
		return {
            zhuhuCount: 0,
            laifangdengjiCount: 0,
            churudengjiCount: 0,
            gaoweiloudongCount: 0,
		};
	},
  mounted(){
    this.init();
    this.getzhuhuCount();
    this.zhuhuChat1();
    this.zhuhuChat2();
    this.getlaifangdengjiCount();
    this.laifangdengjiChat1();
    this.getchurudengjiCount();
    this.churudengjiChat1();
    this.getgaoweiloudongCount();
    this.gaoweiloudongChat1();
  },
  methods:{
    init(){
        if(this.$storage.get('Token')){
        this.$http({
            url: `${this.$storage.get('sessionTable')}/session`,
            method: "get"
        }).then(({ data }) => {
            if (data && data.code != 0) {
            router.push({ name: 'login' })
            }
        });
        }else{
            router.push({ name: 'login' })
        }
    },
    getzhuhuCount() {
        this.$http({
            url: `zhuhu/count`,
            method: "get"
        }).then(({
            data
        }) => {
            if (data && data.code == 0) {
                this.zhuhuCount = data.data
            }
        })
    },

    zhuhuChat1() {
      this.$nextTick(()=>{

        var zhuhuChart1 = echarts.init(document.getElementById("zhuhuChart1"),'macarons');
        this.$http({
            url: "zhuhu/group/fanzuiqianke",
            method: "get",
        }).then(({ data }) => {
            if (data && data.code === 0) {
                let res = data.data;
                let xAxis = [];
                let yAxis = [];
                let pArray = []
                for(let i=0;i<res.length;i++){
                    xAxis.push(res[i].fanzuiqianke);
                    yAxis.push(parseFloat((res[i].total)));
                    pArray.push({
                        value: parseFloat((res[i].total)),
                        name: res[i].fanzuiqianke
                    })
                }
                var option = {};
                option = {
                        title: {
                            text: '犯罪前科',
                            left: 'center'
                        },
                        tooltip: {
                          trigger: 'item',
                          formatter: '{b} : {c} ({d}%)'
                        },
                        series: [
                            {
                                type: 'pie',
                                radius: '55%',
                                center: ['50%', '60%'],
                                data: pArray,
                                emphasis: {
                                    itemStyle: {
                                        shadowBlur: 10,
                                        shadowOffsetX: 0,
                                        shadowColor: 'rgba(0, 0, 0, 0.5)'
                                    }
                                }
                            }
                        ]
                };
                // 使用刚指定的配置项和数据显示图表。
                zhuhuChart1.setOption(option);
                  //根据窗口的大小变动图表
                window.onresize = function() {
                    zhuhuChart1.resize();
                };
            }
        });
      })
    },

    zhuhuChat2() {
      this.$nextTick(()=>{

        var zhuhuChart2 = echarts.init(document.getElementById("zhuhuChart2"),'macarons');
        this.$http({
            url: "zhuhu/group/nianling",
            method: "get",
        }).then(({ data }) => {
            if (data && data.code === 0) {
                let res = data.data;
                let xAxis = [];
                let yAxis = [];
                let pArray = []
                for(let i=0;i<res.length;i++){
                    xAxis.push(res[i].nianling);
                    yAxis.push(parseFloat((res[i].total)));
                    pArray.push({
                        value: parseFloat((res[i].total)),
                        name: res[i].nianling
                    })
                }
                var option = {};
                option = {
                    title: {
                        text: '年龄段',
                        left: 'center'
                    },
                    tooltip: {
                      trigger: 'item',
                      formatter: '{b} : {c}'
                    },
                    xAxis: {
                        type: 'category',
                        data: xAxis
                    },
                    yAxis: {
                        type: 'value'
                    },
                    series: [{
                        data: yAxis,
                        type: 'bar'
                    }]
                };
                // 使用刚指定的配置项和数据显示图表。
                zhuhuChart2.setOption(option);
                  //根据窗口的大小变动图表
                window.onresize = function() {
                    zhuhuChart2.resize();
                };
            }
        });
      })
    },





    getlaifangdengjiCount() {
        this.$http({
            url: `laifangdengji/count`,
            method: "get"
        }).then(({
            data
        }) => {
            if (data && data.code == 0) {
                this.laifangdengjiCount = data.data
            }
        })
    },

    laifangdengjiChat1() {
      this.$nextTick(()=>{

        var laifangdengjiChart1 = echarts.init(document.getElementById("laifangdengjiChart1"),'macarons');
        this.$http({
            url: "laifangdengji/group/zhuhuxingming",
            method: "get",
        }).then(({ data }) => {
            if (data && data.code === 0) {
                let res = data.data;
                let xAxis = [];
                let yAxis = [];
                let pArray = []
                for(let i=0;i<res.length;i++){
                    xAxis.push(res[i].zhuhuxingming);
                    yAxis.push(parseFloat((res[i].total)));
                    pArray.push({
                        value: parseFloat((res[i].total)),
                        name: res[i].zhuhuxingming
                    })
                }
                var option = {};
                option = {
                    title: {
                        text: '来访统计',
                        left: 'center'
                    },
                    tooltip: {
                      trigger: 'item',
                      formatter: '{b} : {c}'
                    },
                    xAxis: {
                        type: 'category',
                        data: xAxis
                    },
                    yAxis: {
                        type: 'value'
                    },
                    series: [{
                        data: yAxis,
                        type: 'bar'
                    }]
                };
                // 使用刚指定的配置项和数据显示图表。
                laifangdengjiChart1.setOption(option);
                  //根据窗口的大小变动图表
                window.onresize = function() {
                    laifangdengjiChart1.resize();
                };
            }
        });
      })
    },






    getchurudengjiCount() {
        this.$http({
            url: `churudengji/count`,
            method: "get"
        }).then(({
            data
        }) => {
            if (data && data.code == 0) {
                this.churudengjiCount = data.data
            }
        })
    },

    churudengjiChat1() {
      this.$nextTick(()=>{

        var churudengjiChart1 = echarts.init(document.getElementById("churudengjiChart1"),'macarons');
        this.$http({
            url: "churudengji/group/leixing",
            method: "get",
        }).then(({ data }) => {
            if (data && data.code === 0) {
                let res = data.data;
                let xAxis = [];
                let yAxis = [];
                let pArray = []
                for(let i=0;i<res.length;i++){
                    xAxis.push(res[i].leixing);
                    yAxis.push(parseFloat((res[i].total)));
                    pArray.push({
                        value: parseFloat((res[i].total)),
                        name: res[i].leixing
                    })
                }
                var option = {};
                option = {
                        title: {
                            text: '进出分析',
                            left: 'center'
                        },
                        tooltip: {
                          trigger: 'item',
                          formatter: '{b} : {c} ({d}%)'
                        },
                        series: [
                            {
                                type: 'pie',
                                radius: ['25%', '55%'],
                                roseType: 'area',
                                center: ['50%', '60%'],
                                data: pArray,
                                emphasis: {
                                    itemStyle: {
                                        shadowBlur: 10,
                                        shadowOffsetX: 0,
                                        shadowColor: 'rgba(0, 0, 0, 0.5)'
                                    }
                                }
                            }
                        ]
                };
                // 使用刚指定的配置项和数据显示图表。
                churudengjiChart1.setOption(option);
                  //根据窗口的大小变动图表
                window.onresize = function() {
                    churudengjiChart1.resize();
                };
            }
        });
      })
    },






    getgaoweiloudongCount() {
        this.$http({
            url: `gaoweiloudong/count`,
            method: "get"
        }).then(({
            data
        }) => {
            if (data && data.code == 0) {
                this.gaoweiloudongCount = data.data
            }
        })
    },

    gaoweiloudongChat1() {
      this.$nextTick(()=>{

        var gaoweiloudongChart1 = echarts.init(document.getElementById("gaoweiloudongChart1"),'macarons');
        this.$http({
            url: "gaoweiloudong/group/gaoweizhuangtai",
            method: "get",
        }).then(({ data }) => {
            if (data && data.code === 0) {
                let res = data.data;
                let xAxis = [];
                let yAxis = [];
                let pArray = []
                for(let i=0;i<res.length;i++){
                    xAxis.push(res[i].gaoweizhuangtai);
                    yAxis.push(parseFloat((res[i].total)));
                    pArray.push({
                        value: parseFloat((res[i].total)),
                        name: res[i].gaoweizhuangtai
                    })
                }
                var option = {};
                option = {
                        title: {
                            text: '高危比例',
                            left: 'center'
                        },
                        tooltip: {
                          trigger: 'item',
                          formatter: '{b} : {c} ({d}%)'
                        },
                        series: [
                            {
                                type: 'pie',
                                radius: '55%',
                                center: ['50%', '60%'],
                                data: pArray,
                                emphasis: {
                                    itemStyle: {
                                        shadowBlur: 10,
                                        shadowOffsetX: 0,
                                        shadowColor: 'rgba(0, 0, 0, 0.5)'
                                    }
                                }
                            }
                        ]
                };
                // 使用刚指定的配置项和数据显示图表。
                gaoweiloudongChart1.setOption(option);
                  //根据窗口的大小变动图表
                window.onresize = function() {
                    gaoweiloudongChart1.resize();
                };
            }
        });
      })
    },






  }
};
</script>
<style lang="scss" scoped>
    .cardView {
        display: flex;
        flex-wrap: wrap;
        width: 100%;

        .cards {
            display: flex;
            align-items: center;
            width: 100%;
            margin-bottom: 10px;
            justify-content: center;
            .card {
                width: calc(25% - 20px);
                margin: 0 10px;
                /deep/.el-card__body{
                    padding: 0;
                }
            }
        }
    }
</style>
