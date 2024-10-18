# Tourism Ecosystem - Design and Implementation


## Service list
 - core_app - Gateway and authentication service
 - ticket_app - Event Ticketing and Information service
 - hotel_app - Accommodation service 
 - ride_app - Transportation service 

## Launch requirement
When you need to use user information, run the `core_app` application first, and then start the corresponding application(`ticket_app`, `hotel_app`, `ride_app`).

> No need to authenticate user information, no startup sequence required.

## Install Dependencies and Run the Application
### Python Version
> We recommend using the latest version of Python. Flask supports Python 3.8 and newer.

### Install Dependencies
Use bash shell execute `exec_install.sh` script
```bash
sh exec_install.sh
```
**or** 

execute the command in `exec_install.sh` script one by one
```bash
python3 -m venv .venv

. .venv/bin/activate

pip install flask flask-sqlalchemy flask-login
```

### Run the Application
Use bash shell execute `exec_run.sh` script
```bash
sh exec_run.sh
```
**or** 

execute the command in `exec_run.sh` script one by one, the port should same as `url` in the `config.json` file.
```bash
. .venv/bin/activate

flask --app project run --port=8000 --debug
```