-- This query calculates daily stock returns by comparing each day’s closing price to the previous day’s. It also displays trading volume, allowing analysis of both performance and liquidity over time.

SELECT 
    Date, 
    Close, 
    Volume, 
    (Close - LAG(Close) OVER (ORDER BY Date)) / LAG(Close) OVER (ORDER BY Date) * 100 AS daily_return
FROM StockPrices
ORDER BY Date DESC;

-- This query counts how many financial news articles were published on each day. It helps identify peaks in media coverage, which can be linked to market volatility.

SELECT 
    DATE(date) AS news_day,
    COUNT(*) AS nb_articles
FROM NewsArticles
GROUP BY DATE(date)
ORDER BY news_day DESC;

-- This query summarizes the number of geopolitical/financial events per day, along with their average sentiment (AvgTone) and importance (GoldsteinScale). It provides a daily measure of market-relevant global context.

SELECT 
    Date,
    COUNT(*) AS nb_events,
    AVG(AvgTone) AS avg_sentiment,
    AVG(GoldsteinScale) AS avg_importance
FROM Events
GROUP BY Date
ORDER BY Date DESC;

-- This query combines stock trading volume (from the Yahoo Finance API) with event data (from GDELT) on the same dates. It tests whether days with higher event activity correspond to abnormal market volumes.

SELECT 
    Date(api.Date) as Date,
    api.Volume,
    COUNT(e.EventID) AS nb_events,
    AVG(e.AvgTone) AS avg_sentiment
FROM YahooAPI api
LEFT JOIN Events e ON api.Date = e.Date
GROUP BY api.Date, api.Volume
ORDER BY api.Date DESC;

-- This query links financial news articles to concurrent events from GDELT, aggregating sentiment. It allows analysis of how global events align with specific news headlines.
SELECT 
    DATE(n.date) AS news_day,
    n.title,
    COUNT(e.EventID) AS nb_events,
    AVG(e.AvgTone) AS avg_sentiment
FROM NewsArticles n
LEFT JOIN Events e ON DATE(n.date) = e.Date
GROUP BY news_day, n.title
ORDER BY news_day DESC;

-- This query merges market data (Yahoo API) with both news and event datasets. For each trading day, it shows the stock performance, volume, number of news articles, number of events, and their average sentiment. It is the core integrative query to study correlations between sentiment, news flow, events, and stock price movements.
SELECT 
    api.Date,
    api.Close,
    api.Volume,
    api.Ticker,
    COUNT(DISTINCT n.NewsID) AS nb_articles,
    COUNT(DISTINCT e.EventID) AS nb_events,
    AVG(e.AvgTone) AS avg_sentiment
FROM YahooAPI api
LEFT JOIN NewsArticles n ON DATE(n.date) = api.Date
LEFT JOIN Events e ON e.Date = api.Date
GROUP BY api.Date, api.Close, api.Volume, api.Ticker
ORDER BY api.Date DESC;

