## ARA BELLEK TAŞMASI ARAÇ SETİ
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
<br>Kötü Karakter Tespiti: Güvenli bir payload geliştirme sürecine katkı sağlar.<br>
<br>Ofset Bulma: EIP kaydını doğru şekilde manipüle edebilmek için ofset değerlerini hesaplar.<br>
<br>Exploit Geliştirme: Tespit edilen zafiyet üzerinden sistem kontrolünü ele geçirme adımlarını içerir.<br>

Projenin Kullanım Alanları
Eğitim: Siber güvenlik konularında pratik yapmak isteyenler için bir öğrenme aracı.
<br>Araştırma: Buffer Overflow ile ilgili daha derin analizler yapmak isteyen güvenlik araştırmacılarına kaynak sağlar.<br>
<br>Etik Testler: İzinli test senaryolarında zafiyet tespiti ve düzeltme süreçlerine yardımcı olur.<br>

**Geliştirme Süreci:
<br>Fuzzing: Hedef uygulamanın hataya yol açabilecek zafiyet noktaları belirlenir.
<br>Ofset Hesaplama: Taşma işlemi sırasında EIP kaydının üzerine yazılan adresin yeri hesaplanır.<br>
<br>Kötü Karakterlerin Çıkarılması: Exploit sırasında sorun çıkarabilecek karakterler belirlenir ve payload'dan çıkarılır.<br>
<br>Exploit Oluşturma: Tüm bilgiler birleştirilerek nihai bir istismar kodu geliştirilir.<br>**


Copyright [2024] [Proje Geliştiricileri]

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

---

### Sorumluluk Reddi
Bu proje yalnızca eğitim ve araştırma amaçlıdır. Yetkisiz sistemlere izinsiz erişim etik dışıdır ve yasadışıdır. Araçları yalnızca yasal izin alınmış sistemlerde kullanın. Bu araçların kötüye kullanımından proje geliştiricileri sorumlu tutulamaz.



