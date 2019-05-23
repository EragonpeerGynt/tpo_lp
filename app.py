import os
import sys
dirname, filename = os.path.split(os.path.abspath(__file__))
serverdir = os.path.join(dirname, "src", "server")
sys.path.append(serverdir)
import server

app=server.heroku_star()

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)