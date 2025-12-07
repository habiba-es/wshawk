# Publishing WSHawk to PyPI

## One-Time Setup

### 1. Create PyPI Account
- Go to https://pypi.org/account/register/
- Create account with your email
- Verify email

### 2. Install Build Tools
```bash
pip install --upgrade pip setuptools wheel twine
```

## Publishing Steps

### 1. Clean Previous Builds
```bash
cd /home/regaan/Desktop/wshawk
rm -rf build/ dist/ *.egg-info
```

### 2. Build Package
```bash
python setup.py sdist bdist_wheel
```

### 3. Check Package
```bash
twine check dist/*
```

### 4. Upload to PyPI
```bash
twine upload dist/*
```

Enter your PyPI username and password when prompted.

## After Publishing

Users can install with:
```bash
pip install wshawk
```

Then use either:
```bash
# Interactive mode (recommended)
wshawk-interactive

# Direct mode
wshawk wss://target.com/socket
```

## Updating Version

1. Edit `setup.py` - change version number
2. Repeat publishing steps above

## Test Before Publishing (Optional)

Upload to TestPyPI first:
```bash
twine upload --repository testpypi dist/*
pip install --index-url https://test.pypi.org/simple/ wshawk
```
