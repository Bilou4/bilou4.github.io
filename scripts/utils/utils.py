import webbrowser
import os

def get_clipboard_selected_text():
    return os.popen('xclip -o').read()

def open_firefox_tab(url):
    firefox = webbrowser.get('firefox')
    firefox.open_new_tab(str(url))