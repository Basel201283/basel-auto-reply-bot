import requests
import time

TOKEN = '8081564428:AAFZs6K2hki6LOAeQLD47wpcmCZBpViYBGs'
URL = f"https://api.telegram.org/bot{TOKEN}/"

last_update_id = 0

def get_updates():
    response = requests.get(URL + "getUpdates", params={"offset": last_update_id + 1})
    return response.json()

def send_message(chat_id, text):
    requests.post(URL + "sendMessage", data={"chat_id": chat_id, "text": text})

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

while True:
    updates = get_updates()
    if "result" in updates:
        for update in updates["result"]:
            last_update_id = update["update_id"]
            chat_id = update["message"]["chat"]["id"]
            send_message(chat_id, auto_reply)
    time.sleep(2)
