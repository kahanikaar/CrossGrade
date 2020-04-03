import os
stream = []
arr=["dpkg -l | grep -B 1 i386","apt-get install -f","apt-get dist-upgrade -f","apt-get autoremove","aptitude markauto '~ri386~i'","aptitude purge '~ri386~i'","aptitude purge '~ri386~c'","dpkg --remove-architecture i386"]
	output=stream[i].read()