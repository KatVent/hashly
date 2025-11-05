# 🔒 Hashly

A simple Python CLI tool to hash text or files using different algorithms. Built with Typer.

## 🚀 Features
- Hash plain text or file using MD5, SHA1, SHA256 or SHA512
- Default to SHA256 if no algorithm is specified

## 🛠️ Installation

### Option 1: Run inside a virtual environment
'''bash
git clone
https://github.com/KatVent/hashly.git
cd Hashly
python3 -m venv .venv
source .venv/bin/activate
pip install build
python -m build
pip install dist/hashly-1.0-py3-none-any.whl
'''


### Option 2: Install globally
'''bash
pip install pipx # if not installed
pipx install
git+https://github.com/KatVent/hashly.git
'''


## 💡 Usage

### Hash text

''' bash 
hashly text "hello" --md5
'''

### Hash file

''' bash 
hashly file ./example.txt --sha1
'''