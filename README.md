Buffer Overflow Exploitation Toolkit
Bu proje, Buffer Overflow (Taşma) zafiyetlerini analiz etmek ve istismar etmek için bir araç seti sunar. Araçlar, adım adım bir süreçle zafiyet tespiti yapmayı ve etkili exploit geliştirmeyi kolaylaştırmak için tasarlanmıştır.

Proje İçeriği:
<br> Proje, aşağıdaki Python betiklerini içerir: <br>

**fuzzing.py: Bir uygulama veya serviste zafiyet tespiti için fuzzing gerçekleştirme.**
**<br> badchars.py: Payload içinde sorun oluşturabilecek kötü karakterleri belirleme. <br>**
**offset.py: Taşma noktası ve EIP kontrolü için gerekli ofseti bulma.**
**<br> exploit.py: Nihai exploit kodunu oluşturarak hedef uygulamayı veya servisi istismar etme. <br>**

Amacımız

Bu projenin amacı, güvenlik araştırmacıları ve siber güvenlik öğrencilerine eğitim materyali sunmaktır. Proje, Buffer Overflow zafiyetlerinin tespiti ve exploit geliştirme sürecini öğrenmek isteyenler için kılavuz niteliği taşır.

Yetenekler
Fuzzing: Çeşitli girdilerle bir uygulamanın dayanıklılığını test eder.
Kötü Karakter Tespiti: Güvenli bir payload geliştirme sürecine katkı sağlar.
Ofset Bulma: EIP kaydını doğru şekilde manipüle edebilmek için ofset değerlerini hesaplar.
Exploit Geliştirme: Tespit edilen zafiyet üzerinden sistem kontrolünü ele geçirme adımlarını içerir.
Projenin Kullanım Alanları
Eğitim: Siber güvenlik konularında pratik yapmak isteyenler için bir öğrenme aracı.
Araştırma: Buffer Overflow ile ilgili daha derin analizler yapmak isteyen güvenlik araştırmacılarına kaynak sağlar.
Etik Testler: İzinli test senaryolarında zafiyet tespiti ve düzeltme süreçlerine yardımcı olur.
Geliştirme Süreci
Fuzzing: Hedef uygulamanın hataya yol açabilecek zafiyet noktaları belirlenir.
Ofset Hesaplama: Taşma işlemi sırasında EIP kaydının üzerine yazılan adresin yeri hesaplanır.
Kötü Karakterlerin Çıkarılması: Exploit sırasında sorun çıkarabilecek karakterler belirlenir ve payload'dan çıkarılır.
Exploit Oluşturma: Tüm bilgiler birleştirilerek nihai bir istismar kodu geliştirilir.


Sorumluluk Reddi
Bu proje yalnızca eğitim ve araştırma amaçlıdır. Yetkisiz sistemlere izinsiz erişim etik dışıdır ve yasadışıdır. Araçları yalnızca yasal izin alınmış sistemlerde kullanın. Bu araçların kötüye kullanımından proje geliştiricileri sorumlu tutulamaz.
