import Vue from 'vue'
import IconSearch from './IconSearch.vue'
import VueClipboard from 'vue-clipboard2'

Vue.use(VueClipboard)
new Vue({
  el: '#app',
  render: h => h(IconSearch)
})
