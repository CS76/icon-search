<template>
  <div class="container is-fluid">
    <div class="columns is-mobile has-text-left">
      <div class="column">
        <div class="content-wrapper">
          <div class="sources has-text-centered">
            <span v-for="resource in resources">
              <button @click="changeSelectedResource(resource)" :class="[selectedResource == resource ? 'is-primary' : '']" class="button is-small"><b><span class="capitalize">{{ resource }}</span></b></button> 
            </span>    
          </div>
          <div class="field">
            <label class="label has-text-grey" for="search">Search <span class="capitalize">{{ selectedResource }}</span> Icons </label>
            <div class="columns is-mobile">
              <div class="column is-three-quarters">
                <p class="control has-icons-left has-icons-right">
                  <input autocomplete="off" name="search" class="input" type="text" v-model="query" v-on:keyup="search">
                  <span class="icon is-small is-left">
                    <i class="fa fa-search"></i>
                  </span>
                </p>
              </div>
              <div class="column">
                <img style="margin-top: 10px;" src="https://www.algolia.com/assets/pricing_new/algolia-powered-by-ac7dba62d03d1e28b0838c5634eb42a9.svg" alt="">
              </div>
            </div>
          </div>
          <div v-if="selectedResource == 'fontawesome5'">
            <fontawesome-5 :query="query" :loading="loading" :icons="icons">
            </fontawesome-5>
          </div>
          <div v-if="selectedResource == 'fontawesome'">
            <fontawesome :query="query" :loading="loading" :icons="icons"></fontawesome>
          </div>
          <div v-if="selectedResource == 'foundation'">
            <zurb :query="query" :loading="loading" :icons="icons"></zurb>
          </div>
          <div v-if="selectedResource == 'material'">
            <material :query="query" :loading="loading" :icons="icons"></material>
          </div>
          <div v-if="selectedResource == 'iconic'">
            <iconic :query="query" :loading="loading" :icons="icons"></iconic>
          </div>
          <div>
              <small>
                <span>
                  <a target="_blank" class="has-text-black-bis" href="https://opensource.org/">
                    <img src="https://opensource.org/files/osi_keyhole_300X300_90ppi_0.png" style="height: 14px;"> MIT license</a>   |  <a target="_blank" class="has-text-black-bis" href="https://github.com/CS76/icon-search"> <i class="fab fa-github"></i> GitHub</a>
                </span>
                <span class="is-pulled-right">
                  Made with <i class="fa fa-heart has-text-danger"></i> by <a href="https://twitter.com/mailcs76">CS76</a>
                </span>
              </small>  
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
  import algoliasearch from 'algoliasearch'
  import FontAwesome5 from './FontAwesome5.vue'
  import FontAwesome from './FontAwesome.vue'
  import Material from './Material.vue'
  import Zurb from './Zurb.vue'
  import Iconic from './Iconic.vue'
  
  export default {
    name: 'icon-search',
    components: {
      'fontawesome-5': FontAwesome5,
      'fontawesome' : FontAwesome,
      'material' : Material,
      'zurb' : Zurb,
      'iconic' : Iconic
    },
    data () {
      return {
        query: '',
        client: null,
        index: null,
        resources: [ 'fontawesome5' , 'fontawesome', 'foundation', 'material', 'iconic' ],
        selectedResource: 'fontawesome5',
        icons: [],        
        loading: false
      }
    },
    mounted: function () {
      this.client = algoliasearch('OMA2ZHV973', '8c9692471755b1485c8478332779b4fa')
      this.index = this.client.initIndex('icon-search')
    },
    methods: {
      search: function () {
        var that = this
        this.loading = true;
        this.index.search({ query: this.query, hitsPerPage: 3000, filters: 'source:' + that.selectedResource }, function searchDone (err, content) {
          that.loading = false
          if (err) {
            console.error(err)
            return
          }
          if (that.query === '') {
            that.icons = []
            
          } else {
            that.icons = content.hits
          }
        })
      },
      changeSelectedResource: function (selection) {
        this.icons = []
        this.query = ''
        this.selectedResource = selection
      }
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
html, body{
  font-size: 0.8em;
}

.loader,
.loader:before,
.loader:after {
  border-radius: 50%;
  width: 2.5em;
  height: 2.5em;
  -webkit-animation-fill-mode: both;
  animation-fill-mode: both;
  -webkit-animation: load7 1.8s infinite ease-in-out;
  animation: load7 1.8s infinite ease-in-out;
}
.loader {
  color: inherit;
  font-size: 10px;
  margin: 50px auto;
  position: relative;
  text-indent: -9999em;
  -webkit-transform: translateZ(0);
  -ms-transform: translateZ(0);
  transform: translateZ(0);
  -webkit-animation-delay: -0.16s;
  animation-delay: -0.16s;
  border: none;
}
.loader:before,
.loader:after {
  content: '';
  position: absolute;
  top: 0;
}
.loader:before {
  left: -3.5em;
  -webkit-animation-delay: -0.32s;
  animation-delay: -0.32s;
}
.loader:after {
  left: 3.5em;
}
@-webkit-keyframes load7 {
  0%,
  80%,
  100% {
    box-shadow: 0 2.5em 0 -1.3em;
  }
  40% {
    box-shadow: 0 2.5em 0 0;
  }
}
@keyframes load7 {
  0%,
  80%,
  100% {
    box-shadow: 0 2.5em 0 -1.3em;
  }
  40% {
    box-shadow: 0 2.5em 0 0;
  }
}

.nmb{
  margin-bottom: 5px;
}

::-webkit-scrollbar {
    width: 0px;
    background: transparent; /* make scrollbar transparent */
}


.material-icons.md-18 { font-size: 18px; }
.material-icons.md-24 { font-size: 24px; }
.material-icons.md-36 { font-size: 36px; }
.material-icons.md-48 { font-size: 48px; }

/* Rules for using icons as black on a light background. */
.material-icons.md-dark { color: rgba(0, 0, 0, 0.54); }
.material-icons.md-dark.md-inactive { color: rgba(0, 0, 0, 0.26); }

/* Rules for using icons as white on a dark background. */
.material-icons.md-light { color: rgba(255, 255, 255, 1); }
.material-icons.md-light.md-inactive { color: rgba(255, 255, 255, 0.3); }

h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

.capitalize {
  text-transform: capitalize;
}

a {
  color: #181AEF;
}

p{
  font-size: 0.9em;
}

button{
  margin: 0 3px;
}

.label{
  font-size: 0.8em;
}

.sources{
  border: 1px solid #f1f1f4;
  padding: 10px 5px;
  margin-bottom: 20px;
  border-radius: 4px;
}

.button.is-primary{
  background-color: #181AEF;
}

.button.is-primary:hover, .button.is-primary.is-hovered {
    background-color: #181AEF;
}

.input:focus, .input.is-focused, .input:active, .input.is-active, .textarea:focus, .textarea.is-focused, .textarea:active, .textarea.is-active {
    border-color: #181AEF;
}

.h5em{
  height: 5em;
}

.h100{
  height: 100%;
}

.vc{
  display: flex;
  justify-content: center;
  align-items: center;
}

.card{
  margin-bottom: 15px;
  margin-top: 10px;
}

.tag{
  margin-left: 10px;
}

.pointer{
  cursor: pointer;
}

i:hover{
  color: #5BCEBF;
}

.overlay{
  position: absolute;
  bottom: 0;
  right: 0;
  margin: 20px;
  font-weight: bold;
  padding: 10px 30px;
  -webkit-box-shadow: 0 2px 3px rgba(10, 10, 10, 0.1), 0 0 0 1px rgba(10, 10, 10, 0.1);
  box-shadow: 0 2px 3px rgba(10, 10, 10, 0.1), 0 0 0 1px rgba(10, 10, 10, 0.1);
  background-color: rgba(0,0,0,0.7);
  color: #fff;
}

pre code {
    padding: 0;
    font-size: inherit;
    color: inherit;
    white-space: pre-wrap;
    background-color: transparent;
    border-radius: 0;
}

.content pre {
  display: block;
  padding: 15px;
  padding-bottom: 0px;
  font-size: 13px;
  line-height: 1.42857143;
  word-break: break-all;
  word-wrap: break-word;
  color: #333;
  background-color: #f5f5f5;
  border: 1px solid #eee;
  border-radius: 4px;
  white-space: pre-wrap;
  white-space: -moz-pre-wrap;
  white-space: -pre-wrap;
  white-space: -o-pre-wrap;
  word-wrap: break-word;
  padding-top: 10px;
  margin-top: 5px;
}

.content hr {
  margin: 1em -24px;
}

.card-header-title img{
  height: 30px;
  padding-right: 10px;
}

.card-header-title{
  line-height: 30px;
  font-size: 18px;
  font-weight: lighter;
  text-align: center;
  padding-left: 20px;
}

.content ol {
    margin-left: 0em;
    margin-top: 0;
}

.content ol li{
    margin-left: 0em;
    margin-bottom: 5px;
}

.white{
  border: 1px solid #f1f1f4;
  background-color: white;
  border-radius: 50%;
}

.black{
  border: 1px solid #f1f1f4;
  background-color: black;
  border-radius: 50%;
}

.large{ font-size: 50px; line-height: 50px; }
.medium { font-size: 35px; padding: 0 5px; }
.small { font-size: 20px; padding: 0 5px; }

.style1 { font-size: 50px; color: #B8D30B; }
.style2 { font-size: 50px; color: #2DAEBF; text-shadow: 0px 1px 0px #0092b3, 0px 2px 0px #0087a6, 0px 3px 0px #008099, 0px 4px 0px #00758c, 0px 5px 0px #555, 0px 6px 0px #006a80, 0px 0px 0px #006073, 0px 8px 7px #005566; }
.style3 { font-size: 50px; color: #E33100; text-shadow: 0 0 5px #fff, 0 0 10px #fff, 0 0 15px #fff, 0 0 20px #E33100, 0 0 30px #E33100, 0 0 40px #E33100, 0 0 50px #E33100, 0 0 75px #E33100; }
.style4 { font-size: 50px; text-shadow: 0 1px 3px rgba(0,0,0,0.25); color: #A9014B; }
.style5 { font-size: 50px; color: rgba(245, 159, 26, 0.8); text-shadow: 1px 4px 6px #FFF, 0 0 0 #000, 1px 4px 6px #FFF; }

.is-mobile{
  display: -webkit-box !important;
}

</style>
