# **Basit Discord Bot**
Bu bir temel Discord botudur. slash(/), prefix komutları ve aktiviteler içerir.

### Kurulum
- Ana dizine ***ayarlar.py*** dosyası oluşturun.
>ayarlar.py
```py
ayarlar = {
    "on_taki": ">", #ön takı, prefix (maybe it won't work if we call it different here)
    "TOKEN": "TOKEN",
    "game": "Bir şey"
}

#Bot gelişticilerinin listesi:
DEVELOPERS_IDS = [AUTHOR IDS] #Geliştiricilerin Discord idleri. (yalnızca Int değer)
```
- Gerekli kütüpahaneleri kuralım:
```bash
pip install discord.py
pip install discord
pip install random
pip install time
```
- Botu Discord'a ekle. [Discord Developer Portal](https://discord.com/developers)
- Botu sunucunuza davet edin.
- Botu çalıştırın.

## **ÖNEMLİ**
- Botunuzun tokenini asla paylaşımayın.
- [Burada](main.py) 28. satırda botu deneyeceğiniz sunucun İD yi koyuyorsunuz. Çünkü bu bir test botudur.