import sys
sys.stdout.reconfigure(encoding='utf-8')

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def analyze_tweets(tweets):
    analyzer = SentimentIntensityAnalyzer()
    results = []
    
    for tweet in tweets:
        vs = analyzer.polarity_scores(tweet)
        compound = vs['compound']
        
        if compound >= 0.05:
            sentiment = "Positive"
        elif compound <= -0.05:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"
            
        results.append({
            "tweet": tweet,
            "compound_score": compound,
            "sentiment": sentiment
        })
        
    return results

if __name__ == "__main__":
    # A small manual dataset of tweets
    manual_tweets = [
        "I love the new design of this app! It's so intuitive. 😍",
        "This update is literally the worst. It keeps crashing on my phone.",
        "Just had my morning coffee. Time to start the day.",
        "The customer service was amazing. They resolved my issue in 5 minutes! 👏",
        "I'm feeling very indifferent about this new feature. It's okay, I guess.",
        "Why does it take so long to load now? Terribly slow...",
        "The weather today is completely normal.",
        "Absolutely fantastic experience! Highly recommend it.",
        "I hate the new layout. Please change it back."
    ]
    
    print("--- Starting Twitter Sentiment Analysis ---\n")
    analyzed_results = analyze_tweets(manual_tweets)
    
    for idx, result in enumerate(analyzed_results, 1):
        print(f"Tweet {idx}: \"{result['tweet']}\"")
        print(f"Sentiment: {result['sentiment']} (Compound Score: {result['compound_score']})")
        print("-" * 60)
        
    print("\n--- Analysis Complete ---")
