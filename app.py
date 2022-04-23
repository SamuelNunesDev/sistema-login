from bottle import route, run, template, static_file, get, error
import os

@route('/')
def index():
    return template('index')

@route('/login')
def login():
    return template('login')

#assets routes

@get('/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root='views/assets/css')

@get('/<filename:re:.*\.(png|jpg|ico)>')
def images(filename):
    return static_file(filename, root='views/assets/images')

@get('/<filename:re:.*\.js>')
def scripts(filename):
    return static_file(filename, root='views/assets/js')

@get('/fonts/poppins/<filename:re:.*\.(ttf|woff|woff2)>')
def fontsPopping(filename):
    return static_file(filename, root='views/assets/fonts')

@get('/fonts/montserrat/<filename:re:.*\.(ttf|woff|woff2)>')
def fontsWebfonts(filename):
    return static_file(filename, root='views/assets/fonts')

@get('/fonts/<filename:re:.*\.(ttf|woff|woff2)>')
def fontsWebfonts(filename):
    return static_file(filename, root='views/assets/fonts')

@error(404)
def error404(error):
    return template('notFound')

if __name__ == '__main__':
    if os.environ.get('APP_ENV') == 'production':
        run(host='0.0.0.0', port=os.environ.get('PORT', 5000))
    else:
        run(host='localhost', port=8000, debug=True, reloader=True)