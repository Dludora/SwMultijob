const { defineConfig } = require('@vue/cli-service')
const path = require("path");
module.exports = defineConfig({
	transpileDependencies: true,
	// configureWebpack: {
	//     module: {
    // 	  rules: [
    //     	// 配置读取 *.md 文件的规则
    //     	{
    //       		test: /\.md$/,
    //       		use: [
    //         		{ loader: "html-loader" },
    //         		{ loader: "markdown-loader", options: {} }
    //       		]
    //     	}
	// 		]
	// 	}
  	// },
});