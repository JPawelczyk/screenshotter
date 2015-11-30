# screenshotter - Super quick Imgur-Screenshot-Uploader

This tiny program enables you to (once you bind it to a key) take and upload a screenshot by hitting just one button. Mark the section of the screen you want to grab and the link to your image is already in your clipboard. It doesn't get more convenient. This is obviously especially useful if you frequently share screenshots with friends on Skype, etc.

To use this script, you need an Imgur API key. If you don't already have one you can obtain it [here](https://imgur.com/signin?redirect=http://api.imgur.com/oauth2/addclient). Just open the screenshot.py file with your favorite text-editor and insert your personal Imgur API key (you will have to enter two separate keys, the client ID and the client secret, just copy and paste them inbetween the two apostrophes next to the corresponding variable name).
You will also need to install the imgurpython Python library if it's not already present on your system. I suggest using ```pip```. Just execute the following: ```pip install imgurpython```.
Lastly, you'll need to install ```scrot```, a command-line screengrabber. The procedure for installing scrot varies from OS to OS. Use Google if you need help.

Feel free to [email me](mailto:pawelczyk.johannes@gmail.com) with any suggestions, requests or criticism!
