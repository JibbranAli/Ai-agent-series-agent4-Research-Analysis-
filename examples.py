#!/usr/bin/env python3
"""
Examples - Real-world usage examples
Created by: Syed Jibbran Ali
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

def example_1_ev_market_trends():
    """Example 1: Analyze EV market trends"""
    print("Example 1: Electric Vehicle Market Trends")
    print("=" * 50)
    
    try:
        from trend_tracker import TrendTracker
        from report_generator import ReportGenerator
        
        tracker = TrendTracker()
        generator = ReportGenerator()
        
        # Find EV trends
        print("Finding EV market trends...")
        trends = tracker.find_trends("Electric Vehicles", 5)
        
        print(f"\nFound {len(trends)} trends:")
        for i, trend in enumerate(trends, 1):
            print(f"{i}. {trend['name']}")
            print(f"   Growth: {trend['growth_rate']}%")
            print(f"   Impact: {trend['impact']}")
            print(f"   Adoption: {trend['adoption_level']}")
        
        # Predict future
        print("\nPredicting future trends...")
        prediction = tracker.predict_future("Electric Vehicles", 12)
        print(f"Confidence: {prediction['confidence']}")
        print(f"Key predictions: {len(prediction['predictions'])}")
        
        # Generate report
        print("\nGenerating trend report...")
        trend_data = {
            'trends': trends,
            'prediction': prediction
        }
        report = generator.create_report("EV Market Trends 2024", trend_data)
        result = generator.save_as_markdown(report, "ev_trends_report")
        print(f"Report saved: {result}")
        
        return True
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return False

def example_2_ai_company_comparison():
    """Example 2: Compare AI companies"""
    print("\nExample 2: AI Company Comparison")
    print("=" * 50)
    
    try:
        from market_analyzer import MarketAnalyzer
        from report_generator import ReportGenerator
        
        analyzer = MarketAnalyzer()
        generator = ReportGenerator()
        
        companies = ["OpenAI", "Anthropic", "Google AI"]
        
        print("Analyzing AI companies...")
        company_analyses = []
        for company in companies:
            analysis = analyzer.analyze_company(company, "Artificial Intelligence")
            company_analyses.append(analysis)
            print(f"✓ Analyzed {company}")
        
        # Compare companies
        print("\nComparing companies...")
        comparison = analyzer.compare_companies(companies)
        print(f"Market cap leader: {comparison['leaders']['market_cap']}")
        print(f"Revenue leader: {comparison['leaders']['revenue']}")
        
        # Generate comparison report
        print("\nGenerating comparison report...")
        comparison_data = {
            'companies': company_analyses,
            'comparison': comparison
        }
        report = generator.create_report("AI Company Comparison", comparison_data)
        result = generator.save_as_markdown(report, "ai_comparison_report")
        print(f"Report saved: {result}")
        
        return True
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return False

def example_3_fintech_opportunities():
    """Example 3: Analyze fintech opportunities"""
    print("\nExample 3: Fintech Market Opportunities")
    print("=" * 50)
    
    try:
        from market_analyzer import MarketAnalyzer
        from trend_tracker import TrendTracker
        from report_generator import ReportGenerator
        
        analyzer = MarketAnalyzer()
        tracker = TrendTracker()
        generator = ReportGenerator()
        
        # Analyze fintech market
        print("Analyzing fintech market...")
        market = analyzer.analyze_market("Fintech")
        print(f"Market size: ${market['market_size']:,}")
        print(f"Growth rate: {market['growth_rate']}%")
        
        # Find opportunities
        print("\nFinding opportunities...")
        opportunities = analyzer.find_opportunities("Fintech", "India")
        print(f"Region: {opportunities['region']}")
        print(f"Growth potential: {opportunities['growth_potential']}%")
        
        # Track trends
        print("\nTracking fintech trends...")
        trends = tracker.find_trends("Fintech", 3)
        print(f"Found {len(trends)} trends")
        
        # Generate report
        print("\nGenerating opportunity report...")
        opportunity_data = {
            'market': market,
            'opportunities': opportunities,
            'trends': trends
        }
        report = generator.create_report("Fintech Opportunities Analysis", opportunity_data)
        result = generator.save_as_markdown(report, "fintech_opportunities_report")
        print(f"Report saved: {result}")
        
        return True
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return False

def example_4_tech_startup_analysis():
    """Example 4: Analyze tech startup ecosystem"""
    print("\nExample 4: Tech Startup Ecosystem Analysis")
    print("=" * 50)
    
    try:
        from research_agent import ResearchAgent
        from trend_tracker import TrendTracker
        from report_generator import ReportGenerator
        
        agent = ResearchAgent()
        tracker = TrendTracker()
        generator = ReportGenerator()
        
        # Analyze startup trends
        print("Analyzing startup trends...")
        trends = tracker.find_trends("Tech Startups", 4)
        
        # Find emerging trends
        print("\nFinding emerging trends...")
        emerging = tracker.identify_emerging_trends("Technology")
        print(f"Found {len(emerging)} emerging trends")
        
        # Analyze market
        print("\nAnalyzing tech market...")
        market = agent.analyze_market("Technology")
        print(f"Market size: ${market['market_size']:,}")
        
        # Generate report
        print("\nGenerating startup analysis report...")
        startup_data = {
            'trends': trends,
            'emerging_trends': emerging,
            'market': market
        }
        report = generator.create_report("Tech Startup Ecosystem Analysis", startup_data)
        result = generator.save_as_markdown(report, "startup_ecosystem_report")
        print(f"Report saved: {result}")
        
        return True
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return False

def example_5_investment_research():
    """Example 5: Investment research analysis"""
    print("\nExample 5: Investment Research Analysis")
    print("=" * 50)
    
    try:
        from research_agent import ResearchAgent
        from market_analyzer import MarketAnalyzer
        from report_generator import ReportGenerator
        
        agent = ResearchAgent()
        analyzer = MarketAnalyzer()
        generator = ReportGenerator()
        
        # Research investment target
        target_company = "Tesla"
        print(f"Researching investment target: {target_company}")
        
        # Company analysis
        company_analysis = agent.research_company(target_company)
        print(f"Company: {company_analysis['name']}")
        print(f"Industry: {company_analysis['industry']}")
        
        # Competitor analysis
        print("\nAnalyzing competitors...")
        competitors = agent.find_competitors(target_company)
        print(f"Found {len(competitors)} competitors")
        
        # Market analysis
        print("\nAnalyzing market...")
        market = agent.analyze_market(company_analysis['industry'])
        print(f"Market size: ${market['market_size']:,}")
        
        # Investment recommendation
        print("\nGenerating investment analysis...")
        investment_data = {
            'company': company_analysis,
            'competitors': competitors,
            'market': market,
            'investment_metrics': {
                'market_cap': company_analysis['market_cap'],
                'revenue': company_analysis['revenue'],
                'growth_rate': market['growth_rate'],
                'competitive_position': 'Strong',
                'risk_level': 'Medium',
                'recommendation': 'Consider for portfolio'
            }
        }
        
        report = generator.create_report(f"{target_company} Investment Analysis", investment_data)
        result = generator.save_as_markdown(report, f"{target_company.lower()}_investment_report")
        print(f"Report saved: {result}")
        
        return True
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return False

def main():
    """Main function to run all examples"""
    config = load_config()
    
    print("Research & Analysis Agent - Real-World Examples")
    print("=" * 60)
    print(f"Agent: {config.get('agent_name', 'Research Agent')}")
    print(f"Version: {config.get('version', '1.0.0')}")
    print(f"Created by: {config.get('created_by', 'Syed Jibbran Ali')}")
    print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)
    
    # Run all examples
    examples = [
        ("EV Market Trends", example_1_ev_market_trends),
        ("AI Company Comparison", example_2_ai_company_comparison),
        ("Fintech Opportunities", example_3_fintech_opportunities),
        ("Tech Startup Analysis", example_4_tech_startup_analysis),
        ("Investment Research", example_5_investment_research)
    ]
    
    success_count = 0
    total_examples = len(examples)
    
    for name, example_func in examples:
        print(f"\nRunning {name}...")
        try:
            if example_func():
                success_count += 1
                print(f"✓ {name} completed successfully")
            else:
                print(f"✗ {name} failed")
        except Exception as e:
            print(f"✗ {name} failed with error: {str(e)}")
    
    # Summary
    print("\n" + "=" * 60)
    print("Examples Summary")
    print("=" * 60)
    print(f"Completed: {success_count}/{total_examples} examples")
    
    if success_count == total_examples:
        print("✓ All examples completed successfully!")
        print("\nGenerated reports:")
        print("• ev_trends_report.md - EV market trends analysis")
        print("• ai_comparison_report.md - AI company comparison")
        print("• fintech_opportunities_report.md - Fintech opportunities")
        print("• startup_ecosystem_report.md - Tech startup analysis")
        print("• tesla_investment_report.md - Investment research")
        
        print("\nThese examples demonstrate:")
        print("• Market trend analysis and prediction")
        print("• Company comparison and competitive analysis")
        print("• Market opportunity identification")
        print("• Startup ecosystem analysis")
        print("• Investment research and due diligence")
        
    else:
        print(f"✗ {total_examples - success_count} examples failed")
        print("\nTroubleshooting:")
        print("1. Make sure all modules are present")
        print("2. Install required dependencies")
        print("3. Check for any import errors")
    
    print(f"\nExamples completed at {datetime.now().strftime('%H:%M:%S')}")

if __name__ == "__main__":
    main()