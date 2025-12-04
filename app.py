import bottle
import routes # don't remove this, that's how it works!

app = bottle.default_app()

if __name__ == '__main__':
    bottle.run(app=app, host='0.0.0.0', port=8080, debug=True, reloader=True)