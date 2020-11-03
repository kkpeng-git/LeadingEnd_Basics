## 前期回顾



### CSS的三种引入方式

 CSS的引入方式共有三种：行内样式、内部样式表、外部样式表。 

### CSS选择器

标签选择器、class选择器、id选择器

class选择器的代表符号  " . "

class选择器的代表符号  " # "

### CSS字体

#### 字体常用的样式

- **font-family**	 属性用于设置字体。网页中常用的字体有宋体、微软雅黑、黑体等， 

- **font-size**	 属性用于设置字号，该属性的值可以使用相对长度单位，也可以使用绝对长度单位。 

- **font-style**	 字体倾斜除了用 i 和 em 标签之外，可以使用CSS 来实现 

- **font-weight**	 字体加粗除了用 b 和 strong 标签之外，可以使用CSS 来实现 

- **font-variant**	字体的字母大小写

- **font**	 font属性用于对字体样式进行综合设置  

  ​	选择器{font: font-style font-weight font-size/line-height font-family;} 

  ​	使用font属性时，必须按上面语法格式中的顺序书写，不能更换顺序，各个属性以空格隔开 

### CSS文本

#### 文本常用的样式

- **text-align**	 属性用于设置文本内容的水平对齐，相当于html中的align对齐属性 
- **text-indent**	 属性用于设置首行文本的缩进，其属性值可为不同单位的数值、em字符宽度的倍数、或相对于浏览器窗口宽度的百分比%，允许使用负值, 建议使用em作为设置单位。 
- **text-decoration**	 通常我们用于给链接修改装饰效果 
- **letter-spacing**	 属性增加或减少字符间的空白（字符间距）。 
- **word-spacing**	 单词之间的空白距离 
- 如果之间比一个空格距离要宽的话，就多加几个&nbsp，这个方法虽然可行，总觉得是太暴力了，于是自己使用了css来实现该效果，但是中间也遇到一些以前没注意问题，那就是word-spacing和letter-spacing的差别。 
- **line-height**		 属性用于设置行间距，就是行与行之间的距离，即字符的垂直间距，一般称为行高 

### CSS背景

#### 背景的常用样式

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



# CSS 提升



## 盒子模型 （CSS重点）

其实，CSS就三个大模块： 盒子模型 、 浮动 、 定位，其余的都是细节。要求这三部分，无论如何也要学的非常精通。

所谓盒子模型就是把HTML页面中的元素看作是一个矩形的盒子，也就是一个盛装内容的容器。每个矩形都由元素的**内容（content）、内边距（padding）、边框（border）和外边距（margin）**组成。

![1603096374298](C:\Users\SpuerCoder\AppData\Roaming\Typora\typora-user-images\1603096374298.png)



### 边框（border）

边框就是那层皮。 橘子皮。。柚子皮。。橙子皮。。。 

- **border-width**	边框的宽度
- **border-style** 	边框的样式
- **border-color**	边框的颜色

```html
<head>
    <meta charset="UTF-8">
    <title>盒子模型---边框</title>
    <style>
        div {
            width: 200px;
            height: 200px;
            /*边框 复合样式 */
            /*border: 1px solid red;*/

            /*border-width: 2px; !* 边框的宽度 *!*/
            /*border-style: solid; !* 边框的样式 *!*/
            /*border-color: blue; !* 边框的颜色 *!*/

            /*单独设置边框的写法*/
            border-top: 1px solid red; /* 实线 */
            border-left: 1px dotted green; /* 点线 */
            border-right: 2px dashed blue; /* 虚线 */
            border-bottom: 5px double orange; /* 双线 */
        }
    </style>
</head>
<body>
    <div></div>
</body>
```



### 内边距（padding）

指边框与内容之间的距离

- **padding-top:**      上内边距
- **padding-right:**      右内边距
- **padding-bottom:**      下内边距
- **padding-left:**      左内边距
- **padding:**      第一个上  第二个右 第三个下 第四个左

```html
<head>
    <meta charset="UTF-8">
    <title>盒子模型---内边距</title>
    <style>
        div {
            width: 300px;
            height: 300px;
            border: 1px solid blue;

            /*
            特点：
            1. 内边距会撑大盒子
            2. 内边距不能设置负值

            */
            /*padding-top: 50px;*/
            /*padding-left: 50px;*/
            /*padding-right: 50px;*/
            /*padding-bottom: 50px;*/

            /*复合样式*/
            /*当参数值为一个的时候：上下左右都会*/
            /*padding: 50px;*/
            /*当参数值为两个的时候：第一个上下  第二个左右*/
            /*padding: 50px 100px;*/
            /*当参数值为两个的时候：第一个上  第二个左右 第三个下*/
            /*padding: 50px 100px 60px;*/
            /*当参数值为两个的时候：第一个上  第二个右 第三个下 第四个左*/
            padding: 50px 100px 60px 80px;
        }
    </style>
</head>
<body>
    <div>
        我是模型
    </div>
</body>
```



### 外边距（margin）

 设置外边距会在元素之间创建“空白”， 这段空白通常不能放置其他内容。 

- **margin-top:**    上外边距
- **margin-right:**    右外边距
- **margin-bottom:**    下外边距
- **margin-left:**    上外边距
- **margin:**    上外边距 右外边距 下外边距 左外边

 取值顺序跟内边距相同。 

```html
<head>
    <meta charset="UTF-8">
    <title>盒子模式---外边距</title>
    <style>
        /*
        特点：
        1. 不会撑大盒子
        2. 可以设置负值
        */
        div {
            width: 300px;
            height: 300px;
            /*行内块状元素*/
            /*
            1. 可以设置宽高
            2. 不会自动换行
            3. 当多个行内块状标签写在一起的时候，排列方式从左到右
            */
            /*display: inline-block;*/
        }

        #div1 {
            border: 2px solid green;
            /*margin-top: 50px; !*上外边距*!
            margin-left: 50px; !*左外边距*!
            !*margin-bottom: 50px;!*下外边距*!*!
            margin-right: 50px; !*右外边距*!*/

            /*margin: 50px 100px;*/

            /*margin: auto;  !*水平居中*!*/

            margin-bottom: 100px;
        }

        #div2 {
            border: 2px solid red;
            margin-top: 150px;
        }
    </style>
</head>
<body>
    <div id="div1"></div>
    <div id="div2"></div>

</body>
```





### **盒子模型布局稳定性**

​	开始学习盒子模型，同学们最大的困惑就是， 分不清内外边距的使用，什么情况下使用内边距，什么情况下使用外边距？

答案是： 其实他们大部分情况下是可以混用的。 就是说，你用内边距也可以，用外边距也可以。 你觉得哪个方便，就用哪个。

但是，总有一个最好用的吧，我们根据稳定性来分，建议如下：

 按照 优先使用 宽度 （width） 其次 使用内边距（padding） 再次 外边距（margin）。 

**原因：**

margin 会有外边距合并 还有 ie6下面margin 加倍的bug（讨厌）所以最后使用。

padding 会影响盒子大小， 需要进行加减计算（麻烦） 其次使用。

width 没有问题（嗨皮）我们经常使用宽度剩余法 **宽度剩余法**来做。

```html
<head>
    <meta charset="UTF-8">
    <title>盒子模型布局稳定性</title>
    <style>
        div{
            width: 300px;
            height: 50px;
            border: 1px solid red;
        }
        h3{
            /*
            主要讲述  浏览器检查元素（F12）margin 和 padding区别。 背景颜色的平移
            */
            /*margin-left: 10px;*/
            padding-left: 10px;
            background-color: orange;
        }
    </style>
</head>
<body>
    <div>
        <h3>我们是冠军</h3>
    </div>
</body>
```

**宽度剩余法**

![1603112506453](C:\Users\SpuerCoder\AppData\Roaming\Typora\typora-user-images\1603112506453.png)



### 盒子阴影

 box-shadow:水平阴影 垂直阴影 模糊距离 阴影尺寸 阴影颜色  内/外阴影； 

| 值           | 描述                                           |
| ------------ | ---------------------------------------------- |
| **h-shadow** | 必需。水平阴影的位置。允许负值                 |
| **v-shadow** | 必需。垂直阴影的位置。允许负值                 |
| **blur**     | 可选。模糊距离                                 |
| **spread**   | 可选。阴影的尺寸                               |
| **color**    | 可选。阴影的颜色                               |
| **inset**    | 可选。将外部阴影（ouset）改为内部阴影（inset） |

1、前两个属性是必须写的。其余的可以省略。

2、外阴影 (outset) 但是不能写 默认 想要内阴影 inset

```html
<head>
    <meta charset="UTF-8">
    <title>盒子阴影</title>
    <style>
        h1{
            font-size: 100px;
            /*text-shadow: 水平距离 垂直距离 模糊 阴影颜色;*/
            text-shadow: 10px 3px 3px rgba(0,0,0,.5);
        }
        div{
            width: 200px;
            height: 200px;
            border: 10px solid red;
            box-shadow: 5px 5px 3px 4px rgba(0,0,0, .5);
        }
    </style>
</head>
<body>
    <h1>我们是冠军</h1>
    <div></div>
</body>
```





### 浮动（float）

#### 什么是浮动

-  元素的浮动是指设置了浮动属性的元素会脱离标准普通流的控制，移动到其父元素中指定位置的过程。 

#### 浮动详细内幕特性

-  浮动脱离标准流，不占位置，会影响标准流。浮动只有左右浮动。 
-  浮动首先创建包含块的概念（包裹）。就是说， 浮动的元素总是找理它最近的父级元素对齐。但是不会超出内边距的范围。 
-  浮动的元素排列位置，跟上一个元素（块级）有关系。如果上一个元素有浮动，则A元素顶部会和上一个元素的顶部对齐；如果上一个元素是标准流，则A元素的顶部会和上一个元素的底部对齐。 

```html
<head>
    <meta charset="UTF-8">
    <title>浮动</title>
    <style>
        /*#div4{
        !*1. 设置高度  不建议使用*!
        !*height: 200px;*!

        !*2. 设置超出部分隐藏  不建议使用*!
        !*overflow: hidden;*!
        }*/

        /*4. 使用after伪元素清除浮动*/
        #div4:after{
            display: block;
            clear: both;  /*清除浮动*/
            content: "";
        }
        #div1, #div2, #div3 {
            width: 200px;
            height: 200px;
        }

        #div1 {
            background-color: red;
            float: left;
        }

        #div2 {
            background-color: green;
            float: left;
        }

        #div3 {
            background-color: blue;
            float: left;
        }
        #div5{
            width: 200px;
            height: 200px;
        }
    </style>
</head>
<body>
    <div id="div4">
        <div id="div1"></div>
        <div id="div2"></div>
        <div id="div3"></div>

        <!-- 3. 添加一个空的div  不建议使用 -->
        <!--<div id="div5"></div>-->
    </div>
</body>
```



### 定位（position）

#### 元素的定位属性

元素的定位属性主要包括定位模式和偏移量两部分

| 边偏移属性 | 描述                                           |
| ---------- | ---------------------------------------------- |
| top        | 顶端偏移量，定义元素相对于其父元素上边线的距离 |
| bottom     | 底部偏移量，定义元素相对于其父元素下边线的距离 |
| left       | 左侧偏移量，定义元素相对于其父元素左边线的距离 |
| right      | 右侧偏移量，定义元素相对于其父元素右边线的距离 |

 也就说，以后定位要和这边偏移搭配使用了， 比如 top: 100px; left: 30px; 等等 

#### **position**属性的常用值 

| 值       | 描述                                             |
| -------- | ------------------------------------------------ |
| static   | 自动定位（默认定位方式）                         |
| relative | 相对定位，相对于其原文档流的位置进行定位         |
| absolute | 绝对定位，相对于其上一个已经定位的父元素进行定位 |
| fixed    | 固定定位，相对于浏览器窗口进行定位               |

#### 静态定位（static）

​	静态定位是所有元素的默认定位方式，当position属性的取值为static时，可以将元素定位于静态位置。 所谓静态位置就是各个元素在HTML文档流中默认的位置。

上面的话翻译成白话： 就是网页中所有元素都默认的是静态定位哦！ 其实就是标准流的特性。

在静态定位状态下，无法通过边偏移属性（top、bottom、left或right）来改变元素的位置。

**PS： 静态定位其实没啥可说的。**



#### 相对定位（relattive）

 	相对定位是将元素相对于它在标准流中的位置进行定位，当position属性的取值为relative时，可以将元素定位于相对位置。对元素设置相对定位后，可以通过边偏移属性改变元素的位置，但是它在文档流中的位置仍然保留。 

**注意：**

1、相对定位最重要的一点是，它可以通过边偏移移动位置，但是原来的所占的位置，继续占有。

2、其次，每次移动的位置，是以自己的左上角为基点移动（相对于自己来移动位置）

就是说，相对定位的盒子仍在标准流中，它后面的盒子仍以标准流方式对待它。（相对定位不脱标）

如果说浮动的主要目的是 让多个块级元素一行显示，那么定位的主要价值就是 移动位置， 让盒子到我们想要的位置上去。

```html
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style type="text/css">
        .box {
            background: red;
            width: 100px;
            height: 100px;
            float: left;
            margin: 5px;
        }

        .two {
            background-color: green;
            position: relative;
            top: 50px;
            left: 50px;
        }
    </style>
</head>
<body>
    <div class="box">One</div>
    <div class="box  two">Two</div>
    <div class="box">Three</div>
    <div class="box">Four</div>
</body>
```





#### 绝对定位（absolute）

绝对定位最重要的一点是，它可以通过边偏移移动位置，但是它完全脱标，完全不占位置。 

绝对定位是将元素依据最近的已经定位（绝对、固定或相对定位）的父元素（祖先）进行定位。 

**子绝父相**

- 这句话的意思是 子级是绝对定位的话， 父级要用相对定位。 

- 首先， 我们说下， 绝对定位是将元素依据最近的已经定位绝对、固定或相对定位）的父元素（祖先）进行定位。就是说， 子级是绝对定位，父亲只要是定位即可（不管父亲是绝对定位还是相对定位，甚至是固定定位都可以），就是说， 子绝父绝，子绝父相都是正确的。 

  **所以，我们可以得出如下结论：**

  - 因为子级是绝对定位，不会占有位置， 可以放到父盒子里面的任何一个地方。

  - 父盒子布局时，需要占有位置，因此父亲只能是 相对定位。这就是子绝父相的由来。

```html
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        .box {
            width: 300px;
            height: 300px;
            border: 2px solid red;
            /*float: left;*/
        }

        .two {
            background-color: #ff00ef;
            position: absolute;
            top: 50px;
            left: 50px;
        }

    </style>
</head>
<body>
    <div class="box">1</div>
    <div class="box two">2</div>
    <div class="box">3</div>
    <div class="box">4</div>
</body>
```





#### 固定定位（fixed）

​	固定定位是绝对定位的一种特殊形式，类似于 正方形是一个特殊的 矩形。它以**浏览器窗口作为参照物**来定义网页元素。当position属性的取值为fixed时，即可将元素的定位模式设置为固定定位。 

​	当对元素设置固定定位后，它将脱离标准文档流的控制，始终依据浏览器窗口来定义自己的显示位置。不管浏览器滚动条如何滚动也不管浏览器窗口的大小如何变化，该元素都会始终显示在浏览器窗口的固定位置。 

**固定定位有两点**

-   固定定位的元素跟父亲没有任何关系，只认浏览器。 
-   固定定位完全脱标，不占有位置，不随着滚动条滚动。 

 **ie6等低版本浏览器不支持固定定位。** 

```html
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style type="text/css">
        .box {
            background: red;
            width: 300px;
            height: 300px;
            /*float: left;*/
            margin: 5px;
        }

        .two {
            background-color: green;
            position: fixed;
            top: 50px;
            left: 50px;
        }
    </style>
</head>
<body>
    <div class="box">One</div>
    <div class="box  two">Two</div>
    <div class="box">Three</div>
    <div class="box">Four</div>
    <div class="box">Four</div>
    <div class="box">Four</div>
    <div class="box">Four</div>
</body>

```



#### 层级（z-index）

 当对多个元素同时设置定位时，定位元素之间有可能会发生重叠。 

 在CSS中，要想调整重叠定位元素的堆叠顺序，可以对定位元素应用z-index层叠等级属性，其取值可为正整数、负整数和0。 

**注意：**

**1、**z-index的默认属性值是0，取值越大，定位元素在层叠元素中越居上。

**2、**如果取值相同，则根据书写顺序，后来居上。

**3、**后面数字一定不能加单位。

**4、**只有相对定位，绝对定位，固定定位有此属性，其余标准流，浮动，静态定位都无此属性，亦不可指定此属性。

```html
<head>
    <meta charset="UTF-8">
    <title>层级</title>
    <style>
        /*z-index 建立在定位元素上*/
        ul{
            list-style: none;  /*取消前缀*/
            position: relative;
        }
        ul li{
            width: 100px;
            height: 100px;
            position: absolute;
        }
        .li1{
            background: red;
            z-index: 2;
        }
        .li2{
            background: green;
            z-index: 1;
        }
        .li3{
            background: blue;
        }
    </style>
</head>
<body>
    <ul>
        <li class="li1"></li>
        <li class="li2"></li>
        <li class="li3"></li>
    </ul>
</body>

```



## 作业

```html
<head>
    <meta charset="UTF-8">
    <title>作业</title>
    <link rel="stylesheet" href="css/reset.css">  <!-- 导入重置样式表 -->
    <style>
        .slide {
            width: 550px;
            height: 400px;
            border: 1px solid grey;
            margin: 50px auto;

            position: relative;
        }

        /*图片区域*/
        .slide .pic {
            position: absolute;
            top: 0;
            left: 0;
        }

        .slide .pic img {
            width: 550px;
            height: 400px;
        }

        /*左右箭头*/
        .slide .btn {
            height: 400px;
        }

        .slide .btn li {
            width: 30px;
            height: 30px;
            border: 1px solid #fff;
            border-radius: 50%;
            position: absolute;
            /*设置 < 和 >  的文本*/
            color: white;
            text-align: center; /*左右居中*/
            line-height: 30px; /*垂直居中*/
            top: 50%;
            /*沿Y轴移本身高度的一半*/
            transform: translateY(-50%);
            /*让鼠标变成一个小手*/
            cursor: pointer;

        }

        /*鼠标滑入时 改变背景颜色*/
        .slide .btn li:hover {
            background-color: rgba(223, 223, 223, 0.3);
        }

        .slide .btn .left {
            left: 0;
            margin-left: 10px;
        }

        .slide .btn .right {
            right: 0;
            margin-right: 10px;
        }

        /*小圆圈*/
        .slide .tab {
            position: absolute;
            bottom: 10px;
            left: 50%;
            transform: translateX(-50%);
        }

        .slide .tab li {
            float: left;
            width: 8px;
            height: 8px;
            border: 2px solid #78ffd2;
            border-radius: 50%;
            background-color: aqua;
            margin-left: 5px;
            /*让鼠标变成一个小手*/
            cursor: pointer;
        }
        .slide .tab li:hover {
            background-color: #ff00ef;
        }

    </style>
</head>
<body>
    <div class="slide">
        <!--图片列表-->
        <ul class="pic">
            <li>
                <img src="images/590x400.jpg" alt="图片出错了">
            </li>
        </ul>
        <!--左右箭头-->
        <ul class="btn">
            <li class="left">&lt;</li>
            <li class="right">&gt;</li>
        </ul>
        <!--小圆圈-->
        <ul class="tab">
            <li></li>
            <li></li>
            <li></li>
            <li></li>
        </ul>
    </div>
</body>

```



