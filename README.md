# ChainiumScanTesting
## About

Python sripts to ensure quality of ChainiumScan project developed by Own and team of students from Faculty of electrical engineering in Tuzla.

QA team uses Selenium for automation testing and Python programming language.

API: https://github.com/OwnMarket/OwnBlockchainExplorer

Web development: https://github.com/Amell-Diz/ChainiumScan/tree/master/src

The project is in progress.

## Installation

To use Python scripts from this project, you need to set up some things first!

Update:
```bash
$ sudo apt-get update
```
Install Python 3.6 version if you don't already have it:
```bash
$ sudo apt-get install python3.6
```
Install pip:
```bash
$ sudo apt install -y python3-pip
```
Also, virtualenv:
```bash
$ pip install virtualenv
```
Selenium automates browser. Read more about Selenium [here](https://www.seleniumhq.org/).
Install selenium package for Python by typing command:
```bash
$ pip install selenium
```
Unittest for test-cases. Unittest is a framework:
```bash
$ pip install unittest
```
## Set up Chrome webdriver

Since scripts are written to automate Chrome browser, you need to install Chrome.
If you already use Chrome, update it.

Check the version of Chrome by opening web browser and:
1) Click on the three dots in the upper right corner
2) Click Help
3) Click About Google Chrome

The version will appear below the logo. 
Mine: *Version 76.0.3809.87 (Official Build) (64-bit)*

Open [this link](https://sites.google.com/a/chromium.org/chromedriver/) to download appropriate webdriver. Remember version of your Google Chrome and download the same version of webdriver.

Now open a new terminal and type command:
```bash
```


## Clone the project

Open new terminal:
```bash
$ git clone https://github.com/merimakopic/ChainiumScanTesting.git
```
```bash
$ cd ChainiumScanTesting/Tests/Scripts
```
Open Home or comming repository: Blocks, Transactions, Validators by typing command:

```bash
$ cd 'name_of_repository'
```
For example:
```bash
$ cd Home
```
To run Python script, type:
```bash
$ python 'name_of_the_file.py'
```
For example:
```bash
$ python search.py
```
