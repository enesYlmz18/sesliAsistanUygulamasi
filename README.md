# VoiceAssistant - Python ile Basit Sesli Asistan

Bu proje, Python kullanarak geliştirilen basit bir sesli asistan uygulamasıdır. Sesli komutlarınızı anlayarak çeşitli görevleri yerine getirebilir: saat söylemek, haber okumak, internette arama yapmak, sistem komutlarını çalıştırmak ve daha fazlası.

## 🎯 Özellikler

- 🔊 Türkçe sesli komut algılama
- 🧠 Doğal dil ile temel etkileşim
- ⏰ Saat ve tarih sorgulama
- 🌐 Web'de arama yapma (Google, YouTube)
- 📁 Sistem uygulamalarını açma
- 🔄 Sesli yanıt ile geri bildirim
- 🖼️Basit Çizim Yapma

## ⚙️ Gereksinimler

Aşağıdaki Python kütüphanelerine ihtiyaç vardır:

- `speechrecognition`
- `pyttsx3`
- `datetime`
- `webbrowser`
- `pywhatkit`
- `requests`
- `os`
- `re`
- `time`
- `platform`
- `speedtest`
- `numpy`
- `math`
- `urllib`
- `response`
- `googlesearch-search`
- `subprocess`
- `wikipedia`
- `matplotlib`
- `random`

Kurmak için:


pip install -r requirements.txt
Eğer requirements.txt yoksa, tek tek şu şekilde kurabilirsiniz:


pip install SpeechRecognition pyttsx3 feedparser pywhatkit
Ayrıca ses tanıma için sisteminizde mikrofon bağlı olmalıdır.

🚀 Nasıl Kullanılır?
Python ortamınızı açın.

voicaAssistants.py dosyasını çalıştırın:

python voicaAssistants.py
Asistan sizi sesli olarak karşılayacak ve komutlarınızı bekleyecek.

Örnek komutlar:

"Saat kaç?"

"Hesap Makinesini Aç"

"hava kaç derece"

"Bilgisayarı kapat"

"Bugün günlerden ne"

"Not Al"

"Matematik işlemi yap"

📁 Proje Dosyaları
sesliAsistan.py: Ana Python dosyası, asistanın tüm işlevselliğini içerir.

🔐 Notlar
Bazı komutlar (örneğin bilgisayar kapatma) işletim sistemine özgüdür ve yönetici izni gerektirebilir.

Mikrofonunuz düzgün çalışmıyorsa ses algılama başarısız olabilir.

Türkçe dil desteği için pyttsx3 motor ayarları değiştirilmiştir (sapi5/Windows destekli).

🧑‍💻 Katkıda Bulun
Katkı sağlamak isterseniz fork edip pull request gönderebilirsiniz. Geliştirme önerileri ve hata bildirimleri için issues bölümünü kullanabilirsiniz.

📄 Lisans
Bu proje açık kaynaklıdır. Dilerseniz üzerinde değişiklik yapabilir ve kendi projelerinizde kullanabilirsiniz.

