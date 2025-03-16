# 🏛️ PublicPulse

Public Pulse is an **AI-driven app** that ensures transparency, accountability, and fairness in AI-driven governance and decision-making. It evaluates public trust in government posts and individual user credibility based on participation and engagement metrics. Moreover it recommends government to take action or respond for what users have raised or showed their opinions and concerns by giving a report which summarizes the results of the public's opinions with and without bias so we can calculate a proper credibility score, an effective decision is made by government with respect to citizen's choice using credibility score. Here admins are Government and AI panelist (includes AI and representatives from NITI AAYOG) and the users are citizens of India.

## 📌 Features

- **User Credit Score**: Assigns credit scores to users based on activity, participation, and AI panel review.
- **AI Auditing Panel**: Periodically evaluates AI-driven decisions for fairness with the users rating to the AI model.
- **Trust Score**: Periodically, the users are asked to rate the working of AI panelist, according to it the model is enhanced to create a fair environment.
- **Aadhaar-Based Authentication**: Ensures secure user verification, and there is no breach of security as this app is handled by Government and we pull the Aadhar from the Government database.
- **Pull Request Mechanism**: Allows users to voice out, through AI panelist by submitting valid evidence which is reliable with the trust score its then accepted or rejected.
- **Appeal Mechanism**: Allows users to voice out, when the Pull Request is constantly rejected even with valid evidence or user don't feel satisfied enough trying, they can approach the NITI AAYOG representatives (who serves as another admin)
- **Community Trust Visualization**: Generates reports on public trust sentiment. Aggregates community trust metrics for government insights.

## 🛠️ Technologies Used

- **Python** (Flask/Django for backend)
- **SQLite** (Database)
- **Pandas, Matplotlib** (Data processing and visualization)
- **TextBlob/VADER** (Sentiment Analysis)
- **Google Colab** (Development and Testing)

## 🚀 Installation & Setup

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/Public-Pulse.git
   cd Public-Pulse
   ```
2. **Set up a virtual environment (optional but recommended):**
   ```sh
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```
3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
## 💻 UI Flow

publicpulse/
- ├── templates/
- │   ├── login.html
- │   ├── dashboard_india.html         ( Represents Bharat's events and crimes )
- │   ├── dashboard.html               ( Represents Global events and crimes )
- │   ├── users.html                   ( Can pull request and appeal here )
- │   ├── trustscore.html
- ├── static/
- │   ├── style.css
- ├── requiremnts.txt
- ├── README.md


## 📊 Usage

- **User Credit System**: Users gain or lose trust based on verified logins, participation, and interaction quality.
- **Collective Trust Analysis**: Government officials can analyze and visualize community trust through AI-driven insights.
- **Transparency**: The results after collectively concluded is displayed to users.

## 📈 Future Enhancements

- **Federated Learning Integration** for secure AI model training across decentralized data sources.
- **Blockchain-based Trust Ledger** to ensure tamper-proof credit scoring.
- **Advanced Sentiment Analysis** using transformer models like BERT.
- **Mobile App** version for wider accessibility.
  

## 📜 License.

Public Pulse - This project is proprietary and **cannot** be used, modified, or distributed without explicit permission from the owner.  
See the [LICENSE](./LICENSE) file for more details.

Copyright (c) 2025 [Shreya Vijaykumar](https://github.com/ShreyaVijaykumar)

---

💡 *Built to foster AI transparency and public trust in governance and to allign with Sustainable Development Goals!*

*THESE CODES ARE THE IMPORTANT ALGORITHMS AND UI THAT ARE USED IN THIS APP.
THESE ALGORITHMS ARE JUST TESTED AND TRAINED WITH SAMPLE DATAS.*
