# EmotionDetector 😐😄😡

This project captures real-time facial expressions using your webcam and analyzes emotions using DeepFace.  
When a significant emotion is detected, it sends a personalized message to a configured Telegram chat, providing advice or support.

## 🚀 Features

- Real-time face detection using webcam
- Emotion analysis with [DeepFace](https://github.com/serengil/deepface)
- Telegram bot integration to send alerts based on detected emotions
- Configurable thresholds and messages
- Customizable for use in mental health, education, or interactive AI systems

## 🧠 Technologies Used

- Python 3
- OpenCV
- DeepFace
- Telegram Bot API
- NumPy, Pandas

## ⚙️ Installation

```bash
git clone https://github.com/agui1era/EmotionDetector.git
cd EmotionDetector
pip install -r requirements.txt

TELEGRAM_TOKEN=your_bot_token
TELEGRAM_CHAT_ID=your_chat_id
🎥 How It Works
The webcam opens and starts detecting faces.

Emotions are analyzed in real time using DeepFace.

If a specific emotion exceeds the configured threshold, a message is sent to Telegram.

The message includes a suggestion or emotional support text.

