# Tourism Ecosystem - Design and Implementation


## Service list
 - core_app - Gateway and authentication service, default port is 8000
 - ticket_app - Event Ticketing and Information service, default port is 8001
 - hotel_app - Accommodation service, default port is 8002
 - ride_app - Transportation service, default port is 8003

## Launch requirement
When you need to use user information, run the `core_app` application first, and then start the corresponding application(`ticket_app`, `hotel_app`, `ride_app`).

> No need to authenticate user information, no startup sequence required.

## Install Dependencies and Run the Application
### Python Version
> We recommend using the latest version of Python. Flask supports Python 3.8 and newer.

### Install Dependencies
Enter special service documentation
```bash
cd core_app
```

Use bash shell execute `exec_install.sh` script
```bash
sh exec_install.sh
```
**or** 

No bash shell or in `windows` envirionment execute follow command one by one
```cmd
python3 -m venv .venv

.venv\Scripts\activate

pip install flask flask-sqlalchemy flask-login requests
```

### Run the Application
Use bash shell execute `exec_run.sh` script
```bash
sh exec_run.sh
```
**or** 

No bash shell or in `windows` envirionment execute follow command one by one, the port should same as `url` in the `config.json` file.
```bat
.venv\Scripts\activate

flask --app project run --port=8000 --debug
```