from bottle import route, run

@route('/')
def index():
    return "<a href='/About'>About</a>""<a href='/Biography'>Biography</a>""<a href='/Pic'>Pictures</a>"

@route ('/About')
def About():
    return "Here is ifno about steve jobs"

@route('/Biography')
def bottle():
    return "Here is biograph from steve jobs"

@route('/Pic')
def Pic():
    return "Here is pictures of steve jobs"
run()
