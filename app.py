from flask import Flask, render_template
import os

app = Flask(__name__)



# Selects the page for which a function is to be defined. Right now there will only be one page in your website.

@app.route('/')

def hello():

    env_var = os.environ['PORT']
    os.environ['PORT'] = '5000'
    #print("PATH: ", env_var)

    #print("Hello World", file=sys.stderr)

    #return "<h1>Hello World!</h1>" \
    #      "\nThis is my introduction to Flask!" \
    #     "\nI can write a lot of things on this page.\nLet's get started!"

    return render_template('app.html')

# The above function returns the HTML code to be displayed on the page



if __name__ == '__main__':

   app.run(port=5000)