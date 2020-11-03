## JSON

​	JSON(JavaScript Object Notation) 是一种轻量级的数据交换格式，采用完全独立于语言的文本格式，是理想的数据交换格式。同时，JSON是 JavaScript 原生格式，这意味着在 JavaScript 中处理 JSON数据不须要任何特殊的 API 或工具包。 

```html
<head>
    <meta charset="UTF-8">
    <title>JSON</title>
</head>
<body>
    <script>
        // 定义一个json对象。以键值对存在
        var obj = {"name": "qingge", "age": 18, "sex": "man"};
        console.log(obj);   // 可读性
        console.log(obj['name']);
        console.log(obj.name);

        obj.name = "Sunshine Boy";  // 可写性
        console.log(obj.name);

        // for in 如果是遍历数组 key为下标
        // for in 如果是JSON key为键
        /*for (var key in obj) {
        console.log(key);  // 输入 json的key
        console.log(obj.key);  // undefined
        console.log(obj[key]);  // 用此方法
    }*/

        // JSON对象转字符串
        console.log(typeof obj);  // object
        var obj2 = JSON.stringify(obj);  // 转字符串
        console.log(typeof obj2);  // string
        var obj3 = JSON.parse(obj2); // 转JSON对象
        console.log(typeof obj3);  // object


    </script>
</body>
```



## Ajax

​	AJAX 是一种在无需重新加载整个网页的情况下，能够更新部分网页的技术。

​	通过在后台与服务器进行少量数据交换，AJAX 可以使网页实现异步更新。这意味着可以在不重新加载整个网页的情况下，对网页的某部分进行更新。 

​	

### 传统的前后交付方式--form表单

```html
<head>
    <meta charset="UTF-8">
    <title>传统的前后交付方式--form表单</title>
</head>
<body>
    <h1>传统的前后交互</h1>
    <form action="/" method="post">
        用户名：<input type="text" name="user" placeholder="请输入用户名"><br>
        密&emsp;码：<input type="password" name="pwd" placeholder="请输入密码"><br>
        <input type="submit" name="" id="" value="登陆">
    </form>
</body>
```

```python
import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("Ajax_form.html")

    def post(self, *args, **kwargs):
        print(self.get_argument("user"))
        print(self.get_argument("pwd"))
        self.write("登陆成功")
        
if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/", MainHandler),
    ])
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()
```



### Ajax的前后交互

```html
<head>
    <meta charset="UTF-8">
    <title>Ajax的前后交互</title>

</head>
<body>
    <h1>Ajax前后交互</h1>
    <input type="text" name=""> +
    <input type="text" name=""> =
    <input type="text" name="">
    <button type="button" id="btn">计算</button>
    <script src="https://cdn.bootcdn.net/ajax/libs/jquery/3.4.1/jquery.js"></script>
    <script>
        var aIpt = $("input");
        var oBox = $("#btn");

        // 计算按钮的单击事件
        oBox.click(function () {
            // 获取值
            var a = aIpt.eq(0).val();
            var b = aIpt.eq(1).val();
            // console.log(a + b);
            $.ajax({
                "type": "post",  // 提交的方式
                "url": "/",   // 提交的路径
                "data": {   // 提交的数据，json数据
                    "aa": a,
                    "bb": b
                },
                // 成功回调函数
                "success":function (data) {
                    var c = data['result'];
                    aIpt.eq(2).val(c);
                },
                // 请求错误之后的回调函数
                "error":function (error) {
                    console.log(error);
                }
            })

        })
    </script>
</body>
```

```python
import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("Ajax_jquery.html")

    def post(self, *args, **kwargs):
        a = int(self.get_argument("aa"))
        b = int(self.get_argument("bb"))
        c = a + b
        print(c)
        return_data = {"result": c}
        self.write(return_data)


if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/", MainHandler),
    ])
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()

```




