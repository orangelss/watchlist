from flask import Flask, escape, url_for, render_template
app = Flask(__name__)
#接下来，我们要注册一个处理函数，这个函数是处理某个请求的处理函数，
# Flask 官方把它叫做视图函数（view funciton），你可以理解为“请求处理函数”。
#所谓的“注册”，就是给这个函数戴上一个装饰器帽子。我们使用 app.route()
# 装饰器来为这个函数绑定对应的 URL，当用户在浏览器访问这个 URL 的时候，
# 就会触发这个函数，获取返回值，并把返回值显示到浏览器窗口：
@app.route('/')
#当用户在浏览器地址栏访问这个地址，在这里即 http://localhost:5000/
#服务器解析请求，发现请求 URL 匹配的 URL 规则是 /，因此调用对应的处理函数 hello()
#获取 hello() 函数的返回值，处理后返回给客户端（浏览器）
#浏览器接受响应，将其显示在窗口上
def hello():
    return 'Welcome to My Watchlist!'

@app.route('/user/<name>')
def user_page(name):
    return 'User : %s' % escape(name)
#除此之外，它还有一个重要的作用：作为代表某个路由的端点（endpoint），
# 同时用来生成 URL。对于程序内的 URL，为了避免手写，Flask 提供了一个 url_for 函数来生成 URL，
# 它接受的第一个参数就是端点值，默认为视图函数的名称：
@app.route('/test')
def test_url_for():
    print(url_for('hello')) #输出hello
    print(url_for('user_page', name='tom'))
    print(url_for('test_url_for'))
    print(url_for('test_url_for', num=2)) #输出/test?num=2
    return 'Test page'
name = 'liushaui'
movies = [
{'title': 'My Neighbor Totoro', 'year': '1988'},
    {'title': 'Dead Poets Society', 'year': '1989'},
    {'title': 'A Perfect World', 'year': '1993'},
    {'title': 'Leon', 'year': '1994'},
    {'title': 'Mahjong', 'year': '1996'},
    {'title': 'Swallowtail Butterfly', 'year': '1996'},
    {'title': 'King of Comedy', 'year': '1999'},
    {'title': 'Devils on the Doorstep', 'year': '1999'},
    {'title': 'WALL-E', 'year': '2008'},
    {'title': 'The Pork of Music', 'year': '2012'},
]
@app.route('/')
def index():
    return render_template('index.html', name=name, movies=mobies)