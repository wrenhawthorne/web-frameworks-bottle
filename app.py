import bottle
import routes

app = bottle.default_app()

if __name__ == '__main__':
    bottle.run(app=app, host='localhost', port=8080, debug=True, reloader=True)