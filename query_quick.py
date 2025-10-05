#!/usr/bin/env python3
"""
Simple Query Interface - Quick command-line queries
"""

import sys
import json
from datetime import datetime

def load_config():
    """Load configuration"""
    try:
        with open('config.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {"agent_name": "Research & Analysis Agent"}

def show_usage():
    """Show usage instructions"""
    print("Research & Analysis Agent - Quick Query Interface")
    print("=" * 60)
    print("=" * 60)
    print("\nUsage Examples:")
    print("python query_quick.py company Tesla")
    print("python query_quick.py market Electric Vehicles")
    print("python query_quick.py trends AI")
    print("python query_quick.py competitors Tesla")
    print("python query_quick.py news Tesla")
    print("python query_quick.py investment Apple")
    print("\nAvailable Commands:")
    print("- company <name>     - Research a company")
    print("- market <industry>  - Analyze a market")
    print("- trends <topic>     - Track trends")
    print("- competitors <name> - Find competitors")
    print("- news <query>       - Search news")
    print("- investment <name>  - Investment research")

def query_company(company_name):
    """Query company information"""
    try:
        from research_agent import ResearchAgent
        agent = ResearchAgent()
        
        print(f"Researching {company_name}...")
        info = agent.research_company(company_name)
        
        print(f"\n{company_name} Analysis:")
        print(f"Industry: {info['industry']}")
        print(f"Market Cap: ${info['market_cap']:,}")
        print(f"Revenue: ${info['revenue']:,}")
        print(f"Employees: {info['employees']:,}")
        print(f"Founded: {info['founded_year']}")
        print(f"Headquarters: {info['headquarters']}")
        
        print(f"\nTop Strengths:")
        for strength in info['strengths'][:3]:
            print(f"  - {strength}")
        
        print(f"\nTop Opportunities:")
        for opportunity in info['opportunities'][:3]:
            print(f"  - {opportunity}")
            
    except Exception as e:
        print(f"Error: {str(e)}")

def query_market(industry):
    """Query market information"""
    try:
        from research_agent import ResearchAgent
        agent = ResearchAgent()
        
        print(f"Analyzing {industry} market...")
        market = agent.analyze_market(industry)
        
        print(f"\n{industry} Market Analysis:")
        print(f"Market Size: ${market['market_size']:,}")
        print(f"Growth Rate: {market['growth_rate']}%")
        print(f"Market Maturity: {market.get('market_maturity', 'Growing')}")
        
        print(f"\nKey Players:")
        for player in market['key_players'][:3]:
            print(f"  - {player}")
        
        print(f"\nMarket Trends:")
        for trend in market['trends'][:3]:
            print(f"  - {trend}")
            
    except Exception as e:
        print(f"Error: {str(e)}")

def query_trends(topic):
    """Query trend information"""
    try:
        from research_agent import ResearchAgent
        from trend_tracker import TrendTracker
        
        agent = ResearchAgent()
        tracker = TrendTracker()
        
        print(f"Tracking trends for {topic}...")
        trends = agent.track_trends(topic)
        
        print(f"\nFound {len(trends)} trends:")
        for i, trend in enumerate(trends, 1):
            print(f"\n{i}. {trend['name']}")
            print(f"   Growth Rate: {trend['growth_rate']}%")
            print(f"   Impact: {trend['impact']}")
            print(f"   Adoption: {trend['adoption_level']}")
        
        # Predict future
        print(f"\nFuture Prediction:")
        prediction = tracker.predict_future(topic, 12)
        print(f"Confidence: {prediction['confidence']}")
        print("Key predictions:")
        for pred in prediction['predictions'][:3]:
            print(f"  - {pred}")
            
    except Exception as e:
        print(f"Error: {str(e)}")

def query_competitors(company_name):
    """Query competitor information"""
    try:
        from research_agent import ResearchAgent
        agent = ResearchAgent()
        
        print(f"Finding competitors for {company_name}...")
        competitors = agent.find_competitors(company_name)
        
        print(f"\nFound {len(competitors)} competitors:")
        for i, comp in enumerate(competitors, 1):
            print(f"\n{i}. {comp['name']}")
            print(f"   Market Share: {comp['market_share']}%")
            print(f"   Revenue: ${comp['revenue']:,}")
            print(f"   Employees: {comp['employees']:,}")
            
    except Exception as e:
        print(f"Error: {str(e)}")

def query_news(query):
    """Query news information"""
    try:
        from web_search import WebSearch
        search = WebSearch()
        
        print(f"Searching news for: {query}")
        results = search.find_info(query, 5)
        
        print(f"\nFound {len(results)} news articles:")
        for i, result in enumerate(results, 1):
            print(f"\n{i}. {result['title']}")
            print(f"   Source: {result['source']}")
            print(f"   Date: {result['date']}")
            print(f"   Credibility: {result['credibility_score']}")
            
    except Exception as e:
        print(f"Error: {str(e)}")

def query_investment(company_name):
    """Query investment information"""
    try:
        from research_agent import ResearchAgent
        agent = ResearchAgent()
        
        print(f"Investment research for {company_name}...")
        
        # Get company info
        info = agent.research_company(company_name)
        competitors = agent.find_competitors(company_name)
        market = agent.analyze_market(info['industry'])
        
        print(f"\nInvestment Analysis for {company_name}:")
        print(f"Market Cap: ${info['market_cap']:,}")
        print(f"Revenue: ${info['revenue']:,}")
        print(f"Industry: {info['industry']}")
        print(f"Market Size: ${market['market_size']:,}")
        print(f"Market Growth: {market['growth_rate']}%")
        print(f"Competitors: {len(competitors)}")
        
        # Investment assessment
        print(f"\nInvestment Assessment:")
        if info['market_cap'] > 1000000000000:
            print("  - Large Cap Company")
        elif info['market_cap'] > 10000000000:
            print("  - Mid Cap Company")
        else:
            print("  - Small Cap Company")
        
        if market['growth_rate'] > 20:
            print("  - High Growth Market")
        else:
            print("  - Moderate Growth Market")
        
        print("  - Consider for portfolio diversification")
        
    except Exception as e:
        print(f"Error: {str(e)}")

def main():
    """Main function"""
    if len(sys.argv) < 3:
        show_usage()
        return
    
    command = sys.argv[1].lower()
    query = " ".join(sys.argv[2:])
    
    print(f"Research & Analysis Agent")
    print(f"Query: {command} - {query}")
    print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 50)
    
    if command == "company":
        query_company(query)
    elif command == "market":
        query_market(query)
    elif command == "trends":
        query_trends(query)
    elif command == "competitors":
        query_competitors(query)
    elif command == "news":
        query_news(query)
    elif command == "investment":
        query_investment(query)
    else:
        print(f"Unknown command: {command}")
        show_usage()

if __name__ == "__main__":
    main()
