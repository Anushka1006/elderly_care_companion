# 👵 SeniorVoice Companion
**Empowering Independent Living through Generative AI and Accessible Design.**

## 🌟 The Mission
Seniors often face "Information Overload" after medical visits, leading to medication errors and anxiety. SeniorVoice Companion solves this by acting as a digital translator, turning complex healthcare data into simple, safe, and actionable daily tasks.

## 🛠️ Deep Feature Breakdown
### 1. 📋 Medical Jargon Compression
* **Objective**: Reduce cognitive load for elderly users.
* **Logic**: Uses Llama 3.3 to identify dosage, frequency, and lifestyle changes from raw doctor notes.
* **Output**: A 3-point checklist rendered in high-contrast text for easy reading.

### 2. 🚨 Intelligent Safety Net (SOS)
* **Real-time Monitoring**: Scans user chat input for emergency intent.
* **Keyword Detection**: Triggers alerts for words like "dizzy," "fell," or "chest pain".
* **Visual Response**: Flashes a high-visibility red alert to confirm the emergency state.

### 3. ♿ Senior-First UI/UX (Accessibility)
* **Visuals**: Uses a #F3E5F5 Light Lavender background to reduce glare.
* **Typography**: Global font size locked at 22px+ for users with visual impairments.
* **Simplicity**: Minimalist sidebar and large touch-friendly buttons.



## 🏗️ Technical Stack
* **Framework**: Streamlit (Python).
* **AI Engine**: Groq Inference API.
* **Model**: Llama-3.3-70b-versatile (High-speed reasoning).
* **Environment**: Python Dotenv for secure key management.

## 🔒 Security & Privacy
* **Local Processing**: No medical data is stored permanently; it is processed in-memory.
* **Key Safety**: Uses `.gitignore` to ensure developer API keys are never exposed on public repositories.

## 🚀 Installation & Setup
* **1.Clone the Project**:
git clone https://github.com/Anushka1006/elderly_care_companion.git
cd elderly-care-companion
* **2.Setup Virtual Environment**:
python -m venv venv
.\venv\Scripts\activate
* **3.Install dependencies**:
pip install -r requirements.txt
* **4.Run Application**:
streamlit run app.py
## 🗺️ Roadmap
- [ ] Integration with Twilio for automated SMS alerts to family members.
- [ ] Voice-to-Text native browser support for hands-free interaction.
- [ ] Weekly health trend summaries for doctors.