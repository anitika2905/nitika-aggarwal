from app import app
@app.route('/')
@app.route('/index')
def index():
    user={'username':'NITIKA'}
    return '''
<html>
    <head>
        <title>Home Page - microblog</title>
     </head>
      <body bgcolor='purple'>
         <h1>hello, '''+user['username']+''' </h1>
        </body>
</html>'''
