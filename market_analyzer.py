#!/usr/bin/env python3
"""
Market Analyzer - Simplified Version
Market analysis functionality for companies and industries
Created by: Syed Jibbran Ali
"""

import json
from datetime import datetime
from typing import Dict, List, Any

class MarketAnalyzer:
    """
    Simple market analyzer for company and industry analysis
    """
    
    def __init__(self):
        self.config = self.load_config()
    
    def load_config(self):
        """Load configuration"""
        try:
            with open('config.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {"agent_name": "Research & Analysis Agent"}
    
    def analyze_company(self, company_name: str, industry: str = None) -> Dict[str, Any]:
        """
        Analyze a company comprehensively
        
        Args:
            company_name: Name of the company
            industry: Industry sector (optional)
            
        Returns:
            Company analysis data
        """
        print(f"Analyzing company: {company_name}")
        
        if not industry:
            industry = self.guess_industry(company_name)
        
        analysis = {
            'name': company_name,
            'industry': industry,
            'market_cap': self.generate_market_cap(),
            'revenue': self.generate_revenue(),
            'employees': self.generate_employee_count(),
            'founded_year': self.generate_founded_year(),
            'headquarters': self.generate_headquarters(),
            'description': f"{company_name} is a leading company in the {industry} industry.",
            
            # SWOT Analysis
            'strengths': [
                'Strong brand recognition',
                'Innovative products/services',
                'Experienced management team',
                'Financial stability',
                'Market leadership position'
            ],
            'weaknesses': [
                'High competition',
                'Market saturation',
                'Regulatory challenges',
                'Dependence on key markets'
            ],
            'opportunities': [
                'Market expansion',
                'Technology advancement',
                'Strategic partnerships',
                'New product development',
                'International growth'
            ],
            'threats': [
                'Economic uncertainty',
                'Competitive pressure',
                'Technology disruption',
                'Regulatory changes',
                'Market volatility'
            ],
            
            # Financial metrics
            'profit_margin': self.generate_profit_margin(),
            'debt_ratio': self.generate_debt_ratio(),
            'growth_rate': self.generate_growth_rate(),
            
            'analysis_date': datetime.now().strftime('%Y-%m-%d')
        }
        
        return analysis
    
    def find_competitors(self, company_name: str, industry: str = None) -> List[Dict[str, Any]]:
        """
        Find and analyze competitors
        
        Args:
            company_name: Name of the company
            industry: Industry sector
            
        Returns:
            List of competitor analysis
        """
        print(f"Finding competitors for {company_name}")
        
        if not industry:
            industry = self.guess_industry(company_name)
        
        competitors = []
        competitor_names = [
            f"{industry} Leader Inc.",
            f"{industry} Solutions Corp",
            f"{industry} Technologies Ltd",
            f"{industry} Innovations Inc",
            f"{industry} Global Corp"
        ]
        
        for i, name in enumerate(competitor_names):
            competitor = {
                'name': name,
                'industry': industry,
                'market_share': round(25 - i * 4, 1),  # Decreasing market share
                'revenue': self.generate_revenue() * (0.8 + i * 0.05),
                'employees': self.generate_employee_count() * (0.7 + i * 0.1),
                'strengths': [
                    f'Strong {industry} presence',
                    'Innovative technology',
                    'Customer loyalty',
                    'Financial resources'
                ],
                'weaknesses': [
                    'Limited market reach',
                    'High costs',
                    'Regulatory challenges'
                ],
                'competitive_position': self.get_competitive_position(i)
            }
            competitors.append(competitor)
        
        return competitors
    
    def analyze_market(self, industry: str) -> Dict[str, Any]:
        """
        Analyze a market/industry
        
        Args:
            industry: Industry to analyze
            
        Returns:
            Market analysis data
        """
        print(f"Analyzing {industry} market")
        
        market_data = {
            'industry': industry,
            'market_size': self.generate_market_size(),
            'growth_rate': self.generate_growth_rate(),
            'market_maturity': self.get_market_maturity(),
            
            # Key players
            'key_players': [
                f"{industry} Leader",
                f"{industry} Solutions",
                f"{industry} Technologies",
                f"{industry} Innovations"
            ],
            
            # Market trends
            'trends': [
                f'{industry} digitalization',
                f'{industry} sustainability focus',
                f'{industry} automation',
                f'{industry} customer experience'
            ],
            
            # Opportunities
            'opportunities': [
                'Emerging markets',
                'Technology adoption',
                'Regulatory support',
                'Consumer demand growth',
                'Innovation opportunities'
            ],
            
            # Challenges
            'challenges': [
                'Market saturation',
                'Intense competition',
                'Economic uncertainty',
                'Regulatory complexity',
                'Technology disruption'
            ],
            
            # Market segments
            'segments': {
                'Enterprise': 40,
                'SMB': 30,
                'Consumer': 30
            },
            
            'analysis_date': datetime.now().strftime('%Y-%m-%d')
        }
        
        return market_data
    
    def find_opportunities(self, industry: str, region: str = "Global") -> Dict[str, Any]:
        """
        Find market opportunities
        
        Args:
            industry: Industry to analyze
            region: Geographic region
            
        Returns:
            Opportunity analysis
        """
        print(f"Finding opportunities in {industry} ({region})")
        
        opportunities = {
            'industry': industry,
            'region': region,
            'market_size': self.generate_market_size(),
            'growth_potential': self.generate_growth_rate(),
            
            # Investment opportunities
            'investment_opportunities': [
                f'{industry} startups',
                f'{industry} technology',
                f'{industry} infrastructure',
                f'{industry} services'
            ],
            
            # Growth drivers
            'growth_drivers': [
                'Technology advancement',
                'Market expansion',
                'Consumer demand',
                'Regulatory support',
                'Economic growth'
            ],
            
            # Risk factors
            'risk_factors': [
                'Market volatility',
                'Competition',
                'Regulatory changes',
                'Economic uncertainty',
                'Technology disruption'
            ],
            
            # Market entry strategies
            'entry_strategies': [
                'Direct investment',
                'Partnership approach',
                'Acquisition strategy',
                'Organic growth',
                'Joint ventures'
            ],
            
            'analysis_date': datetime.now().strftime('%Y-%m-%d')
        }
        
        return opportunities
    
    def compare_companies(self, companies: List[str]) -> Dict[str, Any]:
        """
        Compare multiple companies
        
        Args:
            companies: List of company names
            
        Returns:
            Comparison analysis
        """
        print(f"Comparing companies: {', '.join(companies)}")
        
        comparison = {
            'companies': companies,
            'comparison_date': datetime.now().strftime('%Y-%m-%d'),
            'metrics': {}
        }
        
        # Generate comparison data for each company
        for company in companies:
            analysis = self.analyze_company(company)
            comparison['metrics'][company] = {
                'market_cap': analysis['market_cap'],
                'revenue': analysis['revenue'],
                'employees': analysis['employees'],
                'profit_margin': analysis['profit_margin'],
                'growth_rate': analysis['growth_rate'],
                'strengths_count': len(analysis['strengths']),
                'weaknesses_count': len(analysis['weaknesses'])
            }
        
        # Find leader in each metric
        comparison['leaders'] = {
            'market_cap': max(comparison['metrics'].keys(), 
                            key=lambda x: comparison['metrics'][x]['market_cap']),
            'revenue': max(comparison['metrics'].keys(), 
                          key=lambda x: comparison['metrics'][x]['revenue']),
            'growth_rate': max(comparison['metrics'].keys(), 
                             key=lambda x: comparison['metrics'][x]['growth_rate'])
        }
        
        return comparison
    
    def guess_industry(self, company_name: str) -> str:
        """Guess industry based on company name"""
        name_lower = company_name.lower()
        
        industry_keywords = {
            'Technology': ['tech', 'software', 'ai', 'data', 'cloud', 'digital'],
            'Automotive': ['auto', 'car', 'vehicle', 'tesla', 'ford', 'bmw'],
            'Financial': ['bank', 'finance', 'fintech', 'paypal', 'visa'],
            'Healthcare': ['health', 'medical', 'pharma', 'bio', 'med'],
            'Energy': ['energy', 'oil', 'gas', 'solar', 'wind'],
            'Retail': ['retail', 'shop', 'store', 'amazon', 'walmart'],
            'Telecommunications': ['telecom', 'phone', 'mobile', 'verizon']
        }
        
        for industry, keywords in industry_keywords.items():
            if any(keyword in name_lower for keyword in keywords):
                return industry
        
        return 'Technology'  # Default
    
    def generate_market_cap(self) -> int:
        """Generate realistic market cap"""
        import random
        return random.randint(1000000000, 2000000000000)  # 1B to 2T
    
    def generate_revenue(self) -> int:
        """Generate realistic revenue"""
        import random
        return random.randint(100000000, 500000000000)  # 100M to 500B
    
    def generate_employee_count(self) -> int:
        """Generate realistic employee count"""
        import random
        return random.randint(100, 500000)
    
    def generate_founded_year(self) -> int:
        """Generate realistic founded year"""
        import random
        return random.randint(1950, 2020)
    
    def generate_headquarters(self) -> str:
        """Generate realistic headquarters"""
        cities = ['San Francisco, CA', 'New York, NY', 'London, UK', 'Tokyo, Japan', 'Berlin, Germany']
        import random
        return random.choice(cities)
    
    def generate_profit_margin(self) -> float:
        """Generate realistic profit margin"""
        import random
        return round(random.uniform(5, 25), 1)  # 5% to 25%
    
    def generate_debt_ratio(self) -> float:
        """Generate realistic debt ratio"""
        import random
        return round(random.uniform(0.1, 0.6), 2)  # 10% to 60%
    
    def generate_growth_rate(self) -> float:
        """Generate realistic growth rate"""
        import random
        return round(random.uniform(5, 50), 1)  # 5% to 50%
    
    def generate_market_size(self) -> int:
        """Generate realistic market size"""
        import random
        return random.randint(10000000000, 1000000000000)  # 10B to 1T
    
    def get_competitive_position(self, rank: int) -> str:
        """Get competitive position based on rank"""
        positions = ['Market Leader', 'Strong Challenger', 'Follower', 'Niche Player', 'Emerging']
        return positions[min(rank, len(positions) - 1)]
    
    def get_market_maturity(self) -> str:
        """Get market maturity level"""
        import random
        maturity_levels = ['Emerging', 'Growing', 'Mature', 'Declining']
        return random.choice(maturity_levels)

def main():
    """Demo function"""
    print("Market Analyzer - Demo")
    print("=" * 30)
    
    analyzer = MarketAnalyzer()
    
    # Demo company analysis
    print("\n1. Company Analysis:")
    tesla_analysis = analyzer.analyze_company("Tesla")
    print(f"   Company: {tesla_analysis['name']}")
    print(f"   Industry: {tesla_analysis['industry']}")
    print(f"   Market Cap: ${tesla_analysis['market_cap']:,}")
    print(f"   Strengths: {len(tesla_analysis['strengths'])} identified")
    
    # Demo competitor analysis
    print("\n2. Competitor Analysis:")
    competitors = analyzer.find_competitors("Tesla", "Automotive")
    print(f"   Found {len(competitors)} competitors")
    for comp in competitors[:2]:
        print(f"   - {comp['name']}: {comp['market_share']}% market share")
    
    # Demo market analysis
    print("\n3. Market Analysis:")
    market = analyzer.analyze_market("Electric Vehicles")
    print(f"   Market Size: ${market['market_size']:,}")
    print(f"   Growth Rate: {market['growth_rate']}%")
    print(f"   Key Players: {len(market['key_players'])}")
    
    # Demo opportunity analysis
    print("\n4. Opportunity Analysis:")
    opportunities = analyzer.find_opportunities("Fintech", "India")
    print(f"   Region: {opportunities['region']}")
    print(f"   Market Size: ${opportunities['market_size']:,}")
    print(f"   Growth Potential: {opportunities['growth_potential']}%")
    
    # Demo company comparison
    print("\n5. Company Comparison:")
    comparison = analyzer.compare_companies(["Tesla", "Ford", "BMW"])
    print(f"   Compared {len(comparison['companies'])} companies")
    print(f"   Market Cap Leader: {comparison['leaders']['market_cap']}")
    
    print("\nDemo completed successfully!")

if __name__ == "__main__":
    main()
