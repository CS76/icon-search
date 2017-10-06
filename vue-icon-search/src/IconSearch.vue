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
          <div v-if="icons.length > 0">
            <span v-if="query != ''">
              Results ({{ icons.length }})
              <br>
            </span>
            <span v-for="icon in icons">
              <div v-if="selectedResource == 'fontawesome'">
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
              </div>
              <div v-if="selectedResource == 'material'">
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
                    <div class="content  has-text-centered">
                      <div class="columns is-mobile">
                        <div class="column vc h5em">
                          <span>
                            <i class="material-icons md-48 pointer">{{ icon.class }}</i><br>
                            <small class="has-text-grey-light">
                              <a v-clipboard:copy="getCopyText('material','html',icon, 4)"
                                v-clipboard:success="onCopy">HTML</a> 
                              | 
                              <a v-clipboard:copy="getCopyText('material','css',icon, 4)"
                                v-clipboard:success="onCopy">CSS</a>
                            </small>
                          </span>
                        </div>
                        <div class="column vc h5em">
                          <span>
                            <i class="material-icons md-36 pointer">{{ icon.class }}</i><br>
                            <small class="has-text-grey-light">
                              <a v-clipboard:copy="getCopyText('material','html',icon, 3)"
                                v-clipboard:success="onCopy">HTML</a> 
                              | <a v-clipboard:copy="getCopyText('material','css',icon, 3)"
                                v-clipboard:success="onCopy">CSS</a>
                            </small>
                          </span>
                        </div>
                        <div class="column vc h5em">
                          <span>
                            <i class="material-icons md-24 pointer">{{ icon.class }}</i><br>
                            <small class="has-text-grey-light">
                              <a v-clipboard:copy="getCopyText('material','html',icon, 2)"
                          v-clipboard:success="onCopy">HTML</a> | <a v-clipboard:copy="getCopyText('material','css',icon, 2)"
                          v-clipboard:success="onCopy">CSS</a>
                            </small>
                          </span>
                        </div>
                        <div class="column vc h5em">
                          <span>
                            <i class="material-icons md-18 pointer">{{ icon.class }}</i><br>
                            <small class="has-text-grey-light">
                              <a v-clipboard:copy="getCopyText('material','html',icon, 1)"
                          v-clipboard:success="onCopy">HTML</a> | <a v-clipboard:copy="getCopyText('material','css',icon, 1)"
                          v-clipboard:success="onCopy">CSS</a>
                            </small>
                          </span>
                        </div>
                      </div>
                    </div>
                  </div>
                  <footer class="card-footer">
                    <span class="card-footer-item pointer">
                      <a target="_blank" :href="'https://storage.googleapis.com/material-icons/external-assets/v4/icons/svg/ic_'+icon.class+'_black_24px.svg'">SVG</a>
                    </span>
                    <span class="card-footer-item pointer">
                      <a target="_blank" :href="'https://storage.googleapis.com/material-icons/external-assets/v4/icons/zip/ic_'+icon.class+'_black_24dp.zip'">PNG</a>
                    </span>
                    <a v-clipboard:copy="getCopyText('material','unicode', icon, 0)" v-clipboard:success="onCopy" class="card-footer-item"><small class="has-text-grey-light">[{{icon.unicode}}]</small></a>
                  </footer>
                </div>
              </div>
              <div v-if="selectedResource == 'iconic'">
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
                        <div class="column vc h5em has-text-centered">
                          <a v-clipboard:copy="getCopyText('iconic','img',icon, 1)"
                          v-clipboard:success="onCopy">
                            <span v-html="icon.assets.font"></span><br>
                            <small>img tag</small>
                          </a>
                        </div>
                         <div class="column vc h5em has-text-centered">
                          <a v-clipboard:copy="getCopyText('iconic','svg',icon, 1)"
                          v-clipboard:success="onCopy">
                            <span v-html="icon.assets.font"></span><br>
                            <small>SVG sprite</small>
                          </a>
                        </div>
                         <div class="column vc h5em has-text-centered">
                          <a v-clipboard:copy="getCopyText('iconic','font',icon, 1)"
                          v-clipboard:success="onCopy">
                            <span v-html="icon.assets.font"></span><br>
                            <small>Icon Font</small>
                          </a>
                        </div>
                         <div class="column vc h5em has-text-centered">
                          <a v-clipboard:copy="getCopyText('iconic','bootstrap',icon, 1)"
                          v-clipboard:success="onCopy">
                            <span v-html="icon.assets.font"></span><br>
                            <small>Bootstrap</small>
                          </a>
                        </div>
                         <div class="column vc h5em has-text-centered">
                          <a v-clipboard:copy="getCopyText('iconic','foundation',icon, 1)"
                          v-clipboard:success="onCopy">
                            <span v-html="icon.assets.font"></span><br>
                            <small>Foundation </small>
                          </a>
                        </div>
                      </div>
                    </div>
                  </div>
                  <footer class="card-footer">
                  </footer>
                </div>
              </div>
              <div v-if="selectedResource == 'foundation'">
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
            <div>
            <span v-if="selectedResource == 'fontawesome'">
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
                  <a href="http://fontawesome.io/assets/font-awesome-4.7.0.zip" class="card-header-icon" aria-label="more options">
                    <span class="icon">           
                      <i class="fa fa-download" aria-hidden="true"></i>
                    </span>
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
            </span>
            <span v-if="selectedResource == 'material'">
              <div class="card">
                <header class="card-header">
                  <p class="card-header-title">
                      <img src="./assets/material.svg"> Material Icons
                      <small>
                        <a target="_blank" href="https://material.io/icons/" class="card-header-icon has-text-grey" aria-label="more options">
                            <i class="fa fa-link" aria-hidden="true"></i>
                        </a>
                      </small>
                  </p>
                </header>
                <div class="card-content">
                  <div class="content">
                    <p>
                      <b><span class="has-text-info">Setup Method 1. Using via Google Web Fonts</span></b>
                      <ol>
                        <li>The easiest way to set up icon fonts for use in any web page is through Google Web Fonts. All you need to do is include a single line of HTML:</li>
                        <li>
                          <pre><code class="html"><span class="nt">&lt;link</span> <span class="na">rel=</span><span class="s">"stylesheet"</span> <span class="na">href=</span><span class="s">"https://fonts.googleapis.com/icon?family=Material+Icons"</span><span class="nt">&gt;</span>
                          </code></pre>
                        </li>
                        <li>
                          Similar to other Google Web Fonts, the correct CSS will be served to activate the 'Material Icons' font specific to the browser. An additional CSS class will be declared called .material-icons. Any element that uses this class will have the correct CSS to render these icons from the web font.
                        </li>
                      </ol>
                      <hr>
                      <b><span class="has-text-info">Setup Method 2. Self hosting</span></b><br>
                      <ol>
                        <li>For those looking to self host the web font, some additional setup is necessary. Host the icon font in a location, for example https://example.com/material-icons.woff and add the following CSS rule:</li>
                        <li>
                          <pre><code class="lang-css">@font-face {
  font-family: 'Material Icons';
  font-style: normal;
  font-weight: 400;
  src: url(https://example.com/MaterialIcons-Regular.eot); /* For IE6-8 */
  src: local('Material Icons'),
    local('MaterialIcons-Regular'),
    url(https://example.com/MaterialIcons-Regular.woff2) format('woff2'),
    url(https://example.com/MaterialIcons-Regular.woff) format('woff'),
    url(https://example.com/MaterialIcons-Regular.ttf) format('truetype');
}
                          </code></pre>
                        </li>
                      </ol>
                      </p>
                  </div>
                </div>
              </div>
            </span>
            <span v-if="selectedResource == 'iconic'">
              <div class="card">
                <header class="card-header">
                  <p class="card-header-title">
                     <b>OPEN</b>  IONIC
                     <small>
                        <a target="_blank" href="https://useiconic.com/open/" class="card-header-icon has-text-grey" aria-label="more options">
                            <i class="fa fa-link" aria-hidden="true"></i>
                        </a>
                      </small>
                  </p>
                  <a href="https://github.com/iconic/open-iconic/archive/master.zip" class="card-header-icon" aria-label="more options">
                    <span class="icon">           
                      <i class="fa fa-download" aria-hidden="true"></i>
                    </span>
                  </a>
                </header>
                <div class="card-content">
                  <div class="content">
                    <p>
                      <b><span class="has-text-info">Getting started with Open Iconic</span></b>
                      <ol>
                        <li><span class="has-text-info"><b>SVG</b></span></li><br>
                        <li>Displaying Open Iconic's SVGs are a snap. Just treat them like your typical image and away you go!<br></li>
                        <li>
                          <pre><code class="html"><span class="nt">&lt;img</span> <span class="na">alt=</span><span class="s">"icon name"</span> <span class="na">src=</span><span class="s">"/open-iconic/svg/icon-name.svg"</span><span class="nt">&gt;</span>
                          </code></pre>
                        </li>
                        <hr>
                        <li><span class="has-text-info"><b>Font</b></span></li><br>
                        <li>Icon fonts are a great fallback for SVG—and our font is pretty great.</li><br>
                        <li>
                          <small><b>Head</b></small>
                          <pre class=" language-markup"><code class=" language-markup"><span class="token"><span class="token"><span class="token punctuation">&lt;</span>link</span> <span class="token attr-name">href</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>/open-iconic/font/css/open-iconic.css<span class="token punctuation">"</span></span> <span class="token attr-name">rel</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>stylesheet<span class="token punctuation">"</span></span><span class="token punctuation">&gt;</span></span></code><br></pre>
                        </li><br>
                        <li>
                          <small><b>Body</b></small>
                          <pre class=" language-markup"><code class=" language-markup"><span class="token"><span class="token"><span class="token punctuation">&lt;</span>span</span> <span class="token attr-name">class</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>oi<span class="token punctuation">"</span></span> <span class="token attr-name">data-glyph</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>icon-name<span class="token punctuation">"</span></span> <span class="token attr-name">title</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>icon name<span class="token punctuation">"</span></span> <span class="token attr-name">aria-hidden</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>true<span class="token punctuation">"</span></span><span class="token punctuation">&gt;</span></span><span class="token"><span class="token"><span class="token punctuation">&lt;/</span>span</span><span class="token punctuation">&gt;</span></span></code><br></pre>
                        </li>
                        <hr>
                        <li><span class="has-text-info"><b>Bootstrap Font</b></span></li><br>
                        <li>Use Bootstrap? We have a collection of stylesheets which are designed to work perfectly with it.</li>
                        <li>
                          <small><b>Head</b></small>
                          <pre class=" language-markup"><code class=" language-markup"><span class="token"><span class="token"><span class="token punctuation">&lt;</span>link</span> <span class="token attr-name">href</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>/open-iconic/font/css/open-iconic-bootstrap.css<span class="token punctuation">"</span></span> <span class="token attr-name">rel</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>stylesheet<span class="token punctuation">"</span></span><span class="token punctuation">&gt;</span></span></code><br></pre>
                        </li><br>
                        <li>
                          <small><b>Body</b></small>
                          <pre class=" language-markup"><code class=" language-markup"><span class="token"><span class="token"><span class="token punctuation">&lt;</span>span</span> <span class="token attr-name">class</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>oi oi-icon-name<span class="token punctuation">"</span></span> <span class="token attr-name">title</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>icon name<span class="token punctuation">"</span></span> <span class="token attr-name">aria-hidden</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>true<span class="token punctuation">"</span></span><span class="token punctuation">&gt;</span></span><span class="token"><span class="token"><span class="token punctuation">&lt;/</span>span</span><span class="token punctuation">&gt;</span></span></code><br></pre>
                        </li>
                        <hr>
                        <li><span class="has-text-info"><b>Foundation Font</b></span></li><br>
                        <li>Iconic also works for Foundation and functions just like Foundation's icon font.</li><br>
                        <li>
                          <small><b>Head</b></small>
                          <pre class=" language-markup"><code class=" language-markup"><span class="token"><span class="token"><span class="token punctuation">&lt;</span>link</span> <span class="token attr-name">href</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>/open-iconic/font/css/open-iconic-foundation.css<span class="token punctuation">"</span></span> <span class="token attr-name">rel</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>stylesheet<span class="token punctuation">"</span></span><span class="token punctuation">&gt;</span></span></code><br></pre>
                        </li><br>
                        <li>
                          <small><b>Body</b></small><br>
                          <pre class=" language-markup"><code class=" language-markup"><span class="token"><span class="token"><span class="token punctuation">&lt;</span>span</span> <span class="token attr-name">class</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>fi-icon-name<span class="token punctuation">"</span></span> <span class="token attr-name">title</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>icon name<span class="token punctuation">"</span></span> <span class="token attr-name">aria-hidden</span><span class="token attr-value"><span class="token punctuation">=</span><span class="token punctuation">"</span>true<span class="token punctuation">"</span></span><span class="token punctuation">&gt;</span></span><span class="token"><span class="token"><span class="token punctuation">&lt;/</span>span</span><span class="token punctuation">&gt;</span></span></code><br></pre>
                        </li>
                      </ol>
                      </p>
                  </div>
                </div>
              </div>
            </span>
            <span v-if="selectedResource == 'foundation'">
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
                  <a href="http://zurb.com/playground/uploads/upload/upload/288/foundation-icons.zip" class="card-header-icon" aria-label="more options">
                    <span class="icon">           
                      <i class="fa fa-download" aria-hidden="true"></i>
                    </span>
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
            </span>
          </div>
            <div>
              <small>
                <span>
                  <a target="_blank" class="has-text-black-bis" href="https://opensource.org/">
                    <img src="https://opensource.org/files/osi_keyhole_300X300_90ppi_0.png" style="height: 14px;"> MIT license</a>   |  <a target="_blank" class="has-text-black-bis" href="https://github.com/CS76/icon-search"> <i class="fa fa-github"></i> GitHub</a>
                  
                </span>
                <span class="is-pulled-right">
                  Made with <i class="fa fa-heart has-text-danger"></i> by <a href="https://twitter.com/mailcs76">CS76</a>
                </span>
              </small>  
            </div>
          </div>
          <div v-if="isVisible" class="overlay vc">
            <p><i class="fa fa-lg fa-clipboard"></i> Copied to clipboard!</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import algoliasearch from 'algoliasearch'

export default {
  name: 'icon-search',
  data () {
    return {
      query: '',
      client: null,
      index: null,
      resources: [ 'fontawesome', 'foundation', 'material', 'iconic' ],
      selectedResource: 'fontawesome',
      icons: [],
      isVisible: false,
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
    },
    onCopy: function (e) {
      this.isVisible = true
      var that = this
      setTimeout(function () {
        that.isVisible = false
      }, 3000)
    },
    onError: function (e) {
      alert('Failed to copy texts')
    },
    getCopyText: function (library, type, icon, size) {
      if (library === 'fontawesome') {
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
      } else if (library === 'material') {
        if (type === 'html') {
          if (size === 4) {
            return '<i class="material-icons md-48">' + icon.class + '</i>'
          } else if (size === 3) {
            return '<i class="material-icons md-36">' + icon.class + '</i>'
          } else if (size === 2) {
            return '<i class="material-icons md-24">' + icon.class + '</i>'
          } else {
            return '<i class="material-icons md-18">' + icon.class + '</i>'
          }
        } else if (type === 'css') {
          if (size === 4) {
            return '.material-icons.md-48 { font-size: 48px; }'
          } else if (size === 3) {
            return '.material-icons.md-36 { font-size: 36px; }'
          } else if (size === 2) {
            return '.material-icons.md-24 { font-size: 24px; }'
          } else {
            return '.material-icons.md-18 { font-size: 18px; }'
          }
        } else {
          return '<i class="material-icons">&#xE84D;</i>'
        }
      } else if (library === 'iconic') {
        if (type === 'font') {
          return icon.assets.font
        } else if (type === 'img') {
          return icon.assets.img
        } else if (type === 'svg') {
          return icon.assets.svg
        } else if (type === 'foundation') {
          return icon.assets.foundation
        } else if (type === 'bootstrap') {
          return icon.assets.bootstrap
        }
      } else if (library === 'foundation') {
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
