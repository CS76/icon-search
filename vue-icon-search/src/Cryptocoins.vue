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
              <span v-if="icon.prefix == 'far' || icon.prefix == 'fal'" class="tag is-info">
                PRO
              </span>
              <small class="tag is-light">{{ icon.version }}</small>
            </span>
          </header>
          <div class="card-content">
            <div class="content">
              <div class="columns is-mobile">
                <div class="column vc h10em">
                  <i v-clipboard:copy="getCopyText('cryptoicons','html', icon, 16)"
                  v-clipboard:success="onCopy"
                  :class="'pointer '+icon.class" style="font-size: 16px;"></i>
                </div>
                <div class="column vc h10em">
                  <i v-clipboard:copy="getCopyText('cryptoicons','html', icon, 24)"
                  v-clipboard:success="onCopy"
                  :class="'pointer '+icon.class" style="font-size: 24px;"></i>
                </div>
                <div class="column vc h10em">
                  <i v-clipboard:copy="getCopyText('cryptoicons','html', icon, 32)"
                  v-clipboard:success="onCopy"
                  :class="'pointer '+icon.class" style="font-size: 32px;"></i>
                </div>
                <div class="column vc h10em">
                  <i v-clipboard:copy="getCopyText('cryptoicons','html', icon, 48)"
                  v-clipboard:success="onCopy"
                  :class="'pointer '+icon.class" style="font-size: 48px;"></i>
                </div>
                <div class="column vc h10em">
                  <i v-clipboard:copy="getCopyText('cryptoicons','html', icon, 64)"
                  v-clipboard:success="onCopy"
                  :class="'pointer '+icon.class" style="font-size: 64px;"></i>
                </div>
              </div>
            </div>
          </div>
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
            <b>Cryptocoins <a target="_blank" href="https://github.com/AllienWorks/cryptocoins"><i class="fas fa-chevron-double-right"></i></a></b>
          </p>

             <a target="_blank" href="https://github.com/AllienWorks/cryptocoins" class="card-header-icon has-text-primary" aria-label="more options">
                <span><i class="fas fa-download" aria-hidden="true"></i> Download</span>
            </a>
                <!-- <span class="is-right tag is-danger">
                  <b>BETA</b>
                </span> -->
            </header>
            <div class="card-content">
              <p><b>Cryptocoins is the most complete free vector iconpack of your favourite cryptocurrencies.</b></p><br>
              <p class="has-text-centered">
                <i class="cc BTC" title="BTC"></i>
                <i class="cc ETH" title="ETH"></i>
                <i class="cc XRP" title="XRP"></i>
                <i class="cc EOS" title="EOS"></i>
                <i class="cc XLM" title="XLM"></i>
                <i class="cc LTC" title="LTC"></i>
                <i class="cc ZEC" title="ZEC"></i>
              </p>
              <label><small>INSTALLATION</small></label><br>
              <ul>
                <li>
                  - via SVG: when you need just a few icons in your project.
                </li>
                <li>
                  - Webfont version: ideal when you want to include all icons at once.
                </li>
                <li>
                  - NPM package: <code>>$ npm i cryptocoins-icons</code>
                </li>
                <li>
                  - CDN: Both svg icons and the webfont are also available on <a href="https://www.jsdelivr.com/package/npm/cryptocoins-icons" target="_blank"> jsDelivr CDN </a>.
                </li>
              </ul>
            </p>
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
      name: 'cryptocoins',
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
            return '<i class="' + icon.class + '" style="font-size:' + size + 'px"></i>'
          } else {
            return icon.unicode
          }
        }
      }
    }
  </script>

  <!-- Add "scoped" attribute to limit CSS to this component only -->
  <style scoped>
  @import 'assets/cryptocoins/webfont/cryptocoins.css';
  @import 'https://pro.fontawesome.com/releases/v5.0.9/css/all.css';

  .icons {
    margin: 3rem 0;
  }

  i.cc { font-size: 4rem; display: inline-block; margin: 0 1.3rem 1.3rem 0; transition: 0.1s ease all; }
  i.cc:hover { color: #0060BD; transform: rotate(-20deg); transform-origin: 0.49em 0.7em; }

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
