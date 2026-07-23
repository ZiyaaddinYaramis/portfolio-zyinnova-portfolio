# Yüzeyler Arası Düzeltme Matrisi

> Kayıt tarihi: 23 Temmuz 2026  
> İlgili görev: A-04  
> Kanonik kaynak:
> [`PROFESSIONAL-PROFILE-SOURCE.md`](PROFESSIONAL-PROFILE-SOURCE.md)

## 1. Amaç

Bu belge; aktif portfolyo, indirilebilir mevcut CV, GitHub profili/repoları,
eski GitHub Pages yayını ve kanonik profesyonel bilgi kaynağı arasındaki
farkları tek uygulama listesinde toplar.

Matristeki `Mevcut` ifadeleri doğru kabul edilmez. Uygulama sırasında
`Hedef` sütunu ve kanonik ana kaynak esas alınır. Hassas kişisel değerler bu
belgeye kopyalanmaz.

## 2. Öncelik tanımları

| Öncelik | Anlamı |
|---|---|
| `P0` | Açık kişisel veri, yanlış eğitim kaydı veya aktif eski yayın gibi hemen ele alınacak risk |
| `P1` | Profesyonel kimlik, tarih, dil, kurum veya deneyim çelişkisi |
| `P2` | Proje, teknoloji, katkı ve durum iddiası |
| `P3` | Dokümantasyon, SEO, erişilebilirlik veya sunum iddiası |

## 3. Gizlilik ve eski yayın

| Kimlik | Öncelik | Yüzey ve mevcut durum | Hedef düzeltme | Görev |
|---|---|---|---|---|
| `FIX-PRIV-001` | `P0` | `ziyaaddinyaramis.github.io` arşiv reposuna rağmen hâlâ canlıdır; doğum bilgisi, açık adres, telefon ve kişisel Gmail yayımlar | GitHub Pages yayını kapatılır ve eski adresin artık kişisel veri sunmadığı doğrulanır | H-06 |
| `FIX-PRIV-002` | `P0` | Arşiv repo herkese açık kaldığı için yayını kapatmak kaynak dosyalardaki kişisel veriyi tek başına gizlemez | Yerel arşiv korunarak GitHub reposu private yapılır veya kamuya açık kaynak hassas verilerden temizlenir; kullanıcı onayıyla uygulanır | H-06 |
| `FIX-PRIV-003` | `P0` | Aktif portfolyodan indirilen mevcut PDF açık adres, telefon, kişisel Gmail ve fotoğraf içerir | Doğrulanmış İngilizce ve Fince PDF'ler tamamlanınca eski genel indirme kaldırılır | B-04–B-06, C-04–C-05, D-05–D-06 |
| `FIX-PRIV-004` | `P0` | Movie Explorer README'si kişisel Gmail adresi içerir | Adres kaldırılır; gerekiyorsa `contact@zyinnova.com` kullanılır | H-07 |

Eski yayın: <https://ziyaaddinyaramis.github.io/>  
Arşiv repo:
<https://github.com/ZiyaaddinYaramis/ZiyaaddinYaramis.github.io>

## 4. Profesyonel kimlik ve iletişim

| Kimlik | Öncelik | Yüzey ve mevcut durum | Hedef düzeltme | Görev |
|---|---|---|---|---|
| `FIX-ID-001` | `P1` | Site title, metadata, hero ve footer `Founder & Full-Stack Developer`, `Product Builder`, `Startup Founder` gibi farklı başlıklar kullanır | Site başlığı `Software Developer • Founder of ZyInnova`; uzun profesyonel başlık `Full-Stack Software Developer \| Founder, ZyInnova` olur | D-01, G-05 |
| `FIX-ID-002` | `P1` | Mevcut PDF `Full Stack Developer (Java & Flutter) \| Web & Mobile Applications` başlığını kullanır | Kanonik uzun başlık kullanılır; teknoloji adları unvanın yerine geçirilmez | B-01, C-01 |
| `FIX-ID-003` | `P1` | GitHub profil README'si `Founder & Full-Stack Developer at ZyInnova` ile başlar; hesap bio'su kurucu rolünü tutarlı taşımıyor | Başlık ve bio kanonik sıraya alınır: önce yazılım geliştiriciliği, sonra ZyInnova kuruculuğu | H-05 |
| `FIX-ID-004` | `P1` | Site `Lead Developer`, `production-ready`, `real/scalable products` ve tam ürün yaşam döngüsü gibi kanıtsız olgunluk iddiaları kullanır | `Founder & Software Developer`; yalnızca doğrulanmış geliştirme ve ürün sahipliği ifadeleri kullanılır | D-01, D-04, G-05 |
| `FIX-ID-005` | `P1` | Site, PDF ve GitHub Kerava konumunu yayımlar; kanonik kayıtta kamuya açık konum henüz teyit edilmemiştir | Kullanıcı teyidine kadar yeni CV'lere ve yenilenen metadata'ya konum eklenmez | B-01, D-01, H-05 |
| `FIX-ID-006` | `P1` | Aktif sitede kurumsal e-posta doğru olsa da eski yüzeyler kişisel Gmail kullanır | Tüm genel yüzeylerde yalnızca `contact@zyinnova.com` kullanılır | D-01, H-05–H-07 |

## 5. Eğitim, dil ve deneyim

| Kimlik | Öncelik | Yüzey ve mevcut durum | Hedef düzeltme | Görev |
|---|---|---|---|---|
| `FIX-FACT-001` | `P0` | Eski GitHub Pages Metropolia öğrenciliğini ve beklenen 2025 başlangıcını/ilerlemesini yayımlar | Metropolia kaydı tüm genel yüzeylerden kaldırılır; yalnızca özel kariyer notunda kalır | H-06 |
| `FIX-FACT-002` | `P1` | Aktif site KEUDA'yı `2023–Present` gösterir; PDF 2025 mezuniyetini gösterir | Mezuniyet 2025 kullanılır; başlangıç tarihi diploma görülmeden eklenmez | D-02, B-01, C-01 |
| `FIX-FACT-003` | `P1` | Site İngilizceyi `Professional working level`, Finceyi `Developing` gösterir | Turkish Native, English B2, Finnish B2 | D-03 |
| `FIX-FACT-004` | `P1` | Site `Founder & Lead Developer — ZyInnova`, PDF `Founder & Developer`; ikisi de 2024 başlangıcı verir | Rol `Founder & Software Developer`; başlangıç tarihi ek kanıt gelene kadar kesinleştirilmez | D-04, B-01 |
| `FIX-FACT-005` | `P1` | `Wisequarter`, `Techproed` ve `Sisustuskliniikka/Sisustusklinikka` yazımları yüzeyler arasında değişir | `Wise Quarter` ve `TechPro Education` kullanılır; Sisustusklinikka yazımı belge bekler | B-01, D-01 |
| `FIX-FACT-006` | `P1` | TechPro kaydı site ve PDF'de iş deneyimi akışındadır | Tamamlanma belgesi gelirse mesleki eğitim bölümüne taşınır | B-01, C-01, D-01 |
| `FIX-FACT-007` | `P1` | Roseance, Sisustusklinikka, Wise Quarter ve Turkish National Police kişisel rol/tarihleri mevcut yüzeylerde kesin ifade edilir | Belgelenmemiş ayrıntılar yeni CV/site metnine kesin iddia olarak taşınmaz | B-01–B-02, D-01 |

## 6. Projeler

| Kimlik | Öncelik | Yüzey ve mevcut durum | Hedef düzeltme | Görev |
|---|---|---|---|---|
| `FIX-PROJ-001` | `P2` | LemmikkiLife aktif portfolyo, mevcut CV ve GitHub seçkisinde yoktur | Öncelikli ZyInnova ürünü olarak `In development` statüsüyle öne çıkarılır; kamuya açık ürün amacı kullanılabilir, kod/sonuç iddiası kanıt bekler | E-02, E-06, H-05 |
| `FIX-PROJ-002` | `P2` | Site GameScan için Flutter/Firebase; ZyInnova listesi React/Vite der | Erişilebilir kod gelene kadar teknoloji etiketi kaldırılır; yalnızca private/in-development ürün amacı yayımlanır | E-01, E-06 |
| `FIX-PROJ-003` | `P2` | Todo App sitede `Live` görünür ve yalnızca genel GitHub profiline bağlanır | `Public prototype` kullanılır ve doğrudan genel repo bağlantısı verilir; EN/FI desteği açık yazılır | E-04, E-06 |
| `FIX-PROJ-004` | `P2` | PDF Todo için Turkish/English/Finnish ve MVVM/modüler mimari iddia eder | Kodla doğrulanan EN/FI, Firebase Auth, Firestore ve bildirim kapsamı kullanılır; TR/MVVM iddiası kanıt bekler | B-03, H-07 |
| `FIX-PROJ-005` | `P2` | Movie Explorer README/PDF/GitHub seçkisi çok dillilik, favoriler ve daha geniş ürün kapsamı ima eder | Yalnızca TMDB popüler film listeleme prototipi ve işbirliği niteliği kullanılır; kişisel katkı ayrıca belirlenir | B-03, E-04, H-05, H-07 |
| `FIX-PROJ-006` | `P2` | PDF Zikirmatik'te titreşim geri bildirimi iddia eder ve tutorial niteliğini söylemez | Seçilmiş portfolyodan çıkarılır veya açıkça tutorial/learning exercise olarak etiketlenir; titreşim iddiası kaldırılır | B-03, E-04, H-05 |
| `FIX-PROJ-007` | `P2` | PDF/eski site klasik oyunları özgün geliştirme gibi sunar | Seçilmiş ürün portfolyosundan çıkarılır; kalırsa tutorial kaynağı açıkça belirtilir | B-03, E-06 |
| `FIX-PROJ-008` | `P2` | Aktif sitede `Next ZyInnova Product` ve `Studio Template System` yer tutucuları yayımlanır | İki kart kaldırılır | E-05 |
| `FIX-PROJ-009` | `P2` | Eski GitHub Pages doğrulanmamış Weather App'i gerçek proje olarak sunar | Kanıt bulunmadıkça yeni seçkiye alınmaz | H-06 |
| `FIX-PROJ-010` | `P2` | Mevcut PDF aktif portfolyonun GitHub Pages üzerinde barındırıldığını söyler; repo README'si Hostinger der | Kanonik canlı adres verilir; barındırma ayrıntısı CV'den çıkarılır | B-03 |
| `FIX-PROJ-011` | `P2` | Site bütün kartları `Founder-built` olarak gruplar; kişisel katkı sınırları belgelenmemiştir | ZyInnova ürünleri, kişisel prototipler ve işbirliği/öğrenme çalışmaları ayrı sınıflandırılır | D-04, E-06 |

LemmikkiLife kayıtları:

- Liste: <https://zyinnova.com/projects>
- Kapalı detay: <https://zyinnova.com/projects/lemmikkilife>

## 7. Teknik yetkinlik ve kalite iddiaları

| Kimlik | Öncelik | Yüzey ve mevcut durum | Hedef düzeltme | Görev |
|---|---|---|---|---|
| `FIX-SKILL-001` | `P2` | Site, PDF ve GitHub; Java/Spring, React/Vite/Tailwind, Python, C#, SQL/MySQL/SQLite, WordPress ve mimari kalıpları tek düzeyde listeler | Projeyle doğrulanan teknolojiler proje bağlamıyla; diğerleri belge gelirse `coursework/foundational` olarak kullanılır | B-01–B-03, D-01, H-05 |
| `FIX-SKILL-002` | `P2` | PDF yüzdeli/uzmanlık benzeri yoğun beceri sunumu yapar; eski site yüzde seviyeleri yayımlar | Yüzde, `advanced`, `expert` ve kanıtsız seviye nitelemesi kullanılmaz | B-01, C-01, H-06 |
| `FIX-SKILL-003` | `P2` | GitHub README ve site `production`, maintainable architecture, accessibility ve performance çalışmalarını genel sonuç gibi sunar | Yalnızca test veya proje kanıtıyla desteklenen ifadeler tutulur | D-01, F-01–F-05, G-01–G-06, H-05 |
| `FIX-QUAL-001` | `P3` | README siteyi `production-ready`, erişilebilir, performans için optimize ve SEO-ready ilan eder; doğrulama görevleri henüz tamamlanmadı | Kalite iddiaları testlerden sonra ölçülü sonuçlarla yazılır | F-01–F-05, G-01–G-06, H-01 |
| `FIX-QUAL-002` | `P3` | HTML'de fazladan kapanış etiketi ve yinelenen `Projects` başlığı bulunur | HTML doğrulanır ve yinelenen/bozuk yapı temizlenir | F-01, G-05 |
| `FIX-QUAL-003` | `P3` | Mobil menü gerçek button değildir; buna rağmen README klavye erişilebilirliği iddia eder | Menü ve durum yönetimi düzeltildikten sonra erişilebilirlik iddiası yeniden değerlendirilir | F-01–F-04 |

## 8. CV ve GitHub sunumu

| Kimlik | Öncelik | Yüzey ve mevcut durum | Hedef düzeltme | Görev |
|---|---|---|---|---|
| `FIX-PUB-001` | `P1` | Site tek, dili belirsiz `CV`/`Download CV` bağlantısı sunar | `Download CV — English` ve `Lataa CV — Suomi` seçenekleri eklenir | D-05 |
| `FIX-PUB-002` | `P2` | GitHub profil README'si Zikirmatik ve henüz temizlenmemiş Movie Explorer'ı seçilmiş iş olarak gösterir; LemmikkiLife yoktur | Seçki kanonik proje kararına göre yeniden sıralanır; LemmikkiLife öncelikli ürün olarak eklenir | H-05 |
| `FIX-PUB-003` | `P2` | GitHub pinleri arşivlenmiş eski Pages reposu ve ağırlıklı eğitim repolarını öne çıkarır | Eski repo unpin edilir; güncel portfolyo ve doğrulanmış proje repoları pinlenir | H-05–H-06 |
| `FIX-PUB-004` | `P3` | GitHub profil README'si yeni konumlandırmaya yaklaşmış olsa da başlık, beceri ve proje kapsamı kanonik kaynakla tam eşleşmez | Profil README'si ana kaynaktan yeniden üretilir ve profil görünümü tekrar doğrulanır | H-05 |

GitHub profil README'sinin doğrudan repo kaydı 23 Temmuz 2026 tarihinde
kontrol edilmiştir:
<https://github.com/ZiyaaddinYaramis/ZiyaaddinYaramis>

## 9. Uygulama sırası

1. `P0` eski yayın ve kişisel veri riskleri H-06 planıyla güvenli biçimde
   kapatılır; aktif PDF ancak yeni PDF'ler hazır olduğunda değiştirilir.
2. B ve C aşamalarında iki CV yalnızca kanonik kaynaktan üretilir.
3. D ve E aşamalarında aktif site ile proje seçkisi eşitlenir; LemmikkiLife
   öncelikli, fakat açıkça geliştirme aşamasında sunulur.
4. F ve G aşamalarında teknik kalite iddiaları test edilir.
5. H aşamasında GitHub profili, açık repo README'leri ve eski yayın temizlenir.
6. Commit, push ve deployment yalnızca kullanıcı onayından sonra yapılır.

## 10. A-04 kabul sonucu

- Tespit edilen çelişkilerin tümü kimlik, öncelik, hedef ve görevle
  eşleştirilmiştir.
- Hassas kişisel değerler belgeye kopyalanmamıştır.
- Doğrulama bekleyen bilgi yeni yayın için onaylanmış sayılmamıştır.
- LemmikkiLife'ın önceliği kullanıcı kararı olarak kaydedilmiş, teknik kapsamı
  ise kanıt düzeyinde sınırlandırılmıştır.

## 11. Aşama D uygulama sonucu

Yerel portfolyo kaynağında aşağıdaki kayıtlar 23 Temmuz 2026 tarihinde
uygulanmış ve `scripts/audit_stage_d.py` ile doğrulanmıştır:

- `FIX-PRIV-003`
- `FIX-ID-001`, `FIX-ID-004`, `FIX-ID-005`, `FIX-ID-006`
- `FIX-FACT-002`–`FIX-FACT-007`
- `FIX-PROJ-001`–`FIX-PROJ-003`, `FIX-PROJ-008`, `FIX-PROJ-011`
- `FIX-SKILL-001`
- `FIX-PUB-001`

Bu sonuç yalnızca yerel kaynak ağacı içindir. Canlı site, GitHub profili, eski
GitHub Pages yayını ve Git geçmişi ilgili H görevleri tamamlanana kadar
çözülmüş kabul edilmez.
