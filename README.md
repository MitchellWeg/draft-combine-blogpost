# Comebine Stats blogpost

## How to run:

### The dashboard itself

Make sure docker is installed. Then, in the root of the directory, run: `docker-compose up`
This will launch the following services:

| Service             | Port |
|---------------------|------|
| Grafana (Dashboard) | 3000 |
| MySQL (Database)    | 3306 |


Then you can navigate to `localhost:3000`, where you'll be greeted by the Grafana prompt.
The default username and password is `admin`. 
Upon first login, you'll be prompted to change your password.

### Loading in the data.
A python helper script is included to help load in the data.
The original dataset includes two csv's, one for the draft, and one for the combine.
The helper script combines the two datasets into one, and inserts it into the database.

To run the helper script:

```bash
virtualenv env
pip install -r requirements.txt
python database.py
```
