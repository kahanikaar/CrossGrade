import os
stream[]
arr= ["aptitude search '?narrow(?not(?archive("^[^n][^o].*$")),?version(CURRENT))?architecture(i386)' ","apt-get install linux-image-amd64 busybox-static dctrl-tools aptitude","dpkg --add-architecture amd64","apt-get update","reboot"]
for i in range(len(arr)):
	stream[i]=os.popen(arr[i])
	output=stream[i].read()

