# Secret Santa

Organize a secret santa or a killer game using AWS SNS.

## Setup
Clone the repository
```bash
cd secret-santa-aws
virtualenv venv -p python3.8
. venv/bin/activate

# Get dependencies
pip install --upgrade pip && pip install -r requirements.txt
```

## Usage
Ensure you have correctly configured your AWS account credentials.
```bash
cp players.json.sample players.json
# Edit the file with players names and international phone numbers.

python secret-santa.py
```
