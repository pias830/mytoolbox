# mytoolbox

## Get started

```bash
cd ws
git clone https://github.com/pias830/mytoolbox.git
python3 -m venv venv    #sets up the virtual environment
source venv/bin/activate    #activates the virtual environment 
pip install -r requirements.txt     #installs dependencies (only in the virtual environment)
deactivate      #deactivates the virtual environment
```

## Develop

```bash
source venv/bin/activate    #on Linux and macOS

venv\Scripts\activate       #on Windows

# Develop, at your own risk

deactivate
```


## Installing the toolbox

```bash
cd mytoolbox
pip install .
```

## Usage

Email scanner
```bash
emails <Country> #your desired country with a capitalized first letter
```

Subdomain enumeration
```bash
subdomain 'domain'
```

Subpage enumeration
```bash
subpage 'domain'
```

Cat fact
```bash
catfact
```

Brute force
```bash
bruteforce --url http://example.com/login --user username --max-length 4 --chars abc123
bruteforce --url http://localhost:3000/auth/login --user user@example.com --max-length 8 --chars adoprsw
```

Brute force Selenium
```bash
bfselenium --url http://localhost:3000 --user user@example.com --max-length 8 --chars adoprsw
```
