import Vue from 'vue'
import IconSearch from './IconSearch.vue'
import VueClipboard from 'vue-clipboard2'
import router from './router'

Vue.config.productionTip = false

Vue.use(VueClipboard)

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  render: h => h(IconSearch)
})
