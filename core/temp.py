# import cv2
# import numpy as np
# img_path = r'C:\Users\PPC\git\RS_BOT_2.0\library\reference\window_01.png'
# img = cv2.imread(img_path, 0)
# img_edges = cv2.Canny(img, 100, 100)
# cv2.imshow("img", img)
# cv2.imshow("img_edges", img_edges)
# cv2.waitKey()


import cv2
import os
import numpy as np

# import Mouse as mouse

import Screenshot

# mouse.moveMouseTo(800,200)

# rs_bag = Screenshot.shoot(0,0,500,500,'hsv')
#
# # cv2.imwrite('asdf.png', rs_bag)
# cv2.imshow('Detected', rs_bag)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# import win32api
# import time
# from core import RS
#
# def keyWasUnPressed():
#     print "keyWasUnPressed"
#
# def keyWasPressed():
#     print "keyWasPressed"
#
#
# def isKeyPressed(key):
#     #"if the high-order bit is 1, the key is down; otherwise, it is up."
#     return (win32api.GetKeyState(key) & (1 << 7)) != 0
#
#
# def setup_screen():
#     print "setup"
#
# key = ord('A')
#
# wasKeyPressedTheLastTimeWeChecked = False
# while True:
#     keyIsPressed = isKeyPressed(key)
#     if keyIsPressed and not wasKeyPressedTheLastTimeWeChecked:
#         keyWasPressed()
#     # if not keyIsPressed and wasKeyPressedTheLastTimeWeChecked:
#     #     keyWasUnPressed()
#     wasKeyPressedTheLastTimeWeChecked = keyIsPressed
#     time.sleep(0.01)


# import RS
# import Screenshot
#
#
# img_rgb = cv2.imread(r'C:\Users\PPC\git\RS_BOT_2.0\ababa.png')
#
# pt = RS.getFullPosition(img_rgb)
# # Screenshot.showRectangle(img_rgb, pt)
# cv2.imshow('Detected', img_rgb)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# import RandTime
# import win32api, win32con
#
# def click(x,y):
#     win32api.SetCursorPos((x,y))
#     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
#     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
#
#
# click(500,500)
# RandTime.randTime(0,0,0,0,0,9)#time between click
# click(800,800)
# RandTime.randTime(0,0,0,0,0,9)#time between click
# click(900,900)
# RandTime.randTime(0,0,0,0,0,9)#time between click
# click(500,500)
# RandTime.randTime(0,0,0,0,0,9)#time between click
# click(800,800)
# RandTime.randTime(0,0,0,0,0,9)#time between click
# click(900,900)
# RandTime.randTime(0,0,0,0,0,9)#time between click


import Mouse
import RandTime

Mouse.win32Click(1776,690)
RandTime.randTime(0, 0, 0, 0, 0,25)  # time between click
Mouse.win32Click(1775,655)
RandTime.randTime(0, 0, 0, 0, 0,25)  # time between click
Mouse.win32Click(1828,644)

