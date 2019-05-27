import json
import requests

postaja = raw_input('Postaja: ')
postaja.replace(" ", "%20")
print(postaja)

trola = 'https://www.trola.si/'
link = trola + postaja
print(link)

resp = requests.get(link)
print(resp)

a = resp.text
#print(a.encode("utf-8"))


text_file = open("templates/bus.html", "w")
text_file.write(a.encode("utf-8"))
text_file.close()



#json_data = json.loads(resp.text)
#print(resp.json())
#print(type(resp))
#a = resp.json()


