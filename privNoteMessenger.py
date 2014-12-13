#!/usr/bin/python3

import time
from splinter import Browser

def getPrivNoteURL(message):
    browser = Browser('phantomjs')
    #ghost.show()
    browser.visit("https://privnote.com/")
    command = "document.getElementById('id_body').value='"+message+"';"
    result = browser.evaluate_script(command)
    command = "document.getElementById('button').click();"
    result = browser.evaluate_script(command)
    time.sleep(2)
    command = "document.getElementById('notelink').value;"
    result = browser.evaluate_script(command)
    print (result)

message = input("Input message: ")
getPrivNoteURL(message)
