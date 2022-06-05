import { createApp } from 'vue'
import axios from 'axios'
import VueAxios from "vue-axios"
import ElementPlus from 'element-plus'

import 'element-plus/dist/index.css'
import PrimeVue from 'primevue/config'
import App from './App.vue'
import router from './router'
import store from './store'


import 'primevue/resources/themes/saga-blue/theme.css'       //theme
import 'primevue/resources/primevue.min.css'                 //core css
import 'primeicons/primeicons.css'                           //icons
import "primeflex/primeflex.css";
import './assets/style/reset.css'

const app = createApp(App)
app.use(ElementPlus)
app.use(store)
app.use(router)
app.use(PrimeVue)
app.use(VueAxios,axios)

app.mount('#app')
axios.defaults.baseURL = "http://127.0.0.1:8000/api/backend/"

// 引入所有语言包
import hljs from 'highlight.js'


import VMdPreview from '@kangc/v-md-editor/lib/preview';
import '@kangc/v-md-editor/lib/style/preview.css';
import VMdEditor from '@kangc/v-md-editor/lib/codemirror-editor';
import '@kangc/v-md-editor/lib/style/codemirror-editor.css';
import githubTheme from '@kangc/v-md-editor/lib/theme/github.js';
import '@kangc/v-md-editor/lib/theme/style/github.css';
// emoji
import createEmojiPlugin from '@kangc/v-md-editor/lib/plugins/emoji/index';
import '@kangc/v-md-editor/lib/plugins/emoji/emoji.css';
// 显示代码行数
import createLineNumbertPlugin from '@kangc/v-md-editor/lib/plugins/line-number/index';
// 快速复制
import createCopyCodePlugin from '@kangc/v-md-editor/lib/plugins/copy-code/index';
import '@kangc/v-md-editor/lib/plugins/copy-code/copy-code.css';
// 流程图
import createMermaidPlugin from '@kangc/v-md-editor/lib/plugins/mermaid/cdn';
import '@kangc/v-md-editor/lib/plugins/mermaid/mermaid.css';

VMdPreview.use(createMermaidPlugin());

// codemirror 编辑器的相关资源
import Codemirror from 'codemirror';
// mode
import 'codemirror/mode/markdown/markdown';
import 'codemirror/mode/javascript/javascript';
import 'codemirror/mode/css/css';
import 'codemirror/mode/htmlmixed/htmlmixed';
import 'codemirror/mode/vue/vue';
// edit
import 'codemirror/addon/edit/closebrackets';
import 'codemirror/addon/edit/closetag';
import 'codemirror/addon/edit/matchbrackets';
// placeholder
import 'codemirror/addon/display/placeholder';
// active-line
import 'codemirror/addon/selection/active-line';
// scrollbar
import 'codemirror/addon/scroll/simplescrollbars';
import 'codemirror/addon/scroll/simplescrollbars.css';
// style
import 'codemirror/lib/codemirror.css';

VMdEditor.Codemirror = Codemirror;
VMdEditor.use(githubTheme, {
  Hljs: hljs,
});
VMdPreview.use(githubTheme, {
  Hljs: hljs,
});
VMdPreview.use(createEmojiPlugin());
VMdPreview.use(createLineNumbertPlugin());
VMdPreview.use(createCopyCodePlugin());
app.use(VMdEditor);
app.use(VMdPreview);

// 登录保持
// router.beforeEach((to, from, next) => {
//   store.commit('getToken')
//   const token = store.state.user.token
//   if(!token && to.name !== 'login') {
//     next({ name: 'login' })
//   } else {
//     next()
//   }
// })
