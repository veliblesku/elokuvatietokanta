# Asennusohje

Varmista aluksi, että python ja git ovat asennettuina.

````
git clone git@github.com:veliblesku/elokuvatietokanta.git
````
tai

[Lataa tästä](https://github.com/veliblesku/elokuvatietokanta/archive/master.zip) ja pura tiedosto.

### Aja seuraava komento projektin juurihakemistossa, joka luo virtuaaliympäristön:
````
python3 -m venv venv
````
Ota virtuaaliympäristö käyttöön:
````
source venv/bin/activate
````
Asenna projektin riippuvuudet:
````
pip install -r requirements.txt
````

Tämän jälkeen aja:
`````
python app.py
`````
Sovellus käynnistyy oletusarvoisesti portissa 5000 ja löydät lokaalin testiympäristön osoitteesta http://localhost:5000/ .
