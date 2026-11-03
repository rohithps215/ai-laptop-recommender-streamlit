# 💻 AI Laptop Decision Assistant

An AI-powered laptop recommendation chatbot that helps users find suitable laptops based on their budget, performance requirements, and intended usage.

The application uses **Google Gemini** to understand user requirements and **Python-based decision logic** to filter, rank, and recommend laptops.

## ✨ Features

- **AI-powered chatbot:** Understands natural-language laptop requirements.
- **Budget filtering:** Finds laptops within the user's budget.
- **Smart ranking:** Ranks laptops using a weighted scoring system.
- **Dedicated GPU filtering:** Helps users find laptops suitable for gaming and graphics-intensive tasks.
- **Clarification handling:** Asks follow-up questions when requirements are unclear.
- **Impossible request handling:** Explains when no laptop matches the requested specifications.
- **Conversation download:** Allows users to download their chat history.

## 🛠️ Technologies Used

- Python
- Streamlit
- Google Gemini API
- Google GenAI SDK
- JSON
- Python-dotenv

## 🧠 How It Works

1. The user describes their laptop requirements through the chatbot.
2. Gemini understands the request and decides when to call the Python recommendation tool.
3. Python filters laptops based on the requirements.
4. A weighted scoring system ranks the matching laptops.
5. Gemini explains the recommendations in a simple format.

## 📊 Decision Scoring System

The application uses a weighted scoring system out of 100.

| Criteria | Weight |
|---|---:|
| Price | 30% |
| Processor | 20% |
| RAM | 15% |
| Storage | 10% |
| GPU | 15% |
| Usage suitability | 10% |
| **Total** | **100%** |

The application uses internal dataset scores for processor and GPU performance. These are demonstration values, not verified benchmark results.

## 🧪 Test Scenarios

The application was tested using five scenarios:

1. **Normal request:** Find a laptop under ₹50,000 for programming.
2. **Gaming request:** Find a laptop with a dedicated GPU.
3. **Budget request:** Find the best laptop under ₹35,000.
4. **Ambiguous request:** Respond to "I want a good laptop" by asking for clarification.
5. **Impossible request:** Handle a request for an RTX 4060 laptop under ₹20,000.

All five test scenarios passed.

## 📁 Project Structure

```text
AI-Laptop-Decision-Assistant/
│
├── app.py
├── llm.py
├── tools.py
├── config.py
├── laptop_data.json
├── test_scenarios.json
├── obstacle_log.txt
├── requirements.txt
├── README.md
├── .gitignore
└── .env
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd AI-Laptop-Decision-Assistant
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the environment

Windows:

```powershell
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure the API key

Create a `.env` file in the project folder:

```env
GEMINI_API_KEY=your_api_key_here
GEMINI_MODEL=gemini-2.5-flash
```

Use your own valid Gemini API key.

### 6. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

## ⚠️ Dataset Limitations

The project currently uses a curated dataset of 12 laptop entries stored in `laptop_data.json`.

Laptop prices and performance scores are illustrative values used for demonstrating the recommendation system. They are not live retail prices or verified benchmark results.

The application does not currently fetch real-time laptop listings from online stores.

## 🔮 Future Improvements

- Expand the laptop dataset.
- Integrate real-time product and price information.
- Add more detailed GPU and processor comparisons.
- Improve recommendation accuracy.
- Add filters for display, battery life, and portability.

## 👨‍💻 Project Goal

This project demonstrates how Large Language Models can work together with traditional Python logic to create an interactive decision-support application.

**Built with Python, Streamlit, and Google Gemini.**