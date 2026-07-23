# Aşama E — Proje Portfolyosu Kalite Kaydı

> Doğrulama tarihi: 23 Temmuz 2026  
> İlgili görevler: E-01–E-07  
> Sonuç: Geçti  
> Yayın durumu: Yerel kaynak güncellendi; canlı deployment yapılmadı

## Proje kararları

| Proje | Doğrulanan durum | Portfolyo kararı |
|---|---|---|
| LemmikkiLife | ZyInnova listesinde geliştirme aşamasında; detaylar ve proje deposu özel/kapalı | İlk kart; teknoloji ve tamamlanmış özellik iddiası olmadan `In Development` |
| GameScan | ZyInnova listesinde ve ZyInnova GitHub profilinde aktif geliştirme projesi; proje deposu özel/kapalı | Özel ürün amacıyla kart; teknoloji yığını yayımlanmaz |
| Multi-language Todo App | Açık Flutter reposu; Firebase Auth, Firestore, EN/FI yerelleştirme ve bildirim bağımlılıkları doğrulandı | `Public Prototype`; doğrudan repo bağlantısı |
| Founder Portfolio | Yerel kaynak, açık repo ve canlı adres doğrulandı | `Live`; HTML, CSS ve JavaScript kapsamı |
| Movie Explorer | Açık işbirliği reposu; kod kapsamından geniş README iddiaları ve kişisel Gmail içeriyor | Ana seçkiye alınmadı; H-07 temizliği bekliyor |
| Zikirmatik | README tarafından tutorial/learning exercise olarak tanımlanıyor | Ana seçkiye alınmadı |

## ZyInnova katkı sınırı

Kullanıcı teyidine göre ZyInnova, kurucu tarafından yönetilen ürün çatısıdır.
ZyInnova'nın ayrı GitHub organizasyonu <https://github.com/zyinnova> olarak
doğrulandı. Organizasyon dışarıdan iki açık depo (`zyinnova` ve `.github`)
göstermekte; kullanıcı teyidine göre bazı ürün depoları organizasyon altında
özel tutulmaktadır. Canlı site dokuz proje/ürün kaydı yayımlamaktadır. Özel
proje kodları ve kişisel commit kapsamı dışarıdan erişilebilir olmadığından,
GameScan ve LemmikkiLife için kişisel teknoloji, tamamlanmış özellik veya sonuç
iddiası kullanılmaz.

## Görsel sistemi

- LemmikkiLife ve GameScan için ZyInnova proje listesindeki resmî konsept
  kapakları kullanıldı.
- Kapaklar 1280 × 720 WebP biçiminde ve sırasıyla yaklaşık 88 KB ve 32 KB'dir.
- Todo ve Founder Portfolio için 1280 × 720, kod tabanlı SVG illüstrasyonlar
  hazırlandı.
- Her görselde boyut, açıklayıcı `alt`, lazy loading ve konsept/illüstrasyon
  niteliğini açıklayan figcaption bulunur.

## Arayüz ve içerik

- Seçki sırası: LemmikkiLife, GameScan, Multi-language Todo App, Founder
  Portfolio.
- Yer tutucu kartlar bulunmaz.
- Movie Explorer, Zikirmatik ve tutorial oyunlar seçilmiş ürün çalışması olarak
  gösterilmez.
- Hero Typed.js zamanlaması `typeSpeed: 55`, `backSpeed: 70` ve
  `backDelay: 650` olarak hızlandırıldı.

## Otomatik kontrol

`scripts/audit_stage_e.py` aşağıdaki maddeleri doğrular:

- Dört kartın sırası, durumu ve kanıt sınırları.
- GameScan ve LemmikkiLife kartlarında kanıtsız teknoloji bulunmaması.
- Todo ve Founder Portfolio teknoloji/kapsam eşleşmesi.
- Kişisel GitHub ile ZyInnova organizasyon GitHub bağlantılarının ayrı sunulması.
- Yer tutucu, tutorial ve işbirliği projelerinin ana seçkide bulunmaması.
- Doğrudan proje/repo bağlantıları.
- Dört görselin varlığı, boyutları, dosya bütçeleri, `alt` ve lazy-loading
  özellikleri.
- Hızlandırılmış hero animasyon ayarları.

## Kapsam sınırı

Bu aşama GitHub README temizliği, özel repo yayımlama, canlı deployment veya
ZyInnova ürünlerinin teknik uygulamasını doğrulama işlemi yapmaz. Bunlar kanıt
ve yayın kararı gerektiren H aşaması veya ayrı ürün görevleridir.
