# edu-pentest-toolbox

## Initialize project

```bash
git clone https://github.com/miwashi-edu/edu-pentest-toolbox.git
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
deactivate
```

## Develop

```bash
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Develop

deactivate
```


## Install toolbox

```bash
pip install .

# Test it
pentest
```

## Usage

Brute force

```bash
bruteforce --url http://example.com/login --user username --max-length 4 --chars abc123
bruteforce --url http://localhost:3000/auth/login --user user@example.com --max-length 8 --chars adoprsw

bfselenium --url http://localhost:3000 --user user@example.com --max-length 8 --chars adoprsw
```

