def add():
    html_background = open("html_files/index.html")
    html_file = open("html_files/calendar_conf.html","r")
    html_file = html_background.read().replace("<!--WINDOW-->", html_file.read())
    csser = open("static/style/styl.css", "r")
    html_file = html_file.replace("/*STYLE*/", csser.read())
    return html_file