from flask import Flask
import index
app = Flask(__name__.split(".")[0])

#funkciji, ki se pokličeta ko uporabnik zahteva začetno stran aplikacije
@app.route('/')
def slash():
    return index.main_page()

@app.route('/index.html')
def slash_index():
    return index.main_page()