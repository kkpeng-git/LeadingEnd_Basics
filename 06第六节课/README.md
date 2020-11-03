## Math对象

```html
<head>
    <meta charset="UTF-8">
    <title>Math对象</title>
</head>
<body>
    <script>
        document.write(Math.sqrt(9) + "<br>");  // 开平方 3   
        document.write(Math.abs(-122) + "<br>");  // 绝对值 122
        document.write(Math.PI + "<br>");  // π 3.141592653589793
        document.write(Math.pow(2, 4) + "<br>");  // 次方  2的4次方
        document.write(Math.round(123.75) + "<br>");  // 取整  四舍五入  124
        document.write(Math.ceil(123.1) + "<br>"); // 向上取整  不管小数位，直接加一
        document.write(Math.floor(123.9) + "<br>");// 向下取整  不管小数位，也不进行四舍五入
        document.write(Math.max(2, 3, 4, 5, 7) + "<br>"); // 取最大数
        document.write(Math.min(2, 3, 4, 5, 7) + "<br>"); // 取最小数
        document.write(Math.random() + "<br>"); // 随机数 范围 0 ~ 1（1不可取）
        document.write(Math.random() * 100 + "<br>"); // 0 ~ 100
        document.write(Math.round(Math.random() * 100) + "<br>"); // 0 ~ 100  取整
    </script>
</body>
```



## 日期对象

```html
<head>
    <meta charset="UTF-8">
    <title>日期对象</title>
</head>
<body>
    <script>
        // 定义日期对象
        var today = new Date();
        console.log(today);  // Fri Oct 23 2020 13:38:31 GMT+0800 (中国标准时间)

        console.log(today.getFullYear());  // 获取年份
        console.log(today.getMonth() + 1);    // 获取月  月份是从0开始的   所以需要 +1
        console.log(today.getDate());   // 获取日
        console.log(today.getDay());  // 获取星期
        console.log(today.getHours());  // 获取小时
        console.log(today.getMinutes());  // 获取分钟
        console.log(today.getSeconds());  // 获取秒
        console.log(today.getMilliseconds());  // 获取毫秒

        // 时间戳
        var timestamp = Date.now();  // 方法返回自 1970 年 1 月 1 日以来的毫秒数
        console.log(timestamp);
    </script>
</body>
```



## 定时器

```html
<head>
    <meta charset="UTF-8">
    <title>定时器</title>
</head>
<body>
    <script>
        /*
        setTimeout()
            特点：一次性的，时间到就执行
            在指定的时间后 执行一次
    */
        var timer1 = setTimeout(function () {
            console.log(111);
        }, 2000);
        clearTimeout(timer1);

        /*
        setInterval()
            特点：周期性的，根据设定的时间周期进行
            已指定的时间周期进行循环执行
    */
        var timer2 = setInterval(function () {
            console.log(222);
        }, 2000);
        clearInterval(timer2);
    </script>
</body>
```



## 窗口跳转

```html
<head>
    <meta charset="UTF-8">
    <title>窗口跳转</title>
</head>
<body>
    <button type="button" id="btu">跳转窗口</button>
    <script>
        var oBtn = document.getElementById("btu");
        // 在原来的窗口上实现跳转
        /*oBtn.onclick = function () {
            window.location.href = "http://baidu.com"
        }*/

        // 打开新窗口
        oBtn.onclick = function () {
            window.open('http://baidu.com')
        }

    </script>
</body>
```



## 函数

**函数的分类**

```html
<head>
    <meta charset="UTF-8">
    <title>函数的分类</title>
</head>
<body>
    <script>
        // 有名函数 func就是函数的名字
        function func() {
            console.log(111);
        }
        func();  // 调用函数


        // 匿名函数  事件函数
        document.onclick = function(){
            console.log(222);
        }
    </script>
</body>
```

**函数传参**

```html
<head>
    <meta charset="UTF-8">
    <title>函数传参</title>
</head>
<body>
    <script>
        /*
        函数传参
            形参
            实参
            不定参
    */
        /*
        	好比是一个工厂
        	蒙牛工厂     原料：奶牛、饲料、水
        			   产出物： 奶制品
       		钢铁工厂    原料：铁矿石、煤炭
       				  产出物：钢铁建材
			参数（原料）：就是进入方法的数据
			返回值（产出物）：就是从方法中出来的数据
        */
        
        // x是形参
        function func(x) {
            console.log(x);
        }
        func('111');  // '111' 实参

        function sum(x, y) {  // x,y 形参
            console.log(x + y);
        }
        sum(2, 4); // 2,4 实参



        function add() {
            console.log(arguments);  // argumentsd  不定长参数
        }
        add(123);
        add(123,'123');

        function add2(x,y) {
            console.log(arguments);  //
            console.log(x, y);  // 1 undefined（未定义）
        }
        add2(1);

        function tra() {
            for (var i=0;i<arguments.length;i++){
                console.log(arguments[i]);
            }
        }
        tra(1,2,3,4)
    </script>
</body>
```

**函数的返回值**

```html
<head>
    <meta charset="UTF-8">
    <title>函数的返回值</title>
</head>
<body>
    <div id="box"></div>
    <script>
        // 下面两个系统所定义好的函数没有返回值，所以得到undefined   功能性函数,仅仅只是实现某个功能
        var a = alert(111111);
        console.log(a);  // undefined   所以alert无返回值

        var b = console.log(2);
        console.log(b);// undefined  所以console.log无返回值

        // 定义了返回值，所以会得到返回结果
        var oBox = document.getElementById("box");
        console.log(oBox);  // 有返回值

        function func1() {
            console.log(1);
        }
        var a = func1();
        console.log(a);  // undefined

        function func2() {
            console.log(1);
            return "我返回了"
        }
        var b = func2();
        console.log(b);

        function func3(x,y) {
            return x+y;  // return后面的代码不会执行。  因为已经退出此函数
            console.log(1);
        }
        var c = func3(1, 2);
        console.log(c);

    </script>
</body>
```

**函数的作用域**

```html
<head>
    <meta charset="UTF-8">
    <title>函数的作用域</title>
</head>
<body>
    <script>
        /*
        函数作用域
        全局作用域  全局变量
        在函数里面用var定义的变量是局部变量
        在函数里面  没有用var的变量，会成为全局变量
        子作用域会改变父作用域的值  (在子作用域没有使用var的情况下)
    */
        /* var a = 100;
    function func() {
        var a = 200;
        // a = 200;   // 在函数里面  没有用var的变量，会成为全局变量
        alert(a)
    }
    alert(a);  // 100
    func();  // 200
    alert(a);  // 100*/

        /* var a = 100;
   function func1() {
       var a = 200;
       function func2() {
           var a = 300;
       }
       func2();
       alert(a)
   }
   alert(a);  // 100
   func1();  // 200
   alert(a)  // 100*/


        /*
        var 和 let 的区别
            var定义的变量，没有块的概念，可以跨块访问, 不能跨函数访问。
            let定义的变量，只能在块作用域里访问，不能跨块访问，也不能跨函数访问。
    */
        //======== var =====================================
        {
            var i= 1;
            console.log(i);
        }
        console.log(i);  // 可见，通过var定义的变量可以跨块作用域访问到。
        function A() {
            var b = 2;
            console.log(b); // 2
        }
        A();
        // console.log(b); // 报错，	// 可见，通过var定义的变量不能跨函数作用域访问到
        //=================================================

        //======== let =====================================
        {
            let j= 1;
            console.log(j);
        }
        // console.log(j); // 报错
        function B() {
            let c = 2;
            console.log(c); // 2
        }
        B();
        console.log(c);
        //=================================================

    </script>
</body>
```

**递归函数**

```html
<head>
    <meta charset="UTF-8">
    <title>递归函数</title>
</head>
<body>
    <script>
        function add(x) {
            if (x == 1) {
                return 1;
            }else {
                return add(x-1)*x  // 阶乘 5*4*3*2*1 = 120
            }
        }
        console.log(add(5));
    </script>
</body>
```

**自定义函数**

```html
<head>
    <meta charset="UTF-8">
    <title>自定义函数</title>
</head>
<body>
    <script>
        // 自己去调用自己
        ~function () {
            console.log(1)
        }();
        +function () {
            console.log(2312);
        }();

        (function () {
            console.log(2);
        }())
    </script>
</body>
```

**异常**

```html
<head>
    <meta charset="UTF-8">
    <title>异常</title>
</head>
<body>
    <button type="button" id="btu" onclick="func()">异常</button>
    <button type="button" id="btu2" onclick="func2()">自定义异常</button>
    <script>
        /*
        try 正确执行的代码   可能会出错的代码
        catch 执行错误后执行
        finally 不管正确还是错误都会执行
        throw  自定义异常
    */
        function func() {
            var num = 100;
            try {
                alert("我是" + num)
            } catch (e) {
                alert("错误类型:" + e.name + "\n错误信息:" + e.message);  // ReferenceError  非法引用
            } finally {
                alert("不管是正确还是错误都会执行")
            }
        }

        function func2() {
            var num = 11;
            try {
                if (num < 100) throw "太小了";
                if (num == 100) throw "刚刚好";
                if (num >= 100) throw "太大了";
            } catch (e) {
                alert("输入的值：" + e);
            }
        }
    </script>
</body>
```



## 作业

```html
<head>
    <meta charset="UTF-8">
    <title>作业</title>
    <style>
        p {
            text-align: center; /*水平居中*/
            height: 80px;
            line-height: 80px; /* 让文字下去一点  距离顶部 */
            font-size: 22px;
        }

        span.time {
            color: red;
            font-size: 30px;
        }

        .hour {
            color: grey;
            font-size: 18px;
        }
    </style>
</head>
<body>
    <p>
        <span class="word"></span>
        <span class="time"></span>
        <span class="word"></span>
    </p>
    <p>
        <span class="today"></span>
        <span class="hour"></span>
    </p>
    <script>
        // 获取元素
        var aWord = document.querySelectorAll(".word");
        var oTime = document.querySelector(".time");
        var oP = document.getElementsByTagName("p");
        var oToday = document.querySelector(".today");
        var oHour = document.querySelector(".hour");

        // 倒计时
        var times = 10;   // 初始化倒计时时间
        function func1() {
            if (times > 0) {
                aWord[0].innerText = '距离上课还有';
                oTime.innerText = times;
                aWord[1].innerText = '秒！';
            } else {
                // oP[0].innerText = "开始上课！";
                oP[0].innerHTML = "<h2 style='color: red'>开始上课！</h2>";
                // 清除定时器
                clearInterval(timer1);
                clearInterval(timer2);
            }
            times--;
        }

        func1();  // 打开页面的时候会发现需要等一秒钟。所以我们先手动执行一次
        timer1 = setInterval(func1, 1000);

        // 北京时间
        function func2() {
            var today = new Date();
            var year = today.getFullYear();
            var month = today.getMonth() + 1;
            var date = today.getDate();
            var hours = today.getHours();
            var minutes = today.getMinutes();
            var seconds = today.getSeconds();
            if (minutes < 10) minutes = "0" + minutes;
            if (hours < 10) hours = "0" + hours;
            if (seconds < 10) seconds = "0" + seconds;
            oToday.innerText = "北京时间：" + year + "年" + month + "月" + date + "日";
            oHour.innerText = hours + ":" + minutes + ":" + seconds;
        }

        func2();  // 打开页面的时候会发现需要等一秒钟。所以我们先手动执行一次
        timer2 = setInterval(func2, 1000);
    </script>
</body>
```





























## Math对象

```html
<head>
    <meta charset="UTF-8">
    <title>Math对象</title>
</head>
<body>
    <script>
        document.write(Math.sqrt(9) + "<br>");  // 开平方 3   
        document.write(Math.abs(-122) + "<br>");  // 绝对值 122
        document.write(Math.PI + "<br>");  // π 3.141592653589793
        document.write(Math.pow(2, 4) + "<br>");  // 次方  2的4次方
        document.write(Math.round(123.75) + "<br>");  // 取整  四舍五入  124
        document.write(Math.ceil(123.1) + "<br>"); // 向上取整  不管小数位，直接加一
        document.write(Math.floor(123.9) + "<br>");// 向下取整  不管小数位，也不进行四舍五入
        document.write(Math.max(2, 3, 4, 5, 7) + "<br>"); // 取最大数
        document.write(Math.min(2, 3, 4, 5, 7) + "<br>"); // 取最小数
        document.write(Math.random() + "<br>"); // 随机数 范围 0 ~ 1（1不可取）
        document.write(Math.random() * 100 + "<br>"); // 0 ~ 100
        document.write(Math.round(Math.random() * 100) + "<br>"); // 0 ~ 100  取整
    </script>
</body>
```



## 日期对象

```html
<head>
    <meta charset="UTF-8">
    <title>日期对象</title>
</head>
<body>
    <script>
        // 定义日期对象
        var today = new Date();
        console.log(today);  // Fri Oct 23 2020 13:38:31 GMT+0800 (中国标准时间)

        console.log(today.getFullYear());  // 获取年份
        console.log(today.getMonth() + 1);    // 获取月  月份是从0开始的   所以需要 +1
        console.log(today.getDate());   // 获取日
        console.log(today.getDay());  // 获取星期
        console.log(today.getHours());  // 获取小时
        console.log(today.getMinutes());  // 获取分钟
        console.log(today.getSeconds());  // 获取秒
        console.log(today.getMilliseconds());  // 获取毫秒

        // 时间戳
        var timestamp = Date.now();  // 方法返回自 1970 年 1 月 1 日以来的毫秒数
        console.log(timestamp);
    </script>
</body>
```



## 定时器

```html
<head>
    <meta charset="UTF-8">
    <title>定时器</title>
</head>
<body>
    <script>
        /*
        setTimeout()
            特点：一次性的，时间到就执行
            在指定的时间后 执行一次
    */
        var timer1 = setTimeout(function () {
            console.log(111);
        }, 2000);
        clearTimeout(timer1);

        /*
        setInterval()
            特点：周期性的，根据设定的时间周期进行
            已指定的时间周期进行循环执行
    */
        var timer2 = setInterval(function () {
            console.log(222);
        }, 2000);
        clearInterval(timer2);
    </script>
</body>
```



## 窗口跳转

```html
<head>
    <meta charset="UTF-8">
    <title>窗口跳转</title>
</head>
<body>
    <button type="button" id="btu">跳转窗口</button>
    <script>
        var oBtn = document.getElementById("btu");
        // 在原来的窗口上实现跳转
        /*oBtn.onclick = function () {
            window.location.href = "http://baidu.com"
        }*/

        // 打开新窗口
        oBtn.onclick = function () {
            window.open('http://baidu.com')
        }

    </script>
</body>
```



## 函数

**函数的分类**

```html
<head>
    <meta charset="UTF-8">
    <title>函数的分类</title>
</head>
<body>
    <script>
        // 有名函数 func就是函数的名字
        function func() {
            console.log(111);
        }
        func();  // 调用函数


        // 匿名函数  事件函数
        document.onclick = function(){
            console.log(222);
        }
    </script>
</body>
```

**函数传参**

```html
<head>
    <meta charset="UTF-8">
    <title>函数传参</title>
</head>
<body>
    <script>
        /*
        函数传参
            形参
            实参
            不定参
    */
        /*
        	好比是一个工厂
        	蒙牛工厂     原料：奶牛、饲料、水
        			   产出物： 奶制品
       		钢铁工厂    原料：铁矿石、煤炭
       				  产出物：钢铁建材
			参数（原料）：就是进入方法的数据
			返回值（产出物）：就是从方法中出来的数据
        */
        
        // x是形参
        function func(x) {
            console.log(x);
        }
        func('111');  // '111' 实参

        function sum(x, y) {  // x,y 形参
            console.log(x + y);
        }
        sum(2, 4); // 2,4 实参



        function add() {
            console.log(arguments);  // argumentsd  不定长参数
        }
        add(123);
        add(123,'123');

        function add2(x,y) {
            console.log(arguments);  //
            console.log(x, y);  // 1 undefined（未定义）
        }
        add2(1);

        function tra() {
            for (var i=0;i<arguments.length;i++){
                console.log(arguments[i]);
            }
        }
        tra(1,2,3,4)
    </script>
</body>
```

**函数的返回值**

```html
<head>
    <meta charset="UTF-8">
    <title>函数的返回值</title>
</head>
<body>
    <div id="box"></div>
    <script>
        // 下面两个系统所定义好的函数没有返回值，所以得到undefined   功能性函数,仅仅只是实现某个功能
        var a = alert(111111);
        console.log(a);  // undefined   所以alert无返回值

        var b = console.log(2);
        console.log(b);// undefined  所以console.log无返回值

        // 定义了返回值，所以会得到返回结果
        var oBox = document.getElementById("box");
        console.log(oBox);  // 有返回值

        function func1() {
            console.log(1);
        }
        var a = func1();
        console.log(a);  // undefined

        function func2() {
            console.log(1);
            return "我返回了"
        }
        var b = func2();
        console.log(b);

        function func3(x,y) {
            return x+y;  // return后面的代码不会执行。  因为已经退出此函数
            console.log(1);
        }
        var c = func3(1, 2);
        console.log(c);

    </script>
</body>
```

**函数的作用域**

```html
<head>
    <meta charset="UTF-8">
    <title>函数的作用域</title>
</head>
<body>
    <script>
        /*
        函数作用域
        全局作用域  全局变量
        在函数里面用var定义的变量是局部变量
        在函数里面  没有用var的变量，会成为全局变量
        子作用域会改变父作用域的值  (在子作用域没有使用var的情况下)
    */
        /* var a = 100;
    function func() {
        var a = 200;
        // a = 200;   // 在函数里面  没有用var的变量，会成为全局变量
        alert(a)
    }
    alert(a);  // 100
    func();  // 200
    alert(a);  // 100*/

        /* var a = 100;
   function func1() {
       var a = 200;
       function func2() {
           var a = 300;
       }
       func2();
       alert(a)
   }
   alert(a);  // 100
   func1();  // 200
   alert(a)  // 100*/


        /*
        var 和 let 的区别
            var定义的变量，没有块的概念，可以跨块访问, 不能跨函数访问。
            let定义的变量，只能在块作用域里访问，不能跨块访问，也不能跨函数访问。
    */
        //======== var =====================================
        {
            var i= 1;
            console.log(i);
        }
        console.log(i);  // 可见，通过var定义的变量可以跨块作用域访问到。
        function A() {
            var b = 2;
            console.log(b); // 2
        }
        A();
        // console.log(b); // 报错，	// 可见，通过var定义的变量不能跨函数作用域访问到
        //=================================================

        //======== let =====================================
        {
            let j= 1;
            console.log(j);
        }
        // console.log(j); // 报错
        function B() {
            let c = 2;
            console.log(c); // 2
        }
        B();
        console.log(c);
        //=================================================

    </script>
</body>
```

**递归函数**

```html
<head>
    <meta charset="UTF-8">
    <title>递归函数</title>
</head>
<body>
    <script>
        function add(x) {
            if (x == 1) {
                return 1;
            }else {
                return add(x-1)*x  // 阶乘 5*4*3*2*1 = 120
            }
        }
        console.log(add(5));
    </script>
</body>
```

**自定义函数**

```html
<head>
    <meta charset="UTF-8">
    <title>自定义函数</title>
</head>
<body>
    <script>
        // 自己去调用自己
        ~function () {
            console.log(1)
        }();
        +function () {
            console.log(2312);
        }();

        (function () {
            console.log(2);
        }())
    </script>
</body>
```

**异常**

```html
<head>
    <meta charset="UTF-8">
    <title>异常</title>
</head>
<body>
    <button type="button" id="btu" onclick="func()">异常</button>
    <button type="button" id="btu2" onclick="func2()">自定义异常</button>
    <script>
        /*
        try 正确执行的代码   可能会出错的代码
        catch 执行错误后执行
        finally 不管正确还是错误都会执行
        throw  自定义异常
    */
        function func() {
            var num = 100;
            try {
                alert("我是" + num)
            } catch (e) {
                alert("错误类型:" + e.name + "\n错误信息:" + e.message);  // ReferenceError  非法引用
            } finally {
                alert("不管是正确还是错误都会执行")
            }
        }

        function func2() {
            var num = 11;
            try {
                if (num < 100) throw "太小了";
                if (num == 100) throw "刚刚好";
                if (num >= 100) throw "太大了";
            } catch (e) {
                alert("输入的值：" + e);
            }
        }
    </script>
</body>
```



## 作业

```html
<head>
    <meta charset="UTF-8">
    <title>作业</title>
    <style>
        p {
            text-align: center; /*水平居中*/
            height: 80px;
            line-height: 80px; /* 让文字下去一点  距离顶部 */
            font-size: 22px;
        }

        span.time {
            color: red;
            font-size: 30px;
        }

        .hour {
            color: grey;
            font-size: 18px;
        }
    </style>
</head>
<body>
    <p>
        <span class="word"></span>
        <span class="time"></span>
        <span class="word"></span>
    </p>
    <p>
        <span class="today"></span>
        <span class="hour"></span>
    </p>
    <script>
        // 获取元素
        var aWord = document.querySelectorAll(".word");
        var oTime = document.querySelector(".time");
        var oP = document.getElementsByTagName("p");
        var oToday = document.querySelector(".today");
        var oHour = document.querySelector(".hour");

        // 倒计时
        var times = 10;   // 初始化倒计时时间
        function func1() {
            if (times > 0) {
                aWord[0].innerText = '距离上课还有';
                oTime.innerText = times;
                aWord[1].innerText = '秒！';
            } else {
                // oP[0].innerText = "开始上课！";
                oP[0].innerHTML = "<h2 style='color: red'>开始上课！</h2>";
                // 清除定时器
                clearInterval(timer1);
                clearInterval(timer2);
            }
            times--;
        }

        func1();  // 打开页面的时候会发现需要等一秒钟。所以我们先手动执行一次
        timer1 = setInterval(func1, 1000);

        // 北京时间
        function func2() {
            var today = new Date();
            var year = today.getFullYear();
            var month = today.getMonth() + 1;
            var date = today.getDate();
            var hours = today.getHours();
            var minutes = today.getMinutes();
            var seconds = today.getSeconds();
            if (minutes < 10) minutes = "0" + minutes;
            if (hours < 10) hours = "0" + hours;
            if (seconds < 10) seconds = "0" + seconds;
            oToday.innerText = "北京时间：" + year + "年" + month + "月" + date + "日";
            oHour.innerText = hours + ":" + minutes + ":" + seconds;
        }

        func2();  // 打开页面的时候会发现需要等一秒钟。所以我们先手动执行一次
        timer2 = setInterval(func2, 1000);
    </script>
</body>
```




