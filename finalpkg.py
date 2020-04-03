import os
stream = []
arr=["dpkg -l | grep i386 | wc","dpkg -i $(echo $(grep-status --field=Status "install ok installed"| grep-dctrl --field=Architecture i386 --show-field=Package --no-field-names | sed 's/$/*.deb/'))","apt-get download gawk:amd64 libgadu3:amd64"]
	stream[i]=os.popen(arr[i])
	output=stream[i].read()