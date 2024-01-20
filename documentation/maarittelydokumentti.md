# Määrittelydokumentti

Opinto-ohjelma: TKT
Ohjelmointikieli: Python
Muut osaamisalueen kielet: JavaScript, TypeScript
Projektin kieli: Englanti
Dokumentaation kieli: Suomi

## Minesweeper eli Miinaharava

Projektini aihe on Miinaharava. Luon ensin pohjan Miinaharava-pelille, ja sitten luon algoritmin, joka osaa ratkaista Miinaharavan parhailla mahdollisilla todennäköisyyksillä. Mikäli Miinaharava-peli ei ole lukijalle tuttu, se menee yksinkertaisesti näin: Pelialue on ruudukko, jonka jokaisen ruudun takaa löytyy joko miina tai numero, joka kertoo miinojen määrän ympäröivien kahdeksan ruudun alueella. Pelaajan on tarkoitus päättelyiden perusteella löytää kaikki pelialueen miinat ja merkitä ne lipulla ilman, että pelaaja avaa yhtäkään ruutua, jossa on miina. Mikäli pelaaja osuu miinaan, peli on hävitty. 

Tutustuin kurssimateriaalissa esiteltyyn David Becerran [Algorithmic Approaches to Playing Minesweeper](https://dash.harvard.edu/bitstream/handle/1/14398552/BECERRA-SENIORTHESIS-2015.pdf?sequence=1&isAllowed=y)-tutkielmaan. Tässä käsiteltiin muun muassa Miinaharavan ensimmäistä siirtoa koskevia todennäköisyyksiä. Becerra esitti väitteen, että kulmaruudusta pelin aloittaminen on turvallisin vaihtoehto, koska kulmaruutu on todennäköisemmin numero 0 (ei miinoja ympärillä). Tässä Becerra on täysin oikeassa, ja tätä periaatetta aion toteuttaa algoritmissani. Becerra esitti tutkielmassaan myös muita hyviä päätelmiä, jotka esittelen seuraavissa kappaleissa tarkemmin.

Becerran mukaan Miinaharavan toinen ongelma on arvausten toteuttaminen. Arvaamista tulee välttää, mutta mikäli peliä ei voi jatkaa ilman arvaamista, on arvattava vaihtoehtoa, jossa riski on pienin. Samoin tulee suosia arvauksia, jotka auttavat pelin etenemistä. Kuitenkin satunnaisesti vastaan tulee tilanteita, joissa on pakko arvata kahden täysin yhtä todennäköisen vaihtoehdon välillä. Mikäli muun pelitilanteen eteneminen ei voi helpottaa tätä arvausta, arvaus on tapana tehdä heti, jotta arvauksen ollessa väärin uuden pelin pääsee aloittamaan mahdollisimman nopeasti. Kuitenkin, omassa algoritmissani haluan jättää tällaiset arvaukset viimeiseksi, tavoitteenani päästä pelissä mahdollisimman pitkälle, vaikkei voittoa tapahtuisikaan.

Olen tuonut esille jo arvaamiseen liittyvät kohdat, mutta seuraavaksi esittelen pelin normaalin kulun. Ensimmäiseksi algoritmin tulisi tarkastaa, löytyykö pelistä tilanteita, joissa yhtä ruutua (ja sen ympäröiviä ruutuja) tarkastamalla voi tehdä varmoja päätelmiä. Tätä kutsutaan single point (SP) strategiaksi. Esimerkki tällaisesta tilanteesta on, kun ruudun numero vastaa ympäröivien ruutujen merkittyjen miinojen määrää. Tällöin tiedetään, että edellämainitun ruudun ympärillä kaikki merkitsemättömät ruudut ovat turvallisia. Algoritmin tulisi siis tässä tilanteessa avata kaikki turvalliset ruudut.