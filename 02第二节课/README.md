

## 前期回顾



### 块级标签特点：

```html
在html中<div>、 <p>、<h1>、<form>、<ul> 和 <li>就是块级元素
    1、每个块级元素都从新的一行开始，并且其后的元素也另起一行。（真霸道，一个块级元素独占一行）

    2、元素的高度、宽度、行高以及顶和底边距都可设置。

    3、元素宽度在不设置的情况下，是它本身父容器的100%（和父元素的宽度一致），除非设定一个宽度。
```

### 内联标签特点：

```html
内联标签特点：
<span>、<a>、<label>、<input>、 <img>、 <strong> 和<em>就是典型的内联元素
    1、和其他元素都在一行上；

    2、元素的高度、宽度、行高及顶部和底部边距不可设置；

    3、元素的宽度就是它包含的文字或图片的宽度，不可改变。
```

### 内联块状标签：

```html
内联块状标签:
	内联块状元素（inline-block）就是同时具备内联元素、块状元素的特点
	因为可以设置宽高
	<img>、<input>标签就是这种内联块状标签。
```

### 基础的HTML转义字符

```html
 &nbsp; &#160; 空格 
 &emsp;  一个字符的空格
< &lt; &#60; 小于号 
> &gt; &#62; 大于号 
≤ &le; &#8804; 小于等于号 
≥ &ge; &#8805; 大于等于号
```

### form表单的基本属性以及参数

```
文本框   密码框   单选框   多选框
上传文件   下拉框   文本域   隐藏域   实现分组
```

# CSS 入门

## CSS的三种引入方式

 CSS的引入方式共有三种：行内样式、内部样式表、外部样式表。 

 CSS通常称为CSS样式表或层叠样式表（级联样式表），主要用于设置HTML页面中的文本内容（字体、大小、对齐方式等）、图片的外形（宽高、边框样式、边距等）以及版面的布局等外观显示样式。 

 CSS以HTML为基础，提供了丰富的功能，如字体、颜色、背景的控制及整体排版等，而且还可以针对不同的浏览器设置不同的样式。 



### 一、行内样式

```html
使用style属性引入CSS样式。
内联样式，又有人称行内样式、行间样式、内嵌样式。是通过标签的style属性来设置元素的样式
示例：
<h1 style="color:red;">style属性的应用</h1>
<p  style="font-size:14px;color:green;">直接在HTML标签中设置的样式</p>
实际在写页面时不提倡使用，在测试的时候可以使用。
```


### 二、内部样式表

```html
在style标签中书写CSS代码。style标签写在head标签中。
语法中，style标签一般位于head标签中title标签之后，也可以把他放在HTML文档的任何地方
示例：
<head>
   <style type="text/css">
      h3 {
            color:red;
         }
   </style>
</head>
```

### 三、外部样式表

```html
CSS代码保存在扩展名为.css的样式表中
HTML文件引用扩展名为.css的样式表，有两种方式：链接式、导入式。
该语法中，link标签需要放在的三个属性head头部标签中，并且必须指定link标签，具体如下：

href：定义所链接外部样式表文件的URL，可以是相对路径，也可以是绝对路径。
type：定义所链接文档的类型，在这里需要指定为“text/CSS”，表示链接的外部文件为CSS样式表。
rel：定义当前文档与被链接文档之间的关系，在这里需要指定为“stylesheet”，表示被链接的文档是一个样式表文件。

语法：
1、链接式
<link type="text/css" rel="styleSheet"  href="CSS文件路径" />
2、导入式
<style type="text/css">
  @import url("css文件路径");
</style>
```

```html
<head>
    <meta charset="UTF-8">
    <title>CSS的三种引入方式</title>
    <!--2. 内部样式   写在style标签里面-->
    <style>
        p {
            color: green;
        }
    </style>
    <!--3. 外部样式：写在CSS表里面-->
    <link rel="stylesheet" href="css/css1.css">
</head>
<body>
    <!--1. 写在标签里面  不建议使用在开发中，用于测试-->
    <!--行内样式-->
    <p style="color: red">我是段落标签</p>

    <p>我是段落标签</p>
</body>
--------------------------------------------------------------------------------------
外部css文件
p {
    color: blue;
}
```

### 四、三种样式表的总结

| 样式表     | 优点                   | 缺点                     | 使用情况       | 控制范围           |
| ---------- | ---------------------- | ------------------------ | -------------- | ------------------ |
| 行内样式表 | 书写方便，权重高       | 没有实现样式和结构相分离 | 较少           | 控制一个标签（少） |
| 内部样式表 | 部分结构和样式相分离   | 没有彻底分离             | 较多           | 控制一个页面（中） |
| 外部样式表 | 完全实现结构和样式分离 | 需要引入                 | 最多，强烈推荐 | 控制整个站点（多） |



## CSS 选择器

 ![img](file:///C:/Users/SpuerCoder/Documents/WXWork/1688853094146384/Cache/Image/2020-10/企业微信截图_16029195726010.png) 

### 标签选择器（元素选择器）

-  标签选择器最大的优点是能快速为页面中同类型的标签统一样式，同时这也是他的缺点，不能设计差异化样式。

- 标签选择器 可以把某一类标签全部选择出来 div span

### 类选择器（class选择器）

- 类选择器使用“.”（英文点号）进行标识，后面紧跟类名，其基本语 

- 类选择器最大的优势是可以为元素对象定义单独或相同的样式。 可以选择一个或者多个标签 

### id 选择器

- id选择器使用“#”进行标识，后面紧跟id名 

- 该语法中，id名即为HTML元素的id属性值，大多数HTML元素都可以定义id属性，元素的id值是唯一的，只能对应于文档中某一个具体的元素。 

- 用法基本和类选择器相同。 

### id选择器和类选择器区别

- 在同一个页面内，不允许有相同名字的id对象出现，但是允许相同名字的class。 

- 类选择器（class） 好比人的名字， 是可以多次重复使用的， 比如 张伟 王伟 李伟 李娜 

- id选择器 好比人的身份证号码， 全中国是唯一的， 不得重复。 只能使用一次。 

- id选择器和类选择器最大的不同在于 使用次数上。 

```html
<head>
    <meta charset="UTF-8">
    <title>CSS选择器</title>
    <style>
        /*权重大小：id选择器 > class选择器 > 标签选择器*/
        /*选择器越精确，权重值越高*/

        /* 标签选择器 */
        p {
            color: red;
        }
        /*class（类） 选择器*/
        .p1 {
            color: green;
        }
        /*id 选择器*/
        #p2 {
            color: blue;
        }
    </style>
</head>
<body>
    <p class="p1">我是段落标签1</p>
    <p id="p2" class="p1" >我是段落标签2</p>
    <p class="p1">我是段落标签3</p>
</body>
```

### 群组选择器

-  要为不同的HTML对象定义相同的样式时，可以采用群组声明。 
-  上述规则在选择器中指定了多个对象，对象之间用逗号来分隔。逗号告诉浏览器，规则中包含两个不同的选择器。这样的选择器叫群组选择器。 
-  使用逗号对选择器进行分隔，使用页面中所有的p, span, .blue, #blue都具有相同的样式。这样做的好处是，需要使用相同样式的地方只需要书写一次，可以减少代码量，改善CSS代码的结构，提高网页的性能。 
- `p, span, .blue, #blue { color: blue; }`

### 全选选择器 （通配符选择器）

-  通配符选择器用“*”号表示，他是所有选择器中作用范围最广的，能匹配页面中所有的元素。 

-  使用通配符选择器定义CSS样式，清除所有HTML标记的默认边距。 

-  \* { margin: 0;           /* 定义外边距*/      padding: 0;          /* 定义内边距*/ } 

### 层次选择器

#### 1、后代选择器

- 选中parent元素内部后代 **所有** n 元素。 

#### 		2、子代选择器

- 选中 parent 元素内部 的**子元素** n 

#### 		3、兄弟选择器

- 选中 brother 元素**后面**的**所有**某一类**兄弟**元素 n。 

#### 		4、相邻兄弟选择器

- 选中brother元素**后面**的某一个**相邻**的**兄弟**元素n。 

```html
<head>
    <meta charset="UTF-8">
    <title>CSS选择器</title>
    <style>
        /*群组选择器*/
        /*p, span {
        color: red;
        }*/

        /*全选 选择器*/
        /** {
        color: green;
        }*/

        /*层次选择器*/
        /*a. 后代选择器*/
        /*div span{
        color: blueviolet;
        } */

        /*div ul{
        list-style: none;  !* 列表的样式。去除样式 *!
        }*/
        /*b. 子代选择器*/
        div > ul {
            list-style: none;
        }

        /*c. 兄弟选择器*/
        #p22~p{
            color: aqua;
        }

        /*d. 相邻兄弟选择器*/
        #p22+p{
            color: #ff00ef;
        }
    </style>
</head>
<body>
    <div>
        <p>我是段落标签1</p>
        <p id="p22">我是段落标签2
            <span>我是段落标签里面的文本标签</span>
        </p>
        <p>我是段落标签3</p>
        <p>我是段落标签4</p>
        <span>我是文本标签1
            <b>我是粗体标签</b>
        </span>
        <p>我是段落标签5</p>
        <h1>我是一级标题</h1>
        <ul>
            <li>1</li>
            <li>2
                <ul>
                    <li>11</li>
                    <li>22</li>
                </ul>
            </li>
            <li>3</li>
        </ul>
    </div>
</body>
```

#### 5、属性选择器

-  根据元素的属性和属性值来匹配元素。他们通用的语法有方括号[ ]组成，其中包含属性名称，后跟可选条件以匹配属性的值 

-  如果希望选择有某个属性的元素，而不论属性值是什么，可以使用简单属性选择器。 
-  还可以根据多个属性进行选择，只需将属性选择器链接在一起即可。
-  除了选择拥有某些属性的元素，还可以进一步缩小选择范围，只选择有特定属性值的元素。 

```html
<head>
    <meta charset="UTF-8">
    <title>CSS选择器</title>
    <style>
        /*属性选择器*/
        p[name='p1']{
            color: red;
        }
    </style>
</head>
<body>
    <p name="p1">我是段落标签1</p>
    <p name="p2">我是段落标签2</p>
</body>
```

#### 6、伪类选择器

- link  visited hover active

```html
<head>
    <meta charset="UTF-8">
    <title>CSS选择器</title>
    <style>
        /*伪类选择器*/
        /*未访问*/
        a:link {
            color: pink;
        }

        /*访问过后*/~
        a:visited {
            color: green;
        }

        /*鼠标移入的改变*/
        a:hover {
            color: coral;
        }

        /*点击未松开  激活状态*/
        a:active {
            color: black;
        }
    </style>
</head>
<body>
    <!--空链接-->
    <a href="#">我是超链接</a>
</body>
```

### CSS字体/文本

#### 1、字体常用的样式

- **font-family**	 属性用于设置字体。网页中常用的字体有宋体、微软雅黑、黑体等， 

- **font-size**	 属性用于设置字号，该属性的值可以使用相对长度单位，也可以使用绝对长度单位。 

- **font-style**	 字体倾斜除了用 i 和 em 标签之外，可以使用CSS 来实现 

- **font-weight**	 字体加粗除了用 b 和 strong 标签之外，可以使用CSS 来实现 

- **font-variant**	字体的字母大小写

- **font**	 font属性用于对字体样式进行综合设置  

  ​	选择器{font: font-style font-weight font-size/line-height font-family;} 

  ​	使用font属性时，必须按上面语法格式中的顺序书写，不能更换顺序，各个属性以空格隔开 

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>字体的常用样式</title>
        <style>
            p{
                /*字体类型*/
                /*font-family: 新宋体;*/
                /*!*字体大小*!*/
                /*font-size: 40px;*/
                /*!*字体的样式*!*/
                /*font-style: italic;*/
                /*!*字体的粗细*!*/
                /*font-weight: bold;*/
                /*!*字体的字母大小写*!*/
                /*font-variant: small-caps;*/

                /*复合样式*/
                /* 顺序： 字体样式，字体大小写，字体粗细，字体大小，字体类型 */
                font: italic small-caps bold 40px 新宋体;
            }
        </style>
    </head>
    <body>
        <p>我是段落标签</p>
        <p>HELLO WORLD</p>
        <p>hello world</p>
    </body>
</html>
```

#### 2、文本常用的样式

- **text-align**	 属性用于设置文本内容的水平对齐，相当于html中的align对齐属性 
- **text-indent**	 属性用于设置首行文本的缩进，其属性值可为不同单位的数值、em字符宽度的倍数、或相对于浏览器窗口宽度的百分比%，允许使用负值, 建议使用em作为设置单位。 
- **text-decoration**	 通常我们用于给链接修改装饰效果 
- **letter-spacing**	 属性增加或减少字符间的空白（字符间距）。 
- **word-spacing**	 单词之间的空白距离 
-  如果之间比一个空格距离要宽的话，就多加几个&nbsp，这个方法虽然可行，总觉得是太暴力了，于是自己使用了css来实现该效果，但是中间也遇到一些以前没注意问题，那就是word-spacing和letter-spacing的差别。 
- **line-height**		 属性用于设置行间距，就是行与行之间的距离，即字符的垂直间距，一般称为行高 

```html
<head>
    <meta charset="UTF-8">
    <title>文本的常用样式</title>
    <style>
        p {
            /*对齐方式*/
            /*默认状态是 往左对齐*/
            text-align: left;
            /*首行缩进*/
            text-indent: 2em;  /* em代表一个中文字符的距离 */
            /*文本线*/
            /*underline 下划线 */
            /*line-through 删除线 */
            text-decoration: underline;
            /*字距*/
            letter-spacing: 10px;
            /*词距 注意：需要加空格 */
            word-spacing: 50px;
            /*行高  可以解决单行文本的垂直对齐*/
            line-height: 50px;
        }
        span {
            text-align: right;
        }
    </style>
</head>
<body>
    <p>我是段落标签 我是段落标签</p>
    <span>我是文本标签</span>
</body>
```

#### 3、背景的常用样式

- **background-color**	背景颜色

- **background-image**	背景图片地址

- **background-repeat**	是否平铺

  参数： 

  repeat : 背景图像在纵向和横向上平铺（默认的）

  no-repeat : 背景图像不平铺

  repeat-x : 　背景图像在横向上平铺

  repeat-y : 背景图像在纵向平铺

- **background-size**	背景大小

- **background-position**	背景位置

- **background**    	顺序：颜色，图片，平铺，定位/大小

```html
<head>
    <meta charset="UTF-8">
    <title>背景的常用样式</title>
    <style>
        div {
            width: 300px;
            height: 300px;
            border: 1px solid red;
            /*背景颜色*/
            background-color: green;
            background-image: url("images/590x400.jpg");
            /*背景大小*/
            background-size: 150px 100px;
            /*背景平铺*/
            background-repeat: no-repeat;
            /*背景位置*/
            background-position: center;
            /*background-position: 50% 20%;*/
            /*background-position: left top;*/
            /*复合样式*/
            /* 顺序：颜色，图片，平铺，定位/大小 */
            /*background: red url("images/590x400.jpg") no-repeat center/150px 100px;*/

        }
    </style>
</head>
<body>
    <div></div>
</body>
```



## 作业

```html
<head>
    <meta charset="UTF-8">
    <title>作业</title>
    <style>
        div {
            width: 380px;
            height: 460px;
            border: 1px solid grey;
            border-radius: 10px;
            background-color: #f9f9f9;
            margin: auto;
            padding: 0 20px;

        }

        p,.lab1 {
            font-size: 14px;
            color: grey;
        }

        a {
            text-decoration: none;
        }

        /*鼠标滑入的时候加下划线*/
        a:hover {
            text-decoration: underline;
        }

        .ipt1 {
            width: 323px;
            height: 35px;
            border-radius: 5px;
            border: 1px solid #d7d7d7;
            margin-bottom: 20px;
        }

        .sel1 {
            width: 60px;
            height: 39px;
            border-radius: 5px;
            border: 1px solid #d7d7d7;
            margin-bottom: 20px;

        }

        .ipt2 {
            width: 258px;
            height: 35px;
            border-radius: 5px;
            border: 1px solid #d7d7d7;
            margin-bottom: 20px;

        }

        .ipt4 {
            width: 220px;
            height: 35px;
            border-radius: 5px;
            border: 1px solid #d7d7d7;
            margin-bottom: 20px;
        }

        .btu1 {
            width: 100px;
            height: 39px;
            border-radius: 5px;
            border: 1px solid #d7d7d7;
            /*margin-bottom: 20px;*/
            background: url("images/590x400.jpg") center/100px 39px;
            vertical-align: middle;
        }
        .btu2{
            width: 380px;
            height: 44px;
            border-radius: 5px;
            border: 1px solid #d7d7d7;
            margin-top: 20px;
            background-color: #3ac7eb;
            color: #fff;
            font-size: 16px;
        }
    </style>
</head>
<body>
    <div>
        <h2>请注册</h2>
        <p>已有账号？
            <a href="#">登陆</a>
        </p>
        <form action="#">
            <label for="username">用户名</label>
            <input type="text" placeholder="请输入用户名" id="username" name="user" class="ipt1"><br>
            <label for="phone">手机号</label>
            <select name="prePhone" id="prePhone" class="sel1">
                <option value="+86">+86</option>
                <option value="+86" selected>+0731</option>
            </select>
            <input type="text" placeholder="请输入手机号" name="phone" id="phone" class="ipt2"><br>
            <label for="pwd">密&emsp;码</label>
            <input type="password" placeholder="请输入密码" id="pwd" name="passwd" class="ipt1"><br>
            <label for="code">验证码</label>
            <input type="text" placeholder="输入验证码" name="code" id="code" class="ipt4">
            <input type="button" class="btu1"><br>
            <input type="checkbox" name="isAgree" id="isAgree" style="vertical-align: middle">
            <label for="isAgree" class="lab1">阅读并接受协议</label><br>
            <input type="submit" value="注册" class="btu2">
        </form>
    </div>
</body>
```
