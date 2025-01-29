# OpenSees Documentation

If you are looking for the online documentation, visit the repo through the URL [https://opensees.stairlab.io](https://opensees.stairlab.io)


## Building the HTML files


### 1. Download the repo using git from a terminal window

```
git clone https://github.com/stairlab/OpenSeesDocumentation.git
```

### 2. Building requires sphinx and some packages for sphinx

```
pip install -Ur requirements.txt
```

### 3. Once sphinx is installed and the repo downloaded, type `make html` to build it

```
make html
```

### 4. If it works the html files are in the build/html folder

on Linux type the following to open a browser with index page

```
xdg-open ./build/html/index.html
````

on a Mac

```
open ./build/html/index.html
```

