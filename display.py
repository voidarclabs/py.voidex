import os

print('Launch taskbar and enable desktop mode')
os.system('adb shell settings put global overlay_display_devices 1920x1080/200')
os.system('adb shell dumpsys display | grep -i mdisplayid=[1*-9*]*')
displaynum = input('input the last number: ')
os.system('scrcpy --display=' + displaynum + ' -b 3000000')
os.system('adb shell settings put global overlay_display_devices none')
