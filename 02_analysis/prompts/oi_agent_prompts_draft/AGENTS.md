# OI Agent Prompt Seti — Geçici Taslak

Bu klasör, Osteogenesis Imperfecta (OI) odaklı VSCode Agent prompt setinin **onay öncesi** taslağını içerir.

## Amaç
- miRNA prompt mimarisini referans alarak OI'ye özgü, zincirlenebilir ve denetlenebilir prompt/agent seti sağlamak.
- Genotip-fenotip, varyant yorumlama, diferansiyel ekspresyon, yolak/ağ, literatür entegrasyonu, terapötik hedef skorlama ve raporlama adımlarını kapsamak.

## Güvenlik ve kapsam
- Klinik iddialar yalnızca gözlenebilir kanıta dayandırılır.
- Belirsiz/veri-eksik durumlarda varsayım açık etiketlenir.
- Çıktılar `draft` statüsündedir; ana workspace'e entegrasyon için kullanıcı onayı gerekir.

## Önerilen kullanım
1. `OI Reanalysis Coordinator` ile orkestrasyon.
2. Alt ajanlar ile domain inceleme (QA, istatistik, varyant, yorum).
3. 7 kategori promptunun pipeline sırasıyla çağrılması.
