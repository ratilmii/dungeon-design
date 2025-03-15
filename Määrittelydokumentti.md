# Dungeon Design  

## Projektin tarkoitus  
Tarkoituksena on kehittää Pythonilla työkalu generoimaan luolastoja, joita voi sitten käyttää esimerkiksi videopelikehityksessä tai pöytäroolipelaamisessa tarvittavien karttojen luomiseen.  

Käyttäjä määrittelee eri parametreja, esimerkiksi:  
- Huoneiden määrä  
- Huoneiden välillä olevien käytävien määrä  
- Vaihtoehtoisten reittien määrä  
- Luolaston kompleksisuus  

Generoitu luolasto päivittyy reaaliajassa, tai riittävän lähellä sitä, jotta käyttö olisi dynaamista ja erilaisten vaihtoehtojen generointi tapahtuisi nopeasti. Kun käyttäjä on tyytyväinen lopputulokseen, voi luolaston tallentaa tiedostoon (tallennustyyppi tarkentuu projektin aikana).  

## Algoritmit ja toteutus  
Tarkoituksena on hyödyntää **Delaunay-triangulaatiota**, joka toteutetaan **Bowyer-Watson -algoritmilla**. Mahdolliset bonustoiminnallisuudet ja niihin käytetyt algoritmit tarkentuvat projektin aikana.  

## Projektin tiedot  
- **Opinto-ohjelma:** tietojenkäsittelytieteen kandidaatti  
- **Dokumentaation kieli:** suomi  
- **Ohjelmointikielet, joilla tehtyjä töitä voin vertaisarvioida:** Python, Java, C++  

## Lisätietoja  
- [Delaunay-triangulation (Wikipedia)](https://en.wikipedia.org/wiki/Delaunay_triangulation)  
- [Bowyer-Watson algorithm (Wikipedia)](https://en.wikipedia.org/wiki/Bowyer%E2%80%93Watson_algorithm)  
