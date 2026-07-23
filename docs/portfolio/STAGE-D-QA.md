# Aşama D — Portfolyo İçerik Kalite Kaydı

> Doğrulama tarihi: 23 Temmuz 2026  
> İlgili görevler: D-01–D-06  
> Sonuç: Geçti  
> Yayın durumu: Yalnızca yerel kaynak güncellendi; canlı deployment yapılmadı

## Uygulanan içerik kararları

- Hero başlığı `Software Developer • Founder of ZyInnova` olarak eşitlendi.
- Uzun profesyonel başlık
  `Full-Stack Software Developer | Founder, ZyInnova` olarak kullanıldı.
- About ve Resume özetleri doğrulanmış İngilizce CV içeriğiyle eşitlendi.
- ZyInnova, kurucu tarafından yönetilen üst ürün ve çalışma çatısı olarak
  anlatıldı.
- Deneyim bölümü güncel ZyInnova rolüne ek olarak kullanıcı tarafından
  belgelendiği teyit edilen Roseance Oy, Sisustusklinikka.fi, Wise Quarter ve
  Turkish National Police kayıtlarını `Earlier Experience` altında içeriyor.
- TechPro Education kaydı iş deneyimi yerine `Additional Training` altında
  gösteriliyor.
- Eski deneyim açıklamaları rol ve tarih düzeyinde tutuldu; doğrulanmamış
  teknoloji, ayrıntılı sorumluluk ve sonuç iddiası eklenmedi.
- Kişisel LinkedIn profili korunmaktadır. Kullanıcının doğruladığı
  `https://www.linkedin.com/company/zyinnova/` adresi şirket bağlantısı olarak
  hero, iletişim alanı ve ZyInnova yapılandırılmış verisine ayrıca eklendi.
- Hero'daki kanonik unvan sabit tutuldu; Typed.js hareketi doğrulanmış odak
  alanlarını gösteren ikinci satırda yeniden etkinleştirildi.
- KEUDA kaydı 2025 mezuniyeti ve `Software Developer` tutkintonimikesiyle
  düzeltildi; Metropolia kaydı yayımlanmadı.
- Dil seviyeleri Turkish Native, English B2 ve Finnish B2 olarak eşitlendi.
- LemmikkiLife hem Resume hem Projects bölümünde ilk sıraya alındı ve
  `In development` olarak sınırlandırıldı.
- Todo App `Public prototype`, Founder Portfolio `Live` olarak gösterildi.
- GameScan teknoloji etiketleri ve iki yer tutucu proje kartı kaldırıldı.

## CV yayın kontrolü

- İngilizce PDF:
  `assets/cv/Ziyaaddin_Yaramis_CV_EN.pdf`
- Fince PDF:
  `assets/cv/Ziyaaddin_Yaramis_CV_FI.pdf`
- Her iki dosya üst menü, Resume bölümü ve footer içinde ayrı dil seçeneğiyle
  bağlantılıdır.
- İngilizce arayüzdeki indirme etiketi `Finnish CV` olarak düzeltildi.
- Web varlıklarındaki PDF SHA-256 değerleri doğrulanmış `output/pdf`
  dosyalarıyla aynıdır.
- Eski `assets/cv/MyResume-Ziyaaddin-Yaramis.pdf` dosyası ve tüm aktif HTML
  bağlantıları kaldırıldı.
- Eski dosyanın Git geçmişi ve canlı sunucudaki mevcut kopyası H-06/H-09
  görevlerinde ayrıca ele alınacaktır.

## Otomatik kontrol

`scripts/audit_stage_d.py` aşağıdaki maddeleri doğruladı:

- HTML ayrıştırma hatası bulunmuyor.
- Başlık, hero, About, Resume ve yapılandırılmış veri kanonik değerleri taşıyor.
- KEUDA, dil, güncel ve önceki deneyim, ek eğitim, beceri ve proje kayıtları
  doğrulanmış kapsamla eşleşiyor.
- LemmikkiLife seçili projelerde ilk sırada.
- Eski unvanlar, yanlış tarihler, doğrulanmamış sorumluluk/teknoloji iddiaları,
  konum ve eski PDF bağlantısı bulunmuyor.
- İki CV bağlantısı üç ayrı arayüz noktasında bulunuyor.
- Yerel görsel, stil, script ve PDF bağlantılarının tamamı mevcut.
- HTML kimlikleri benzersiz ve tüm görsellerin `alt` metni var.

## Tarayıcı kontrolü

| Kontrol | Sonuç |
|---|---|
| Masaüstü görünüm | 1440 × 900, yatay taşma yok |
| Mobil görünüm | 390 × 844, yatay taşma yok |
| Hero başlığı | Görünür ve mobilde güvenli biçimde satır kırıyor |
| Hero animasyonu | Typed.js metni doğrulanmış üç odak alanı arasında değişiyor |
| LinkedIn bağlantıları | Kişisel profil ve ZyInnova şirket sayfası ayrı etiketli |
| Resume iki sütun | Masaüstünde dengeli; mobilde tek sütuna dönüyor |
| Mobil menü | Açılıyor, Resume bağlantısı çalışıyor ve seçimden sonra kapanıyor |
| İngilizce PDF | Yerel URL doğrudan açıldı |
| Fince PDF | Yerel URL doğrudan açıldı |
| Konsol | Hata veya uyarı yok |

## Kapsam sınırı

Bu aşamada canlı siteye commit, push veya deployment yapılmadı. Aşama E,
proje kanıtlarını ve proje kartlarının görsel/teknik kalitesini daha ayrıntılı
ele alacaktır. Aşama F ve G erişilebilirlik, performans, güvenlik ve SEO
denetimlerini tamamlayacaktır.
