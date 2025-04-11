# 🚌 AI Bus Route Announcer 🚏

An AI-powered real-time bus route announcer that uses **YOLOv5**, **EasyOCR**, and **Google Text-to-Speech (gTTS)** to:

- Detect buses through a webcam 🎥  
- Read number plates using OCR 🔍  
- Match with a predefined dataset 📄  
- Announce the route in **Malayalam** 🔊🇮🇳

---

## 📸 How It Works

1. The webcam captures real-time video.
2. YOLOv5 identifies objects — we filter for `"bus"` 🚌.
3. The number plate region is extracted and enhanced for clarity.
4. EasyOCR reads the number plate 🔠.
5. If the plate exists in the dataset:
   - The system checks the **current time** to decide between morning/evening routes 🌅🌆.
   - Announces the matched bus route in Malayalam using gTTS 🔊.

---

## 🛠️ Technologies Used

- 🧠 **YOLOv5** – Object Detection  
- 👓 **EasyOCR** – Optical Character Recognition  
- 🗣️ **gTTS** – Google Text-to-Speech (Malayalam)  
- 🎮 **Pygame** – To play the announcements  
- 🐍 **Python** – The glue that brings it all together!

---

## 📂 Sample Bus Dataset

```python
bus_route = {
    "KL01AB1234": {
        "morning": "തോമസൺസ് ട്രാവെൽ, എരുമേലി, മൂക്കൂട്ടുതറ",
        "evening": "തോമസൺസ് ട്രാവെൽ, കോട്ടയം വഴി തിരികെ"
    },
    ...
}
