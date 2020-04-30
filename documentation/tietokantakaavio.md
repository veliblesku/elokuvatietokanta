![Kaavio](https://github.com/veliblesku/elokuvatietokanta/blob/master/documentation/img/TietokantakaavioFinal.png)

# CREATE TABLE -lauseet
```
CREATE TABLE person (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	birthday DATETIME, 
	PRIMARY KEY (id)
);
```
```
CREATE TABLE account (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	username VARCHAR(144) NOT NULL, 
	password VARCHAR(144) NOT NULL, 
	PRIMARY KEY (id)
);
```
```
CREATE TABLE movie (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	duration INTEGER NOT NULL, 
	budget FLOAT NOT NULL, 
	year INTEGER NOT NULL, 
	account_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(account_id) REFERENCES account (id)
);
```
```
CREATE TABLE role (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	"roleName" VARCHAR(144) NOT NULL, 
	account_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(account_id) REFERENCES account (id)
);
```
```
CREATE TABLE rating (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	rating INTEGER, 
	account_id INTEGER NOT NULL, 
	movie_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(account_id) REFERENCES account (id), 
	FOREIGN KEY(movie_id) REFERENCES movie (id)
);
```
```
CREATE TABLE roles_in_movies (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	movie_id INTEGER, 
	account_id INTEGER, 
	role_id INTEGER, 
	person_id INTEGER, 
	PRIMARY KEY (id), 
	UNIQUE (movie_id, role_id, person_id), 
	FOREIGN KEY(movie_id) REFERENCES movie (id), 
	FOREIGN KEY(account_id) REFERENCES account (id), 
	FOREIGN KEY(role_id) REFERENCES role (id), 
	FOREIGN KEY(person_id) REFERENCES person (id)
);
```
