import webbrowser
from time import sleep

dino_url='chrome://dino'


webbrowser.get('google-chrome').open_new_tab('https://www.python.org')
# webbrowser.get('/usr/bin/google-chrome %s').open_new_tab('https://www.python.org')
print('hello trex')
sleep(1)