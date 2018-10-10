<template>
  <div class="columns">
    <div class="icontent-wrapper" v-if="icons.length > 0">
      <span v-if="query != ''">
        Results ({{ icons.length }})
        <br>
      </span>
      <span v-for="icon in icons">
        <div class="card">
          <header class="card-header">
            <p class="card-header-title">
              <b>{{ icon.name }}</b>
            </p>
            <span class="card-header-icon has-text-grey-light" aria-label="more options">
              <small class="tag is-light">{{ icon.category }}</small><small class="tag is-light">{{ icon.version }}</small>
            </span>
          </header>
          <div class="card-content">
            <div class="content">
              <div class="columns is-mobile">
                <div class="column vc h5em">
                  <i v-clipboard:copy="getCopyText('fontawesome','html',icon, 5)"
                     v-clipboard:success="onCopy"
                     :class="'pointer fa fa-5x '+icon.class">
                  </i>
                </div>
                <div class="column vc h5em">
                  <i v-clipboard:copy="getCopyText('fontawesome','html',icon, 4)"
                  v-clipboard:success="onCopy"
                  :class="'pointer fa fa-4x '+icon.class"></i>
                </div>
                <div class="column vc h5em">
                  <i v-clipboard:copy="getCopyText('fontawesome','html',icon, 3)"
                  v-clipboard:success="onCopy"
                  :class="'pointer fa fa-3x '+icon.class"></i>
                </div>
                <div class="column vc h5em">
                  <i v-clipboard:copy="getCopyText('fontawesome','html',icon, 2)"
                  v-clipboard:success="onCopy"
                  :class="'pointer fa fa-2x '+icon.class"></i>
                </div>
                <div class="column vc h5em">
                  <i v-clipboard:copy="getCopyText('fontawesome','html',icon, 1)"
                  v-clipboard:success="onCopy"
                  :class="'pointer fa '+icon.class"></i>
                </div>
              </div>
            </div>
          </div>
          <footer class="card-footer">
            <div class="card-footer-item pointer">
              <span v-clipboard:copy="getCopyText('fontawesome','square-o',icon, 0)" v-clipboard:success="onCopy" class="fa-stack fa-lg">
                <i class="fa fa-square-o fa-stack-2x"></i>
                <i :class="'fa '+icon.class+' fa-stack-1x'"></i>
              </span>
            </div>
            <span class="card-footer-item pointer">
              <span v-clipboard:copy="getCopyText('fontawesome','circle',icon, 0)" v-clipboard:success="onCopy" class="fa-stack fa-lg">
                <i class="fa fa-circle fa-stack-2x"></i>
                <i :class="'fa '+icon.class+' fa-stack-1x fa-inverse'"></i>
              </span>
            </span>
            <span v-clipboard:copy="getCopyText('fontawesome','square',icon, 0)" v-clipboard:success="onCopy" class="card-footer-item pointer">
              <span class="fa-stack fa-lg">
                <i class="fa fa-square fa-stack-2x"></i>
                <i :class="'fa '+icon.class+' fa-stack-1x fa-inverse'"></i>
              </span>
            </span>
            <span v-clipboard:copy="getCopyText('fontawesome','ban',icon, 0)" v-clipboard:success="onCopy" class="card-footer-item pointer">
              <span class="fa-stack fa-lg">
                <i :class="'fa '+icon.class+' fa-stack-1x'"></i>
                <i class="fa fa-ban fa-stack-2x has-text-danger"></i>
              </span>
            </span>
            <a v-clipboard:copy="getCopyText('fontawesome','unicode', icon, 0)" v-clipboard:success="onCopy" class="card-footer-item"><small class="has-text-grey-light">[{{icon.unicode}}]</small></a>
          </footer>
        </div>
      </span>
    </div>
    <div v-else>
      <span v-if="query != '' && icons.length == 0">
        <span v-if='loading'>
          <div class="loader"></div>
        </span>
        <span v-else>
          <hr class="nmb">
          No results
          <br>
        </span>
      </span>
        <div class="card">
          <header class="card-header">
            <p class="card-header-title">
                <img src="./assets/fontawesome.svg"> Font Awesome Icons
                <small>
                  <a target="_blank" href="http://fontawesome.io" class="card-header-icon has-text-grey" aria-label="more options">
                      <i class="fa fa-link" aria-hidden="true"></i>
                  </a>
                </small>
            </p>
            <a href="https://fontawesome.com/v4.7.0/" target="_blank" class="card-header-icon has-text-primary" aria-label="more options">
              <i class="fa fa-download" aria-hidden="true" style="padding-right: 5px;"></i> Download
            </a>
          </header>
          <div class="card-content">
            <div class="content">
              <p>
              <ol>
                <li><b><span class="has-text-info">Font Awesome CDN</span></b></li>
                <li>Font Awesome CDN is the easiest way to get Font Awesome on your website or app, all with just a single line of code. No downloading or installing!</li>
                <li>Copy your code & place near the top of your HTML's <code>&lt;head&gt;</code></li><br>
                <li><small><b>CDN link:</b></small><pre><code class="html"><span class="nt">&lt;script</span><span class="na"> src=</span><span class="s">"https://use.fontawesome.com/452826394c.js"</span><span>&gt;</span> <span class="nt">&lt;script&gt;</span>
                  </code></pre>
                </li>
                <hr>
                <li><b><span class="has-text-info">Download and Customize</span></b><br></li>
                <li>Copy the entire <code>font-awesome</code> directory into your project.</li><br>
                <li>
                  In the <code>&lt;head&gt;</code> of your html, reference the location to your font-awesome.min.css.
                </li>
                <li>
                   <pre><code class="html"><span class="nt">&lt;link</span> <span class="na">rel=</span><span class="s">"stylesheet"</span> <span class="na">href=</span><span class="s">"path/to/font-awesome/css/font-awesome.min.css"</span><span class="nt">&gt;</span>
                  </code></pre>
                </li>
              </ol>
              </p>
            </div>
          </div>
        </div>
    </div>
    <div v-if="isVisible" class="overlay vc">
      <p><i class="fa fa-lg fa-clipboard"></i> Copied to clipboard!</p>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'FontAwesome',
    component: [ ],
    data () {
      return {
        isVisible: false
      }
    },
    props: ['query', 'icons', 'loading'],
    mounted: function () {
    },
    methods: {
      onCopy: function (e) {
        this.isVisible = true
        var that = this
        setTimeout(function () {
          that.isVisible = false
        }, 3000)
      },
      getCopyText: function (library, type, icon, size) {
        if (type === 'html') {
          if (size <= 1) {
            return '<i class="fa fa-lg ' + icon.class + '"></i>'
          } else {
            return '<i class="fa fa-' + size + 'x ' + icon.class + '"></i>'
          }
        } else if (type === 'square-o') {
          return '<span class="fa-stack fa-lg"><i class="fa fa-square-o fa-stack-2x"></i><i class="fa ' + icon.class + ' fa-stack-1x"></i></span>'
        } else if (type === 'circle') {
          return '<span class="fa-stack fa-lg"><i class="fa fa-circle fa-stack-2x"></i><i class="fa ' + icon.class + ' fa-stack-1x fa-inverse"></i></span>'
        } else if (type === 'square') {
          return '<span class="fa-stack fa-lg"><i class="fa fa-square fa-stack-2x"></i><i class="fa ' + icon.class + ' fa-stack-1x fa-inverse"></i></span>'
        } else if (type === 'ban') {
          return '<span class="fa-stack fa-lg"><i class="fa ' + icon.class + ' fa-stack-1x"></i><i class="fa fa-ban fa-stack-2x has-text-danger"></i></span>'
        } else {
          return icon.unicode
        }
      }
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
@import 'https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css';

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
