import os
stream = []
arr=["dpkg -i lib*_amd64.deb","for deb in *_amd64.deb; do dpkg -i $deb; done","dpkg --configure -a",""]
	stream[i]=os.popen(arr[i])
	output=stream[i].read()