import VueRouter from 'vue-router'

//引入组件
import Index from '../pages'
import Home from '../pages/home/home'
import Login from '../pages/login/login'
import Register from '../pages/register/register'
import Center from '../pages/center/center'
import News from '../pages/news/news-list'
import NewsDetail from '../pages/news/news-detail'
import zhuhuList from '../pages/zhuhu/list'
import zhuhuDetail from '../pages/zhuhu/detail'
import zhuhuAdd from '../pages/zhuhu/add'
import laifangdengjiList from '../pages/laifangdengji/list'
import laifangdengjiDetail from '../pages/laifangdengji/detail'
import laifangdengjiAdd from '../pages/laifangdengji/add'
import churudengjiList from '../pages/churudengji/list'
import churudengjiDetail from '../pages/churudengji/detail'
import churudengjiAdd from '../pages/churudengji/add'
import wuyecuijiaoList from '../pages/wuyecuijiao/list'
import wuyecuijiaoDetail from '../pages/wuyecuijiao/detail'
import wuyecuijiaoAdd from '../pages/wuyecuijiao/add'
import gaoweiloudongList from '../pages/gaoweiloudong/list'
import gaoweiloudongDetail from '../pages/gaoweiloudong/detail'
import gaoweiloudongAdd from '../pages/gaoweiloudong/add'
import aboutusList from '../pages/aboutus/list'
import aboutusDetail from '../pages/aboutus/detail'
import aboutusAdd from '../pages/aboutus/add'

const originalPush = VueRouter.prototype.push
VueRouter.prototype.push = function push(location) {
	return originalPush.call(this, location).catch(err => err)
}

//配置路由
export default new VueRouter({
	routes:[
		{
      path: '/',
      redirect: '/index/home'
    },
		{
			path: '/index',
			component: Index,
			children:[
				{
					path: 'home',
					component: Home
				},
				{
					path: 'center',
					component: Center,
				},
				{
					path: 'news',
					component: News
				},
				{
					path: 'newsDetail',
					component: NewsDetail
				},
				{
					path: 'zhuhu',
					component: zhuhuList
				},
				{
					path: 'zhuhuDetail',
					component: zhuhuDetail
				},
				{
					path: 'zhuhuAdd',
					component: zhuhuAdd
				},
				{
					path: 'laifangdengji',
					component: laifangdengjiList
				},
				{
					path: 'laifangdengjiDetail',
					component: laifangdengjiDetail
				},
				{
					path: 'laifangdengjiAdd',
					component: laifangdengjiAdd
				},
				{
					path: 'churudengji',
					component: churudengjiList
				},
				{
					path: 'churudengjiDetail',
					component: churudengjiDetail
				},
				{
					path: 'churudengjiAdd',
					component: churudengjiAdd
				},
				{
					path: 'wuyecuijiao',
					component: wuyecuijiaoList
				},
				{
					path: 'wuyecuijiaoDetail',
					component: wuyecuijiaoDetail
				},
				{
					path: 'wuyecuijiaoAdd',
					component: wuyecuijiaoAdd
				},
				{
					path: 'gaoweiloudong',
					component: gaoweiloudongList
				},
				{
					path: 'gaoweiloudongDetail',
					component: gaoweiloudongDetail
				},
				{
					path: 'gaoweiloudongAdd',
					component: gaoweiloudongAdd
				},
				{
					path: 'aboutus',
					component: aboutusList
				},
				{
					path: 'aboutusDetail',
					component: aboutusDetail
				},
				{
					path: 'aboutusAdd',
					component: aboutusAdd
				},
			]
		},
		{
			path: '/login',
			component: Login
		},
		{
			path: '/register',
			component: Register
		},
	]
})
