# mytoolbox

## Get started

```bash
cd ws
git clone https://github.com/pias830/mytoolbox.git
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
deactivate
```

## Develop

```bash
source venv/bin/activate    # Linux 
source venv/bin/activate    # macOS
venv\Scripts\activate       # Windows

# Develop at your own risk, or pleasure

deactivate
```


## Installing a toolbox

```bash
cd miwashi_toolbox
pip install .
# or
cd pias_toolbox
pip install .
```

## Usage



```bash
bruteforce --url http://example.com/login --user username --max-length 4 --chars abc123
bruteforce --url http://localhost:3000/auth/login --user user@example.com --max-length 8 --chars adoprsw

bfselenium --url http://localhost:3000 --user user@example.com --max-length 8 --chars adoprsw
```

