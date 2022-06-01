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
app.use(VueAxios,axios);
app.mount('#app')

