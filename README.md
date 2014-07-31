#Create pro/config.py

> PORT=5888

> SECRET="sessionsecret"


> LOGIN="youlogin"


> PASSWORD="youpassword"


#Create virtual env

`$ virtualenv env`

`$ source env/bin/active`

`$ pip install -r requirements.txt`


# init db
`$ python get_base.py`

`$ python debug.py`