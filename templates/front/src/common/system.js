export function isAuth(tableName, key) {
  let role = localStorage.getItem("UserTableName");
  let menus = [{"backMenu":[{"child":[{"appFrontIcon":"cuIcon-pay","buttons":["新增","查看","修改","删除","首页总数"],"menu":"住户","menuJump":"列表","tableName":"zhuhu"}],"menu":"住户管理"},{"child":[{"appFrontIcon":"cuIcon-news","buttons":["新增","查看","修改","删除","首页总数"],"menu":"来访登记","menuJump":"列表","tableName":"laifangdengji"}],"menu":"来访登记管理"},{"child":[{"appFrontIcon":"cuIcon-vip","buttons":["新增","查看","修改","删除","首页总数"],"menu":"出入登记","menuJump":"列表","tableName":"churudengji"}],"menu":"出入登记管理"},{"child":[{"appFrontIcon":"cuIcon-present","buttons":["新增","查看","修改","删除"],"menu":"物业催缴","menuJump":"列表","tableName":"wuyecuijiao"}],"menu":"物业催缴管理"},{"child":[{"appFrontIcon":"cuIcon-album","buttons":["查看","修改","删除","首页总数","新增"],"menu":"高危楼栋","menuJump":"列表","tableName":"gaoweiloudong"}],"menu":"高危楼栋管理"},{"child":[{"appFrontIcon":"cuIcon-taxi","buttons":["查看","修改"],"menu":"关于我们","tableName":"aboutus"},{"appFrontIcon":"cuIcon-link","buttons":["查看","修改"],"menu":"系统简介","tableName":"systemintro"},{"appFrontIcon":"cuIcon-full","buttons":["查看","修改"],"menu":"轮播图管理","tableName":"config"},{"appFrontIcon":"cuIcon-news","buttons":["新增","查看","修改","删除"],"menu":"社区公告","tableName":"news"}],"menu":"系统管理"}],"frontMenu":[],"hasBackLogin":"是","hasBackRegister":"否","hasFrontLogin":"否","hasFrontRegister":"否","roleName":"管理员","tableName":"users"},{"backMenu":[{"child":[{"appFrontIcon":"cuIcon-present","buttons":["查看","支付"],"menu":"物业催缴","menuJump":"列表","tableName":"wuyecuijiao"}],"menu":"物业催缴管理"},{"child":[{"appFrontIcon":"cuIcon-album","buttons":["查看"],"menu":"高危楼栋","menuJump":"列表","tableName":"gaoweiloudong"}],"menu":"高危楼栋管理"}],"frontMenu":[],"hasBackLogin":"是","hasBackRegister":"否","hasFrontLogin":"是","hasFrontRegister":"是","roleName":"住户","tableName":"zhuhu"}];
  for(let i=0;i<menus.length;i++){
    if(menus[i].tableName==role){
      for(let j=0;j<menus[i].frontMenu.length;j++){
          for(let k=0;k<menus[i].frontMenu[j].child.length;k++){
            if(tableName==menus[i].frontMenu[j].child[k].tableName){
              let buttons = menus[i].frontMenu[j].child[k].buttons.join(',');
              return buttons.indexOf(key) !== -1 || false
            }
          }
      }
    }
  }
  return false;
}

/**
 *  * 获取当前时间（yyyy-MM-dd hh:mm:ss）
 *   */
export function getCurDateTime() {
    let currentTime = new Date(),
    year = currentTime.getFullYear(),
    month = currentTime.getMonth() + 1 < 10 ? '0' + (currentTime.getMonth() + 1) : currentTime.getMonth() + 1,
    day = currentTime.getDate() < 10 ? '0' + currentTime.getDate() : currentTime.getDate(),
    hour = currentTime.getHours(),
    minute = currentTime.getMinutes(),
    second = currentTime.getSeconds();
    return year + "-" + month + "-" + day + " " +hour +":" +minute+":"+second;
}

/**
 *  * 获取当前日期（yyyy-MM-dd）
 *   */
export function getCurDate() {
    let currentTime = new Date(),
    year = currentTime.getFullYear(),
    month = currentTime.getMonth() + 1 < 10 ? '0' + (currentTime.getMonth() + 1) : currentTime.getMonth() + 1,
    day = currentTime.getDate() < 10 ? '0' + currentTime.getDate() : currentTime.getDate();
    return year + "-" + month + "-" + day;
}
