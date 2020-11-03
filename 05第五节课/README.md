## JS运算符

```html
<head>
    <meta charset="UTF-8">
    <title>操作符</title>
</head>
<body>

    <script>
        /*
    * 算术运算符
    *  + - * / %
    总结如下：对非Number（字符串除外）的值进行加运算时会先将其转换成Number型在运算，注意任何值和NaN运算都是NaN;对于含有字符串类型的相加运算则看成连字符且优先级从左向右
    */
        var a = 2;
        var b = 3;
        var c = '4';
        /*    document.write(a + b + "<br>");  // 直接在页面打印
        document.write(a + c + "<br>");  // 当数字加上字符串的时候  执行的是拼接
        document.write(c - a + "<br>");  // 隐式转换
        document.write(c * a + "<br>");  // 隐式转换
        document.write(c / a + "<br>");  // 隐式转换
        document.write(c % a + "<br>");  // 隐式转换*/
        
        /*document.write(1 + true + "<br>");  // 隐式转换
    document.write(1 + false + "<br>");  // 隐式转换
    document.write(10 + null + "<br>");  // 隐式转换
    document.write(1 + undefined + "<br>");  // 隐式转换   NaN 非数字的值*/

        /*
        赋值运算符
        ++ 放在后面的时候，先打印值，在加1
        ++ 放在前面的时候，先加一，在打印值
        
    */
        document.write((b = 5) + "<br>");
        document.write((b += 1) + "<br>");
        document.write((b -= 1) + "<br>");

        document.write((b++) + "<br>"); // 先打印
        // document.write((b) + "<br>"); // 后加一

        document.write((++b) + "<br>");
        // document.write((b) + "<br>");


        /*
        逻辑运算符
        || 或
        && 与
        ! 取反   真的变假的。  假的变真的
    */
        document.write((2 > 3 || 3 < 5) + "<br>");
        document.write((2 > 3 && 3 < 5) + "<br>");
        document.write(!(2 > 3 && 3 < 5) + "<br>");
        document.write((true || null) + "<br>");

        /*
        比较运算符
        == 先转换类型  在比较值   等于但不全等
        === 全等 先比较类型，在比较值
    */
        var a = 2;
        var b = '2';
        document.write((a == b) + "<br>");  // true
        document.write((a === b) + "<br>");  // false
        document.write((null == null) + "<br>");  // true
        document.write((null == undefined) + "<br>");  // true
        document.write((NaN == NaN) + "<br>");  // false 因为不确定值

    </script>
</body>
```



## JS流程控制

```html
<head>
    <meta charset="UTF-8">
    <title>JS流程控制</title>
</head>
<body>
    <script>
        /*
        if ... else
        if ... else if ... else
    */
        var name = "B";
        if (name === "A") {
            document.write("大奖");
        } else if (name === "B") {
            document.write("二等奖");
        } else {
            document.write("三等奖");
        }
        document.write("<br>");

        /*
        switch 语句
        · 计算一次 switch 表达式
        · 把表达式的值与每个 case 的值进行对比
        · 如果存在匹配，则执行关联代码
        break 跳出当前代码块


    */

        var day = 3;
        switch (day) {
            case 1:
                document.write("星期一");
                break;
            case 2:
                document.write("星期二");
                break;
            case 3:
                document.write("星期三");
                // break;
            case 4:
                document.write("星期四");
                // break;
            case 5:
                document.write("星期五");
                break;
            default:
                document.write("请输入1~5的数字");
        }
    </script>
</body>
```



## JS循环

```html
<head>
    <meta charset="UTF-8">
    <title>循环</title>
</head>
<body>
    <!--此处最后讲-->
    <ul>
        <li>1</li>
        <li>2</li>
        <li>3</li>
        <li>4</li>
    </ul>
    <script>
        /*
        for 循环
        for(初始值;判断条件;更新初始值)
        循序：循环初始值-》判断-》执行-》更新-》判断-》执行
        特点：先判断在执行
    */
        /*    for (var i = 1; i <= 5; i++) {
            if (i == 3) {
                // break;
                continue;  //跳出本次循环
            }
            document.write("我跑了" + i + "圈<br>");  // 循环体
        }*/

        /*
        for...in 语句
        遍历一个数组的时候。得到的是数组中对应的下标值
    */
        var array = [1, 2, 3, 4, 5, 6];
        for (var i in array) {  // 得到的i 并不是array数组中的元素，而是下标
            document.write(array[i] + "<br>")
        }

        /*
        while 循环
        和for 循环顺序相同
        特点：先判断在执行
    */
        /*    var i = 1;  // 声明循环变量
        while (i <= 5) {  // 判断循环条件
            document.write("我跑了" + i + "圈<br>");  // 循环体
            i++;  // 更新循环条件
        }*/

        /*
        do while
        特点：先执行在判断
        不管初始条件是否成立，都至少执行一次
    */
        /*    var i = 1;
        do {
            document.write("我跑了" + i + "圈<br>");  // 循环体
            i++;
        }while (i<=5);*/


        /*
        需求：
            点击li标签。给出对应的角标
    */
        // var aLi = document.getElementsByTagName("li");
        // 第一种
        // var 为全局变量
        /*        for (var i = 0; i < aLi.length; i++) {
                aLi[i].index = i;
                aLi[i].onclick = function () {
                    // alert(this.innerText);
                    alert(this.index);
                }
            }
            document.write(i)  // 可以正常打印i变量中的值*/
        // 第二种
        // let 用于局部变量(块级)  所在的代码块内有效  ES6中新加的关键字（变量声明）
        /*    for (let i = 0; i < aLi.length; i++) {
            // aLi[i].index = i;
            aLi[i].onclick = function () {
                alert(i)
            }
        }
        document.write(i)  // 无法打印 i变量中的值*/

    </script>
</body>
```



## 字符串方法

```html
<head>
    <meta charset="UTF-8">
    <title>字符串方法</title>
</head>
<body>
    <script>
        var str = "hello world";
        console.log(str.length); // 长度  空格也算

        console.log(str.indexOf("o"));  // 查找下标  只会给出首次出现的
        // 因为上面知道第一个 “l” 的索引值来第2位，所以从第3位在继续找
        console.log(str.indexOf("o", 5)); // 查找下标  只会给出首次出现的

        console.log(str.split("o"));  // 分割。 返回数组
        console.log(str.split(" "));

        console.log(str.replace("h", "a"));  // 替换

        console.log(str.slice(0, 5)); // 切片  开始索引--》结束索引+1  能设置负值
        console.log(str.substring(5, 0));  // 截取  不能设置负值


    </script>
</body>
```



## 数组方法

````html
<head>
    <meta charset="UTF-8">
    <title>数组方法</title>
</head>
<body>
    <script>
        var array = ["西瓜", "橘子", "香蕉", "椰子", "甘蔗"];
        console.log(array.length);  // 5个元素
        console.log(array.indexOf("香蕉"));  // 下标 2

        console.log(array.push("葡萄"));  // 追加  返回长度
        console.log(array);  // 追加在数组的最后一个

        console.log(array.unshift("苹果"));  // 增加
        console.log(array);  // 添加在数组的最前面

        console.log(array.pop());  // 返回被删除的元素  删除数组中最后一个
        console.log(array);

        console.log(array.shift()); // 返回被删除的元素  删除数组中最前一个
        console.log(array);

        console.log(array.slice(1, 3));  // 切片

        console.log(array.join("-"));  // 拼接  西瓜-橘子-香蕉-椰子-甘蔗

        var arr = ['a', 'z', 's', 'g', 'f',];
        console.log(arr.sort());  // 排序
        console.log(arr.reverse());  // 排序 反向


    </script>
</body>
````



## 补充方法（类型转换）

```html
<head>
    <meta charset="UTF-8">
    <title>补充的方法</title>
</head>
<body>
    <script>
        var num = 12.16;
        console.log(typeof (num));
        console.log(typeof (num.toString()));  // tostring  转string
        console.log(num.toFixed());  // toFixed  把小数变整数  转string
        console.log(num.toFixed(1));  // 保留小数点后几位
        console.log(parseInt(num));  // 转整形
        console.log(parseFloat(num));  // 转浮点型

        // 另外一种转换方式  强制转换
        console.log(typeof String(111));
        console.log(typeof Number("11"));
        console.log(Boolean(null));  // false

    </script>
</body>
```



## 作业

1. 先加入4张图片  <li><img></img><li>
2. 演示 display : none 隐藏图片
3. 给所有的<li>标签设置  dispaly : none。先将所有的图片进行隐藏
4. 在设置一个class = show。dispaly : block   让其中一张图片进行显示
5. 设置小圆点的背景色。给小圆点的<li>加上class : on  随后写背景颜色  让其中一个小圆点进行显示

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

        .slide .pic li {
            display: none;
        }

        .slide .pic li.show {
            display: block;
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
        .slide .tab li.on{
            background-color: #ff00ef;
        }

    </style>
</head>
<body>
    <div class="slide">
        <!--图片列表-->
        <ul class="pic">
            <li class="show"><img src="images/1.jpg" alt="图片出错了"></li>
            <li><img src="images/2.jpg" alt="图片出错了"></li>
            <li><img src="images/3.jpg" alt="图片出错了"></li>
            <li><img src="images/4.jpg" alt="图片出错了"></li>
        </ul>
        <!--左右箭头-->
        <ul class="btn">
            <li class="left">&lt;</li>
            <li class="right">&gt;</li>
        </ul>
        <!--小圆圈-->
        <ul class="tab">
            <li class="on"></li>
            <li></li>
            <li></li>
            <li></li>
        </ul>
    </div>
    <script>
        var aPic = document.querySelectorAll(".pic li");  // 所有的图片
        var aTab = document.querySelectorAll(".tab li");  // 所有的小圆点

        // 小圆点的点击事件    小圆点和图片的下标一致  一一对应
        for (let i = 0; i <aTab.length; i++) {
            aTab[i].onclick = function () {
                for (let j = 0; j < aTab.length; j++) {
                    aPic[j].removeAttribute("class");  // 直接去除class属性
                    aTab[j].removeAttribute("class");  // 直接去除class属性
                }
                aPic[i].className = "show";    // 显示图片
                aTab[i].className = "on"  // 显示小圆点
            }
        }

    </script>
</body>
```





