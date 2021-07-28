from PIL import Image, ImageFont, ImageDraw
import random

class Piramit():
    def __init__(self, karakter, height, yazi=None):
        self.karakter = karakter
        self.height = height

        if yazi is None: self.yazi = ""
        else: self.yazi = str(yazi)

    def full_pyramid(self):
        if self.height < 5 or self.height > 100:
            return print("Yükseklik minimum 5, maksimum 100 olmalıdır.\n")

        bol = self.height / 2
        for i in range(self.height):
            if self.yazi and i == int(bol):
                print(' '*(self.height-i-1)+str(self.yazi))
            print(' '*(self.height-i-1) + self.karakter*(2*i+1))

    def half(self):
        if self.height < 5 or self.height >= 100:
            return print("Yükseklik minimum 5, maksimum 100 olmalıdır.\n")
        
        bol = self.height / 2
        for i in range(self.height):
            if self.yazi and i == int(bol):
                print(' '*(self.height-i-1)+str(self.yazi))
            print(' '*(self.height-i-1) + self.karakter*(1*i+1))

    def double(self):
        if self.height < 5 or self.height >= 100:
            return print("Yükseklik minimum 5, maksimum 100 olmalıdır.\n")

        bol = self.height / 2
        for i in range(self.height):
            if self.yazi and i == int(bol):
                print(' '*(self.height-i-1)+str(self.yazi))
            print(' '*(self.height-i-1) + self.karakter*(1*i+1),end="")
            print(' ',self.karakter*(1*i+1))


class Text():
    def __init__(self, text, karakter=None, fontsize=None):
        self.metin = str(text)
        self.karakter = karakter

        if fontsize is None:
            self.fontsize = 15
        else:
            self.fontsize = fontsize

    def yaz(self):
        if self.karakter is None:
            self.karakter = "#"
        if self.fontsize < 9 or self.fontsize > 100:
            return print("fontsize minimum 9, maksimum 100 olmalıdır.")

        font = ImageFont.truetype("arialbd.ttf", self.fontsize)
        size = font.getsize(self.metin)
        image = Image.new('1', size, 4)
        draw = ImageDraw.Draw(image)
        draw.text((0, 0), self.metin, font=font)
        for row in range(size[1]): 

            line = []
            for col in range(size[0]):
                if image.getpixel((col, row)): line.append(' '),
                else: line.append(self.karakter),
            print(''.join(line))
            
    def rastgele(self):
        if self.fontsize < 9 or self.fontsize > 100:
            return print("fontsize minimum 9, maksimum 100 olmalıdır.")

        liste = ['arial.ttf', 'arial.ttf', 'arial.ttf', 'ariali.ttf', 'arialbd.ttf', 'arialbi.ttf', 'ariblk.ttf', 'bahnschrift.ttf', 'calibril.ttf', 'calibrili.ttf', 'calibri.ttf', 'calibrii.ttf', 'calibrib.ttf', 'calibriz.ttf', 'cambria.ttc', 'cambriai.ttf', 'cambriab.ttf', 'cambriaz.ttf', 'cambria.ttc', 'comic.ttf', 'comici.ttf', 'comicbd.ttf', 'comicz.ttf', 'consola.ttf', 'consolai.ttf', 'consolab.ttf', 'consolaz.ttf', 'constan.ttf', 'constani.ttf', 'constanb.ttf', 'constanz.ttf', 'corbell.ttf', 'corbelli.ttf', 'corbel.ttf', 'corbeli.ttf', 'corbelb.ttf', 'corbelz.ttf', 'cour.ttf', 'couri.ttf', 'courbd.ttf', 'courbi.ttf', 'ebrima.ttf', 'ebrimabd.ttf', 'framd.ttf', 'framdit.ttf', 'gadugi.ttf', 'gadugib.ttf', 'georgia.ttf', 'georgiai.ttf', 'georgiab.ttf', 'georgiaz.ttf', 'impact.ttf', 'javatext.ttf', 'lucon.ttf', 'l_10646.ttf', 'malgun.ttf', 'malgunbd.ttf', 'malgunsl.ttf', 'msjhl.ttc', 'msjh.ttc', 'msjhbd.ttc', 'msjhl.ttc', 'msjh.ttc', 'msjhbd.ttc', 'ntailu.ttf', 'ntailub.ttf', 'phagspa.ttf', 'phagspab.ttf', 'micross.ttf', 'taile.ttf', 'taileb.ttf', 'msyhl.ttc', 'msyh.ttc', 'msyhbd.ttc', 'msyhl.ttc', 'msyh.ttc', 'msyhbd.ttc', 'mvboli.ttf', 'mmrtext.ttf', 'mmrtextb.ttf', 'pala.ttf', 'palai.ttf', 'palab.ttf', 'palabi.ttf', 'segoepr.ttf', 'segoeprb.ttf', 'segoesc.ttf', 'segoescb.ttf', 'segoeuil.ttf', 'seguili.ttf', 'segoeuisl.ttf', 'seguisli.ttf', 'segoeui.ttf', 'segoeuii.ttf', 'seguisb.ttf', 'seguisbi.ttf', 'segoeuib.ttf', 'segoeuiz.ttf', 'seguibl.ttf', 'seguibli.ttf', 'seguihis.ttf', 'seguiemj.ttf', 'seguisym.ttf', 'sylfaen.ttf', 'tahoma.ttf', 'tahomabd.ttf', 'times.ttf', 'timesi.ttf', 'timesbd.ttf', 'timesbi.ttf', 'trebuc.ttf', 'trebucit.ttf', 'trebucbd.ttf', 'trebucbi.ttf', 'verdana.ttf', 'verdanai.ttf', 'verdanab.ttf', 'verdanaz.ttf']
        sss = random.choice(liste)
        # print("Font: "+ sss)

        rkarakter = ["#", "@", ".","!","'","|","$","+"]
        character = random.choice(rkarakter)
        
        font = ImageFont.truetype(sss, self.fontsize)
        size = font.getsize(self.metin)
        image = Image.new('1', size, 4)
        draw = ImageDraw.Draw(image)
        draw.text((0, 0), self.metin, font=font)
        for row in range(size[1]): 

            line = []
            for col in range(size[0]):
                if image.getpixel((col, row)): line.append(' '),
                else: line.append(character),
            print(''.join(line))