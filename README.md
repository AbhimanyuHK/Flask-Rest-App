# Flask-Rest-App

## Scope
* Inserting rows to database

* Updating rows in database

* Fetching rows from database

* Deleting rows from database


## Install dependencies 
``` $ pip install -r requirements.txt ```


## Run application

``` $ python script/flaskapp.py ```

Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

## Insert rows 

http://127.0.0.1:5000/create

``` 
{
	"firstname" : "abhi",
	"lastname" : "manyu",
	"email" : "abhimanyu@gmail.com"
}
```
## Get row by id

http://127.0.0.1:5000/get/<id>
  
## Get all rows 

http://127.0.0.1:5000/all

## Delete row by id

http://127.0.0.1:5000/delete/<id>
  
  
``` 
{
	"firstname" : "abcd",
	"lastname" : "wxyz",
	"email" : "abcdwxyz@gmail.com"
}
```

## Update row

http://127.0.0.1:5000/update/<id>
  
  
