import os
import json
from flask import request,jsonify
from .Scraper import scrape_news
from . import bp
from transformers import AutoModelForSeq2SeqLM,AutoTokenizer,pipeline
import datetime

model = AutoModelForSeq2SeqLM.from_pretrained('bart-summarizer/checkpoint-440')
tokenizer = AutoTokenizer.from_pretrained('bart-summarizer/checkpoint-440')

def summarize(texts):
    inputs = tokenizer(texts, padding='max_length', truncation=True,max_length=1024, return_tensors='pt')
    summaries = model.generate(input_ids=inputs.input_ids, attention_mask=inputs.attention_mask)
    decoded_summaries = [tokenizer.decode(s, skip_special_tokens=True) for s in summaries]
    return decoded_summaries

def scrape_and_summarize():
    articles = scrape_news()
    summarized_news = []
    for article in articles:
        summary = summarize(article['news'])
        summarized_news.append({
            'title': article['headline'],
            'link': article['url'],
            'summary': summary
        })
    date_and_news = {'date':str(datetime.datetime.now().date()),'summaries':summarized_news}
    with open("summarized_news.json","w") as f:
        json.dump(date_and_news,f)

def load_cached_data():
    if os.path.exists("summarized_news.json"):
        # os.chmod("summarized_news.json",0o777)
        file_time = os.path.getmtime("summarized_news.json")
        file_date = datetime.datetime.fromtimestamp(file_time).date()
        if file_date == datetime.datetime.now().date():
            with open("summarized_news.json","r") as f:
                return json.load(f)
    else:
        return None

@bp.route('/summarize_news', methods=['GET'])
def index():
    cached_data = load_cached_data()
    if cached_data:
        return jsonify(cached_data)
    else:
        scrape_and_summarize()
        return "wait please, news is getting refreshed"