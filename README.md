# 🔒 Hashly

A simple Python CLI tool to hash text or files using different algorithms. Built with Typer.

## 🚀 Features
Hash plain text or file using MD5, SHA1, SHA256 or SHA512

## 🛠️ Installation

### Option 1: Run inside a virtual environment

#### Create virtual environment
```bash
git clone https://github.com/KatVent/hashly.git
cd hashly
python -m venv .venv
```
#### Activate virtual environment based on the OS
```bash
source .venv/bin/activate # For macOS / Linux
.venv\Scripts\Activate.ps1  # For Windows (Powershell)
```
#### Install the package
```bash
pip install .
```

### Option 2: Install globally
```bash
pip install pipx # if not installed
pipx install hashly
```

## 💡 Usage

### Hash text

```bash 
hashly string hello --alg md5
```

### Hash file

```bash 
hashly file ./example.txt --alg sha1
```