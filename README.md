# mytoolbox

A simple toolbox for educational purposes, containing the following tools:

### Email-adress scanner

### Subdomain scanner

### Subpage scanner

### Catfact (wow!)

### Brute force tool

### Selenium brute force tool

### Commit counter

## Get started

```bash
cd ws
git clone https://github.com/pias830/mytoolbox.git
python3 -m venv venv        #if you want to work in a virtual environment, this sets it up
source venv/bin/activate    #activates virtual environment
pip install -r requirements.txt
deactivate      #deactivates virtual environment
```

## Develop

```bash
source venv/bin/activate    #on Linux and macOS
venv\Scripts\activate       #on Windows

#Develop, at your own risk

deactivate
```


## Installing the toolbox

```bash
cd mytoolbox
source venv/bin/activate
pip install .
#Use desired scripts
deactivate
```

## Usage

### Email scanner
```bash
emails 'country' #will create a .txt file to save the email-adresses from desired country
```

### Subdomain enumeration
```bash
subdomain 'domain'
```

### Subpage enumeration
```bash
subpage 'domain'
```

### Cat fact
```bash
catfact
```

### Brute force
```bash
bruteforce --url http://example.com/login --user username --max-length 4 --chars abc123
bruteforce --url http://localhost:3000/auth/login --user user@example.com --max-length 8 --chars adoprsw
```

### Brute force Selenium
```bash
bfselenium --url http://localhost:3000 --user user@example.com --max-length 8 --chars adoprsw
```

### Commit counter
```bash
commits
```
