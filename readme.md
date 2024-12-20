Tabii, işte Telegram Currency Bot için Türkçe bir README:

---

# Telegram Currency Bot

Telegram üzerinden döviz kurları ile kolayca para birimi dönüşümü yapmanızı sağlayan basit ve kullanışlı bir bot. Bot, gerçek zamanlı döviz kuru verilerini kullanarak farklı para birimleri arasında doğru dönüşümler yapmanızı sağlar.

## Özellikler

- Birden fazla para birimi arasında dönüşüm yapma
- Gerçek zamanlı döviz kuru verisi
- Telegram üzerinden kolay etkileşim

## Kurulum

1. **Repoyu klonlayın**

   ```bash
   git clone https://github.com/FrostSue/Telegram-Currency-Bot.git
   cd Telegram-Currency-Bot
   ```

2. **Bağımlılıkları yükleyin**

   Python 3.8+ yüklü olduğundan emin olduktan sonra gerekli kütüphaneleri yükleyin:

   ```bash
   pip install -r requirements.txt
   ```

3. **Telegram bot'unuzu ayarlayın**

   - Telegram üzerinde [BotFather](https://core.telegram.org/bots#botfather) ile yeni bir bot oluşturun.
   - Bot'un API token'ını alın.
   - `config.ini` dosyasındaki token'ı şu şekilde ayarlayın:

     ```python
     API_TOKEN = 'telegram-bot-api-token'
     ```

4. **Bot'u çalıştırın**

   Bot'u başlatmak için şu komutu çalıştırın:

   ```bash
   python bot.py
   ```

   Bot'unuz artık aktif olacak ve Telegram üzerinden döviz dönüşümleri yapabileceksiniz.



## Komutlar

- `/start` – Bot'u başlatır ve tanıtım yapar.
- `/yardim` – Kullanılabilir komutları ve kullanım talimatlarını listeler.

## Desteklenen Para Birimleri

Bot, aşağıdaki gibi birçok para birimini desteklemektedir:

- USD (Amerikan Doları)
- EUR (Euro)
- GBP (İngiliz Sterlini)
