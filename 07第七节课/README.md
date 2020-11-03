## JQuery的引入方式

```html
<head>
    <meta charset="UTF-8">
    <title>JQuery的引入方式</title>
</head>
<body>
    <!--网址引入-->
    <!--<script src="https://cdn.bootcdn.net/ajax/libs/jquery/3.4.1/jquery.js"></script>-->
    <!--本地引入-->
    <script src="js/jquery-3.4.1.js"></script>

    <script>
        /* 测试jquery是否导入 */
        $(function () {
            alert(123123);
        })
    </script>
</body>
```



## jQuery选择器

```html
<head>
    <meta charset="UTF-8">
    <title>jQuery选择器</title>
    <style>
        p {}
        #p1 {}
        .p2 {}
    </style>
</head>
<body>
    <p id="p1" class="p2">我爱祖国</p>
    <script src="js/jquery-3.4.1.js"></script>
    <script>
        /*    var oP = document.getElementsByTagName("p")[0];  // JS语法
        oP.innerText = "我是你爹";*/

        // jQuery获取元素
        console.log($("p"));   // 通过标签
        console.log($("#p1"));  // 通过id
        console.log($(".p2"));  // 通过class

        console.log($("#p1").text());  // 获取文本  innerText
        console.log($("#p1").html());   // 获取文本  innerHtml
        $("#p1").text("我是你爹")   // 修改文本


        /*
        jQuery
            $() jQuery选择器
            text()   html()   修改查看的方法与innerText、innerHtml几乎相同
    */

        // console.log($("#p1").innerText());   // jQuery 不能直接使用js方法

    </script>
</body>
```



## jQuery和js相互转换

```html
<head>
    <meta charset="UTF-8">
    <title>jQuery和js相互转换</title>
</head>
<body>
    <p id="p1" class="p2">我爱祖国</p>
    <p class="p2">我爱祖国</p>
    <p class="p2">我爱祖国</p>
    <script src="js/jquery-3.4.1.js"></script>
    <script>
        // JQ转换JS   JQ使用js的方法
        // $("p").text(123123);  // JQ不需要加下标就可以操作多个元素
        /*
        $("p").get(0).innerText = "我是你爹";
        $("p")[1].innerText = "我是你爹";
    */

        // JS转换JQ
        var aP = document.getElementsByTagName("p");
        $(aP).eq(1).text("123123")  // eq是JQ加下标的方法


    </script>
</body>
```



## jQuery操作HTML属性

```html
<head>
    <meta charset="UTF-8">
    <title>jQuery操作HTML属性</title>
</head>
<body>
    <div></div>
    <script src="js/jquery-3.4.1.js"></script>
    <script>
        /*
        操作Class属性
            addClass  removeClass
    */
        $("div").addClass("div1"); // 增
        $("div").addClass("div2"); // 增 不会覆盖
        $("div").removeClass("div2"); // 删
        $("div").removeClass("div1").addClass("div3"); // 改

        /*
        操作其他属性
            attr  removeAttr
    */
        $("div").attr("id",'div12');   // 增 与js中 setAttribute 相同
        $("div").attr("id",'div13');   // 改
        $("div").removeAttr("id");  // 删  直接吧整个id删除
        // $("div").removeAttr("class");  // 删  直接吧整个class删除

        /*
        toggleClass()
        无则增加  有则删
        可以用于点击事件，点一下增加，点一下删掉。效果
    */
        $("div").toggleClass("div1");  // 会增加 div1
        $("div").toggleClass("div1");  // 会直接删除 div1
    </script>


    <input type="text" value="1">
    <input type="text" value="2">
    <input type="text" value="3">
    <script>
        /*
        获取值默认第一个
        设置值设置所有
    */
        console.log($("input").val());  // 只有第一个value的值
        $("input").val(3333)  //设置值设置所有
    </script>
</body>
```



## jQuery操作CSS样式

```html
<head>
    <meta charset="UTF-8">
    <title>jQuery操作CSS样式</title>
    <style>
        div {
            width: 200px;
            height: 200px;
            border: 5px solid red;
            padding: 50px;
            position: relative;   /*讲定位的时候在写*/
        }
    </style>
</head>
<body>
    <div>
        <p>我是你爹</p>
    </div>
    <script src="js/jquery-3.4.1.js"></script>
    <script>

        /*
        width()  获取本身设置的宽度
        innerWidth()  获取内边距加上宽度之后的宽
        outerWidth()  获取加上padding和border 之后的宽
    */
        console.log($("div").width());  // 200
        console.log($("div").innerWidth());   // 300
        console.log($("div").outerWidth());   // 310

        /*
        css()  修改单个样式
        css({})  修改多个样式  键值对的形式
    */
        $("div").css("width", "300px");
        $("div").css({
            "width": "400px",
            "height": "400px",
            "background-color": "green",
        })
    </script>
    <script>
        /*
        定位父级
            前提是父级要设置定位才行，不然就是距离浏览器的位置
    */
        var box = $("p").position(); // {top : 63, left : 63}
        // {top : 63, left : 63}是不对的，在父级设置定位属性后 {top : 50, left : 50}
        console.log(box.top);
        console.log(box.left);

        /*
        定位窗口
            始终返回相对于浏览器的距离，它会忽略外层元素。
            在不同浏览器中,offset()得到的相对于浏览器的位置不同
    */
        var box1 = $("p").offset();
        console.log(box1); // {top: 79, left: 63}
    </script>
</body>
```



## jQuery事件

```html
<head>
    <meta charset="UTF-8">
    <title>jQuery事件</title>
    <style>
        div{
            width: 200px;
            height: 200px;
            background-color: #ff00ef;
        }
    </style>
</head>
<body>
    <p>我是111</p>
    <p>我是222</p>
    <p>我是333</p>
    <button type="button">移除点击事件</button>

    <div></div>
    <script src="js/jquery-3.4.1.js"></script>
    <script>
        /*
        click()  单击事件
        dblclick()  双击事件
        hover()  当一个函数的时候，划入滑出执行同一个方法
                 当两个函数的时候，第一个滑入事件，第二个滑出事件
        on()  添加事件
        off()   移除on的事件
    */
        $("p").eq(0).click(function () {
            alert(111)
        });
        $("p").eq(1).dblclick(function () {
            alert(222)
        });

        // mouse  鼠标
        $("div").hover(function () {  // 滑入滑出都执行  可以看看源码
            console.log(1);
        },function () {
            console.log(2);
        });

        $("p").on("click",function () {
            $(this).css("background",'red')
        });
        $("button").click(function () {
            $("p").off("click");   // 移除上面的单击事件
        })

    </script>
</body>
```



##  jQuery 动画

```html
<head>
    <meta charset="UTF-8">
    <title>jQuery动画</title>
    <style>
        div {
            width: 200px;
            height: 200px;
            background-color: #3ac7eb;

            position: relative; /*此处讲动画再写*/
        }
    </style>
</head>
<body>
    <button type="button" id="btn1">按钮一</button>
    <button type="button" id="btn2">按钮二</button>
    <div></div>

    <script src="js/jquery-3.4.1.js"></script>
    <script>
        /*
        hide()  隐藏
        show()  显示
    */
        /*    $("#btn1").click(function () {
            $("div").hide();  // 隐藏
        });
        $("#btn2").click(function () {
            $("div").show();  // 显示
        });*/

        /*
        滑动
            slideUp()  向上隐藏
            slideDown()  向下显示
            slideToggle()  取反
    */
        /*    $("#btn1").click(function () {
            $("div").slideUp(2000);
            $("div").slideToggle();
        });
        $("#btn2").click(function () {
            $("div").slideDown(2000);
        });*/

        /*
        淡入
            fadeOut  隐藏
            fadeToggle  显示
            fadeIn 取反
    */
        /*$("#btn1").click(function () {
        $("div").fadeOut(2000);
        $("div").fadeToggle(2000);
    });
    $("#btn2").click(function () {
        $("div").fadeIn(2000);
    });*/

        /*
        自定义  透明度是从  0 - 1
            fadeTo()
    */
        /*    $("#btn1").click(function () {
            $("div").fadeTo(2000,0.2);
        });
        $("#btn2").click(function () {
            $("div").fadeTo(2000,0.8);
        });*/

        /*
        动画
            animate() 动画
            stop()  动画
            delay() 延迟之后在执行  按钮一 -》 按钮二 -》 按钮一
    */
        $("#btn1").click(function () {
            $("div").animate({
                width:300,
                height:300,
                top:100,
                left:300,
            },2000).delay(4000);
        });
        $("#btn2").click(function () {
            $("div").stop();
        });

    </script>
</body>
```



## 作业（动态轮播图）

1. 删除之前的JS代码

```html
 
```


