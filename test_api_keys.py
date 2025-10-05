#!/usr/bin/env python3
"""
API Keys Test - Test your API keys with real data
"""

import json
import requests
from datetime import datetime

def load_config():
    """Load configuration with API keys"""
    try:
        with open('config.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def test_news_api():
    """Test News API with real data"""
    print("Testing News API...")
    
    config = load_config()
    api_key = config.get('api_keys', {}).get('news_api')
    
    if not api_key or api_key == "YOUR_ACTUAL_NEWS_API_KEY":
        print("   - No News API key found")
        return False
    
    try:
        url = "https://newsapi.org/v2/everything"
        params = {
            'q': 'Tesla',
            'apiKey': api_key,
            'pageSize': 3,
            'sortBy': 'publishedAt'
        }
        
        response = requests.get(url, params=params, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            articles = data.get('articles', [])
            print(f"   + News API working! Found {len(articles)} articles")
            
            if articles:
                print(f"   + Latest article: {articles[0]['title'][:50]}...")
                print(f"   + Source: {articles[0]['source']['name']}")
                print(f"   + Published: {articles[0]['publishedAt'][:10]}")
            
            return True
        else:
            print(f"   - News API error: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"   - News API error: {str(e)}")
        return False

def test_alpha_vantage():
    """Test Alpha Vantage API with real data"""
    print("\nTesting Alpha Vantage API...")
    
    config = load_config()
    api_key = config.get('api_keys', {}).get('alpha_vantage')
    
    if not api_key or api_key == "YOUR_ACTUAL_ALPHA_VANTAGE_KEY":
        print("   - No Alpha Vantage API key found")
        return False
    
    try:
        url = "https://www.alphavantage.co/query"
        params = {
            'function': 'GLOBAL_QUOTE',
            'symbol': 'TSLA',
            'apikey': api_key
        }
        
        response = requests.get(url, params=params, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            
            if 'Global Quote' in data:
                quote = data['Global Quote']
                if quote and '05. price' in quote:
                    price = quote['05. price']
                    change = quote['09. change']
                    print(f"   + Alpha Vantage working! Tesla stock data:")
                    print(f"   + Current Price: ${price}")
                    print(f"   + Change: {change}")
                    return True
                else:
                    print("   - No stock data returned")
                    return False
            else:
                print("   - API limit reached or invalid response")
                return False
        else:
            print(f"   - Alpha Vantage error: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"   - Alpha Vantage error: {str(e)}")
        return False

def test_polygon_api():
    """Test Polygon API with real data"""
    print("\nTesting Polygon API...")
    
    config = load_config()
    api_key = config.get('api_keys', {}).get('polygon_api')
    
    if not api_key or api_key == "YOUR_ACTUAL_POLYGON_API_KEY":
        print("   - No Polygon API key found")
        return False
    
    try:
        url = "https://api.polygon.io/v2/aggs/ticker/AAPL/prev"
        params = {
            'apikey': api_key
        }
        
        response = requests.get(url, params=params, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            
            if 'results' in data and data['results']:
                result = data['results'][0]
                price = result.get('c', 'N/A')  # Close price
                volume = result.get('v', 'N/A')  # Volume
                print(f"   + Polygon API working! Apple stock data:")
                print(f"   + Close Price: ${price}")
                print(f"   + Volume: {volume:,}")
                return True
            else:
                print("   - No stock data returned")
                return False
        else:
            print(f"   - Polygon API error: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"   - Polygon API error: {str(e)}")
        return False

def test_web_search_with_real_data():
    """Test web search with real API data"""
    print("\nTesting Web Search with Real Data...")
    
    try:
        from web_search import WebSearch
        
        search = WebSearch()
        
        # Test with real search
        print("   Searching for real Tesla news...")
        results = search.find_info("Tesla stock news", 3)
        
        print(f"   + Found {len(results)} results")
        
        for i, result in enumerate(results[:2], 1):
            print(f"   + Result {i}: {result['title'][:40]}...")
            print(f"     Source: {result['source']}")
            print(f"     Credibility: {result['credibility_score']}")
        
        return True
        
    except Exception as e:
        print(f"   - Web search error: {str(e)}")
        return False

def main():
    """Main test function"""
    print("API Keys Test - Real Data Verification")
    print("=" * 50)
    print(f"Test Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 50)
    
    # Test all APIs
    tests = [
        ("News API", test_news_api),
        ("Alpha Vantage", test_alpha_vantage),
        ("Polygon API", test_polygon_api),
        ("Web Search", test_web_search_with_real_data)
    ]
    
    success_count = 0
    total_tests = len(tests)
    
    for test_name, test_func in tests:
        try:
            if test_func():
                success_count += 1
        except Exception as e:
            print(f"   - {test_name} failed: {str(e)}")
    
    # Summary
    print("\n" + "=" * 50)
    print("API Test Summary")
    print("=" * 50)
    print(f"Successful tests: {success_count}/{total_tests}")
    
    if success_count == total_tests:
        print("+ All API keys working perfectly!")
        print("\nYour system is now using real data from:")
        print("- News API (real news articles)")
        print("- Alpha Vantage (real stock prices)")
        print("- Polygon (real market data)")
        
    elif success_count > 0:
        print(f"+ {success_count} API keys working")
        print("- Some APIs may have rate limits or need verification")
        
    else:
        print("- No API keys working")
        print("\nTroubleshooting:")
        print("1. Check your API keys in config.json")
        print("2. Verify API keys are active")
        print("3. Check API rate limits")
        print("4. Ensure internet connection")
    
    print(f"\nTest completed at {datetime.now().strftime('%H:%M:%S')}")

if __name__ == "__main__":
    main()
