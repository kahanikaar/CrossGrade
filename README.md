# CrossGrade
 Contains Python scripts to automate Cross Grading of Python Architecture
 ### Steps of executing them:
      1)Running first.py : For preparation works, checking which all packages have their support in the other architecture and then installing the foreign arch into the kernel following with a reboot.
      2) Running multiarch.py : Running all packages, and cross grading support of packages as much as possible using multiarch.
      3) Running dpkgexplicit.py : Installing other packages directly from dpkg
      4) Running basepckg.py : Installing base packages from dpkg
      5) Running bootstrapping.py : Bootstrapping all libraries
      6) Running finalpkg.py : Finishing up installation of packages
      7) Running cleanup.py : Finishing up the entire process by removing the files no longer needed.
