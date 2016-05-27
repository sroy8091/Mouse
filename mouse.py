from __future__ import print_function
import pyautogui
print ("Press Ctrl-C to exit")

try:
	while True:
		x,y = pyautogui.position()
		pos = "X: "+str(x).rjust(4)+" Y: "+str(y).rjust(4)
		print(pos, end="")
		print("\b"*len(pos), end="")
except KeyboardInterrupt:
	print ("\nDone")