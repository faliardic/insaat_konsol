# İnşaat Konsol Projesi

Python öğrenme sürecinde geliştirilen, menü tabanlı modüler bir konsol uygulaması.
İnşaat mühendisliği ile ilgili basit hesaplama ve kontrol araçlarını, ayrıca
küçük yardımcı/eğlence modüllerini bir araya getirir.

Bu bir **eğitim / portföy projesidir**; production amaçlı kullanılmaz ve
geliştirme aşamasındadır.

## Çalıştırma

```bash
python main.py
```

Program açıldığında ana menüden bir bölüm seçilir; her bölümün kendi alt
menüsü vardır (`0` ile bir üst menüye dönülür).

## Modül yapısı

| Dosya | Açıklama |
|---|---|
| `main.py` | Ana menü ve program giriş noktası |
| `hesaplamalar.py` | Atalet momenti, beton/donatı metrajı, deprem spektrumu gibi hesaplama modülleri |
| `statik_rehber.py` | Minimum eleman boyutu, temel, gövde/kolon donatısı gibi statik kontrol adımları için rehber menüsü |
| `oyunlar.py` | Küçük yardımcı/eğlence modülleri (ör. bilgi yarışması) |

## Durum

Modüllerin çoğu iskelet/placeholder aşamasındadır ve zamanla genişletilecektir.
