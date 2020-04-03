import os
stream = []
arr=["apt-get download dpkg:amd64 apt:amd64 liblzma5:amd64 libselinux1:amd64","dpkg -i gcc-4.7-base_4.7.2-5_amd64.deb libgcc1_1%3a4.7.2-5_amd64.deb libc6_2.13-38+deb7u1_amd64.deb libbz2-1.0_1.0.6-4_amd64.deb selinux*","dpkg -i zlib1g_1%3a1.2.7.dfsg-13_amd64.deb libstdc++6_4.7.2-5_amd64.deb liblzma5_5.1.1alpha+20120614-2_amd64.deb libapt-pkg4.12_0.9.7.9+deb7u1_amd64.deb  dpkg_1.16.12_amd64.deb apt_0.9.7.9+deb7u1_amd64.deb",]
for i in range(len(arr)):
	stream[i]=os.popen(arr[i])
	output=stream[i].read()