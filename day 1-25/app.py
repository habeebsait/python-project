from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
        <head>
            <title>My First Webpage</title>
        </head>
        <body>
            <h1>Welcome to My Webpage!</h1>
            <p>This is a simple webpage created using Python and Flask.</p>
        </body>
    </html>
    
    '''

if __name__ == '__main__':
    app.run(debug=True)
