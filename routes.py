import bottle

@bottle.route('/')
def home():
    return bottle.template('home')

@bottle.route('/about')
def about():
    return bottle.template('about')

@bottle.route('/static/<filepath:path>')
def server_static(filepath):
    return bottle.static_file(filepath, root='static')
