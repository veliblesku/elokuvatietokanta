# User Stories


## Autentikointi
### Käyttäjä ...
* ... voi rekisteröityä palveluun.
`````
INSERT INTO account (name, username, password) VALUES(..., ..., ...);
`````
* ... voi kirjautua palveluun omilla käyttäjätunnuksillaan.
`````
SELECT a.username, a.password from account WHERE a.username=(given_username) AND a.password=(given_password);
`````

## Elokuvat
### Vierailija ...
* ... voi listata elokuvat.
`````
SELECT * FROM movie;
`````
### Kirjautunut Käyttäjä ...
* ... voi lisätä elokuvia tietokantaan.
`````
INSERT INTO movie (name, duration, budget, year) VALUES(..., ..., ..., ...);
`````
* ... voi muokata elokuvan tietoja.
`````
UPDATE movie set name="new_name", ..., WHERE movie.id="given_id";
`````
* ... voi poistaa elokuvan.
`````
DELETE FROM movie WHERE movie.id="given_id";
`````

## Henkilöt elokuvan teossa
### Vierailija ...
* ... voi listata elokuvan tekijät.
`````
SELECT * FROM person;
`````
### Kirjautunut Käyttäjä ...
* ... voi lisätä elokuvien tekijöitä tietokantaan.
`````
INSERT INTO person (name, birthday) VALUES(..., ...);
`````
## Henkilöiden roolit elokuvien teossa
* ... voi listata elokuvien tekemiseen liittyvät roolit.
`````
SELECT * FROM role;
`````
### Kirjautunut Käyttäjä ...
* ... voi lisätä rooleja elokuvanteossa tietokantaan.
`````
INSERT INTO role (rolename) VALUES(...);
`````
## Kirjautunut käyttäjät... 
* ... voi liittää henkilön, roolin ja elokuvan toisiinsa
`````
INSERT INTO roles_in_movies (movie_id, role_id, person_id) VALUES(movie_id, role_id, person_id);
`````
### Vierailija...
* ... voi listata elokuvan tekoon osallistuneita henkilöitä.
````
SELECT rim.id, p.name, r.rolename FROM roles_in_movies rim JOIN person p ON rim.person_id = p.id JOIN role r ON rim.role_id=r.id  WHERE movie_id=:m_id;
````
## Arvostelut
### Vierailija...
* ... voi nähdä elokuvan arvostelujen keskiarvon.
````
SELECT avg(rating) FROM rating WHERE movie_id=:id;
````

### Kirjautunut Käyttäjä ...
* ... voi nähdä omien arvostelujensa lukumäärän.
````
SELECT COUNT(Rating.id) FROM rating WHERE account_id=:u_id;
````
* ... voi nähdä omien arvostelujensa keskiarvon.
````
SELECT AVG(Rating.rating) FROM rating WHERE account_id=:u_id;
````
* ... voi arvostella elokuvia.
````
INSERT INTO rating (rating, movie_id) VALUES(rating, movie_id);

````
* ... voi listata omat arvostelunsa.
````
SELECT Movie.id, Movie.name, Movie.year, Rating.rating FROM movie LEFT JOIN rating ON Movie.id=rating.movie_id WHERE rating.account_id =:a_id;
````
* ... voi muuttaa elokuvan arvostelua.
````
UPDATE rating set rating="new_rating", WHERE rating.id="given_id";
````
* ... voi poistaa oman arvostelun.
````
DELETE FROM rating WHERE id = given_id;
````
* ... voi tarkastaa onko hän arvostellut jo kyseisen elokuvan (tällöin sovelluksessa myös päivitetään arvostelu)
````
SELECT EXISTS (SELECT * FROM rating WHERE account_id=:a_id AND movie_id=:m_id);
````






