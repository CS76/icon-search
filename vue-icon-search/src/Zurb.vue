<template>
  <div>
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
            <div class="content has-text-centered">
              <div class="columns is-mobile">
                <div class="column vc h5em">
                  <span>
                    <i :class="icon.class+' large'"></i><br>
                    <small class="has-text-grey-light">
                        <a v-clipboard:copy="getCopyText('foundation','html',icon, 3)"
                    v-clipboard:success="onCopy">HTML</a> | <a v-clipboard:copy="getCopyText('foundation','css',icon, 3)"
                    v-clipboard:success="onCopy">CSS</a>
                    </small>
                  </span>
                </div>
                <div class="column vc h5em">
                  <span>
                    <i :class="icon.class+' medium'"></i><br>
                    <small class="has-text-grey-light">
                        <a v-clipboard:copy="getCopyText('foundation','html',icon, 2)"
                    v-clipboard:success="onCopy">HTML</a> | <a v-clipboard:copy="getCopyText('foundation','css',icon, 2)"
                    v-clipboard:success="onCopy">CSS</a>
                    </small>
                  </span>
                </div>
                <div class="column vc h5em">
                  <span>
                    <i :class="icon.class+' small'"></i><br>
                    <small class="has-text-grey-light">
                        <a v-clipboard:copy="getCopyText('foundation','html',icon, 1)"
                    v-clipboard:success="onCopy">HTML</a> | <a v-clipboard:copy="getCopyText('foundation','css',icon, 1)"
                    v-clipboard:success="onCopy">CSS</a>
                      </small>
                  </span>
                </div>
                
              </div>
            </div>
          </div>
          <footer class="card-footer">
            <span class="card-footer-item pointer">
              <a v-clipboard:copy="getCopyText('foundation','css',icon, 4)"
                    v-clipboard:success="onCopy">
                <i :class="icon.class+' style1'"></i>
              </a>
            </span>
            <span class="card-footer-item pointer">
              <a v-clipboard:copy="getCopyText('foundation','css',icon, 5)"
                    v-clipboard:success="onCopy">
                <i :class="icon.class+' style2'"></i>
              </a>
            </span>
            <span class="card-footer-item pointer">
              <a v-clipboard:copy="getCopyText('foundation','css',icon, 6)"
                    v-clipboard:success="onCopy">
                <i :class="icon.class+' style3'"></i>
              </a>
            </span>
            <span class="card-footer-item pointer">
              <a v-clipboard:copy="getCopyText('foundation','css',icon, 7)"
                    v-clipboard:success="onCopy">
                <i :class="icon.class+' style4'"></i>
              </a>
            </span>
            <span class="card-footer-item pointer">
              <a v-clipboard:copy="getCopyText('foundation','css',icon, 8)"
                    v-clipboard:success="onCopy">
                <i :class="icon.class+' style5'"></i>
              </a>
            </span>
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
                <img style="height: 18px; margin: 5px 0" src="./assets/zurb.svg">
                <small>
                  <a target="_blank" href="https://zurb.com/playground/foundation-icon-fonts-3" class="card-header-icon has-text-grey" aria-label="more options">
                      <i class="fa fa-link" aria-hidden="true"></i>
                  </a>
                </small>
            </p>
            <a href="http://zurb.com/playground/uploads/upload/upload/288/foundation-icons.zip" class="card-header-icon has-text-primary" aria-label="more options">
              <i class="fa fa-download" aria-hidden="true" style="padding-right: 5px;"></i> Download
            </a>
          </header>
          <div class="card-content">
            <div class="content">
              <p>
                <b><span class="has-text-info">How to use them</span></b>
                <ol>
                  <li>Zurb has made it super easy for you to get going with these icons! Just <a href="http://zurb.com/playground/uploads/upload/upload/287/foundation-icon-font-3.zip">download the font</a> and follow these simple instructions. You'll be rockin’ in no time.</li><br>
                  <hr>
                  <li><span class="has-text-info"><b>Merge in the styles</b></span></li><br>
                  <li>It's really easy to hook up the pack's stylesheets to bring your new icon web font to life. When you download the fonts, you'll be able to simply merge the <code>foundation-icons.css</code> and <code>foundation-icons.[eot/ttf/svg/woff]</code> files straight into Foundation.</li><br>
                  <hr>
                  <li><span class="has-text-info"><b>Write your markup</b></span></li><br>
                  <li>We've used an <strong>&lt;i&gt;</strong> for icon elements. You just simply apply the appropriate classes that match the icon you want to use. Here's what the markup looks like:</li>
                  <li>
                    <pre><code class="html"><span class="nt">&lt;i</span> <span class="na">class=</span><span class="s">"fi-[icon]"</span><span>&gt;</span><span>&lt;/i&gt;</span>
                    </code></pre>
                  </li><br>
                  <hr>
                  <li><span class="has-text-info"><b>Style away!</b></span></li><br>
                  <li>You can use some awesome CSS techniques to start exploring different styles. Zurb - Foundation come up with a few ourselves, check them out:</li>
                  <li>
                    <ul class="icon-styles large-block-grid-5 small-block-grid-3">
                      <li><i class="fi-heart style3"></i></li>
                      <li><i class="fi-compass style5"></i></li>
                      <li><i class="fi-social-zurb style1"></i></li>
                      <li><i class="fi-cloud style2"></i></li>
                      <li><i class="fi-clipboard-notes style4"></i></li>
                    </ul>
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
          if (size === 3) {
            return '<i class="' + icon.class + ' large"></i>'
          } else if (size === 2) {
            return '<i class="' + icon.class + ' medium"></i>'
          } else {
            return '<i class="' + icon.class + ' small"></i>'
          }
        } else if (type === 'css') {
          if (size === 8) {
            return '.style5 { font-size: 50px; color: rgba(245, 159, 26, 0.8); text-shadow: 1px 4px 6px #FFF, 0 0 0 #000, 1px 4px 6px #FFF; }'
          } else if (size === 7) {
            return '.style4 { font-size: 50px; text-shadow: 0 1px 3px rgba(0,0,0,0.25); color: #A9014B; }'
          } else if (size === 6) {
            return '.style3 { font-size: 50px; color: #E33100; text-shadow: 0 0 5px #fff, 0 0 10px #fff, 0 0 15px #fff, 0 0 20px #E33100, 0 0 30px #E33100, 0 0 40px #E33100, 0 0 50px #E33100, 0 0 75px #E33100; }'
          } else if (size === 5) {
            return '.style2 { font-size: 50px; color: #2DAEBF; text-shadow: 0px 1px 0px #0092b3, 0px 2px 0px #0087a6, 0px 3px 0px #008099, 0px 4px 0px #00758c, 0px 5px 0px #555, 0px 6px 0px #006a80, 0px 0px 0px #006073, 0px 8px 7px #005566; }'
          } else if (size === 4) {
            return '.style1 { font-size: 50px; color: #B8D30B; }'
          } else if (size === 3) {
            return '.large{ font-size: 50px; line-height: 50px; }'
          } else if (size === 2) {
            return '.medium { font-size: 35px; padding: 0 5px; }'
          } else {
            return '.small { font-size: 20px; padding: 0 5px; }'
          }
        }
      }
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
@import 'https://cdn.jsdelivr.net/foundation-icons/3.0/foundation-icons.min.css';

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
