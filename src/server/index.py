def main_page():
    html_background = open("html_files/index.html")
    html_file = html_background.read().replace("$_WINDOW_", "")
    csser = open("static/style/styl.css", "r")
    html_file = html_file.replace("/*STYLE*/", csser.read())
    return html_file