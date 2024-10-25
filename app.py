from flask import Flask
from api.routes import api as api_blueprint

# Define the static folder as 'ui' and set the static URL path to root '/'
app = Flask(__name__, static_folder='ui', static_url_path='/')

app.register_blueprint(api_blueprint)

@app.route('/')
def index():
    return app.send_static_file('index.html')  # Serve the index.html file from ui folder

if __name__ == '__main__':
    app.run(debug=True)
