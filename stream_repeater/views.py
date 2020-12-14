from stream_repeater import app

@app.route('/')
def index():
    return 'stream_repeater online'