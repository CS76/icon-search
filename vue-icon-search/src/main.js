import Vue from 'vue'
import IconSearch from './IconSearch.vue'
import VueClipboard from 'vue-clipboard2'
import VueAnalytics from 'vue-analytics'
import router from './router'

Vue.config.productionTip = false


Vue.use(VueClipboard);

Vue.use(VueAnalytics, {
  id: 'UA-107684006-1'
})

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  render: h => h(IconSearch)
})
