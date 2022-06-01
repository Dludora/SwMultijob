const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  devServer: {
    proxy:{
      // 当我们的本地的请求 有/api的时候，就会代理我们的请求地址向另外一个服务器发出请求
      // 这里的api 表示如果我们的请求地址有/api的时候,就出触发代理机制
      // localhost:8888/api/abc  => 代理给另一个服务器
      '/api':{
        // 目标路径,一般是后台服务器地址
        target:'http://127.0.0.1:8000/',
        // 允许跨域
        changeOrigin: true,
        // 重写路径
        pathRewrite: {
          // 重写路由  localhost:8888/api/login  => www.baidu.com/api/login
          '^/api': '' // 假设我们想把 localhost:8888/api/login 变成www.baidu.com/login 就需要这么做
        }
      }
    }
  },
})
