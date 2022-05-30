## Python 3.6.2

- Install [source](https://krystof.io/installing-alternative-python-versions-on-raspberry-pi/)
    - ```
    cd ~/Downloads
    sudo apt update
    sudo apt upgrade -y
    sudo apt-get install -y build-essential tk-dev libncurses5-dev libncursesw5-dev libreadline6-dev libdb5.3-dev libgdbm-dev libsqlite3-dev libssl-dev libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev libffi-dev tar wget vim
    wget https://www.python.org/ftp/python/3.6.2/Python-3.6.2.tgz
    tar zxf Python-3.6.2.tgz
    cd Python-3.6.2
    ./configure --enable-optimizations
    make -j 4
    sudo make altinstall
    ```
- To verify install
    - ```python3.6 -V```
- To install Python Packages
    - ```sudo python3.6 -m pip install --upgrade pip```
    - sudo python3.6 -m pip install RPi.GPIO

### RPI.GPIO

### Speech Recognition [source + guide](https://realpython.com/python-speech-recognition/#how-speech-recognition-works-an-overview)

### playsound [source + guide](https://www.geeksforgeeks.org/play-sound-in-python/)

- Install
    - ```sudo apt-get install gstreamer-1.0```
    - sudo apt-get install
      gstreamer-1.0 [source](https://stackoverflow.com/questions/40246437/problems-with-gst-in-python-program)

### pygobject

#### optional dependency for playsound

- Install
    - ```
    sudo apt-get install pkg-config
    sudo apt-get install libcairo2-dev
    sudo apt install libgirepository1.0-dev
    sudo python3.6 -m pip install pygobject
    ```
        - sudo apt-get install pkg-config [source](https://github.com/3b1b/manim/issues/751)
        - sudo apt-get install libcairo2-dev [source](https://github.com/3b1b/manim/issues/751)
        - sudo apt install
          libgirepository1.0-dev [source](https://stackoverflow.com/questions/18025730/pygobject-2-28-6-wont-configure-no-package-gobject-introspection-1-0-found)
        - sudo python3.6 -m pip install pygobject

Audio file must be called ding.mp3 and placed in project root
