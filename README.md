# LearnToCodeWithBaseball
love baseball? Want to code? Start here. Using Python and baseball's biggest stars and stats, we'll learn variables, loops, lists, and more! 

> This project is in progress and open to feedback. 💡

**Why Python?** 

Python is one of the easiest programming languages to read and write, which makes it perfect for learning to code for the first time. Python is also lightweight and great for data - Python doesn’t force you to memorize lots of symbols. You focus on what you want to do, not how complicated the language is.

Python is like learning the rules of baseball before learning advanced analytics — it builds a foundation you can grow on.

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
touch baseball.py
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

You can also open VSCode, select Open and select your ```baseball.py``` file. 

**If ```code``` doesn't work, ```Cmd + Shift + P``` -> Shell Command: Install 'Code' command**

## Step 5: Run your first Python program 

Open ```baseball.py``` and type (or copy): 

```python
print("Hello, baseball Python!")
```
### Step 5.2 

> ❗️ you will need to add the Python extension in VSCode. It should prompt you when adding a python file.

In VS Code:
1. Click the Extensions icon on the left sidebar
2. Search for Python
3. Install Python

This extension gives us:
- Syntax highlighting
- Helpful error messages
- Easy run buttons

Run your file either in VSCode or in Terminal. 

In VSCode, select Run. The intergrated terminal should open and you should see: 

```Hello, baseball Python!```

Or in Terminal, type: 

```bash 
python3 baseball.py
```

You'll then see: 

```Hello, baseball Python!```

🎉 That’s it. You just ran your first Python file.

**Why this matters** 
- ```print()``` shows output
- ```.py``` files are Python programs
- ```python3 filename.py``` runs the file in Terminal


