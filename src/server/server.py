from flask import Flask
from flask_sslify import SSLify
import index
app = Flask(__name__.split(".")[0])


#funkciji, ki se pokličeta ko uporabnik zahteva začetno stran aplikacije
@app.route('/')
def slash():
    return index.main_page()

@app.route('/index.html')
def slash_index():
    return index.main_page()


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=False, ssl_context='adhoc')