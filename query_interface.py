#!/usr/bin/env python3
"""
Interactive Query Interface - User-friendly way to enter queries
"""

import json
from datetime import datetime

def load_config():
    """Load configuration"""
    try:
        with open('config.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {"agent_name": "Research & Analysis Agent"}

def show_menu():
    """Show the main menu"""
    print("\n" + "=" * 60)
    print("🔍 Research & Analysis Agent - Query Interface")
    print("=" * 60)
    print("=" * 60)
    print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)
    
    print("\n📋 Available Query Types:")
    print("1. 🔍 Company Research")
    print("2. 📊 Market Analysis") 
    print("3. 📈 Trend Tracking")
    print("4. 🏢 Competitor Analysis")
    print("5. 💰 Investment Research")
    print("6. 📰 News Search")
    print("7. 📋 Generate Report")
    print("8. ❓ Help")
    print("9. 🚪 Exit")
    
    print("\n" + "-" * 60)

def get_user_input():
    """Get user input for queries"""
    try:
        from research_agent import ResearchAgent
        from web_search import WebSearch
        from market_analyzer import MarketAnalyzer
        from trend_tracker import TrendTracker
        from report_generator import ReportGenerator
        
        agent = ResearchAgent()
        web_search = WebSearch()
        market_analyzer = MarketAnalyzer()
        trend_tracker = TrendTracker()
        report_generator = ReportGenerator()
        
    except ImportError as e:
        print(f"Error importing modules: {e}")
        return
    
    while True:
        show_menu()
        
        try:
            choice = input("\n🎯 Enter your choice (1-9): ").strip()
            
            if choice == "1":
                # Company Research
                print("\n🔍 Company Research")
                print("-" * 30)
                company_name = input("Enter company name: ").strip()
                if company_name:
                    print(f"\nResearching {company_name}...")
                    info = agent.research_company(company_name)
                    
                    print(f"\n📊 Results for {company_name}:")
                    print(f"Industry: {info['industry']}")
                    print(f"Market Cap: ${info['market_cap']:,}")
                    print(f"Revenue: ${info['revenue']:,}")
                    print(f"Employees: {info['employees']:,}")
                    print(f"Founded: {info['founded_year']}")
                    print(f"Headquarters: {info['headquarters']}")
                    
                    print(f"\n💪 Strengths:")
                    for strength in info['strengths'][:3]:
                        print(f"  • {strength}")
                    
                    print(f"\n🎯 Opportunities:")
                    for opportunity in info['opportunities'][:3]:
                        print(f"  • {opportunity}")
                
            elif choice == "2":
                # Market Analysis
                print("\n📊 Market Analysis")
                print("-" * 30)
                industry = input("Enter industry name: ").strip()
                if industry:
                    print(f"\nAnalyzing {industry} market...")
                    market = agent.analyze_market(industry)
                    
                    print(f"\n📈 {industry} Market Analysis:")
                    print(f"Market Size: ${market['market_size']:,}")
                    print(f"Growth Rate: {market['growth_rate']}%")
                    print(f"Market Maturity: {market.get('market_maturity', 'Growing')}")
                    
                    print(f"\n🏢 Key Players:")
                    for player in market['key_players'][:3]:
                        print(f"  • {player}")
                    
                    print(f"\n📈 Trends:")
                    for trend in market['trends'][:3]:
                        print(f"  • {trend}")
                
            elif choice == "3":
                # Trend Tracking
                print("\n📈 Trend Tracking")
                print("-" * 30)
                topic = input("Enter topic to track trends: ").strip()
                if topic:
                    print(f"\nTracking trends for {topic}...")
                    trends = agent.track_trends(topic)
                    
                    print(f"\n🔍 Found {len(trends)} trends:")
                    for i, trend in enumerate(trends, 1):
                        print(f"\n{i}. {trend['name']}")
                        print(f"   Category: {trend['category']}")
                        print(f"   Growth Rate: {trend['growth_rate']}%")
                        print(f"   Impact: {trend['impact']}")
                        print(f"   Adoption: {trend['adoption_level']}")
                    
                    # Predict future
                    print(f"\n🔮 Predicting future for {topic}...")
                    prediction = trend_tracker.predict_future(topic, 12)
                    print(f"Confidence: {prediction['confidence']}")
                    print(f"Key predictions:")
                    for pred in prediction['predictions'][:3]:
                        print(f"  • {pred}")
                
            elif choice == "4":
                # Competitor Analysis
                print("\n🏢 Competitor Analysis")
                print("-" * 30)
                company_name = input("Enter company name: ").strip()
                industry = input("Enter industry (optional): ").strip()
                
                if company_name:
                    print(f"\nFinding competitors for {company_name}...")
                    competitors = agent.find_competitors(company_name, industry)
                    
                    print(f"\n🏆 Found {len(competitors)} competitors:")
                    for i, comp in enumerate(competitors, 1):
                        print(f"\n{i}. {comp['name']}")
                        print(f"   Market Share: {comp['market_share']}%")
                        print(f"   Revenue: ${comp['revenue']:,}")
                        print(f"   Employees: {comp['employees']:,}")
                        print(f"   Position: {comp.get('competitive_position', 'Unknown')}")
                
            elif choice == "5":
                # Investment Research
                print("\n💰 Investment Research")
                print("-" * 30)
                company_name = input("Enter company to research for investment: ").strip()
                if company_name:
                    print(f"\nResearching {company_name} for investment...")
                    
                    # Company analysis
                    info = agent.research_company(company_name)
                    competitors = agent.find_competitors(company_name)
                    market = agent.analyze_market(info['industry'])
                    
                    print(f"\n💼 Investment Analysis for {company_name}:")
                    print(f"Market Cap: ${info['market_cap']:,}")
                    print(f"Revenue: ${info['revenue']:,}")
                    print(f"Industry: {info['industry']}")
                    print(f"Market Size: ${market['market_size']:,}")
                    print(f"Market Growth: {market['growth_rate']}%")
                    print(f"Competitors: {len(competitors)}")
                    
                    # Investment recommendation
                    print(f"\n📊 Investment Assessment:")
                    if info['market_cap'] > 1000000000000:  # > 1T
                        print("  • Large Cap Company")
                    elif info['market_cap'] > 10000000000:  # > 10B
                        print("  • Mid Cap Company")
                    else:
                        print("  • Small Cap Company")
                    
                    if market['growth_rate'] > 20:
                        print("  • High Growth Market")
                    else:
                        print("  • Moderate Growth Market")
                    
                    print("  • Consider for portfolio diversification")
                
            elif choice == "6":
                # News Search
                print("\n📰 News Search")
                print("-" * 30)
                query = input("Enter search query: ").strip()
                if query:
                    print(f"\nSearching for: {query}")
                    results = web_search.find_info(query, 5)
                    
                    print(f"\n📰 Found {len(results)} news articles:")
                    for i, result in enumerate(results, 1):
                        print(f"\n{i}. {result['title']}")
                        print(f"   Source: {result['source']}")
                        print(f"   Date: {result['date']}")
                        print(f"   Credibility: {result['credibility_score']}")
                        print(f"   Summary: {result['summary'][:100]}...")
                
            elif choice == "7":
                # Generate Report
                print("\n📋 Generate Report")
                print("-" * 30)
                report_title = input("Enter report title: ").strip()
                company_name = input("Enter company name (optional): ").strip()
                
                if report_title:
                    print(f"\nGenerating report: {report_title}")
                    
                    report_data = {}
                    if company_name:
                        info = agent.research_company(company_name)
                        competitors = agent.find_competitors(company_name)
                        market = agent.analyze_market(info['industry'])
                        report_data = {
                            'company': info,
                            'competitors': competitors,
                            'market': market
                        }
                    else:
                        # General market report
                        industry = input("Enter industry for general report: ").strip()
                        if industry:
                            market = agent.analyze_market(industry)
                            trends = agent.track_trends(industry)
                            report_data = {
                                'market': market,
                                'trends': trends
                            }
                    
                    if report_data:
                        report = agent.create_report(report_title, report_data)
                        filename = f"{report_title.replace(' ', '_').lower()}_report.md"
                        result = agent.save_report(report, filename)
                        print(f"\n✅ {result}")
                    else:
                        print("No data to generate report")
                
            elif choice == "8":
                # Help
                print("\n❓ Help & Usage Guide")
                print("-" * 30)
                print("🔍 Company Research: Analyze any company's financials, strengths, and opportunities")
                print("📊 Market Analysis: Study industry trends, size, and key players")
                print("📈 Trend Tracking: Identify and predict market trends")
                print("🏢 Competitor Analysis: Find and compare competitors")
                print("💰 Investment Research: Evaluate investment opportunities")
                print("📰 News Search: Find recent news and articles")
                print("📋 Generate Report: Create professional reports")
                
                print("\n💡 Tips:")
                print("• Use specific company names (e.g., 'Tesla', 'Apple')")
                print("• Use industry names (e.g., 'Electric Vehicles', 'Technology')")
                print("• Be specific with your queries for better results")
                print("• All data is sourced from credible APIs")
                
            elif choice == "9":
                # Exit
                print("\n👋 Thank you for using Research & Analysis Agent!")
                print("=" * 60)
                break
            
            else:
                print("\n❌ Invalid choice. Please enter 1-9.")
            
            # Ask if user wants to continue
            if choice in ["1", "2", "3", "4", "5", "6", "7"]:
                continue_choice = input("\n🔄 Would you like to make another query? (y/n): ").strip().lower()
                if continue_choice not in ['y', 'yes']:
                    print("\n👋 Thank you for using Research & Analysis Agent!")
                    break
        
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"\n❌ Error: {str(e)}")
            print("Please try again.")

def main():
    """Main function"""
    config = load_config()
    
    print("🚀 Starting Research & Analysis Agent...")
    print("Loading modules...")
    
    try:
        get_user_input()
    except Exception as e:
        print(f"Error starting application: {e}")
        print("Make sure all required files are present.")

if __name__ == "__main__":
    main()
