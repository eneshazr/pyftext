[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9.2](https://img.shields.io/badge/python-3.9.2-yellow.svg)](https://www.python.org/downloads/release/python-392/)

**Description :**

The pyftext module converts your words to Ascii. You can draw Pyramid shapes at any height you want.


**Installation :**

`pip install pyftext`



## How to Use
**Pyramid Arguments :**
```
Piramit(karakter, height, yazi)
karakter	The character to use when creating the shape.
height		Height of the Pyramid
yazi		  Writing in the middle of the created Pyramid
------
full_pyramid()	Full Pyramid
half()		      Half Pyramid 
double()	      Double Half Pyramid

```
**Text Arguments :**
```
Text(text, karakter, fontsize)
text		  The text you want to be created
karakter	Character to use when creating the shape
fontsize	Size of the figure (Default 15)
------
yaz()		  Writes text to the screen
rastgele()	Random font assignment
```


## Examples
**Random Text**
```python
from pyftext import Text

metin = Text(text="YAZILIM  FURYASI", karakter='@', fontsize=10)
metin.rastgele()
```
OUTPUT:
```
    @   @   @@@@@@ @  @    @  @@     @        @@@@ @   @  @@@  @    @   @     @@@@ @
@   @  @ @      @  @  @    @  @@@   @@        @    @   @  @  @  @   @  @ @   @     @
@@ @   @ @     @   @  @    @  @ @   @@        @    @   @  @  @  @@ @   @ @   @     @
 @ @   @ @     @   @  @    @  @ @  @ @        @    @   @  @  @   @ @   @ @    @@   @
  @   @   @   @    @  @    @  @ @@ @ @        @@@@ @   @  @@@     @   @   @     @  @
  @   @@@@@  @     @  @    @  @  @ @ @        @    @   @  @  @    @   @@@@@      @ @
  @  @     @@      @  @    @  @  @@  @        @    @   @  @  @    @  @     @ @   @ @
  @  @     @@@@@@@ @  @@@@ @  @   @  @        @     @@@   @   @   @  @     @  @@@  @
```

**Default Text**

```python
from pyftext import Text

metin = Text(text="YAZILIM  FURYASI", karakter='#',fontsize=10)
metin.yaz()
```
OUTPUT:
```
 #   #    #    ####  #  #     #  #     #        ####  #   #  ####   #   #    #     ###   #
 #   #   # #      #  #  #     #  ##   ##        #     #   #  #   #  #   #   # #   #   #  #
  # #    # #     #   #  #     #  ##   ##        #     #   #  #   #   # #    # #   #      #
   #    #   #   #    #  #     #  # # # #        ####  #   #  ####     #    #   #   ###   #
   #    #####   #    #  #     #  # # # #        #     #   #  #  #     #    #####      #  #
   #    #   #  #     #  #     #  #  #  #        #     #   #  #  #     #    #   #  #   #  #
   #   #     # ####  #  ####  #  #  #  #        #      ###   #   #    #   #     #  ###   #
```

**Pyramids**
```python
from pyftext import Piramit

piramit = Piramit(karakter="#", height=10)
piramit.full_pyramid()
piramit.double()
piramit.half()
```

OUTPUT:
```
         #
        ###        
       #####       
      #######      
     #########     
    ###########    
   #############   
  ###############  
 ################# 
###################
         #  #      
        ##  ##     
       ###  ###    
      ####  ####   
     #####  #####  
    ######  ###### 
   #######  #######
  ########  ########
 #########  #########
##########  ##########
         #
        ##
       ###
      ####
     #####
    ######
   #######
  ########
 #########
##########
```
