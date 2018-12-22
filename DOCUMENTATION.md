# Skriv ()
Skriv () funktionen skriver text och/eller data till konsolen. Skriv () funktionen kan inte läggas in i andra fuktioner.

### Skriv Text/String
skriv ("Hej Världen")

## Andra tillämpningar av Skriv ():
Skriv () kan skriva olika sorters data; Här är alla olika typer fuktionen accepterar.

### Skriv Variabel
skriv ($variabel_namn)

### Skriv Sak från lista (med index nummer)
skriv ($lista[1])

# Variabler
Variabler sparar data under ett namn och kan hämtas med att skriva $ och variabelnamnet efter.

### Text/String Variabel
var min_string = "Hej Världen"

## Andra variabel datatyper.
Du kan spara text, andvändarinput, nummer, matematiklösningar, listor, kombinerade variabler och saker från listor (Med index) och längd av text, nummer och listor (Antal saker).

### Andvändarinput Variabel
var namn = in("Skriv Ditt Namn: ")

### Nummer Variabel
var num1 = 2

### Matematik Variabel (Med nummer)
var resultat = matte(2*3)

### Matematik Variabel (Med variabler)
var resultat = matte($num1 + 3)

### List Variabel (Text och nummer)
var inköp = ["bröd", "smör", "ägg", "mjölk", 1, 4]

### Kombinerade Variabler
var tittel = "Hej, " + $namn

### Sak Från Lista Variabel (Med indexnummer)
var smör = $inköp[1]

### Sak Från Lista Variabel (Med index från variabel)
var smör = $inköp[$indx]

### List Längd Variabel
var min_lista = längd($lista1)

### Text/String Längd Variabel
var min_text = längd("Hej")

### Variabel Längd Variabel
var min_text = längd($text)

# Listor
Listor är en variabel datatyp där du kan spara flera texter, mummer etc. i samma variabel och uder samma variabelnamn. Ex.
Listan inköp ser ut så här: ["bröd", "ägg", "mjök"] Om vi kallar listan inköp, kan man skriva ut hela listan med att skriva: skriv ($inköp) Då skulle man se hela listan men om du vill få ut en skild sak från listan måste du specifiera sakens indexnummer. Varje sak i listan har ett eget indexnummer. 'bröd' skulle ha indexen 0 eftersom 'bröd' är den första saken i listan och listor börjar från 0 inte 1!

## OBS Indexnummer!
### Kom ihåg att listor alltid börjar med 0 och inte 1

### Gör en ny lista
var inköp = ["bröd", "ägg", "mjölk"]

## Andra Listfunktioner
Du kan se hur man andväder listor med variabler under Variabel sektionen av dokumentationen, här är bara de specifika funktionerna som bara listor har!

### Lägg Till Sak
$inköp.till("smör")

### Ta Bort Sak Från Lista
$inköp.bort[2]

# Matte ()
Matte () funktionen kan andvändas själv eller sättas in i variabler. Matte () funktionen tar in två tal i antigen nummerform (heltal) eller nummervariabelform samt ett utryck (+, -, *, /, %).

### Addition
matte (1+2)

## Andra Räknesätt
Du kan kombinera variabler med nummer så här: (1+2) eller ($num1+$num2) eller (1+$num1) eller ($num2+3).

### Subtraktion
matte (1-2)

### Multiplikation
matte (1*2)

### Division
matte (1/2)

### Moduloräkning
matte (1%2)

# Om () & Annars ()
Om () och Annars () går hand i hand och fungerar tillsammans. Om () låter dig testa olika saker. Du kan t.ex. kolla om en variabel är lika med en annan variabel, om ett nummer är större en ett annat nummer osv. Om uttrycket i Om () stämmer körs koden innuti Om () parenteserna {} medan koden innuti Annars () pareneteser {} körs bara om uttrycket i Om () är falsk/inte stämmer. Du kan bara andvända Annars () om du ocskå andvänder Om (), men du kan andvända Om () ensamt. 
Här är några exempel på hur du andvänder Om () och Annars ():

### Kolla om ett tal är störe än ett annant:
var num1 = 2
var num2 = 4
om ($num1 > $num2) {
    skriv ("Större än!")
}
annars {
    skriv ("Inte större än!")
}
                                            
### Utput:
Inte större än!


### Kolla vad advändaren skrev
var namn = in ("Skriv Ditt Namn: ")
om ($namn = "Jonas") {
    skriv ("Hej Jonas")
}
                                            
### Utput:
Skriv Ditt Namn: Jonas
Hej Jonas
                                                    

## Uttryck
Du kan andvända dig av några oika uttryck i Om ().

### Uttryck	Beskrivnng
* =	Lika med/samma

* !	Inte lika med/olika

* \<	Mindre än (bara nummer)

* \>	Större än (bara nummer)

# Kommentarer
Kommentarer är linjer i din kod som ignoreras när koden körs. Detta är praktiskt om du vill organisera din kod och göra den enklare att förstå med hjälp av förklaringar, titlar mm. Alla linjer som börjar med # är en kommentar.

### Ex.
skriv ("Hej Världen!")
\# Detta är en kommentar
\# skriv ("hej")
skriv ("Test 123...")

### Utput
Hej Världen!
Test 123...
                                        
# Töm
Töm kommandot tömmer konsolen (Terminal, Kommandotolken). Detta kan vara praktiskt om din kod behöver visa mycket information.

### Ex.
skriv ("Hej Världen!")
töm
skriv ("Test")

### Utput
Test
                                        
