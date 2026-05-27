# 🔍 findIntern: AI & OSINT Staj Radarı

**findIntern**, siber güvenlik ve yazılım alanlarında staj arayan öğrencilerin ve profesyonel adayların, sektördeki açık pozisyonları ve mülakat stratejilerini en optimize şekilde tespit etmesi için geliştirilmiş **Streamlit** tabanlı akıllı bir arama ve asistan aracıdır.

Proje, geleneksel API'lerin sınırlamalarına veya kesintilerine karşı **Yapay Zeka (LLM)** ve **Açık Kaynak İstihbaratı (OSINT)** yöntemlerini bir arada kullanan yedekli (*failover*) bir mimariyle tasarlanmıştır.

---

## 🚀 Özellikler

* **🤖 Groq AI Staj Asistanı:** `Groq API` üzerinden ultra hızlı çalışan `Llama 3.1` modelini kullanarak seçilen branşa (Cyber Security, Network, Python vb.) ve şehre göre kişiselleştirilmiş, nokta atışı mülakat taktikleri, odaklanılması gereken şirket listeleri ve acil GitHub yol haritaları üretir.
* **⚡ OSINT & Google Dorking Mekanizması:** API kotalarının dolması veya servislerin patlaması durumunda devreye giren, siber güvenlik bakış açısıyla kurgulanmış hedef odaklı Google Dork linkleri üretir. LinkedIn ve Kariyer.net üzerindeki en güncel verileri filtreleyerek doğrudan tarayıcıya aktarır.
* **🔐 Güvenli Mimari (.env):** API anahtarlarının kod içerisine gömülmesini (*hardcoded credentials*) engelleyen, mülakatlarda senior yazılımcıların ve güvenlik analistlerinin dikkat ettiği `.env` tabanlı gizlilik koruması.

---

## 🛠️ Teknik Stack

* **Arayüz:** Streamlit (Python)
* **Yapay Zeka Motoru:** Groq Cloud SDK (`llama-3.1-8b-instant`)
* **Ortam Yönetimi:** Python-Dotenv (Güvenlik Odaklı)
* **İstihbarat / Tarama:** Google Dorking (OSINT) & HTTP Requests

---

## 📦 Kurulum ve Çalıştırma

### 1. Depoyu Klonlayın
```bash
git clone [https://github.com/mustafaColak0/findIntern.git](https://github.com/mustafaColak0/findIntern.git)
cd findIntern
```

## 2. Gerekli Kütüphaneleri Yükleyin:

```bash
pip install streamlit groq python-dotenv requests
```

## 3. API Anahtarını Yapılandırın
Proje kök dizininde .env adında bir dosya oluşturun ve Groq API anahtarınızı ekleyin:

```bash
GROQ_API_KEY=your_groq_api_key_here
```

## 4. Uygulamayı Başlatın

```bash
streamlit run app.py
```
💡 Siber Güvenlik ve Mimari Notu
Bu uygulama geliştirilirken hata toleransı (fault tolerance) ilkesi benimsenmiştir. Dinamik entegrasyonlarda yaşanabilecek API kesintileri, uygulamanın çalışmasını engellemez; sistem otomatik olarak B Planı olan OSINT / Google Dorking modülünü öne çıkararak kullanıcının hedefe ulaşmasını sağlar.

Geliştirici: Mustafa Çolak
"""
