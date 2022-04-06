# ab_testing
AB Testi ile Bidding Yöntemlerinin Dönüşümünün Karşılaştırılması

İş Problemi:
Facebook kısa süre önce mevcut "maximumbidding" adı verilen
teklif verme türüne alternatif olarak yeni bir teklif türü olan
"average bidding"’i tanıttı.

Bir şirket web sitesi için, bu yeni özelliği test
etmeye karar verdi ve average bidding'inmaximumbidding'den
daha fazla dönüşüm getirip getirmediğini anlamak için bir A/B
testi yapmak istiyor.

A/B testi 1 aydır devam ediyor ve şirket şimdi bizden
bu A/B testinin sonuçlarını analiz etmenizi bekliyor.
Şirket için nihai başarı ölçütü Purchase'dır. Bu
nedenle, istatistiksel testler için Purchase metriğine
odaklanılmalıdır.

Bir firmanın web site bilgilerini içeren veri setinde kullanıcıların gördükleri ve tıkladıkları reklam sayıları gibi bilgilerin yanı sıra
buradan gelen kazanç bilgileri yer almaktadır. Kontrol ve Test grubu olmak üzere iki ayrı veri seti vardır. Bu veri setleri
kontrol grubu Maximum Bidding, test grubu Average Bidding uygulanarak iki gruba ayrılmıştır.

Impression: Reklam görüntüleme sayısı
Click: Görüntülenen reklama tıklama sayısı
Purchase: Tıklanan reklamlar sonrası satın alınan ürün sayısı
Earning: Satın alınan ürünler sonrası elde edilen kazanç
