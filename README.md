# Comebine Stats blogpost

Relevant [blogpost](https://mitchellweg.github.io/combine-stats-part-1/)

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

If you have edited the docker-compose.yml in any way, or want to host either Grafana or the database in a different way, you can pass numerous flags to the database helper script:

| Flag | Long                | Description                                                  | Default     |
|------|---------------------|--------------------------------------------------------------|-------------|
| -d   | --data-dir          | The directory where the script should look to find the data. | '../'       |
| -u   | --database-user     | The database user                                            | 'root'      |
| -p   | --database-password | The database password of that user                           | 'root'      |
| -n   | --database-name     | The database name                                            | 'combine'   |
| -ho  | --database-host     | The host where the database is hosted                        | 'localhost' |
| -s   | --start-year        | The start year of the data                                   | '2000'      |
| -e   | --end-year          | The end year of the data                                     | '2022'      |

