from flask import Flask, request
import requests
import os

app = Flask(__name__)
TOKEN = os.getenv("TELEGRAM_TOKEN")
URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

auto_reply = """👋 أهلاً وسهلاً،

في حال تأخر الرد، يُرجى إرسال رسالة عبر واتساب على الرقم التالي:
📱 0162 7605584

إذا كنت تستفسر عن أحد الكورسات، يرجى ذكر المعلومات الأساسية التالية:

1️⃣ الحالة الدراسية:
– طالب/ـة في المدرسة  
– تستعد لاختبار القبول (Aufnahmetest)  
– طالب/ـة في السنة التحضيرية  
– طالب/ـة في الجامعة

2️⃣ المادة المطلوبة:  
رياضيات / فيزياء / كيمياء / الكتروتقنية / TestAS

---

👋 Hallo und herzlich willkommen,

Falls ich nicht sofort antworte, schreiben Sie mir bitte per WhatsApp:  
📱 0162 7605584

Wenn Sie sich für einen Kurs interessieren, geben Sie bitte die folgenden Informationen an:

1️⃣ Ihr aktueller Bildungsstatus:  
– Schüler/in  
– bereiten Sie sich auf den Aufnahmetest vor  
– im Studienkolleg (Vorbereitung)  
– Student/in an einer Hochschule oder Universität

2️⃣ Benötigtes Fach:  
Mathematik / Physik / Chemie / Elektrotechnik / TestAS

---

Basel Kasem"""

@app.route('/', methods=["POST"])
def webhook():
    data = request.get_json()
    if "message" in data and "text" in data["message"]:
        chat_id = data["message"]["chat"]["id"]
        requests.post(URL, data={"chat_id": chat_id, "text": auto_reply})
    return '', 200

@app.route('/', methods=["GET"])
def index():
    return "Bot is running!", 200
