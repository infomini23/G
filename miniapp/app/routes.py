from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Willkommen auf dieser Seite!"

