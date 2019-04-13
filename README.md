# Python syntax, and call graph analysis tool based on Pylint
## CMPUT 497 Project

# Contributors:
* Zhimao Lin
* Yi Zhang
* Wang Dong

# Instructions of Running our Project
## Target machine and environment
* Macbook Pro
* MacOS Mojave Version 10.14.3

## Depedencies
1. Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 03:13:28)

## Running Steps
### Step0: Install dependencies
1. Update your MacOS to MacOS Mojave Version 10.14.3 (The latest version on March 20th, 2019) <br> 
   For more details, you can check [here](https://support.apple.com/en-ca/macos/mojave) or contact [Apple support](https://getsupport.apple.com/?caller=psp&PRKEYS=PF6)

2. Install Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 03:13:28) <br>
   You can download Python 3.7.1 [here](https://www.python.org/ftp/python/3.7.1/python-3.7.1-macosx10.6.pkg). For more details, you can follow the [Python beginners' guide](https://wiki.python.org/moin/BeginnersGuide/Download). After successfully downloading the installer, just open the .pkg file and follow the steps of the installer.

### Step1: Add your input python files in to `please_put_test_python_file_here` folder
Just copy and paste the python files that you want to analyze into `please_put_test_python_file_here` folder. 

### Step2: Run chmod command to give the permision to run the shell script run.sh
Open Terminal on your Mac and direct to our repo directory, `<REPO name>` using command `cd` <br>
  If you do not know how to use command `cd`, you can Google it or check this [tutorial](https://macpaw.com/how-to/use-terminal-on-mac).

#### Run
  > ```chmod +x run.sh```


### Step3: Run `run.sh`
If you want to analyze all Python files in the `please_put_test_python_file_here` folder
#### Run
  > ```./run.sh```

If you want to analyze a specific Python file in the `please_put_test_python_file_here` folder
#### Run
  > ```./run.sh <Python File Name>```