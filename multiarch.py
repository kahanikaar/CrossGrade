import os
stream = []
arr=["apt-get clean","grep-status --field=Status 'install ok installed' | ","  grep-dctrl --field=Multi-Arch same --show-field=Package --no-field-names |","  sed '/libc6-i686/d;/libstlport4.6ldbl/d;/linux-headers-.*686.*/d;/xserver-xorg-video-geode/d' |","  sed 's/$/:amd64/' | ","    xargs apt-get -y install "]
for i in range(len(arr)):
	stream[i]=os.popen(arr[i])
	output=stream[i].read()
