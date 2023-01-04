import requests
url = "http://catalog.rpi.edu/preview_program.php?catoid=24&poid=6545&returnto=604"
content = requests.get(url)
print(content.text)
