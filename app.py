import streamlit as st
import os
from dotenv import load_dotenv
from groq import Groq

# .env dosyasındaki değişkenleri yükle
load_dotenv()

st.set_page_config(page_title="findIntern | Yapay Zeka Staj Radarı", page_icon="🔍", layout="wide")

# GROQ API KEY (Ortam değişkeninden güvenli bir şekilde çekiliyor)
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")

st.title("🔍 findIntern: AI & OSINT Staj Radarı")
st.markdown("---")

# SOL PANEL
st.sidebar.header("🔍 Filtreler")
alan = st.sidebar.selectbox("Branş", ["Cyber Security", "Python Developer","Software Developer", "Data Science", "React", "Network"])
sehir = st.sidebar.selectbox("Şehir", ["İstanbul", "Ankara", "İzmir", "Kocaeli", "Bursa", "Tüm Şehirler"])

# ANA EKRAN BUTONLARI
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🤖 Groq AI Staj Asistanı")
    if st.button("🚀 Yapay Zeka ile Akıllı Strateji Üret"):
        if not GROQ_API_KEY:
            st.error("🚨 GROQ_API_KEY (.env dosyası içinde) bulunamadı! Lütfen kontrol edin kanka.")
        else:
            with st.spinner("Llama 3.1 siber evreni tarıyor ve strateji üretiyor..."):
                try:
                    # Groq İstemcisini Başlat
                    client = Groq(api_key=GROQ_API_KEY)
                    
                    # Yapay zekaya rol biçiyoruz (Prompt Engineering)
                    sehir_text = "Türkiye genelinde" if sehir == "Tüm Şehirler" else f"{sehir} şehrinde"

                    prompt = f"""
                    Sen profesyonel bir siber güvenlik ve insan kaynakları uzmanısın. 
                    {sehir_text} yaşayan ve {alan} alanında staj arayan 2 yıllık bir bilgisayar programcılığı öğrencisine nokta atışı tavsiyeler ver.
                    Hangi şirketlere odaklanmalı, mülakatlarda bu branş için ne sorarlar ve staj bulma şansını artırmak için GitHub'ına acil ne eklemeli?
                    Kısa, net ve hırçın siber güvenlikçi tarzında maddeler halinde cevap ver. Cevabın Türkçe olsun.
                    """
                    
                    chat_completion = client.chat.completions.create(
                        messages=[{"role": "user", "content": prompt}],
                        model="llama-3.1-8b-instant", # Ultra hızlı çalışan model
                    )
                    
                    # Sonucu Ekrana Bas
                    st.success(f"📋 {alan} İçin AI Yol Haritası:")
                    st.write(chat_completion.choices[0].message.content)
                    
                except Exception as e:
                    st.error(f"Groq API bağlantı hatası: {e}")

with col2:
    # OSINT Çözümü
    st.markdown("### ⚡ OSINT / Google Dork Çözümü")
    # Eğer tüm şehirler seçildiyse dorking'e şehir ekleme, spesifik şehir varsa ekle
    sehir_dork = "" if sehir == "Tüm Şehirler" else f"+%22{sehir}%22"
    # Branşa göre özelleştirilmiş Google Dorking linkleri
    google_dork = f"https://www.google.com/search?q=site:linkedin.com/jobs+%22{alan}%22+staj+2026{sehir_dork}"
    st.link_button("👉 LinkedIn Canli İlanlarini Aç (OSINT)", google_dork)

    kariyer_link = f"https://www.kariyer.net/is-ilanlari?kw={alan}%20staj"
    st.link_button("👉 Kariyer.net İlanlarını Aç", kariyer_link)

st.divider()
st.info("💡 Siber Bilgi: API patlamalarına karşı sağ tarafa koyduğumuz Google Dorking (OSINT) mekanizması, LinkedIn'deki en güncel verileri direkt arama motorundan çeker ve asla yarı yolda bırakmaz.")