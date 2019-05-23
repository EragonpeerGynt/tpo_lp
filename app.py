import os
import sys
dirname, filename = os.path.split(os.path.abspath(__file__))
serverdir = os.path.join(dirname, "src", "server")
sys.path.append(serverdir)
import server

server.heroku_star()
