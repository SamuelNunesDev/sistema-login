from bottle import route, run, template, static_file, get, error

@route('/login')
def index():
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
    run(localhost='localhost', port=8000, debug=False, reloader=True)