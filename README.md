bigvim
======================

### 配置步骤

> 注意，该配置需要vim7.4.x. 在MacOS

1. 安装依赖(必须)
  ```
  Git, node, npm
  ```

2. 安装步骤
  ```
  curl -O https://raw.githubusercontent.com/yuanzm/fe-vim/master/install.py && python install.py
  ```

#### 选装

> 建议安装以下依赖以达到最好的使用体验

1. 相关node module
  ```
  npm i -g eslint eslint-config-airbnb babel-eslint eslint-plugin-react #JS 语法，代码规范检查
  或者
  npm i --save-dev eslint eslint-config-airbnb babel-eslint eslint-plugin-react
  npm i -g js-beautify # JS, CSS, HTML 快速格式化
  npm i -g git+https://github.com/ramitos/jsctags.git # tagbar JS 支持
  ```
  相关eslint插件请自行安装

2. 其他依赖

  ag快速搜索插件：
  - Mac: `brew install ctags silversearcher-ag`
  - Ubuntu: `apt-get install ctags silversearcher-ag`

  for YoucomplateMe插件：
  ```
  apt-get install build-essential cmake python-dev #Ubuntu
  brew install cmake #MacOS
  ```
  安装YouCompleteMe如果出现问题，请前往项目主页寻找解决方法,
  - [Ubuntu Linux x64 super-quick installation](https://github.com/Valloric/YouCompleteMe#ubuntu-linux-x64-super-quick-installation)
  - [Mac OS X super-quick installation](https://github.com/Valloric/YouCompleteMe#mac-os-x-super-quick-installation)

3. 安装powerline美化字体:
  推荐[Monaco for Powerline](https://gist.github.com/ruanyl/ea38de37683951c20bf5/raw/5fa73caa4af86285f11539a6b4b6c26cfca2c04b/Monaco%20for%20Powerline.otf) 或者去[Lokaltog/powerline-fonts](https://github.com/Lokaltog/powerline-fonts) 自行寻找

### 内置主题
molokai主题

![molokai](https://raw.githubusercontent.com/ruanyl/bigvim/gh-pages/images/molokai.png)


### 常用自定义快捷键(`<leader>`映射为`,`)

```
空格  开启查找(Easymotion模式)
:W    以sudo的权限保存
(     左括号，在changelist 逆序切换
)     右括号，在changelist 顺序切换，文件内跳转非常有用
,sa  全选(select all)
ctrl + jkhl 进行上下左右窗口跳转,不需要ctrl+w+jkhl
ctrl+p   开启文件搜索 ctrlp
,/   去除匹配高亮
'    :b
qq   关闭当前Buffer
qo   关闭除当前buffer之外的所有buffer
m    在Buffer之间顺序切换
M    在Buffer之间逆序切换
Tab  最大化当前split窗口/切换
,r   快速运行当前文件
H    到行首
L    到行尾
,d   javascript go to defination
```

> 更多地快捷键，请在vimrc中对应的插件寻找


## 主要插件列表

#### [junegunn/vim-plug](https://github.com/junegunn/vim-plug)
使用vim-plug来管理插件，vim-plug能够选择branch，执行插件初始命令,
延迟加载插件等功能

```
:PlugInstall     install
:PlugUpdate      update
:PlugClean       remove plugin not in list
```

#### [scrooloose/nerdtree](https://github.com/scrooloose/nerdtree)
文件浏览器
```
,e
```

![thenerdtree](https://raw.githubusercontent.com/ruanyl/bigvim/gh-pages/images/nerdtree.gif)


#### [majutsushi/tagbar](https://github.com/majutsushi/tagbar)
浏览taglist

```
,t
```

#### [kien/ctrlp.vim](https://github.com/kien/ctrlp.vim)
快速文件搜索+导航
```
f   默认CtrlP查找
,m  相当于mru功能，most recently used
,b  查找buffer
```

ctrl + j/k 进行上下移动 或者小键盘方向键
![ctrlp](https://raw.githubusercontent.com/ruanyl/bigvim/gh-pages/images/ctrlp.gif)

#### [tacahiroy/ctrlp-funky](https://github.com/tacahiroy/ctrlp-funky)
CtrlP插件，类似go to definition的功能

```
,fu 打开搜索
```
![ctrlp-funky](https://raw.githubusercontent.com/ruanyl/bigvim/gh-pages/images/ctrlp-funky.gif)

#### [dyng/ctrlsf.vim](https://github.com/tacahiroy/ctrlp-funky)
CtrlP插件，提供sublime类似的grep搜索

```
,s      #在可视模式下选择要搜索内容
```

![dyng/ctrlsf.vim](https://camo.githubusercontent.com/a7eef846eae3efe4f021f34c9b8526300b872b0f/687474703a2f2f692e696d6775722e636f6d2f4e4f793867776a2e676966)

#### [rking/ag.vim](https://github.com/rking/ag.vim)
提供快速grep功能

```
,,a     #然后输入要检索的内容
```

#### [bling/vim-airline](https://github.com/bling/vim-airline)
状态栏，buffer兰美化

![vim-airline](https://raw.githubusercontent.com/ruanyl/bigvim/gh-pages/images/vim-airline.png)

#### [bronson/vim-trailing-whitespace](https://github.com/bronson/vim-trailing-whitespace)
将代码行最后无效的空格标红

```
,空格    去掉多余空格
```

```
,,m  # 切换书签显示\关闭，更多快捷键请查看vimrc
```

#### [Valloric/MatchTagAlways](https://github.com/Valloric/MatchTagAlways)
高亮显示匹配的标签

![matchtagalways](https://raw.githubusercontent.com/ruanyl/bigvim/gh-pages/images/matchtagalways.gif)

#### [szw/vim-maximizer](https://github.com/szw/vim-maximizer)
最大化当前窗口\返回之前状态切换，在多个split窗口的非常有用

```
tab    # 快捷键设置为tab
```

#### [vim-scripts/matchit.zip](https://github.com/vim-scripts/matchit.zip)
快速匹配() [] {} 等

   `%` 匹配标签，不只是单个的字符，还可以匹配单词，如html标签

#### [alvan/vim-closetag](https://github.com/alvan/vim-closetag)
自动关闭html, xml标签

![closetag](https://raw.githubusercontent.com/ruanyl/bigvim/gh-pages/images/CloseTag.gif)

#### [Valloric/YouCompleteMe](https://github.com/Valloric/YouCompleteMe)
强大的自动补全，如果安装失败，请前往该项目的github wiki查找帮助
![YCM](https://camo.githubusercontent.com/1f3f922431d5363224b20e99467ff28b04e810e2/687474703a2f2f692e696d6775722e636f6d2f304f50346f6f642e676966)
```
向下选择：<tab> 或<c-j>或方向键
向上选择：<c-k>或者方向键
```

#### [scrooloose/nerdcommenter](https://github.com/scrooloose/nerdcommenter)
快速注释工具
```
shift+v 选择要注释的行
,cc  注释单行或者选中行
,cm  多行注释
,cu  解开注释
,ci  在注释和取消注释之间切换
```
![nerdcomment](https://raw.githubusercontent.com/ruanyl/bigvim/gh-pages/images/nerdcomment.gif)

#### [Raimondi/delimitMate](https://github.com/Raimondi/delimitMate)
自动补全：(), [], {}, <>

## Javascript相关插件
#### [pangloss/vim-javascript](https://github.com/pangloss/vim-javascript)
JS语法高亮

#### [editorconfig/editorconfig-vim](https://github.com/editorconfig/editorconfig-vim)
支持.editorconfig文件

#### [romainl/vim-cool](https://github.com/romainl/vim-cool)

#### Inspired by:
1. [bigvim](https://github.com/ruanyl/bigvim)
