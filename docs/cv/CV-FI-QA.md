# Suomenkielisen CV:n laatutarkastus

> Tarkastuspäivä: 23. heinäkuuta 2026  
> Liittyvät tehtävät: C-01–C-05  
> Tulos: Hyväksytty

## Lopulliset tiedostot

- Muokattava DOCX:
  `output/docx/Ziyaaddin_Yaramis_CV_FI.docx`
- Yleinen suomenkielinen PDF:
  `output/pdf/Ziyaaddin_Yaramis_CV_FI.pdf`
- Hyväksytty sisältö:
  `docs/cv/CV-FI-CONTENT.md`
- Toistettavat työkalut:
  `scripts/build_cv_fi.py`, `scripts/finalize_cv_pdf.py` ja
  `scripts/audit_cv_pair.py`

## Sisällön ja kielen tarkastus

- Ammattinimike on `Ohjelmistokehittäjä | ZyInnovan perustaja`.
- Koulutuksessa käytetään virallisia ilmaisuja
  `Tieto- ja viestintätekniikan perustutkinto` ja
  `tutkintonimike: ohjelmistokehittäjä`.
- LemmikkiLife esitellään ensimmäisenä ja merkitään tilaan `Kehitteillä`.
- Todo-sovellus merkitään julkiseksi prototyypiksi, ei julkaistuksi tuotteeksi.
- Keudasta valmistumisvuosi on 2025.
- Kielitaito on turkki äidinkielenä sekä englanti ja suomi B2-tasolla.
- Roseance Oy, Sisustusklinikka.fi, Wise Quarter ja Turkin kansallinen poliisi
  ovat `Aiempi työkokemus` -osiossa käyttäjän vahvistamilla tehtävillä ja
  ajankohdilla.
- TechPro Education on `Lisäkoulutus`-osiossa, ei työkokemuksena.
- Vahvistamattomat vastuu-, teknologia- ja tulosväitteet on jätetty pois.
- Suomenkielinen teksti on tarkistettu luonnollisuuden, taivutuksen,
  termien ja satunnaisten englanninkielisten ilmausten osalta.

## Englannin- ja suomenkielisen version vastaavuus

`scripts/audit_cv_pair.py` vertasi molempien kielten DOCX- ja PDF-tiedostoja.
Tarkastus varmisti samat kanoniset henkilötiedot, teknologiat, projektit,
projektien järjestyksen, valmistumisvuoden, kielitasot ja seitsemän
linkkikohdetta. Kaikki tarkastukset läpäistiin.

## Visuaalinen tarkastus

- DOCX renderöitiin LibreOffice-työnkululla kahdeksi A4-sivuksi. Ennen
  `Valitut projektit` -osiota on tarkoituksellinen sivunvaihto.
- Lopullinen PDF renderöitiin erikseen Popplerilla.
- Molemmat koko sivun kuvat tarkastettiin.
- Tekstiä ei leikkaannu, elementit eivät mene päällekkäin eikä tiedostossa ole
  rikkoutuneita merkkejä, kömpelöä sivunvaihtoa tai ylimääräistä sivua.
- Taitto on yksipalstainen eikä sisällä valokuvaa, taulukkoa, tekstiruutua tai
  koristeellista asetteluobjektia.

## Tekninen tarkastus

| Tarkastus | Tulos |
|---|---|
| PDF:n sivumäärä | 2 |
| PDF:n sivukoko | A4 |
| Valittava PDF-teksti | Hyväksytty; 3 164 poimittua merkkiä |
| Vaaditut osiot | Kaikki kahdeksan löytyvät DOCX- ja PDF-tiedostoista |
| DOCX:n saavutettavuustarkastus | 0 vakavaa, 0 keskitasoista, 0 lievää havaintoa |
| Kuvat ja taulukot | Ei kuvia eikä taulukoita |
| PDF merkitty rakenteiseksi | Kyllä |
| PDF JavaScript | Ei |
| PDF salaus | Ei |
| Ulkoiset linkit | Seitsemän yksilöllistä kohdetta varmennettu |
| Julkinen sähköposti | Vain `contact@zyinnova.com` |
| Kielletyt henkilötiedot | Ei osumia |
| DOCX:n tekijä/viimeisin muokkaaja | Tyhjä |
| PDF:n tekijä | Ziyaaddin Yaramis |
| PDF:n otsikko | Ziyaaddin Yaramis - Suomenkielinen CV |

Varmennetut PDF-linkit:

- `mailto:contact@zyinnova.com`
- `https://portfolio.zyinnova.com/`
- `https://github.com/ZiyaaddinYaramis`
- `https://zyinnova.com/`
- `https://zyinnova.com/projects/lemmikkilife`
- `https://github.com/ZiyaaddinYaramis/github_io_todo_app`
- `https://github.com/ZiyaaddinYaramis/portfolio-zyinnova-portfolio`

## Eheys

- DOCX SHA-256:
  `d7270fc0b469889e27a31a22191b73e015e3b1041a182567260593099355733d`
- PDF SHA-256:
  `4eab59d843b16f144806af6069ebe63747fd5ba755e2761438192890af250930`

Tiivisteet yksilöivät tarkastetut tiedostot. Jos tiedostoja muutetaan,
renderöinti, tarkastukset ja tiivisteet on tehtävä uudelleen.
