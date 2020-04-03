import os
stream = []
arr=["dpkg -i libc6_2.13-38+deb7u1_amd64.deb  libgcc1_1%3a4.7.2-5_amd64.deb libgcc1_4.7.2-5_amd64.deb","dpkg -i dash_0.5.7-3_amd64.deb findutils_4.4.2-4_amd64.deb"]
	stream[i]=os.popen(arr[i])
	output=stream[i].read()