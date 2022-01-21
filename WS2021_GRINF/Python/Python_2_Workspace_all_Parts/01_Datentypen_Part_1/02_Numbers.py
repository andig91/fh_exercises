# Siehe: https://www.tutorialspoint.com/python/python_variable_types.htm

# Wie es der Name schon sagt, speichern Datentype der Famile "Numbers" nummaerische Werte. Number
# Objekte werden angelegt wenn man ihnen einen Wert zuweist.

a = 1
b = 2
print( a )
print( b )

# Natuerlich kann man eine oder mehrere Variablen auch loeschen. Hierfuer miss das Keyword "del" 
# verwendet werden. Die Syntax sieht wie folgt aus: del var1[,var2[,...,varN]]

del a
#print( a )      # Die zugehoerige Fehlermeldung bei Ausfuehrung da schon geloescht: 
                # "NameError: name 'a' is not defined"

a = 1           # Muss neu zugewiesen werden da schon geloescht vorher
del a, b
#print( a )      
#print( b )

# Generell unterstuetzt Python 4 verschiedene nummaerische Datantypen:
#   - int       signed Integer
#   - long      long Integer, der gespeicherte Wert kann auch im Oktal- (8 als Basis) oder 
#               Hexerdezimalsystem (16 als Basis) dargestellt werden
#   - float     Fliesskommazahlen 
#   - complex   Komplexe Zahlen

i = 100
print( type( i ) )
#l = 100L               # ab Python 3 nicht mehr enthalten
#print( type( l ) )
f = 1.234
print( type( f ) )
c = 1+2j
print( type( c ) )

# Beim Rechnen ist zu beachten dass beispielsweise eine Division von 2 Integern auch wieder 
# einen Integer zurueckliefert. Das hat zur Folge dass Beispielsweise bei der folgenden Rechnung
# keine Auswitkungen merkbar sind:

print( 6 / 3 )      # 6 / 3 = 2

# Jedoch bei einer Division die zu einem Rest oder zu Kommastellen fuehren sollte werden die 
# Auswirkungen ersichtlich:

# Hinweis: In Python 3 ist das schon durch eine interne Konvertierung gelöst

print( 7 / 2 )      # 7 / 2 = 3.5 normalerweise. Hier wird aber nur 3 ausgegeben da die Berechnung
                    # auf Basis von Integern durchgefuehrt wird und diese keine reellen Zahlen 
                    # unterstuetzen.

print( 7.0 / 2 )    # Die folgenbden Varianten fuehren zum korrekten Ergebnis. Man kann natuerlich                       
print( 7 / 2.0 )    # auch mit einer Typumwandlung (siehe 03_Typumwandlung) arbeiten , sehen wir  
print( 7.0 / 2.0 )  # uns aber erst spaeter an.