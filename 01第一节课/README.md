## 课程介绍

​	本章节课程，主要是让大家了解前端的基本知识，前端也是IT当中的一个方向，就和我们之前学习的数据库等一样，也是可以单独发展的，所以不要以为前端就只有我们学的这点内容，前端的内容非常多，往往你还没学完一个，新的东西又出来了，前端技术基本上每半年都会更新一次，所以学习起来非常累，要不断的去学。但是基本的东西还是不变的，我们学习的也主要是基本的一些东西，主要是 HTML、CSS 和 javascript，外加上一些其他补充内容。那么今天我们就主要学习HTML这块的内容。 



## HTML介绍

​	在了解HTML之前，那么先了解，什么是网页，我们在日常生活中，浏览淘宝，或者查看公众号，还是小程序，我们所看到的内容，就是网页，而这些网页的载体就是浏览器，但是浏览器的种类是很多的，但是我们发现，同样的网页在不同的浏览器里面都是可以正常浏览的，这是因为不同的浏览器遵循相同的规则，这个规则就是HTML。

​	HTML(HyperText Marked Language)称为[超文本](https://baike.baidu.com/item/超文本/2832422)标记语言，是一种标识性的语言。它包括一系列标签．通过这些标签可以将网络上的文档格式统一，使分散的[Internet](https://baike.baidu.com/item/Internet/272794)资源连接为一个逻辑整体。HTML文本是由HTML命令组成的描述性文本，HTML命令可以说明文字，图形、动画、声音、表格、链接等。

​	超文本是一种组织信息的方式，它通过超级链接方法将文本中的文字、图表与其他信息媒体相关联。这些相互关联的信息媒体可能在同一文本中，也可能是其他文件，或是地理位置相距遥远的某台计算机上的文件。这种组织信息方式将分布在不同位置的信息资源用随机方式进行连接，为人们查找，检索信息提供方便。



## 什么是浏览器

- 浏览器是指在PC上运行的网页浏览软件。 举例QQ，优酷等其他应用。说出区别
-  浏览器是指可以显示网页服务器或者文件系统的HTML文件（标准通用标记语言的一个应用）内容，并让用户与这些文件交互的一种软件。 
-  常用的浏览器有微软的IE、谷歌浏览器、QQ浏览器、火狐等。 




学网页必学的三大语言 html  css   js

编辑器

推荐浏览器建议  Google Firefox，对于其他浏览器会有一定的差异

什么是HTML?   5大部分

HTML不是编程语言，是一种超文本标记语言。学习标签的使用

网站和网页

创建项目，html文件，文件名的命名规范



**什么是 \<!DOCTYPE html> ，他的作用，存在的目的**

```
<!DOCTYPE> 声明位于文档中的最前面的位置，处于 <html> 标签之前。
<!DOCTYPE> 声明不是一个 HTML 标签；它是用来告知 Web 浏览器页面使用了哪种 HTML 版本。
总是给您的 HTML 文档添加 <!DOCTYPE> 声明，确保浏览器能够预先知道文档类型。
```



**HTML文档和HTML标签**

- HTML文档 = 网页 = HTML标签（HTML tag）+ 纯文本
- HTML标签 = 开始标签/开放标签 + 结束标签/闭合标签 = <元素名> + </元素名>
- 某些HTML元素没有结束标签，比如\<br />



\<html> \</html\>  lang是语言的意思   en是英语的意思   zh是中文



标签对中的第一个标签是**开始标签**，第二个标签是**结束标签**

```
<!DOCTYPE html> 声明为 HTML5 文档
<html> 元素是 HTML 页面的根元素
<head> 元素包含了文档的元（meta）数据，如 <meta charset="utf-8"> 定义网页编码格式为 utf-8。
<title> 元素描述了文档的标题
<body> 元素包含了可见的页面内容
<h1> 元素定义一个大标题
<p> 元素定义一个段落
```

```html
<!-- 文档类型的声明 -->
<!DOCTYPE html>
<!-- 文档的开始 -->
<!-- 开始标签 -->
<html lang="en">  <!--zh-->
<!-- 文档的头部 -->
<head>
    <meta charset="UTF-8">
    <title>我的第一个HTML页面</title>
</head>
<body>
<!-- 可视化区域 -->
<!-- 标签的特点 -->
1. 通常都是成双成对出现的，但是也有形影单只的
2. 第一个开始标签，第二个叫做结束标签
3. 单个的标签是自闭合标签
4. 标签都是由尖括号包裹关键字组成
5. 标签不区分大小写，但是推荐小写
</body>
<!-- 结束标签 -->
</html>
```



## HTML \<p> 标签

```html
<p> 标签表示文本的段落，段落通常在可视媒体中表示为文本块，是块级元素。 
```

```html
标签定义及使用说明
    <p> 标签定义段落。
    <p> 元素会自动在其前后创建一些空白。浏览器会自动添加这些空间，您也可以在样式表中规定。
    注意：<p> 标签与 <br> 标签都有换行的意思，不同的是 <p> 标签是大换行（分段），<br> 标签是小换行。
```

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>块级标签的特点</title>
    </head>
    <body>
        <!--特点-->
        <!--1. 设置宽高有效-->
        <!--2. 在不设置宽度的情况下，宽度始终与浏览器的宽度保持一致，与内容无关-->
        <!--3. 霸道，独占一行，可以实现自动换行-->
        <!--4. 当多个块状标签写在一起的时候，默认的排列方式是从上到下-->

        <!--px是像素，长度单位-->
        <!--<p style="width:200px;height: 100px">我是段落标签</p>-->
        <p>我是段落标签</p>
        <p>我是段落标签</p>
        <p>我是段落标签</p>
        <p>我是段落标签</p>

    </body>
</html>
```





## HTML \<span> 标签

````html
<span> 元素是无语义的行内元素，它可以对元素进行分组，使它们以不同的样式显示，请参考下述示例：
    使用 <span> 元素对文本中的一部分进行着色：
	<p>我的母亲有 <span style="color:blue">蓝色</span> 的眼睛。</p>
````

```html
标签定义及使用说明
    <span> 用于对文档中的行内元素进行组合。
    <span> 标签没有固定的格式表现。当对它应用样式时，它才会产生视觉上的变化。如果不对 <span> 应用样式，那么 <span> 元素中的文本与其他文本不会任何视觉上的差异。
    <span> 标签提供了一种将文本的一部分或者文档的一部分独立出来的方式。
```

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>内联标签的特点</title>
    </head>
    <body>
        <!--特点-->
        <!--1. 不能设置宽高，设置宽高无效-->
        <!--2. 宽度只与内容有关-->
        <!--3. 不会自动换行，直到这一行满了为止才换行-->
        <!--4. 当多个内联标签写在一起的时候默认的排列方式是从左到右-->

        <!--<span style="width: 200px;height: 100px">我是文本标签</span>-->
        <span>我是文本标签1111</span>
        <span>我是文本标签1111</span>
        <span>我是文本标签1111</span>
    </body>
</html>
```



------

# 常用的块级标签

```html
<head>
    <meta charset="UTF-8">
    <title>常用的块级标签</title>
</head>
<body>
    <!--标题标签-->
    <h1>我是一级标题</h1>
    <h2>我是二级标题</h2>
    <h3>我是三级标题</h3>
    <h4>我是四级标题</h4>
    <h5>我是五级标题</h5>
    <h6>我是六级标题</h6>
    <!--段落标签-->
    <p>我是段落标签</p>

    <!--列表标签-->
    <!--有序列表-->
    <!--pycharm 快捷键  ol>li*n   -->
    <!--type: A a I i 1-->
    <ol type="1" start="10" reversed>
        <li>苹果</li>
        <li>葡萄</li>
        <li>香蕉</li>
    </ol>

    <!--无序列表-->
    <!--type: disc(实心圆) circle(空心圆) square(实心正方形) none(取消前缀)-->
    <ul type="square">
        <li>a</li>
        <li>b</li>
        <li>c</li>
    </ul>
    <!--定义列表-->
    <dl>
        <dt>水果</dt>
        <dd>葡萄</dd>
        <dd>榴莲</dd>
    </dl>
    <!--div标签-->
    <!--边框 border:边框宽度 实线 颜色-->
    <div style="width: 300px;height: 300px;border: 1px solid red">
        111111
    </div>

</body>
```







## HTML\<ol>标签      有序列表

```html
<ol> 标签在 HTML 中表示有序列表，是 ordered lists 的缩写。您可以自定义有序列表的初始序号，请参考下面的实例：
    <ol>
        <li>咖啡</li>
        <li>茶</li>
        <li>牛奶</li>
    </ol>

    <ol start="10">
        <li>咖啡</li>
        <li>茶</li>
        <li>牛奶</li>
    </ol>
```

| 属性     |         值          | 描述                                                         |
| -------- | :-----------------: | ------------------------------------------------------------ |
| type     | 1 A a I i  （五种） | 规定列表的类型。不赞成使用。请使用样式代替。                 |
| stasrt   |       number        | HTML5不支持，不赞成使用。请使用样式取代它。规定列表中的起始点。 |
| reversed |      reversed       | 指定列表倒序(9,8,7...)                                       |

```html
<!--type: A a I i 1-->
<ol type="1" start="10" reversed>   reversed = v wer s te
    <li>苹果</li>
    <li>葡萄</li>
    <li>香蕉</li>
</ol>
```



## HTML\<ul>标签      无序列表

```html
unordered list
```

| 属性 | 值                            | 描述                       |
| ---- | ----------------------------- | -------------------------- |
| type | dise(默认) square circle none | 规定列表的项目符号的类型。 |

```html
<!--无序列表-->
<!--type: disc(实心圆) circle(空心圆) square(实心正方形) none(取消前缀)-->
<ul type="square">
    <li>a</li>
    <li>b</li>
    <li>c</li>
</ul>
```



## HTML\<dl>标签       自定义列表

\<dl>标签代表一个描述列表。该标签的常用用途是实现词汇表或显示元数据（键值对列表）


```html
标签定义及使用说明
    <dl> 标签定义一个描述列表。
    <dl> 标签与 <dt> （定义项目/名字）和 <dd> （描述每一个项目/名字）一起使用。
    <dl> 标签必须有开始标签和结束标签。
```

```html
<!--定义列表-->
<dl>
    <dt>水果</dt>
    <dd>葡萄</dd>
    <dd>榴莲</dd>
</dl>
```



## HTML\<div>标签

\<div>标签本身并不代表任何东西，使用它可以标记区域，例如样式化（使用class或id属性）、用不同的语言（使用lang属性）标记HTML文档的某个部分

```html
标签定义及使用说明
	<div>标签定义HTML文档中的一个分隔区块或者一个区域部分
	<div>标签常用于组合块级元素，以便通过CSS来对这些元素进行格式化
	可以对同一个<div>标签同时应用class或id属性，但通常情况下我们偏向于只使用其中一种
	为了避免麻烦，您可以不必为每一个<div>标签都加上class或id属性
```

```html
<!--div标签-->
<!--边框 border:边框宽度 实线 颜色-->
<div style="width: 300px;height: 300px;border: 1px solid red">
    111111
</div>
```



# 常用的内联标签

```html
<head>
    <meta charset="UTF-8">
    <title>常用的内联标签</title>
    <style>
        div{
            background: #2b3544;
        }
    </style>
</head>
<body>
    <a href="#bottom" name="top">我是顶部，我要下去</a>
    <!--图片标签-->
    <!--通过网址进行引入-->
    <img src="https://img95.699pic.com/photo/40180/8333.jpg_wh860.jpg!/both/590x400" alt="">
    <!--相对路径-->
    <img src="images/590x400.jpg" alt="图片加载失败">
    <!--绝对路径：不建议用-->
    <img src="F:\HtmlCode\码趣\day1\第一节课\images\590x400.jpg" alt="图片加载失败">
    <br>
    <b>我是粗体标签</b>
    <span>我是正常的</span>
    <i>我是斜的</i>
    <!--超链接-->
    <div style="height: 1000px"></div>
    <a href="http://www.baidu.com" target="_parent">我是超链接</a>
    <!--锚点链接-->
    <a href="#top" name="bottom">我是底部我要上去</a>

    <!--HTML转义-->
    <span>我&nbsp;是&emsp;文本标签</span>

</body>
```





## HTML\<img>标签

\<img> 标签用于展示 HTML 页面中的图像，使得页面能够“图文并茂”  

```html
标签定义及使用说明
	<img>标签定义HTML页面中的图像
	<img>标签有两个必需的属性：src 和 alt。
	从技术上讲，图像并不会插入HTML页面中，而是链接到HTML页面上。<img>标签的作用是被引用的图像创建占位符。
	通过在<a>标签中嵌套<img>标签，给图像添加到另一个文档的链接。
```

```html
<!--图片标签-->
<!--通过网址进行引入-->
<img src="https://img95.699pic.com/photo/40180/8333.jpg_wh860.jpg!/both/590x400" alt="">
<!--相对路径-->
<img src="images/590x400.jpg" alt="图片加载失败">
<!--绝对路径：不建议用-->
<img src="F:\HtmlCode\码趣\day1\第一节课\images\590x400.jpg" alt="图片加载失败">
```



## HTML\<b>标签   粗体

 这 \<b> 元素以粗体标记要强调的文本。对于所有浏览器来说，这意味着要把这段文字以加粗（粗体）样式方式显示。 

```html
<p>这是一个普通的文本- <b>这是一个加粗文本</b>。</p>
```



## HTML\<I>标签   斜体

\<i> 标签中的文本显示为斜体，代表一定范围的文本具有特别的语义。

```html
<p>He named his car <i>The lightning</i>, because it was very fast.</p>
<i>我是斜体标签</i>
```



## HTML\<a>标签  

\<a> 标签用于定义超链接，作用是从一个页面链接到另一个页面。

\<a> 标签最重要的属性是 href 属性，用于创建指向另外一个文档的链接（或超链接）。

```html
标签定义及使用说明
	<a>标签定义超链接，用于从一个页面链接到另一个页面。
	<a>元素最重要的属性是href属性，它指定链接的目标
	在所有浏览器中，链接的默认外观如下：
        未被访问的链接带有下划线而且是蓝色的
        已被访问的链接带有下划线而且是紫色的
        活动链接带有下划线而且是红色的
```

| 属性   | 值                        | 描述 |
| ------ | ------------------------- | ---- |
| target | \_blank（打开一个新页面）<br />\_self（默认） | 规定在何处打开目标 URL。 |

```html
<a href="#bottom" name="top">我是顶部，我要下去</a>
...
...
...
<!--超链接-->
<div style="height: 1000px"></div>
<a href="http://www.baidu.com" target="_blank">我是超链接</a>
<!--锚点链接-->
<a href="#top" name="bottom">我是底部我要上去</a>
```



## HTML 转义字符

```html
♠ &spades; &#9824; 黑桃 
♣ &clubs; &#9827; 梅花 
< &lt; &#60; 小于号 
> &gt; &#62; 大于号 
≤ &le; &#8804; 小于等于号 
≥ &ge; &#8805; 大于等于号
× &times; &#215; 乘号 
÷ &divide; &#247; 除号 
− &minus; &#8722; 减号 
± &plusmn; &#177; 加/减 号 
≠ &ne; &#8800; 不等于号 
¤ &curren; &#164; 一般货币符号 
$ &#36; 美元符号 
¢ &cent; &#162; 分 
£ &pound; &#163; 英镑 
¥ &yen; &#165; 日元 
€ &euro; &#8364; 欧元 
  &nbsp; &#160; 空格 
© &copy; &#169; 版权标志 
® &reg; &#187; 注册标志 
™ &trade; &#153; 商标标志 
“ &ldquo; &#147; 左双引号 
” &rdquo; &#148; 右双引号 
‘ &lsquo; &#145; 做单引号 
’ &rsquo; &#146; 右单引号 
« &laquo; &#171; 左三角双引号 
» &raquo; &#187; 右三角双引号 
‹ &lsaquo; &#8249; 左三角单引号 
› &rsaquo; &#8250; 右三角单引号
© &copy; &#169; 版权标志 
```

```html
<!--HTML转义-->
<span>我&nbsp;是&emsp;文本标签</span>
```



## HTML\<table>标签

![](https://img-blog.csdnimg.cn/20190517150835744.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQwODMxMzgx,size_16,color_FFFFFF,t_70)

\<table>标签用来定义HTML表格，一个简单的HTML表格应该包括两行两列

```html
<table border="1">
    <tr>
        <th>Month</th>
        <th>Savings</th>
    </tr>
    <tr>
        <td>January</td>
        <td>$100</td>
    </tr>
</table>
```

```html
标签定义及使用说明
	<table>标签定义HTML表格。
	一个HTML表格包括<table>元素，一个或多个<tr>、<th>以及<td>元素。
	<tr>元素定义表格行，<th>元素定义表头，<td>元素定义表格单元。
	更复杂的 HTML 表格也可能包括 <caption>、<col>、<colgroup>、<thead>、<tfoot> 以及 <tbody> 元素。
```

```html
<table border="1">
    <!--表格标题-->
    <caption>我的标题</caption>
    <tr>
        <!--colspan: 合并列-->
        <th colspan="2">水果</th>
    </tr>
    <!--tr是行标签-->
    <tr>
        <!--td是列标签-->
        <td>葡萄</td>
        <!--rowspan：合并行-->
        <td rowspan="2">榴莲</td>
    </tr>
    <tr>
        <!--<td>香蕉</td>-->
        <td>西瓜</td>
    </tr>
</table>
```



## HTML\<form>标签

 使用 \<form> 标签可以向服务器传输数据 

```html
带有两个输入字段和一个提交按钮的 HTML 表单：
<form action="demo_form.php" method="get">
  First name: <input type="text" name="fname"><br>
  Last name: <input type="text" name="lname"><br>
  <input type="submit" value="提交">
</form>
```

### GET  和  POST 区别

**Get**

- URL 改变，在URL 里显示 HTML Form 参数的 name/value 值。
- 只适合有少量参数的 HTML Form，因为 URL 长度有字符限制，不能无限长。
- 涉及安全性的信息，比如用户密码，不能用 get，因为会在 URL 上显示，不安全。

**Post**

- URL 不改变，不在 URL 里显示 HTML Form 的数据。
- Form 提交的信息没有长度限制。
- 涉及安全性的信息，如用户密码，应采用 post 方式。

```html
<body>
    <form action="">
        <!--文本框-->
        <!-- placeholder  普累si厚的 -->
        用户名：<input type="text" placeholder="请输入用户名" name="user">
        <br>
        <!--密码框-->
        密&emsp;码：<input type="password" placeholder="请输入密码" name="pwd">
        <br>
        <!--单选框-->
        性&emsp;别：<input type="radio" value="male" name="sex" id="male">
        <label for="male">男</label>
        <!--female fiv mei o -->
        <input type="radio" value="female" name="sex" checked id="female">
        <label for="female">女</label>
        <br>
        <!--多选框-->
        爱&emsp;好：<input type="checkbox" name="hobby" value="play">打游戏
        <input type="checkbox" name="hobby"chenvalue="study">学习
        <input type="checkbox" name="hobby" value="basketball">打篮球
        <br>
        <!--上传文件-->
        <!--accept：限定文件上传的格式-->
        上传头像：<input type="file" accept="image/*" name="file">
        <br>
        <!--下拉框-->
        地&emsp;址：
        <select name="address" id="address">
            <!--进行分组-->
            <optgroup label="中国">
                <!--下拉选项-->
                <option value="HN">湖南</option>
                <option value="HB">河北</option>
                <option value="HB2">湖北</option>
                <option value="ZG" selected>广州</option>
            </optgroup>
        </select>
        <br>
        <!--个人简介-->
        <!--文本域-->
        <!--cols：列   rows：行-->
        个人简介：<!--introduce in雀diu死-->
        <textarea name="introduce" id="introduce" cols="30" rows="10"></textarea>
        <br>
        <input type="submit" value="提交">
        <input type="reset" value="重置">
        <button type="reset">普通按钮</button>
        <!--隐藏域，看不见的东西-->
        <input type="hidden" value="隐藏域">
        <!--readonly：只读-->
        <br>
        <!--disabled  滴sei波-->
        只&emsp;读：<input type="text" value="12182222222" readonly><br>
        禁&emsp;用: <input type="text" value="12182222222" disabled><br>
        <!--实现分组-->
        <!--fiv V set-->
        <fieldset>
            <legend>用户登录</legend>
            用户名：<input type="text" placeholder="请输入用户名" name="user">
            <br>
            密&emsp;码：<input type="password" placeholder="请输入密码" name="pwd">
        </fieldset>
    </form>
    <button type="button">普通按钮</button>
</body>
```



## 作业

```html
<head>
    <meta charset="UTF-8">
    <title>作业</title>
</head>
<body>
    <div>
        <h2>请注册</h2>
        <p>已有账号？
            <a href="#">登陆</a>
        </p>
        <form action="#">
            <label for="username">用户名：</label>
            <input type="text" placeholder="请输入用户名" id="username" name="user"><br>
            <label for="phone">手机号：</label>
            <select name="prePhone" id="prePhone">
                <option value="+86">+86</option>
                <option value="+86" selected>+0731</option>
            </select>
            <input type="text" placeholder="请输入手机号" name="phone" id="phone"><br>
            <label for="pwd">密&emsp;码：</label>
            <input type="password" placeholder="请输入密码" id="pwd" name="passwd"><br>
            <label for="code">验证码：</label>
            <input type="text" placeholder="输入验证码" name="code" id="code">
            <input type="button" value="获取验证码"><br>
            <input type="checkbox" name="isAgree" id="isAgree">
            <label for="isAgree">阅读并接受协议</label><br>
            <input type="submit" value="注册">
        </form>
    </div>
</body>
```





















