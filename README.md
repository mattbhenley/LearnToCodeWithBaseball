# LearnToCodeWithBaseball
love baseball? Want to code? Start here. Using Python and baseball's biggest stars and stats, we'll learn variables, loops, lists, and more! 

## Step 1: Check if Python is already installed (macOS)
Open Terminal

***Applications → Utilities → Terminal***

Run:

```python3 --version```

What you’ll see

✅ Python 3.x.x → Python is installed

❌ command not found → we’ll install it

macOS sometimes ships with a system Python — we will ***NOT*** use python, only python3.

## Step 2: Install Homebrew (recommended) 

What is Homebrew? Homebrew is a popular, free, open-source package manager for macOS and Linuxthat simplifies installing, updating, and managing software from the command line. 

So to install homebrew, we'll simply copy the following command in our terminal. (Open Terminal appliction) 

```/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"```

After it finishes, let's verify that it was installed by checking the version. 

```brew --version```

### Step 2.2: Install Python 

```brew install python```

Verify: 

```bash
python3 --version
pip3 --version
```

We should see something like this: 

```bash
Python 3.12.x
pip 23.x
```
## Step 3: Set up project folder 

In terminal, first, we'll navigate to our Desktop. (alternatively, we can use another location but for beginners, I recommed Desktop)

```bash
mkdir baseball_python
cd baseball_python
```

```cd``` changes our directory to baseball_pyhton 

Create our first file: 

```bash
touch batting_average.py
```

💥 You created your first python file! Congrats. 

## Step 4: Choose an editor (VS Code is recommended) 

Install VSCode 

Download from [VSCode](https://code.visualstudio.com)

Once downloaded, we can open up our project. 

In your terminal window, we can simply type: 

```bash
code .
``` 

The project should open in VSCode. 

You can also open VSCode, select Open and select your ```baseball_pyhton``` folder. 

*** If ```code``` doesn't work, ```Cmd + Shift + P``` -> Shell Command: Install 'Code' command ***

