# Doğrulanmış Profesyonel Bilgi Ana Kaynağı

> Kayıt sürümü: 2.0  
> Son güncelleme: 23 Temmuz 2026  
> İlgili görevler: A-01–A-04, B-01–B-06, C-01–C-05, D-01–D-10, E-01–E-07  
> Kapsam: Portfolyo, İngilizce/Fince CV ve profesyonel profil yüzeyleri

## 1. Amaç ve kullanım

Bu belge, Ziyaaddin Yaramis'in kamuya açık profesyonel bilgilerinin kanonik
ana kaynağıdır. Portfolyo, CV, GitHub profili ve benzeri profesyonel yüzeylerde
birbirinden bağımsız bilgi üretilmez; içerik bu kayıttan alınır.

Bu belge yalnızca doğrulanmış veya yayın kararı verilmiş bilgileri kanonik kabul
eder. Mevcut site, eski CV ve arşiv notlarında yer alan bir ifade, burada
`Onaylı` olarak işaretlenmedikçe doğru kabul edilmez.

## 2. Durum tanımları

| Durum | Anlamı |
|---|---|
| `Onaylı` | Kullanıcı tarafından doğrudan doğrulanmış veya yayın kararı açıkça verilmiş bilgi |
| `Kısmen doğrulandı` | Kurum/terim doğrulandı; kişisel ilişki, rol veya tarih için ek kanıt gerekiyor |
| `Doğrulama bekliyor` | Mevcut kaynaklarda bulunan fakat belge, repo veya kullanıcı teyidi gereken bilgi |
| `Yayınlanmaz` | Ana kaynakta değeri tutulmayan ve kamuya açık yüzeylerden çıkarılacak bilgi |
| `Özel not` | Kariyer planlamasında bilinen fakat resmîleşmeden yayımlanmayacak bilgi |

## 3. Kaynak önceliği

Çelişki olduğunda aşağıdaki sıra kullanılır:

1. Kullanıcının doğrudan ve güncel teyidi
2. Diploma, sertifika, sözleşme veya kurum kaydı gibi resmî belge
3. Çalışan repo, commit geçmişi, canlı demo veya doğrulanabilir proje kaydı
4. Mevcut portfolyo ve CV
5. Eski proje arşivi ve sohbet devir notları

Alt sıradaki bir kaynak, üst sıradaki kaynağın kararını değiştiremez.

## 4. Kanonik kimlik ve konumlandırma

| Kimlik | Alan | Kanonik değer | Durum | Kullanım notu |
|---|---|---|---|---|
| `ID-001` | Ad soyad | Ziyaaddin Yaramis | Onaylı | Tüm profesyonel yüzeylerde aynı yazım |
| `ID-002` | Ana meslek | Software Developer | Onaylı | Mesleki kimlik kurucu rolünden önce gelir |
| `ID-003` | Ana profesyonel başlık | Full-Stack Software Developer \| Founder, ZyInnova | Onaylı | CV, GitHub ve benzeri profesyonel yüzeyler |
| `ID-004` | Portfolyo hero başlığı | Software Developer • Founder of ZyInnova | Onaylı | Portfolyo için kısa biçim |
| `ID-005` | ZyInnova deneyim rolü | Founder & Software Developer | Onaylı | İş/kurucu deneyimi başlığı |
| `ID-006` | ZyInnova tanımı | Kurucu tarafından yönetilen üst ürün ve çalışma çatısı | Onaylı | Altındaki ürünler ayrıca proje olarak gösterilir |
| `ID-007` | Kamuya açık konum | Kerava, Finland | Doğrulama bekliyor | A-02 sırasında teyit edilmeden yeni CV'ye aktarılmaz |
| `ID-008` | Fince profesyonel başlık | Ohjelmistokehittäjä \| ZyInnovan perustaja | Onaylı | Fince CV'de resmî meslek adı; yazılım geliştiriciliği kurucu rolünden önce gelir |

### Konumlandırma sınırları

- ZyInnova şirket büyüklüğü, müşteri sayısı veya ticari başarı iddialarıyla
  anlatılmaz; bu tür bilgiler ayrıca kanıtlanmadan yayımlanmaz.
- `Lead Developer`, `Startup Founder`, `Product Builder` ve
  `production-ready` ifadeleri otomatik olarak kanonik unvana eklenmez.
- Fince profesyonel başlıkta resmî meslek adı `Ohjelmistokehittäjä` kullanılır;
  kurucu rolü `ZyInnovan perustaja` biçiminde ikinci sırada yer alır.

## 5. İletişim, bağlantılar ve gizlilik

| Kimlik | Alan | Kanonik değer | Durum | Kullanım notu |
|---|---|---|---|---|
| `CONTACT-001` | Genel e-posta | `contact@zyinnova.com` | Onaylı | Site ve herkese açık CV'lerde kullanılabilir |
| `CONTACT-002` | Portfolyo | <https://portfolio.zyinnova.com/> | Onaylı | Kişisel portfolyonun kanonik adresi |
| `CONTACT-003` | ZyInnova | <https://zyinnova.com/> | Onaylı | Üst ürün/çalışma çatısı |
| `CONTACT-004` | Kişisel GitHub | <https://github.com/ZiyaaddinYaramis> | Onaylı | Profil içeriği ayrıca güncellenecek |
| `CONTACT-007` | ZyInnova GitHub organizasyonu | <https://github.com/zyinnova> | Onaylı | Şirket/ürün depolarının kurumsal kaynağı; özel depolar dışarıdan listelenmez |
| `CONTACT-005` | Kişisel LinkedIn | <https://www.linkedin.com/in/ziyaaddin-y-8768841bb/> | Onaylı | Kullanıcı 23 Temmuz 2026'da portfolyoda korunmasını istedi |
| `CONTACT-006` | ZyInnova LinkedIn şirket sayfası | <https://www.linkedin.com/company/zyinnova/> | Onaylı | Kullanıcı 23 Temmuz 2026'da doğru şirket sayfası URL'sini verdi; kişisel profilden ayrı etiketlenir |
| `PRIVACY-001` | Açık ev adresi | Değer tutulmaz | Yayınlanmaz | Site, açık repo ve genel CV'lerde kullanılmaz |
| `PRIVACY-002` | Telefon numarası | Değer tutulmaz | Yayınlanmaz | Yalnızca gerekirse özel başvuru varyantında kullanılır |
| `PRIVACY-003` | Kişisel Gmail adresi | Değer tutulmaz | Yayınlanmaz | Genel iletişim için ZyInnova e-postası kullanılır |
| `PRIVACY-004` | Doğum tarihi veya yaş | Değer tutulmaz | Yayınlanmaz | Kamuya açık profesyonel yüzeylerde kullanılmaz |
| `PRIVACY-005` | Fotoğraf | Kullanılmaz | Yayınlanmaz | Herkese açık İngilizce ve Fince CV'de bulunmaz |

Mevcut `assets/cv/MyResume-Ziyaaddin-Yaramis.pdf` dosyası açık adres, kişisel
telefon ve Gmail adresi içerir. Hassas değerler bu belgeye kopyalanmamıştır.
Eski PDF, D-06 kapsamında aktif portfolyo kaynaklarından ve çalışma ağacından
kaldırılmıştır. Git geçmişindeki ve henüz güncellenmemiş canlı deployment'taki
kopya H-06/H-09 kapsamında ayrıca ele alınacaktır.

## 6. Eğitim ve diller

| Kimlik | Alan | Kanonik değer | Durum | Kullanım notu |
|---|---|---|---|---|
| `EDU-001` | KEUDA mezuniyet yılı | 2025 | Onaylı | `Present` veya devam ediyor şeklinde gösterilmez |
| `EDU-002` | KEUDA program adı | Vocational Qualification in Information and Communication Technology; qualification title: Software Developer | Kısmen doğrulandı | Resmî Keuda terminolojisi doğrulandı; kişisel diploma kaydı bekleniyor |
| `EDU-003` | KEUDA başlangıç tarihi | Belirlenecek | Doğrulama bekliyor | Onaylanmadan yayımlanmaz |
| `EDU-004` | Nazilli Polis Meslek Yüksekokulu | Mezuniyet 2006 iddiası | Kısmen doğrulandı | Kurumun tarihsel adı resmî Polis Akademisi kaydında bulundu; kişisel diploma bekleniyor |
| `EDU-005` | Metropolia | Kayıt gerçekleşmedi; süreç izleniyor | Özel not | Resmî öğrencilik başlamadan CV/site eğitim bölümünde yayımlanmaz |
| `EDU-006` | KEUDA Fince program ve tutkintonimike | Tieto- ja viestintätekniikan perustutkinto; tutkintonimike: ohjelmistokehittäjä | Kısmen doğrulandı | OPH ve Keuda terminolojisi doğrulandı; kişisel diploma kaydı bekleniyor |
| `LANG-001` | Türkçe | Native | Onaylı | İngilizce CV gösterimi |
| `LANG-002` | İngilizce | B2 | Onaylı | `Professional working level` yerine açık seviye kullanılır |
| `LANG-003` | Fince | B2 | Onaylı | `Developing` yerine açık seviye kullanılır |

## 7. Deneyim kayıtları

Aşağıdaki kayıtların kurum, rol ve tarih bilgileri kullanıcı tarafından
23 Temmuz 2026'da doğrulandı. Sorumluluk ve teknoloji maddeleri yalnızca ayrıca
doğrulanmış çalışma kapsamıyla yayımlanır.

| Kimlik | Mevcut kayıt | Mevcut tarih | Durum | A-02 doğrulaması |
|---|---|---|---|---|
| `EXP-001` | Founder & Software Developer — ZyInnova | 2024–Present | Doğrulama bekliyor | Yerel portfolyo Git geçmişi Ocak 2026'da başlıyor; 2024 başlangıcı için daha eski repo veya şirket kaydı gerekiyor |
| `EXP-002` | Flutter Developer Intern — Roseance Oy | Oct 2024–Dec 2024 | Onaylı | Kullanıcı resmî sözleşmenin bulunduğunu doğruladı; `Earlier Experience` altında yayımlanır |
| `EXP-003` | Web Developer Intern — Sisustusklinikka.fi | Feb 2024–May 2024 | Onaylı | Kullanıcı resmî sözleşmenin bulunduğunu ve tercih edilen yazımın `Sisustusklinikka.fi` olduğunu doğruladı; `Earlier Experience` altında yayımlanır |
| `EXP-004` | Java Mentor — Wise Quarter | 2022 | Onaylı | Kullanıcı sertifikanın bulunduğunu doğruladı; `Earlier Experience` altında yayımlanır |
| `EXP-005` | Full-Stack Java Developer Training — TechPro Education | 2021 | Onaylı | Kullanıcı kaydın kullanılmasını doğruladı; iş deneyimi değil `Additional Training` altında yayımlanır |
| `EXP-006` | Police Officer — Turkish National Police | 2006–2016 | Onaylı | Kullanıcı diploma ve destekleyici belgelerin bulunduğunu doğruladı; `Earlier Experience` altında yayımlanır |

### 7.1 A-02 karşılaştırma sonuçları

| Kayıt | Karşılaştırma sonucu | Yayın kararı |
|---|---|---|
| KEUDA | Resmî İngilizce program adı ve `Software Developer` yeterlilik unvanı Keuda kaynaklarıyla uyumlu; mevcut sitedeki `2023–Present` ifadesi kullanıcı teyitli 2025 mezuniyetiyle çelişiyor | Mezuniyet 2025 kullanılacak; başlangıç yılı diploma görülmeden eklenmeyecek |
| Nazilli eğitimi | Polis Akademisi kayıtlarında `Nazilli Polis Meslek Yüksekokulu` tarihsel kurum adı bulunuyor | İngilizce çeviri ve 2006 tarihi diploma görülmeden kesinleştirilmeyecek |
| Roseance | `Roseance Oy` adı, yazılım/web/mobil faaliyetleri ve Finlandiya şirket kimliği kurum sitesinde doğrulandı; kullanıcı resmî sözleşmesini teyit etti | Staj rolü ve tarihleri `Earlier Experience` altında kullanılacak |
| Sisustusklinikka | Önceki kaynaklarda iki farklı yazım vardı; kullanıcı resmî sözleşmesini ve `Sisustusklinikka.fi` yazımını teyit etti | Kullanıcı teyitli yazım, rol ve tarihler `Earlier Experience` altında kullanılacak |
| Wise Quarter | Kurum kendini `Wise Quarter` olarak yazıyor; kullanıcı mentorluk sertifikasını teyit etti | Java Mentor rolü ve 2022 tarihi `Earlier Experience` altında kullanılacak |
| TechPro Education | Resmî marka ve program adı doğrulandı; kullanıcı kaydın kullanılmasını teyit etti | İş deneyimi yerine `Additional Training` altında kullanılacak |
| Turkish National Police | EGM İngilizce kaynaklarında `Turkish National Police` adını kullanıyor; kullanıcı diploma ve destekleyici belgeleri teyit etti | Rol ve 2006–2016 tarihleri `Earlier Experience` altında kullanılacak |
| ZyInnova | Aktif portfolyo reposunun ilk yerel commit'i 14 Ocak 2026; bu kayıt 2024 başlangıcını kanıtlamıyor | 2024 tarihi daha eski repo, domain/şirket kaydı veya kullanıcı belgesiyle doğrulanacak |

### 7.2 A-02 kaynak kaydı

Erişim tarihi: 23 Temmuz 2026.

- Keuda, Information and Communication Technology:
  <https://www.keuda.fi/en/information-and-communication-technology-sector/>
- Keuda, qualifications and qualification titles:
  <https://www.keuda.fi/en/keudaDegrees-offered-at/>
- Roseance Oy resmî sitesi:
  <https://www.roseance.com/>
- Wise Quarter resmî sitesi:
  <https://wisequarter.com/>
- TechPro Education, Java programı:
  <https://www.techproeducation.com/en/programs/free-java>
- Emniyet Genel Müdürlüğü:
  <https://www.egm.gov.tr/emniyet-genel-mudurlugu>
- EGM uluslararası eğitim kataloğu:
  <https://www.egm.gov.tr/disiliskiler/emniyet-genel-mudurlugu-uluslararasi-egitim-katalogu>
- Polis Akademisi tarihsel birim kaydı:
  <https://avesis.pa.edu.tr/unitreport/index>
- Yerel Git kanıtı: `Z_Y Resume` reposunun ilk commit'i
  `53cbca0`, 14 Ocak 2026.

### 7.3 C-02 Fince terminoloji kaynak kaydı

Erişim tarihi: 23 Temmuz 2026.

- Työmarkkinatori, Ohjelmistokehittäjä:
  <https://tyomarkkinatori.fi/henkiloasiakkaat/ammattitieto/ammatit/ohjelmistokehittaja>
- Opetushallitus, ammatilliset perustutkinnot:
  <https://www.oph.fi/fi/koulutus-ja-tutkinnot/ammatilliset-perustutkinnot>
- Keuda, tieto- ja viestintätekniikan ala:
  <https://www.keuda.fi/tieto-ja-viestintatekniikan-ala/>

## 8. Teknik yetkinlikler

A-03 sırasında proje manifestleri, uygulama kaynakları ve commit geçmişi
karşılaştırılmıştır. Aşağıdaki kayıtlar teknoloji kullanımını doğrular; ancak
tek başına uzmanlık seviyesi veya üretim deneyimi iddiası oluşturmaz.

| Kimlik | Teknoloji/alan | Proje kanıtı | Durum | Yayın sınırı |
|---|---|---|---|---|
| `TECH-001` | HTML, CSS, JavaScript | Aktif portfolyo kaynakları | Projede doğrulandı | Kişisel web projesi bağlamında kullanılabilir |
| `TECH-002` | Flutter ve Dart | Todo, Movie Explorer ve Zikirmatik kaynakları | Projede doğrulandı | Projenin gerçek kapsamı ayrıca belirtilir |
| `TECH-003` | Firebase Authentication ve Cloud Firestore | Todo kaynak kodu ve bağımlılıkları | Projede doğrulandı | Todo projesi bağlamında kullanılabilir |
| `TECH-004` | İngilizce/Fince yerelleştirme | Todo `supportedLocales` ve çeviri kaynakları | Projede doğrulandı | Desteklenen diller açıkça `English` ve `Finnish` yazılır |
| `TECH-005` | Yerel bildirimler | Todo bağımlılıkları ve görev yönetimi kodu | Projede doğrulandı | Canlı ürün sonucu olarak sunulmaz |
| `TECH-006` | HTTP/REST API kullanımı ve TMDB entegrasyonu | Movie Explorer servis kodu | Projede doğrulandı | Yalnızca popüler film listeleme kapsamı doğrulandı |
| `TECH-007` | Kaboom.js ve JavaScript | Üç klasik oyun reposunun kaynakları | Öğrenme projesinde doğrulandı | Tutorial/learning bağlamı açıkça belirtilir |
| `TECH-008` | React ve Vite | ZyInnova GameScan listeleme sayfasındaki beyan | Doğrulama bekliyor | Erişilebilir repo/kod olmadan kişisel yetkinlik kanıtı sayılmaz |

Aşağıdaki mevcut CV/site iddiaları proje koduyla henüz doğrulanmamıştır:

- Java, Spring Boot, Spring MVC, Hibernate ve Java tabanlı REST API geliştirme
- React ile uygulanmış erişilebilir bir kişisel repo
- SQL, MySQL ve SQLite
- Python ve C#
- WordPress, teknik SEO, MVC, MVVM ve Clean Architecture
- Figma, Trello ve Slack kullanımı

Bu alanlar eğitim veya deneyim belgeleriyle daha sonra doğrulanabilir. Bir
teknoloji yalnızca eğitimde görülmüşse `coursework` veya `foundational` olarak;
gerçek projede kullanılmışsa rol ve kanıtıyla birlikte yazılır. Yüzdeli seviye,
`expert`, `advanced` veya benzeri kanıtsız niteleme kullanılmaz.

## 9. Proje kayıtları

### 9.1 A-03 doğrulanmış proje envanteri

Erişim ve karşılaştırma tarihi: 23 Temmuz 2026.

| Kimlik | Proje | Doğrulanmış teknoloji | Doğrulanmış durum | Portfolyo kararı |
|---|---|---|---|---|
| `PROJ-001` | Portfolio Website | HTML, CSS, JavaScript; mevcut kaynakta Bootstrap yardımcıları, AOS ve Typed.js | `Live`; aktif repo ve kanonik canlı adres doğrulandı | Ana kişisel web projesi olarak kalabilir; içerik ve bağımlılıklar sonraki görevlerde yenilenir |
| `PROJ-002` | Multi-language Todo App | Flutter, Firebase Authentication, Cloud Firestore, English/Finnish localization, local notifications | `Public source / prototype`; doğrudan çalışan demo doğrulanmadı | Seçilmiş proje adayıdır; mevcut `Live` etiketi kullanılmaz. Genel README düzeltilmeli ve daha yeni özel varyantla ilişki netleştirilmeli |
| `PROJ-003` | Movie Explorer | Flutter, Dart, HTTP, TMDB API, dotenv | `Collaborative prototype`; son doğrulanan commit Aralık 2024 | Şimdilik ana seçkide yayımlanmaz. Katkı sınırı, README ve güvenlik temizliği tamamlanırsa öğrenme/işbirliği projesi olabilir |
| `PROJ-004` | Zikirmatik App | Flutter, Dart, temel sayaç ve sıfırlama arayüzü | `Tutorial / learning exercise`; son doğrulanan commit Ekim 2024 | Seçilmiş portfolyodan çıkarılır; istenirse GitHub öğrenme arşivinde tutulur |
| `PROJ-005` | Classic Game Clones | JavaScript ve Kaboom.js | `Tutorial / learning exercises`; Ekim 2024 | Seçilmiş portfolyodan çıkarılır; kurucu ürünü veya özgün ürün olarak anlatılmaz |
| `PROJ-006` | GameScan | Erişilebilir kodla doğrulanmış teknoloji yok; ZyInnova listesi React/Vite beyanı taşıyor | `Private / in development`; ZyInnova GitHub profilinde aktif proje, ürün deposu özel/kapalı | E aşamasında özel ZyInnova ürün amacıyla kart olarak yayımlandı; teknoloji ve sonuç iddiası kullanılmadı |
| `PROJ-007` | Diğer ZyInnova projeleri | Kod/repo doğrulaması yapılmadı | Proje listesinde idea veya development durumunda yedi kayıt | Otomatik olarak kişisel portfolyoya alınmaz; her biri ayrı kanıt sürecinden geçer |
| `PROJ-008` | Next ZyInnova Product / Studio Template System | Doğrulanmış repo, demo veya ürün kaydı yok | Yer tutucu kart | E-05 kapsamında portfolyodan kaldırıldı |
| `PROJ-009` | LemmikkiLife | ZyInnova genel listesinde `App • Flutter • 2025`; erişilebilir kodla doğrulanmadı | `Private / in development`; detay sayfası ve ürün deposu herkese kapalı | E aşamasında ilk kart olarak yayımlandı; teknoloji ve tamamlanmış özellik iddiası olmadan ürün amacıyla sınırlandı |

### 9.2 Proje bazında kanıt ve sınırlar

#### `PROJ-001` — Portfolio Website

- Repo: <https://github.com/ZiyaaddinYaramis/portfolio-zyinnova-portfolio>
- Canlı adres: <https://portfolio.zyinnova.com/>
- Aktif repo geçmişi 14 Ocak 2026'da başlar; bu proje tek başına 2024 tarihli
  ZyInnova başlangıcını kanıtlamaz.
- Canlı yayın doğrulanmıştır; buna rağmen mevcut içerik doğruluğu ve kalite
  standartları sonraki aşamalarda ayrıca düzeltilecektir.

#### `PROJ-002` — Multi-language Todo App

- Genel repo:
  <https://github.com/ZiyaaddinYaramis/github_io_todo_app>
- Daha yeni fakat özel varyant: `ZiyaaddinYaramis/moduler_todo_app`
- Kod; kullanıcı kaydı/girişi, parola sıfırlama, kullanıcıya özel Firestore
  görevleri, öncelik ve teslim tarihi, filtreleme, yerel bildirimler ile
  İngilizce/Fince yerelleştirmeyi doğrular.
- Genel repo son doğrulanan commit'i 27 Kasım 2024, özel varyantınki
  24 Ağustos 2025'tir.
- Repo README'si varsayılan Flutter metnidir. Çalışan web/mağaza demosu
  doğrulanmadığından mevcut sitenin `Live` etiketi yanlıştır.

#### `PROJ-003` — Movie Explorer

- Repo: <https://github.com/ZiyaaddinYaramis/flutter_tmdb_movie_app>
- Kod yalnızca TMDB'den popüler filmleri alıp poster, başlık ve yayın tarihiyle
  listeleyen kapsamı doğrular.
- README'deki Firebase, kimlik doğrulama, favoriler, yorumlar ve benzeri
  özellikler manifest ve uygulama koduyla doğrulanmamıştır.
- README iki geliştirici belirtir ve commit geçmişinde işbirliği görülür;
  Ziyaaddin Yaramis tek geliştirici olarak sunulmaz.
- README kişisel Gmail adresi içerir; gizlilik temizliği sonraki GitHub
  düzenlemesine alınır.

#### `PROJ-004` — Zikirmatik App

- Repo: <https://github.com/ZiyaaddinYaramis/flutter_zikirmatik_app>
- README projeyi açıkça bir eğitim video serisini izleyen öğrenme çalışması
  olarak tanımlar.
- Kod temel sayaç ve sıfırlama davranışını doğrular; mevcut PDF'deki titreşim
  geri bildirimi iddiası kod veya bağımlılıkla doğrulanmamıştır.

#### `PROJ-005` — Classic Game Clones

- Repos:
  [Space Invaders](https://github.com/ZiyaaddinYaramis/Space-Invaders-Kaboom.js),
  [Super Mario Bros](https://github.com/ZiyaaddinYaramis/Super-Mario-Bros-Kaboom.js)
  ve [Zelda](https://github.com/ZiyaaddinYaramis/Zelda-kaboom.js)
- README'ler çalışmaların tutorial tabanlı olduğunu belirtir.
- Space Invaders README'si Vanilla JS/HTML/CSS derken kaynak Kaboom.js yükler;
  teknoloji tanımında kaynak kod esas alınır.

#### `PROJ-006` — GameScan

- GameScan tanıtım detayı:
  <https://zyinnova.com/projects/gamescan>
- ZyInnova proje listesi:
  <https://zyinnova.com/projects>
- ZyInnova GitHub organizasyonu:
  <https://github.com/zyinnova>
- GameScan detay sayfası projeyi özel/kapalı ve henüz herkese açık olmayan bir
  çalışma olarak gösterir.
- ZyInnova listesinde GameScan `Web • React, Vite • 2025 • Development`
  biçimindedir. ZyInnova GitHub organizasyon profilinin `Active projects`
  bölümü de GameScan'i geliştirme aşamasında gösterir. Ürün deposu özel olduğu
  için teknoloji beyanı erişilebilir kaynak koduyla doğrulanana kadar kişisel
  portfolyoda teknoloji yığını yayımlanmaz.
- Listede ayrıca GreenNest, FinSage, LocaLink, SkillTree AI, FixCycle,
  GreenRentalHub ve NordGreenScan bulunur. Bu kayıtların kişisel rol, repo ve
  uygulama kapsamı A-03 sırasında doğrulanmamıştır.

#### `PROJ-009` — LemmikkiLife

- Genel proje listesi:
  <https://zyinnova.com/projects>
- Kapalı detay sayfası:
  <https://zyinnova.com/projects/lemmikkilife>
- ZyInnova listesi projeyi `App • Flutter • 2025 • Development` olarak ve evcil
  hayvan bakımı, aşı/ilaç hatırlatmaları, ürünler ve abonelik kutularını tek
  uygulamada birleştiren ürün amacıyla tanımlar.
- Detay sayfası projeyi özel/kapalı ve henüz herkese açık olmayan çalışma olarak
  gösterir. Kullanıcı, ilgili ürün depolarından bazılarının ayrı
  `zyinnova` GitHub organizasyonunda özel olarak tutulduğunu teyit etmiştir;
  depo içeriği dışarıdan erişilebilir değildir.
- Kullanıcı LemmikkiLife'ın portfolyoda öne çıkarılmasını onaylamıştır. Kanonik
  sunum `ZyInnova altında geliştirilen öncelikli ürün` ve `In development`
  ifadeleriyle sınırlıdır. `Live`, tamamlanmış özellik, sonuç veya kodla
  doğrulanmış Flutter uygulaması iddiası kanıt gelmeden kullanılmaz.

### 9.3 A-03 yayın ilkeleri

- `Live` yalnızca doğrudan erişilebilir çalışan ürün veya demo için kullanılır.
- Genel repo bulunması projeyi kendiliğinden canlı ürün yapmaz.
- README iddiası manifest ve uygulama koduyla çelişirse kaynak kodu esas alınır.
- Tutorial çalışmaları özgün ürün veya ZyInnova ürünü olarak sunulmaz.
- İşbirliği projesinde kişisel katkı sınırı açıklanmadan tek yazarlık ima
  edilmez.
- Özel repo/proje, teknoloji ve sonuç kanıtı gibi kullanılamaz; yalnızca
  doğrulanmış mevcut geliştirme durumu kadar anlatılır.

### 9.4 E aşaması uygulama sonucu

- Seçilmiş proje sırası LemmikkiLife, GameScan, Multi-language Todo App ve
  Founder Portfolio olarak kesinleştirildi.
- GameScan ile LemmikkiLife için ZyInnova canlı listesindeki ürün amacı ve
  `Private / in development` durumu kullanıldı; özel kod teknoloji kanıtı
  sayılmadı.
- Ayrı ZyInnova GitHub organizasyonu doğrulandı; kişisel GitHub ve kurumsal
  GitHub bağlantıları sitede ayrı kimliklerle sunuldu.
- GitHub uygulaması Todo, Movie Explorer ve Zikirmatik repo durumlarını yeniden
  doğruladı. Movie Explorer işbirliği/README temizliği gerektirdiği, Zikirmatik
  ise tutorial niteliği taşıdığı için ana seçkiye alınmadı.
- İki yer tutucu kartın kaldırıldığı doğrulandı.
- ZyInnova'nın resmî LemmikkiLife ve GameScan konsept kapakları optimize WebP
  olarak; Todo ve Founder Portfolio görselleri kod tabanlı SVG olarak eklendi.
- Uygulama ve kalite kaydı
  [`portfolio/STAGE-E-QA.md`](portfolio/STAGE-E-QA.md) dosyasında tutulur.

## 10. CV yayın kararları

| Kimlik | Karar | Durum |
|---|---|---|
| `CV-001` | İngilizce genel CV hazırlanır | Onaylı |
| `CV-002` | Fince genel CV hazırlanır | Onaylı |
| `CV-003` | İki sürüm aynı doğrulanmış gerçekleri ve bilgi mimarisini taşır | Onaylı |
| `CV-004` | PDF'ler düzenlenebilir DOCX kaynaklarından yeniden üretilir | Onaylı |
| `CV-005` | Genel CV'ler 1–2 sayfa, tek sütunlu ve gerçek metinli olur | Onaylı |
| `CV-006` | İngilizce dosya adı `Ziyaaddin_Yaramis_CV_EN.pdf` olur | Onaylı |
| `CV-007` | Fince dosya adı `Ziyaaddin_Yaramis_CV_FI.pdf` olur | Onaylı |
| `CV-008` | İngilizce ana içerik `docs/cv/CV-EN-CONTENT.md` dosyasında tutulur | Tamamlandı |
| `CV-009` | Düzenlenebilir İngilizce kaynak `output/docx/Ziyaaddin_Yaramis_CV_EN.docx` olarak üretilir | Tamamlandı |
| `CV-010` | Genel İngilizce PDF `output/pdf/Ziyaaddin_Yaramis_CV_EN.pdf` olarak üretilir | Tamamlandı |
| `CV-011` | İngilizce CV görsel, bağlantı, metadata, erişilebilirlik ve gizlilik kontrollerini geçer | Tamamlandı |
| `CV-012` | Fince ana içerik `docs/cv/CV-FI-CONTENT.md` dosyasında tutulur | Tamamlandı |
| `CV-013` | Düzenlenebilir Fince kaynak `output/docx/Ziyaaddin_Yaramis_CV_FI.docx` olarak üretilir | Tamamlandı |
| `CV-014` | Genel Fince PDF `output/pdf/Ziyaaddin_Yaramis_CV_FI.pdf` olarak üretilir | Tamamlandı |
| `CV-015` | Fince CV, İngilizce sürümle eşitlik; dil, görsel, bağlantı, metadata, erişilebilirlik ve gizlilik kontrollerini geçer | Tamamlandı |

### 10.1 Portfolyo yayın kayıtları

| Kimlik | Karar | Durum |
|---|---|---|
| `WEB-001` | Hero, About, Resume, footer ve temel metadata kanonik profesyonel başlıklara eşitlenir | Tamamlandı |
| `WEB-002` | Resume yalnızca doğrulanmış beceri, deneyim, eğitim ve dil kayıtlarını kullanır | Tamamlandı |
| `WEB-003` | ZyInnova üst ürün çatısı; LemmikkiLife öncelikli geliştirme ürünü olarak sunulur | Tamamlandı |
| `WEB-004` | İngilizce ve Fince doğrulanmış PDF'ler ayrı indirme seçenekleriyle yayıma hazırlanır | Tamamlandı |
| `WEB-005` | Eski hassas PDF aktif web kaynaklarından ve bağlantılarından kaldırılır | Tamamlandı |
| `WEB-006` | Yerel masaüstü/mobil görünüm, CV bağlantıları ve içerik eşitliği doğrulanır | Tamamlandı |

## 11. Kalan bilinen çelişkiler

Bu bölüm, sonraki görevlerde düzeltilecek mevcut durumun kısa kaydıdır:

- Aşama D değişiklikleri henüz canlı Hostinger yayınına gönderilmemiştir;
  mevcut canlı site H-09 tamamlanana kadar eski içeriği gösterebilir.
- Eski hassas PDF çalışma ağacından kaldırılmış olsa da Git geçmişinde ve mevcut
  canlı deployment'ta bulunabilir; H-06/H-09 tamamlanmadan risk kapanmış
  sayılmaz.
- GitHub profili ve profil README'si henüz kanonik başlık ve seçkiyle
  eşitlenmemiştir.
- Movie Explorer README'si uygulama kodunda bulunmayan Firebase ve ürün
  özellikleri iddia ediyor.
- Zikirmatik ve tutorial oyun repolarının GitHub sunumu henüz temizlenmemiştir.
- Proje kartlarının görsel kanıt, medya optimizasyonu ve ayrıntılı kalite
  çalışması Aşama E'de devam edecektir.

A-04 kapsamındaki tüm maddeler, öncelik ve uygulama göreviyle birlikte
[`CROSS-SURFACE-CORRECTION-MATRIX.md`](CROSS-SURFACE-CORRECTION-MATRIX.md)
belgesinde tutulur.

## 12. Değişiklik ve yayın protokolü

1. Yeni bir bilgi önce bu belgede kaynak ve durumuyla kaydedilir.
2. `Doğrulama bekliyor` bilgisi CV, site veya GitHub'a yeni iddia olarak
   aktarılmaz.
3. Doğrulama tamamlanınca ilgili satır `Onaylı` yapılır ve kanıt türü not edilir.
4. Ardından İngilizce ana CV, Fince CV ve portfolyo aynı kayıtla güncellenir.
5. Özel veya yayınlanmayacak kişisel veriler bu dosyaya değer olarak yazılmaz.
6. Her maddi değişiklikte kayıt sürümü ve son güncelleme tarihi yenilenir.

## 13. Kapanmamış kanıt kuyruğu

A-02 karşılaştırması tamamlandı. Aşağıdaki kişisel kayıtlar için ek kanıt veya
ayrıntı hâlâ gereklidir:

- KEUDA'nın diploma üzerindeki resmî kurum/program adı ve başlangıç tarihi
- Nazilli eğitiminin resmî adı ve mezuniyet bilgisi
- ZyInnova için 2024 başlangıcını gösteren eski repo, domain veya şirket kaydı
- Onaylanan eski deneyimlerde ayrıntılı sorumluluk veya teknoloji maddeleri
- Kamuya açık Kerava konum bilgisinin kesin yayın kararı

A-03 karşılaştırması tamamlandı. Proje bazındaki açık kanıtlar:

- GameScan'in özel repo/kod içeriğine dayalı doğru teknoloji yığını
- GameScan ile diğer ZyInnova projelerinde Ziyaaddin Yaramis'in kişisel katkısı
- LemmikkiLife'ın özel repo/kodu, doğrulanmış özellik kapsamı ve
  yayımlanabilir görselleri
- Todo App için doğrulanabilir çalışan demo ve genel/özel varyant kararı
- Movie Explorer'da Ziyaaddin Yaramis'in somut katkı sınırı
- Kalacak projeler için yayımlanabilir ekran görüntüsü ve ölçülebilir
  sonuç/öğrenim çıktısı

A-04 karşılaştırması tamamlandı. Site, eski CV, GitHub profil/repo metinleri,
eski GitHub Pages yayını ve bu ana kaynak arasındaki tüm kalan çelişkiler
[`CROSS-SURFACE-CORRECTION-MATRIX.md`](CROSS-SURFACE-CORRECTION-MATRIX.md)
belgesindeki tek düzeltme listesine dönüştürülmüştür.
