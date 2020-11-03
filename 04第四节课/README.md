## JavaScript介绍以及起源 

​	Js一种直译型脚本语言，一种动态语言、弱类型语言、支持内置类型。它的解释器被称为javascript引擎。它浏览器的一部分。用于客户端的脚本语言，最早是html网页上使用用来给HTML增加动态效果。 

​	1995年，网景首次设计实现的 。因为网景(Netscape)跟sun合作的，因此才起名叫javascript，它除了语法风格跟Java有点接近，其他**跟Java没有任何关系**  （雷锋和雷峰塔   麻婆和麻婆豆腐）

- JavaScript诞生于1995年，它的出现主要是用于处理网页中的前端验证
- 所谓的前端验证，就是指检查用户输入的内容是否符合一定的规则
- 比如：用户名的长度，密码的长度，邮箱的格式等。



​	"1994年，网景公司（Netscape）发布了Navigator浏览器0.9版。这是历史上第一个比较成熟的网络浏览器，轰动一时。但是，这个版本的浏览器只能用来浏览，不具备与访问者互动的能力。......网景公司急需一种网页脚本语言，使得浏览器可以与网页互动。" 

​	就在这时，发生了另外一件大事：1995年Sun公司将Oak语言改名为Java，正式向市场推出。 
​	Sun公司大肆宣传，许诺这种语言可以"一次编写，到处运行"（Write Once, Run Anywhere），它看上去很可能成为未来的主宰。
​	网景公司动了心，决定与Sun公司结成联盟。它不仅允许Java程序以applet（小程序）的形式，直接在浏览器中运行；甚至还考虑直接将Java作为脚本语言嵌入网页，只是因为这样会使HTML网页过于复杂，后来才不得不放弃。
​	总之，当时的形势就是，网景公司的整个管理层，都是Java语言的信徒，Sun公司完全介入网页脚本语言的决策。因此，Javascript后来就是网景和Sun两家公司一起携手推向市场的，这种语言被命名为"Java+script"并不是偶然的。

​	此时，34岁的系统程序员Brendan Eich（布兰登·艾克）登场了。1995年4月，网景公司录用了他。 

​	Brendan Eich的主要方向和兴趣是函数式编程，网景公司招聘他的目的，是研究将Scheme（si ge me）语言作为网页脚本语言的可能性。Brendan Eich本人也是这样想的，以为进入新公司后，会主要与Scheme语言打交道。 

​	仅仅一个月之后，1995年5月，网景公司做出决策，未来的网页脚本语言必须"看上去与Java足够相似"，但是比Java简单，使得非专业的网页作者也能很快上手。这个决策实际上将Perl、Python、Tcl、Scheme等非面向对象编程的语言都排除在外了。 

​	Brendan Eich被指定为这种"简化版Java语言"的设计师。 

​	但是，他对Java一点兴趣也没有。为了应付公司安排的任务，他只用10天时间就把Javascript设计出来了 

​	由于设计时间太短，语言的一些细节考虑得不够严谨，导致后来很长一段时间，Javascript写出来的程序混乱不堪。如果Brendan Eich预见到，未来这种语言会成为互联网第一大语言，全世界有几百万学习者，他会不会多花一点时间呢？ 

 总的来说，他的设计思路是这样的： 

	 - 借鉴C语言的基本语法
	 - 借鉴Java语言的数据类型和内存管理
	 - 借鉴Scheme语言，将函数提升到“第一等公民”（fisrt class）的地位
	 - 借鉴Self语言，使用基于原型（prototype）的继承机制。

 所以，Javascript语言实际上是两种语言风格的混合产物----（简化的）函数式编程+（简化的）面向对象编程。这是由Brendan Eich（函数式编程）与网景公司（面向对象编程）共同决定的。 



### 什么是语言

- 计算机就是一个由人来控制的机器，人让他干嘛，它就得干嘛（听人的指令）
- 我们要学习的语言就是人和计算机交流的工具，人类通过语言来控制、操作计算机
- 编程语言和我们说的中文、英文本质上没有区别，只是语法比较的特殊



## JS的使用

```html
<head>
    <meta charset="UTF-8">
    <title>JS的使用</title>
    <!--<script>
/*
1.方法用于在网页加载完毕后立刻执行的操作，即当 HTML 文档加载完毕后，立刻执行某个方法。
因为 JavaScript 中的函数方法需要在 HTML 文档渲染完成后才可以使用，如果没有渲染完成，此时的 DOM 树是不完整的，
这样在调用一些 JavaScript 代码时就可能报出"undefined"错误。
2. 但是不建议放在head头部写
*/
window.onload = function () {
alert(123123)
}
</script>-->
</head>
<body>

</body>
<!--<script>
/*放在body的底部去写*/
alert(123)
</script>-->

<!--外部JS文件，进行引入  推荐-->
<script src="js/body.js">
    /*如果使用引入  那么这个script块将会无法使用*/
    alert(12)
</script>

<!--
注意事项：
1. 每一行完整的语句后面加上分号
2. JS严格区分大小写
-->
```



## JS获取元素的方法

```html
<head>
    <meta charset="UTF-8">
    <title>JS获取元素的方法</title>
</head>
<body>
    <div id="div1">
        <p id="p1">我是一个段落1</p>
        <p class="p2">我是一个段落2</p>
        <p class="p2" name="pname">我是一个段落3</p>
    </div>
</body>
<script>
    /*JS获取独有标签*/
    console.log(document.title);
    console.log(document.head);
    console.log(document.body);

    /* var 是定义变量的关键字 */
    /* 变量名不能使用 关键字和保留字也不能用数字 */
    /* innerText  修改文本内容 */
    /* innerText和innerHtml区别
        innerHTML设置或获取标签所包含的HTML+文本信息(从标签起始位置到终止位置全部内容，包括HTML标签，但不包括自身)
        innerText设置或获取标签所包含的文本信息（从标签起始位置到终止位置的内容，去除HTML标签，但不包括自身）
        innerHTML、innerText仅设置标签之间的文本
    */
    /* 获取元素的方法
    getElementById()
    getElementsByClassName()
    getElementsByName()
    getElementsByTagName()  通过标签名
    通过CSS选择器获取元素  (不支持伪类)
        querySelector()   多个的情况下只会获取第一个
        querySelectorAll()  获取选中的所有元素
    */
    var p1 = document.getElementById("p1");
    // p1.innerText = "我不是段落1";
    p1.innerHTML = "<h1>我不是段落1</h1>";
    var p2 = document.getElementsByClassName("p2");
    console.log(p2);
    p2.item(0).innerText = '123123';

    var pname = document.getElementsByName("pname");
    pname[0].innerText = '978678';
    console.log(pname);

    var ptag = document.getElementsByTagName("p");
    ptag[1].innerText = '978678';
    console.log(ptag);

    var qsid = document.querySelector("#p1");
    console.log(qsid);

    console.log(document.querySelectorAll("p")[2]);

    var box = document.getElementById("div1");
    console.log(box.getElementsByClassName("p2"));
</script>
```



## JS基本事件

```html
<head>
    <meta charset="UTF-8">
    <title>JS基本事件</title>
</head>
<body>
<p>点我</p>
<script>
    var aP = document.querySelector("p");
    // 单击事件
    /*aP.onclick = function () {
        alert("别点我")
    };*/
    // 双击事件
    /*aP.ondblclick = function () {
      alert("点了我两下")
    }*/
    // 滑入事件
    /*aP.onmouseenter = function () {
        aP.innerText = "别点我"
    };*/
    // 滑出事件
    /*aP.onmouseleave = function () {
        aP.innerText = "点我"
    };*/
</script>
</body>
```



## JS修改样式

```html
<head>
    <meta charset="UTF-8">
    <title>JS修改样式</title>
    <style>
        div {
            width: 100px;
            height: 100px;
            background-color: red;
        }
    </style>
</head>
<body>
    <div></div>
    <script>
        var obox = document.getElementsByTagName("div")[0];
        obox.onclick = function () {
            obox.style.width = "200px";
            obox.style.height = "200px";
            // obox.style.background = "green";
            // obox.style.backgroundColor = "green";
            // obox.style["background-color"] = "blue";
            obox.style.cssText = "background-color:blue;";
            console.log(obox.style.cssText)

        };
    </script>
</body>
```

**将CSS代码分离至script块**

```html
<head>
    <meta charset="UTF-8">
    <title>JS操作标签属性</title>
    <style>
        .bb {
            width: 100px;
            height: 100px;
            background-color: red;
        }
    </style>
</head>
<body>
    <div id="div1"></div>
    <script>
        var obox = document.getElementById("div1");
        // 单独操作Class属性
        obox.className = "aa";  // 增加
        obox.className = "bb";  // 修改  覆盖
        console.log(obox.className);  // 查
        obox.removeAttribute("class");  // 移除class属性

        // 操作自定义属性
        obox.setAttribute("aa", "a11");  // 增加
        obox.setAttribute("aa", "a22");  // 增加
        console.log(obox.getAttribute("aa"));  // 查
        console.log(obox.hasAttribute("name"));  // 查看是否有此属性  true  false
        obox.removeAttribute("aa");  // 移除aa属性  删除

    </script>
</body>
```



## JS数据类型

```html
<head>
    <meta charset="UTF-8">
    <title>JS基本数据类型</title>
</head>
<body>
    <input type="text" id="ipt1">
    <script>
        var a = 123;   // number 数字类型
        console.log(typeof a);
        var b = "123";   // string 字符串类型
        console.log(typeof b);
        var c = true;
        console.log(typeof c);  // boolean 布尔类型
        var d;
        console.log(typeof d);  // undefined  未定义
        var e = null;
        console.log(typeof e);  // object 对象 (空对象)
        var f = [1, 2, 3, 4, 5];   // 数组 object
        console.log(typeof f);
        
	    // 今日作业细节
        var oinp = document.getElementById("ipt1");
        document.onclick = function(){
            console.log(oinp.value);
        };
    </script>
</body>
```



## 作业

```html
<head>
    <meta charset="UTF-8">
    <title>作业</title>
    <style>
        input {
            height: 30px;
            margin-bottom: 10px;
        }

        div {
            width: 200px;
            height: 200px;
            background-color: #ff00ef;
            line-height: 200px; /*文字垂直居中*/
            text-align: center; /*文字水平居中*/
            color: white;
        }
    </style>
</head>
<body>
    属&emsp;性：<input type="text" placeholder="请输入属性"><br>
    属性值：<input type="text" placeholder="请输入属性值"><br>
    <input type="button" value="设置属性"><br>
    <div id="box">JavaScript</div>
    <script>
        var oBox = document.getElementById("box");
        var aInput = document.getElementsByTagName("input");

        aInput[2].onclick = function () {
            var att = aInput[0].value;
            var attValue = aInput[1].value;

            // oBox.style[att] = attValue;  /* 方法一 设置属性 */
            // oBox.setAttribute('style', att + ":" + attValue);   /*方法二 */
            oBox.style.cssText = att + ":" + attValue;   /* 方法三 */

            aInput[0].value = '';
            aInput[1].value = '';

        }

    </script>
</body>
```




