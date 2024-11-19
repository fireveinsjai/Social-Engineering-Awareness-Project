# Social Engineering Awareness Project

## **Overview**
This project simulates phishing attacks to assess organizational awareness and identify vulnerabilities in employee behavior.

---

## **Features**
- Simulated phishing campaigns using Gophish.
- Fake landing page to capture credentials.
- Metrics collection and employee training materials.

---

## **Tools Used**
- **Gophish**: For managing phishing campaigns and email templates.
- **SET (Social-Engineer Toolkit)**: For advanced social engineering scenarios.
- **Python/Flask**: For setting up the credential collection server.

---

## **How to Set Up**
### 1. Install Gophish
- Follow the guide in [gophish_setup.md](Tools-Setup/gophish_setup.md) to set up Gophish on your system.

### 2. Set Up the Flask Server
- Clone the `collect_data.py` script from the `Flask-Server/` folder and run it on your server to collect credentials.

### 3. Create Phishing Campaign
- Use the templates in `Campaign-Setup/` to create email templates and landing pages.

### 4. Run the Campaign
- Upload your target list and launch the phishing campaign in Gophish.

### 5. Analyze Results
- View the collected data and metrics to analyze the effectiveness of your phishing attack.

---

## **License**
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

## **Disclaimer**
This project is for authorized testing and educational purposes only. Unauthorized use is illegal.
