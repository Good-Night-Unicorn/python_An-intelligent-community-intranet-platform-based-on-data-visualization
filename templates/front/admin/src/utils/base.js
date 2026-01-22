const base = {
    get() {
        return {
            url : "http://localhost:8080/djangokm488/",
            name: "djangokm488",
            // 退出到首页链接
            indexUrl: 'http://localhost:8080/front/dist/index.html'
        };
    },
    getProjectName(){
        return {
            projectName: "基于数据可视化的智慧社区内网平台"
        } 
    }
}
export default base
