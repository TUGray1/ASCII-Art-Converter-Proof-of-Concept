# ASCII-Art-Converter-Proof-of-Concept
Proof of concept for the ASCII art converter web app. This app uses the OpenCV library for working with images, and the Flask web framework.

## Prerequisites
- __Have mini conda installed on your computer__ -> https://www.anaconda.com/docs/getting-started/miniconda/install

## Steps to run the app

### 1.) Clone repo onto device

### 2. Create and activate local environment 
```
conda create -n ascii python=3.11 -y
conda activate ascii
```

### 3.) Install libraries and frameworks
```
conda install numpy opencv flask flask-cors -c conda-forge
```

### 4.) Navigate to and start backend 
```
cd backend
python converter.py
```
__Do not close this terminal__

### 5.) Open app
Go to the fronted folder and right click on index.html and open in browser.
  - If you can't open this app in your browser try running this program in vscode with the Live Server extension installed.

## Tech Stack
- python 3.11
- HTML and js
- OpenCV
- Flask
- numpy
