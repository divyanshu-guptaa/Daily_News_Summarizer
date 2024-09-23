# Daily_News_Summarizer

## Overview

The **Daily News Summarizer** is a web server that scrapes news articles from various sources, summarizes them using **Facebook BART Large CNN** model fine tuned using [this](https://www.kaggle.com/datasets/sunnysai12345/news-summary) dataset. It further presents the summarized news to users efficiently. This project uses **Flask** to serve as a web server and **Selenium** to scrape the news articles. To reduce time complexity, the scraper and summarizer run once daily, storing the summarized news for quick access.

## Tech Stack

- **Python 3.x**
- **Flask**: Web framework for serving the web application.
- **Selenium**: Web scraping tool for automating news extraction.
- **Hugging Face Transformers**: Used for the fine-tuned Facebook Large CNN model to summarize news articles.
- **Pytorch**: Used in integration with transformers to train and fine-tune the model.

## Project Structure


├── app/ <br>
&emsp; └── __init__.py # Initializing blueprint <br>
&emsp; └── routes.py # Integrates Summarizer and Scraper with Flask <br>
&emsp; └── Scraper.py # Web scraper for extracting news articles <br>
├── NewsS_env/ # Python virtual environment (excluded from version control) <br>
├── datasets/ # Dataset for fine-tuning (excluded from version control) <br>
├──chromedriver-win64/ # ChromeDriver used by Selenium for service <br>
├── Summarizer.ipynb # Main code file for summarizer <br>
├── bart-summarizer/ # Fine-tuned BART model (excluded from version control) <br>
├── summarized_news.json <br>
├── run.py # Main run file <br>
├── requirements.txt # Python dependencies <br>
└── README.md # Project documentation (this file) <br>

## Installation

1. **Clone the Repository:**
   
   ```
   git clone https://github.com/divyanshu-guptaa/Daily_News_Summarizer.git
   cd Daily_News_Summarizer
   ````

2. **Create and Activate Virtual Environment:**
   
    ````
    python -m venv NewsS_env
    NewsS_env\Scripts\activate  # On Windows
    NewsS_env/bin/activate      # On Linux
    ````

3. **Install Dependencies:**
   
    ````
    pip install -r requirements.txt
    ````

4. **Download dataset and fine-tune the Model:** <br>
    Download the [dataset](https://www.kaggle.com/datasets/sunnysai12345/news-summary) and store in a folder and specify the location in Summarizer.ipynb. To train and store the model run all of the cells in the jupyter notebook Summarizer.ipynb.

4. **Install and Setup Web Driver:** <br>
    Install the version of web driver compatible with your preferred browser and place the driver in a folder. Also add it to your system path or specify the location in the Scraper.py.

5. **Run the application:** <br>
   Lastly, run the application and go to [http://127.0.0.1:5000/summarize_news/summarize_news](http://127.0.0.1:5000/summarize_news/summarize_news) to view the summarized news.
   ````
   python run.py
   ````

## Contributing
Feel free to submit issues or pull requests to improve this project!

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
   