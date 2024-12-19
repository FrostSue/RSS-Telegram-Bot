
# RSS Telegram Bot 

## Özellikler
- Belirli aralıklarla RSS beslemesi kontrol etme
- Yeni içerikleri Telegram kanalına gönderme
- SQLite ile içerik geçmişini saklama
- `/recent` komutu ile son içerikleri görüntüleme

## Kurulum
1. Bağımlılıkları yükle:
   ```
   pip install -r requirements.txt
   ```

2. `config.ini` dosyasını düzenle
   - Telegram API bilgilerini ekle
   - RSS kaynağını ayarla

3. Botu çalıştır:
   ```
   python main.py
   ```

## Konfigürasyon
- `config.ini` dosyasından bot ayarlarını düzenleyebilirsiniz
- RSS kontrol sıklığını değiştirebilirsiniz

## Gereksinimler
- Python 3.8+
- Telegram API credentials
