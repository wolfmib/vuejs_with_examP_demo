import Vue from 'vue'
import App from './App.vue' //Entry Point

// [Mary]: Step_01: 
    // Register Bootstrap in your app entry-point:
import { BootstrapVue } from 'bootstrap-vue'

// [Mary]: Step_02:
      // Importer des fichiers css

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'



// Steo_01: Install BootstrapVue
Vue.use(BootstrapVue)
Vue.config.productionTip = false



new Vue({
  render: h => h(App),
}).$mount('#app')
