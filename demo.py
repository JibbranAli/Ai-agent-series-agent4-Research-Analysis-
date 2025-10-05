#!/usr/bin/env python3
"""
Simple Demo - Basic functionality demonstration
"""

import json
from datetime import datetime

def load_config():
    """Load configuration"""
    try:
        with open('config.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {
            "agent_name": "Research & Analysis Agent",
            "version": "1.0.0",
            "created_by": "Syed Jibbran Ali"
        }

def demo_research_agent():
    """Demo the main research agent"""
    print("1. Research Agent Demo")
    print("-" * 30)
    
    try:
        from research_agent import ResearchAgent
        
        agent = ResearchAgent()
        
        # Demo company research
        print("   Researching Tesla...")
        tesla_info = agent.research_company("Tesla")
        print(f"   + Company: {tesla_info['name']}")
        print(f"   + Industry: {tesla_info['industry']}")
        print(f"   + Market Cap: ${tesla_info['market_cap']:,}")
        
        # Demo competitor analysis
        print("   Finding competitors...")
        competitors = agent.find_competitors("Tesla", "Electric Vehicles")
        print(f"   + Found {len(competitors)} competitors")
        
        # Demo trend tracking
        print("   Tracking trends...")
        trends = agent.track_trends("Electric Vehicles")
        print(f"   + Found {len(trends)} trends")
        
        # Demo report generation
        print("   Creating report...")
        report_data = {
            'company': tesla_info,
            'competitors': competitors,
            'market': agent.analyze_market("Electric Vehicles")
        }
        report = agent.create_report("Tesla Analysis", report_data)
        result = agent.save_report(report, "demo_tesla_report.md")
        print(f"   + {result}")
        
        return True
        
    except Exception as e:
        print(f"   - Error: {str(e)}")
        return False

def demo_web_search():
    """Demo web search functionality"""
    print("\n2. Web Search Demo")
    print("-" * 30)
    
    try:
        from web_search import WebSearch
        
        search = WebSearch()
        
        # Demo general search
        print("   Searching for AI trends...")
        results = search.find_info("Artificial Intelligence", 3)
        print(f"   + Found {len(results)} results")
        
        # Demo company search
        print("   Searching for Apple...")
        company_results = search.search_company("Apple")
        print(f"   + Found {len(company_results)} results")
        
        # Demo credibility check
        print("   Checking source credibility...")
        score = search.check_source_credibility("https://reuters.com/article")
        print(f"   + Reuters credibility: {score}")
        
        return True
        
    except Exception as e:
        print(f"   - Error: {str(e)}")
        return False

def demo_market_analyzer():
    """Demo market analysis functionality"""
    print("\n3. Market Analyzer Demo")
    print("-" * 30)
    
    try:
        from market_analyzer import MarketAnalyzer
        
        analyzer = MarketAnalyzer()
        
        # Demo company analysis
        print("   Analyzing Tesla...")
        analysis = analyzer.analyze_company("Tesla")
        print(f"   + Company: {analysis['name']}")
        print(f"   + Strengths: {len(analysis['strengths'])} identified")
        
        # Demo market analysis
        print("   Analyzing EV market...")
        market = analyzer.analyze_market("Electric Vehicles")
        print(f"   + Market size: ${market['market_size']:,}")
        print(f"   + Growth rate: {market['growth_rate']}%")
        
        # Demo opportunity analysis
        print("   Finding opportunities...")
        opportunities = analyzer.find_opportunities("Fintech", "India")
        print(f"   + Region: {opportunities['region']}")
        print(f"   + Growth potential: {opportunities['growth_potential']}%")
        
        return True
        
    except Exception as e:
        print(f"   - Error: {str(e)}")
        return False

def demo_trend_tracker():
    """Demo trend tracking functionality"""
    print("\n4. Trend Tracker Demo")
    print("-" * 30)
    
    try:
        from trend_tracker import TrendTracker
        
        tracker = TrendTracker()
        
        # Demo trend finding
        print("   Finding AI trends...")
        trends = tracker.find_trends("Artificial Intelligence", 3)
        print(f"   + Found {len(trends)} trends")
        
        # Demo trend prediction
        print("   Predicting future...")
        prediction = tracker.predict_future("AI", 12)
        print(f"   + Confidence: {prediction['confidence']}")
        print(f"   + Predictions: {len(prediction['predictions'])}")
        
        # Demo sentiment analysis
        print("   Analyzing sentiment...")
        sentiment = tracker.analyze_trend_sentiment("Blockchain")
        print(f"   + Sentiment: {sentiment['overall_sentiment']}")
        print(f"   + Score: {sentiment['sentiment_score']}")
        
        return True
        
    except Exception as e:
        print(f"   - Error: {str(e)}")
        return False

def demo_report_generator():
    """Demo report generation functionality"""
    print("\n5. Report Generator Demo")
    print("-" * 30)
    
    try:
        from report_generator import ReportGenerator
        
        generator = ReportGenerator()
        
        # Demo data
        demo_data = {
            'company': {
                'name': 'Tesla',
                'industry': 'Electric Vehicles',
                'market_cap': 800000000000,
                'revenue': 50000000000,
                'employees': 100000,
                'founded_year': 2003,
                'headquarters': 'Austin, TX',
                'description': 'Tesla is a leading electric vehicle manufacturer.',
                'strengths': ['Innovation', 'Brand', 'Technology'],
                'weaknesses': ['Competition', 'Costs'],
                'opportunities': ['Market growth', 'Expansion'],
                'threats': ['Competition', 'Regulation']
            },
            'market': {
                'industry': 'Electric Vehicles',
                'market_size': 500000000000,
                'growth_rate': 25.5,
                'key_players': ['Tesla', 'BYD', 'BMW'],
                'trends': ['Battery tech', 'Autonomous driving'],
                'opportunities': ['Market expansion', 'Technology'],
                'challenges': ['Competition', 'Costs']
            }
        }
        
        # Demo report creation
        print("   Creating comprehensive report...")
        report = generator.create_report("Tesla Market Analysis", demo_data)
        result = generator.save_as_markdown(report, "demo_report")
        print(f"   + {result}")
        
        # Demo summary report
        print("   Creating summary report...")
        summary = generator.create_summary_report("Tesla Summary", demo_data)
        result = generator.save_as_txt(summary, "demo_summary")
        print(f"   + {result}")
        
        return True
        
    except Exception as e:
        print(f"   - Error: {str(e)}")
        return False

def main():
    """Main demo function"""
    config = load_config()
    
    print("Research & Analysis Agent - Simple Demo")
    print("=" * 50)
    print(f"Agent: {config.get('agent_name', 'Research Agent')}")
    print(f"Version: {config.get('version', '1.0.0')}")
    print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 50)
    
    # Run all demos
    demos = [
        demo_research_agent,
        demo_web_search,
        demo_market_analyzer,
        demo_trend_tracker,
        demo_report_generator
    ]
    
    success_count = 0
    total_demos = len(demos)
    
    for demo in demos:
        try:
            if demo():
                success_count += 1
        except Exception as e:
            print(f"   ✗ Demo failed: {str(e)}")
    
    # Summary
    print("\n" + "=" * 50)
    print("Demo Summary")
    print("=" * 50)
    print(f"Completed: {success_count}/{total_demos} demos")
    
    if success_count == total_demos:
        print("+ All demos completed successfully!")
        print("\nGenerated files:")
        print("- demo_tesla_report.md - Tesla analysis report")
        print("- demo_report.md - Comprehensive market report")
        print("- demo_summary.txt - Executive summary")
        
        print("\nNext steps:")
        print("1. Check the generated report files")
        print("2. Run 'python examples.py' for more examples")
        print("3. Read README.md for detailed usage instructions")
        
    else:
        print(f"- {total_demos - success_count} demos failed")
        print("\nTroubleshooting:")
        print("1. Make sure all required files are present")
        print("2. Check that Python dependencies are installed")
        print("3. Run 'pip install requests pandas beautifulsoup4 lxml'")
    
    print(f"\nDemo completed at {datetime.now().strftime('%H:%M:%S')}")

if __name__ == "__main__":
    main()