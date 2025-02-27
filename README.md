# 📢 Fast-Track AI-Powered Fake News Detector

### **AI System for Rapid Misinformation Detection & Analysis**

![Project Banner](./assets/project_image_2.png)

## ** Project Overview**
This AI system provides **real-time misinformation detection** by analysing articles, blogs, and social media content using NLP and AI-driven credibility checks.

- **AI-Powered Fact-Checking** (GPT-4o, LangChain)  
- **Social Media Scraping** (Twitter, Reddit, News APIs)  
- **Bias & Sentiment Analysis** (NLP-based heuristics)  
- **Graph-Based Propagation Analysis** (Misinformation spread tracking)  
- **API & UI for Real-Time Use** (Gradio/FastAPI)

---

## ** Features**
- **Real-Time Fake News Detection**: Evaluate article credibility instantly.  
- **AI-Powered Fact-Checking**: Cross-checks with verified sources.  
- **Bias & Sentiment Analysis**: Understand the tone & political bias of content.  
- **Graph-Based Spread Analysis**: Maps misinformation propagation over networks.  
- **User-Friendly API & UI**: Deploy with minimal effort.

---

## ** Tech Stack**
| Component  | Technology  |
|------------|------------|
| **Backend** | FastAPI / Flask  |
| **AI Model** | OpenAI GPT-4o, LangChain  |
| **Web Scraping** | BeautifulSoup, Tweepy, NewsAPI |
| **Frontend** | Gradio / Streamlit |
| **Deployment** | Hugging Face Spaces / Vercel |
| **Testing** | Pytest |

---

## ** Project Structure**
```
ai-fake-news-detector
├── app
│   ├── main.py        # FastAPI/Flask backend
│   ├── fact_checker.py  # AI-based credibility scoring
│   ├── bias_analysis.py # NLP-powered sentiment & bias detection
├── ui
│   ├── gradio_ui.py   # User interface (Gradio)
├── utils
│   ├── scraper.py     # Web scraping utilities
│   ├── propagation.py # Graph-based misinformation analysis
├── tests
│   ├── test_app.py    # Unit tests
├── deployment
│   ├── Dockerfile     # Deployment setup
│   ├── requirements.txt
├── README.md
```

---

## ** Setup & Installation**

### **1️. Clone Repository**
```sh
git clone https://github.com/YOUR-USERNAME/ai-fake-news-detector.git
cd ai-fake-news-detector
```

### **2️. Install Dependencies**
```sh
pip install -r requirements.txt
```

### **3️. Run Locally**
```sh
python app/main.py
```
Access the web UI at `http://localhost:7860`

---

## ** Deployment**
### ** Deploy on Hugging Face Spaces**
1️. Push to a new Hugging Face Space.  
2️. Set `app/main.py` as entry point.  

OR

### ** Deploy on Vercel**
1️. Run `vercel deploy` in the repo directory.
2️. Access live app on `your-vercel-url.com`

---

## ** Example Usage**
- Enter a website URL or social media post.
- AI checks for misinformation.
- Bias & sentiment analysis provides additional insights.
- Results displayed instantly in UI.

---

## ** Future Improvements**
- Deep Fake Video Detection.  
- Advanced NLP-based propaganda tracking.  
- Improved real-time misinformation network visualization.  
- Integration with major fact-checking databases.  

---

## Contribution Guidelines
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch (`feature-branch-name`).
3. Make your changes and commit them.
4. Submit a pull request.

---

## License
This project is licensed under the **MIT License** – you are free to use, modify, and distribute it.


