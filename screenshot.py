#!/usr/bin/env python

from imgurpython import ImgurClient
import pygtk
import gtk
import datetime
import time
import os

client_id = ''
client_secret = ''

client = ImgurClient(client_id, client_secret)

# Take a screenshot
ts = time.time()
timestamp = datetime.datetime.fromtimestamp(ts).strftime('%d_%m_%Y_%H_%M_%S')
filename = "screenshot_" + timestamp + ".png"
path = "/home/johannes/.screenshots/" + filename
command = "scrot -s " + path
os.system(command)

data = client.upload_from_path(path)
link = data["link"]

# Copy link to clipboard
clipboard = gtk.clipboard_get()
clipboard.set_text(link)
clipboard.store()