from flask import Flask, request, render_template
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
import nltk 
import emoji


nltk.download('stopwords')

set(stopwords.words('english'))
app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('form.html')

@app.route('/', methods=['POST'])
def my_form_post():
    stop_words = stopwords.words('english')
    text1 = request.form['text1'].lower()

    processed_doc1 = ' '.join([word for word in text1.split() if word not in stop_words])

    sa = SentimentIntensityAnalyzer()
    dd = sa.polarity_scores(text=processed_doc1)
    #compound = round((1 + dd['compound'])/2, 2)
    
    #def sentiment_scores(sentence):
    #sid_obj = SentimentIntensityAnalyzer()
    #sentiment_dict = sid_obj.polarity_scores(sentence)
    #print("Sentiment Score is",sentiment_dict['compound'])
    #print("Its", end = " ")
    # decide sentiment as positive, negative and neutral
    if dd['compound'] > 0.0 and dd['pos'] >= 0.4:
        pnn="POSITIVE"
        em = (emoji.emojize(":grinning_face_with_big_eyes:"))
  
    elif   dd['compound'] == 0.0 and dd['neu'] == 1.0 :
        pnn="NEUTRAL"
        em = (emoji.emojize(":neutral_face:"))
 
    else :
        pnn="NEGATIVE"
        em = (emoji.emojize(":smirking_face:"))
        # Driver code
#if __name__ == "__main__" :
 
    
    #sentence = input()
 
    # function calling
    #sentiment_scores(sentence)

    
    
    return render_template('form.html', final=dd, text1=text1,pnn=pnn, em = em)
    

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5002, threaded=True)
    
