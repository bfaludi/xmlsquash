xmlsquash
========

Sok programozási nyelv által a legkényesebb fájlformátum az XML, mivel bejárása, és adatainak értelmes, könnyen feldogozható formára hozása közel sem egyszerű és gyors művelet. 

Ez a csomag azért jött létre, hogy az Internet-en több helyen és Stackoverflow-n feltűnő xml2dict megoldásokkal szemben, egy minden XML típusra működőképes átalakítót adjon, amelyet nagyon könnyű használni.

## Telepítés
Telepítés a szokásos módon történik.

	$ git clone https://github.com/bfaludi/XML2Dict.git
	$ cd XML2Dict
	$ python setup.py install
	
Csomag egyetlen függősége a **pyexpat**, amely a 2.7-es Python verziótól a Python programozási nyelv része.

## Futtatás
Bármelyik programban a felhasználása nagyon egyszerű. A következő példa megmutatja a csomag használatát.
	
	import xml2dict
	
	fp = codecs.open( 'file.xml', 'rb' )
	parser = xml2dict.XML2Dict()
	parser.parseFile( fp )
	fp.close()
	
## Függvények

### XML2Dict()
Az osztály példányosítása nem vár semmilyen paramétert. A kód bármelyik pontjában elvégezhetük. Ez az osztály végzi majd a tényleges XML adat bejárását és konvertálását az expat segítségével.

	from xml2dict import XML2Dict
	parser = XML2Dict()

#### parseString( str )
Szöveg konvertálására használatos. A függvény egyetlen paramétert vár, amely maga az XML szövege.

#### parseFile( file )
Fájl kovnertálására használatos. A függvény egy file pointer-t vár. Az átadott osztálynak kell hogy legyen `read` metódusa.

## Példa

### Bevezetés
Tekintsük a következő XML állományt:

	<?xml version="1.0" encoding="UTF-8"?>
	<item>
	   <maxlng>19.0613420893</maxlng>
	   <minlng>19.0478767813</minlng>
	   <district_id>3</district_id>
	   <terkod>120</terkod>
	   <minlat>47.5373529319</minlat>
	   <maxlat>47.5600603189</maxlat>
	   <lat>47.5487066254</lat>
	   <lng>19.0546094353</lng>
	   <nev>Óbudaisziget</nev>
	   <varosresz_id>1</varosresz_id>
	</item>

Amely a konvertálás után a következő lesz:

	{
	    u'minlng': {u'text': u'19.0478767813'}, 
	    u'district_id': {u'text': u'3'}, 
	    u'terkod': {u'text': u'120'}, 
	    u'minlat': {u'text': u'47.5373529319'}, 
	    u'maxlat': {u'text': u'47.5600603189'}, 
	    u'maxlng': {u'text': u'19.0613420893'}, 
	    u'lat': {u'text': u'47.5487066254'}, 
	    u'lng': {u'text': u'19.0546094353'}, 
	    u'nev': {u'text': u'\xd3budaisziget'}, 
	    u'varosresz_id': {u'text': u'1'}
	}

Fontos tulajdonsága, hogy a tényleges értéket tartalmazó szöveg a `text` kulcsba kerül, és az adott XML gyökér eleme pedig eltűnik, nem kerül külön feltüntetésre.

### Attribútumok, Listák
Tekintsünk egy fokkal komolyabb példát, amely már tartalmaz attribútumokat és felsorolásokat is.

	<?xml version="1.0" encoding="UTF-8"?>
	<masters>
	   <master id="18500">
	      <main_release>155102</main_release>
	      <images>
	         <image height="588" type="primary" uri="http://api.discogs.com/image/R-155102-1217088991.jpeg" uri150="http://api.discogs.com/image/R-150-155102-1217088991.jpeg" width="600" />
	      </images>
	      <artists>
	         <artist>
	            <id>1520</id>
	            <name>Samuel L. Session</name>
	            <anv>Samuel L</anv>
	            <join />
	            <role />
	            <tracks />
	         </artist>
	      </artists>
	      <genres>
	         <genre>Electronic</genre>
	      </genres>
	      <styles>
	         <style>Techno</style>
	      </styles>
	      <year>2001</year>
	      <title>New Soil</title>
	      <data_quality>Correct</data_quality>
	      <videos>
	         <video duration="490" embed="true" src="http://www.youtube.com/watch?v=yOEOrHIOxK0">
	            <title>Samuel L Session - Velvet</title>
	            <description>Samuel L Session - Velvet</description>
	         </video>
	         <video duration="294" embed="true" src="http://www.youtube.com/watch?v=Vgx1zzANNqk">
	            <title>Samuel L. Session - Body N` Soul</title>
	            <description>Samuel L. Session - Body N` Soul</description>
	         </video>
	      </videos>
	   </master>
	   <master id="57423">
	      <main_release>443809</main_release>
	      <images>
	         <image height="525" type="primary" uri="http://api.discogs.com/image/R-443809-1115049619.jpg" uri150="http://api.discogs.com/image/R-150-443809-1115049619.jpg" width="600" />
	         <image height="525" type="secondary" uri="http://api.discogs.com/image/R-443809-1115049647.jpg" uri150="http://api.discogs.com/image/R-150-443809-1115049647.jpg" width="600" />
	         <image height="600" type="secondary" uri="http://api.discogs.com/image/R-443809-1289800278.jpeg" uri150="http://api.discogs.com/image/R-150-443809-1289800278.jpeg" width="600" />
	      </images>
	      <artists>
	         <artist>
	            <id>3225</id>
	            <name>Vince Watson</name>
	            <anv />
	            <join />
	            <role />
	            <tracks />
	         </artist>
	      </artists>
	      <genres>
	         <genre>Electronic1</genre>
	         <genre>Electronic2</genre>
	         <genre>Electronic3</genre>
	      </genres>
	      <styles>
	         <style>Techno</style>
	         <style>Tech House</style>
	      </styles>
	      <year>2005</year>
	      <title>Sublimina</title>
	      <data_quality>Correct</data_quality>
	      <videos>
	         <video duration="411" embed="true" src="http://www.youtube.com/watch?v=hgCKATy4Ij4">
	            <title>Vince Watson - Sublimina (Encryption)</title>
	            <description>Vince Watson - Sublimina (Encryption)</description>
	         </video>
	         <video duration="225" embed="true" src="http://www.youtube.com/watch?v=934QXDz5NuA">
	            <title>Vince Watson - Sublimina (Decryption)</title>
	            <description>Vince Watson - Sublimina (Decryption)</description>
	         </video>
	         <video duration="410" embed="true" src="http://www.youtube.com/watch?v=_yFyCtr2YUU">
	            <title>Vince Watson - Intrisync</title>
	            <description>Vince Watson - Intrisync</description>
	         </video>
	      </videos>
	   </master>
	</masters>
	
Ennek az XML-nek a konvertálása a következő eredménnyel tér vissza:

	{ u'master': [
	    {
	        u'styles': {
	            u'style': {u'text': u'Techno'}
	        }, 
	        u'genres': {
	            u'genre': {u'text': u'Electronic'}
	        }, 
	        u'videos': {
	            u'video': [
	                {
	                    u'duration': u'490', 
	                    u'src': u'http://www.youtube.com/watch?v=yOEOrHIOxK0', 
	                    u'embed': u'true', 
	                    u'description': {u'text': u'Samuel L Session - Velvet'}, 
	                    u'title': {u'text': u'Samuel L Session - Velvet'}
	                }, {
	                    u'duration': u'294', 
	                    u'src': u'http://www.youtube.com/watch?v=Vgx1zzANNqk', 
	                    u'embed': u'true', 
	                    u'description': {u'text': u'Samuel L. Session - Body N` Soul'}, 
	                    u'title': {u'text': u'Samuel L. Session - Body N` Soul'}
	                }
	            ]
	        }, 
	        u'title': {u'text': u'New Soil'}, 
	        u'main_release': {u'text': u'155102'}, 
	        u'year': {u'text': u'2001'}, 
	        u'artists': {
	            u'artist': {
	                u'join': {}, 
	                u'name': {u'text': u'Samuel L. Session'}, 
	                u'anv': {u'text': u'Samuel L'}, 
	                u'tracks': {}, 
	                u'role': {}, 
	                u'id': {u'text': u'1520'}
	            }
	        }, 
	        u'images': {
	            u'image': {
	                u'width': u'600', 
	                u'uri150': u'http://api.discogs.com/image/R-150-155102-1217088991.jpeg', 
	                u'type': u'primary', 
	                u'uri': u'http://api.discogs.com/image/R-155102-1217088991.jpeg', 
	                u'height': u'588'
	            }
	        }, 
	        u'id': u'18500', 
	        u'data_quality': {u'text': u'Correct'}
	    }, {
	        u'styles': {
	            u'style': [
	                {u'text': u'Techno'}, 
	                {u'text': u'Tech House'}
	            ]
	        }, 
	        u'genres': {
	            u'genre': [
	                {u'text': u'Electronic1'}, 
	                {u'text': u'Electronic2'}, 
	                {u'text': u'Electronic3'}
	            ]
	        }, 
	        u'videos': {
	            u'video': [
	                {
	                    u'duration': u'411', 
	                    u'src': u'http://www.youtube.com/watch?v=hgCKATy4Ij4',
	                    u'embed': u'true', 
	                    u'description': {u'text': u'Vince Watson - Sublimina (Encryption)'}, 
	                    u'title': {u'text': u'Vince Watson - Sublimina (Encryption)'}
	                }, {
	                    u'duration': u'225', 
	                    u'src': u'http://www.youtube.com/watch?v=934QXDz5NuA', 
	                    u'embed': u'true', 
	                    u'description': {u'text': u'Vince Watson - Sublimina (Decryption)'}, 
	                    u'title': {u'text': u'Vince Watson - Sublimina (Decryption)'}
	                }, {
	                    u'duration': u'410', 
	                    u'src': u'http://www.youtube.com/watch?v=_yFyCtr2YUU', 
	                    u'embed': u'true', 
	                    u'description': {u'text': u'Vince Watson - Intrisync'}, 
	                    u'title': {u'text': u'Vince Watson - Intrisync'}
	                }
	            ]
	        }, 
	        u'title': {u'text': u'Sublimina'}, 
	        u'main_release': {u'text': u'443809'}, 
	        u'year': {u'text': u'2005'}, 
	        u'artists': {
	            u'artist': {
	                u'join': {},
	                 u'name': {u'text': u'Vince Watson'}, 
	                 u'anv': {}, 
	                 u'tracks': {}, 
	                 u'role': {}, 
	                 u'id': {u'text': u'3225'}
	            }
	        }, 
	        u'images': {
	            u'image': [
	                {
	                    u'width': u'600', 
	                    u'uri150': u'http://api.discogs.com/image/R-150-443809-1115049619.jpg', 
	                    u'type': u'primary', 
	                    u'uri': u'http://api.discogs.com/image/R-443809-1115049619.jpg', 
	                    u'height': u'525'
	                }, {
	                    u'width': u'600', 
	                    u'uri150': 
	                    u'http://api.discogs.com/image/R-150-443809-1115049647.jpg', 
	                    u'type': u'secondary', 
	                    u'uri': u'http://api.discogs.com/image/R-443809-1115049647.jpg', 
	                    u'height': u'525'
	                }, {
	                    u'width': u'600', 
	                    u'uri150': u'http://api.discogs.com/image/R-150-443809-1289800278.jpeg', 
	                    u'type': u'secondary', 
	                    u'uri': u'http://api.discogs.com/image/R-443809-1289800278.jpeg', 
	                    u'height': u'600'
	                }
	            ]
	        }, 
	        u'id': u'57423', 
	        u'data_quality': {u'text': u'Correct'}
	    }
	]}

Ebből a példából már láthatunk sok dologra példát, az attribútumokok a `dict`-ekbe kerülnek, ha van értékük akkor az `text` változóba kerül. Amennyiben az adott nevű elemből több is szerepel, akkor `list`-be kerülnek az összegyűjtött `dict` elemek.

### Kérdés
Ha van, dobj egy levelet a <a href="mailto:hello@bfaludi.com">hello@bfaludi.com</a> email címre, vagy lessed meg a <a href="http://bfaludi.com">bfaludi.com</a> honlapot.