from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Flatiron Cars!"

@app.route('/<string:Model>')
def car(model):
    existing_models = ['Beedle', 'Crossroads', 'M2', 'Panique']
    if model in existing_models:
        return 'Flatiron {model} is in our fleet'
    else:
        return f'Sorry, Flatiron {model} is not in our fleet'
    

if __name__ == '__name__':
        app.run(debug=True)

    





