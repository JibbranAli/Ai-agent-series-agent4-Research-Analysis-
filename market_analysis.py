"""
Market Analysis Module
Provides comprehensive competitive and market analysis capabilities
"""

import json
import requests
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any, Tuple
import pandas as pd
import numpy as np
from dataclasses import dataclass, asdict
import logging

logger = logging.getLogger(__name__)

@dataclass
class CompanyProfile:
    """Represents a company profile with key metrics"""
    name: str
    industry: str
    market_cap: Optional[float] = None
    revenue: Optional[float] = None
    employees: Optional[int] = None
    founded_year: Optional[int] = None
    headquarters: Optional[str] = None
    website: Optional[str] = None
    description: Optional[str] = None
    key_products: List[str] = None
    strengths: List[str] = None
    weaknesses: List[str] = None
    opportunities: List[str] = None
    threats: List[str] = None

@dataclass
class MarketMetrics:
    """Represents market metrics and KPIs"""
    market_size: Optional[float] = None
    growth_rate: Optional[float] = None
    market_share: Dict[str, float] = None
    competitive_intensity: Optional[str] = None
    barriers_to_entry: List[str] = None
    key_trends: List[str] = None

class MarketAnalyzer:
    """Comprehensive market analysis engine"""
    
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Research-Agent/1.0 (Educational Purpose)'
        })
        
        # Financial data API configurations
        self.alpha_vantage_key = config.get('api_keys', {}).get('alpha_vantage')
        self.polygon_api_key = config.get('api_keys', {}).get('polygon_api')
    
    def analyze_company(self, company_name: str, industry: str = None) -> CompanyProfile:
        """
        Analyze a specific company and create a comprehensive profile
        
        Args:
            company_name: Name of the company to analyze
            industry: Industry sector (optional)
            
        Returns:
            CompanyProfile object with comprehensive analysis
        """
        logger.info(f"Analyzing company: {company_name}")
        
        # Search for company information
        company_data = self._gather_company_data(company_name, industry)
        
        # Perform SWOT analysis
        swot_analysis = self._perform_swot_analysis(company_name, industry)
        
        # Create company profile
        profile = CompanyProfile(
            name=company_name,
            industry=industry or company_data.get('industry', 'Unknown'),
            market_cap=company_data.get('market_cap'),
            revenue=company_data.get('revenue'),
            employees=company_data.get('employees'),
            founded_year=company_data.get('founded_year'),
            headquarters=company_data.get('headquarters'),
            website=company_data.get('website'),
            description=company_data.get('description'),
            key_products=company_data.get('key_products', []),
            strengths=swot_analysis.get('strengths', []),
            weaknesses=swot_analysis.get('weaknesses', []),
            opportunities=swot_analysis.get('opportunities', []),
            threats=swot_analysis.get('threats', [])
        )
        
        return profile
    
    def analyze_competitive_landscape(self, industry: str, 
                                    focus_company: str = None) -> Dict[str, Any]:
        """
        Analyze the competitive landscape for an industry
        
        Args:
            industry: Industry to analyze
            focus_company: Specific company to focus on (optional)
            
        Returns:
            Dictionary containing competitive analysis
        """
        logger.info(f"Analyzing competitive landscape for: {industry}")
        
        # Identify key competitors
        competitors = self._identify_competitors(industry, focus_company)
        
        # Analyze market share
        market_share = self._analyze_market_share(industry, competitors)
        
        # Identify key differentiators
        differentiators = self._identify_differentiators(competitors)
        
        # Analyze competitive positioning
        positioning = self._analyze_competitive_positioning(competitors)
        
        analysis = {
            'industry': industry,
            'focus_company': focus_company,
            'competitors': [asdict(comp) for comp in competitors],
            'market_share': market_share,
            'key_differentiators': differentiators,
            'competitive_positioning': positioning,
            'analysis_date': datetime.now().isoformat(),
            'total_competitors': len(competitors)
        }
        
        return analysis
    
    def analyze_market_opportunities(self, industry: str, 
                                   geographic_scope: str = 'global') -> Dict[str, Any]:
        """
        Identify market opportunities within an industry
        
        Args:
            industry: Industry to analyze
            geographic_scope: Geographic scope of analysis
            
        Returns:
            Dictionary containing market opportunity analysis
        """
        logger.info(f"Analyzing market opportunities for: {industry}")
        
        # Market size analysis
        market_size = self._analyze_market_size(industry, geographic_scope)
        
        # Growth potential analysis
        growth_potential = self._analyze_growth_potential(industry)
        
        # Emerging segments
        emerging_segments = self._identify_emerging_segments(industry)
        
        # Investment trends
        investment_trends = self._analyze_investment_trends(industry)
        
        opportunities = {
            'industry': industry,
            'geographic_scope': geographic_scope,
            'market_size': market_size,
            'growth_potential': growth_potential,
            'emerging_segments': emerging_segments,
            'investment_trends': investment_trends,
            'analysis_date': datetime.now().isoformat()
        }
        
        return opportunities
    
    def perform_porter_five_forces(self, industry: str) -> Dict[str, Any]:
        """
        Perform Porter's Five Forces analysis for an industry
        
        Args:
            industry: Industry to analyze
            
        Returns:
            Dictionary containing Five Forces analysis
        """
        logger.info(f"Performing Porter's Five Forces analysis for: {industry}")
        
        five_forces = {
            'industry': industry,
            'threat_of_new_entrants': self._analyze_threat_of_new_entrants(industry),
            'bargaining_power_of_suppliers': self._analyze_supplier_power(industry),
            'bargaining_power_of_buyers': self._analyze_buyer_power(industry),
            'threat_of_substitutes': self._analyze_threat_of_substitutes(industry),
            'competitive_rivalry': self._analyze_competitive_rivalry(industry),
            'overall_attractiveness': self._calculate_industry_attractiveness(industry),
            'analysis_date': datetime.now().isoformat()
        }
        
        return five_forces
    
    def _gather_company_data(self, company_name: str, industry: str) -> Dict[str, Any]:
        """Gather comprehensive company data from multiple sources"""
        # Mock implementation - in real scenario, would integrate with company databases
        mock_data = {
            'industry': industry or 'Technology',
            'market_cap': np.random.uniform(1e9, 1e12),  # Random market cap
            'revenue': np.random.uniform(1e8, 1e11),     # Random revenue
            'employees': np.random.randint(100, 100000), # Random employee count
            'founded_year': np.random.randint(1990, 2020), # Random founding year
            'headquarters': 'San Francisco, CA',
            'website': f'https://{company_name.lower().replace(" ", "")}.com',
            'description': f'{company_name} is a leading company in the {industry or "technology"} sector.',
            'key_products': ['Product A', 'Product B', 'Product C']
        }
        
        return mock_data
    
    def _perform_swot_analysis(self, company_name: str, industry: str) -> Dict[str, List[str]]:
        """Perform SWOT analysis for a company"""
        # Mock SWOT analysis - in real scenario, would analyze actual data
        swot = {
            'strengths': [
                'Strong brand recognition',
                'Innovative product portfolio',
                'Experienced management team',
                'Strong financial position'
            ],
            'weaknesses': [
                'Limited international presence',
                'High dependence on key customers',
                'Regulatory compliance challenges'
            ],
            'opportunities': [
                'Market expansion opportunities',
                'Technology advancement trends',
                'Strategic partnerships',
                'Emerging market growth'
            ],
            'threats': [
                'Intense competition',
                'Economic uncertainty',
                'Regulatory changes',
                'Technology disruption'
            ]
        }
        
        return swot
    
    def _identify_competitors(self, industry: str, focus_company: str) -> List[CompanyProfile]:
        """Identify key competitors in the industry"""
        # Mock competitor identification - in real scenario, would use industry databases
        competitor_names = [
            f"{industry} Leader Inc.",
            f"{industry} Solutions Corp",
            f"{industry} Technologies Ltd",
            f"{industry} Innovations Inc"
        ]
        
        if focus_company:
            competitor_names = [name for name in competitor_names if name != focus_company]
        
        competitors = []
        for name in competitor_names[:4]:  # Limit to top 4 competitors
            profile = self.analyze_company(name, industry)
            competitors.append(profile)
        
        return competitors
    
    def _analyze_market_share(self, industry: str, competitors: List[CompanyProfile]) -> Dict[str, float]:
        """Analyze market share distribution"""
        # Mock market share analysis
        total_market_share = 100.0
        competitor_count = len(competitors)
        
        # Generate realistic market share distribution
        shares = np.random.dirichlet(np.ones(competitor_count)) * total_market_share
        
        market_share = {}
        for i, competitor in enumerate(competitors):
            market_share[competitor.name] = round(shares[i], 2)
        
        # Add "Others" category for remaining market
        others_share = total_market_share - sum(market_share.values())
        if others_share > 0:
            market_share['Others'] = round(others_share, 2)
        
        return market_share
    
    def _identify_differentiators(self, competitors: List[CompanyProfile]) -> Dict[str, List[str]]:
        """Identify key differentiators among competitors"""
        differentiators = {}
        
        for competitor in competitors:
            differentiators[competitor.name] = [
                f"Unique {competitor.name} advantage 1",
                f"Distinctive {competitor.name} feature 2",
                f"Competitive {competitor.name} strength 3"
            ]
        
        return differentiators
    
    def _analyze_competitive_positioning(self, competitors: List[CompanyProfile]) -> Dict[str, str]:
        """Analyze competitive positioning"""
        positioning = {}
        
        positions = ['Market Leader', 'Challenger', 'Follower', 'Niche Player']
        
        for i, competitor in enumerate(competitors):
            positioning[competitor.name] = positions[i % len(positions)]
        
        return positioning
    
    def _analyze_market_size(self, industry: str, geographic_scope: str) -> Dict[str, Any]:
        """Analyze market size and segmentation"""
        # Mock market size analysis
        base_size = np.random.uniform(10e9, 1000e9)  # Random market size
        
        market_size = {
            'total_market_size': base_size,
            'currency': 'USD',
            'geographic_scope': geographic_scope,
            'segments': {
                'Enterprise': base_size * 0.4,
                'SMB': base_size * 0.3,
                'Consumer': base_size * 0.3
            }
        }
        
        return market_size
    
    def _analyze_growth_potential(self, industry: str) -> Dict[str, Any]:
        """Analyze growth potential and trends"""
        # Mock growth analysis
        growth_potential = {
            'cagr_5_year': np.random.uniform(5, 25),  # 5-25% CAGR
            'growth_drivers': [
                'Technology advancement',
                'Market expansion',
                'Regulatory support',
                'Consumer demand growth'
            ],
            'growth_barriers': [
                'Market saturation',
                'Regulatory constraints',
                'Economic uncertainty'
            ],
            'forecast_period': '2024-2029'
        }
        
        return growth_potential
    
    def _identify_emerging_segments(self, industry: str) -> List[Dict[str, Any]]:
        """Identify emerging market segments"""
        # Mock emerging segments
        segments = [
            {
                'segment_name': f'{industry} AI Solutions',
                'growth_rate': '45%',
                'market_size': '2.5B',
                'key_players': ['Company A', 'Company B'],
                'opportunity_level': 'High'
            },
            {
                'segment_name': f'{industry} Sustainability',
                'growth_rate': '32%',
                'market_size': '1.8B',
                'key_players': ['Company C', 'Company D'],
                'opportunity_level': 'Medium'
            }
        ]
        
        return segments
    
    def _analyze_investment_trends(self, industry: str) -> Dict[str, Any]:
        """Analyze investment trends in the industry"""
        # Mock investment analysis
        investment_trends = {
            'total_investment_2024': np.random.uniform(1e9, 50e9),
            'investment_growth_rate': np.random.uniform(10, 50),
            'top_investors': ['VC Fund A', 'VC Fund B', 'Corporate VC C'],
            'investment_focus': [
                'AI and Machine Learning',
                'Sustainability Solutions',
                'Digital Transformation'
            ],
            'average_deal_size': np.random.uniform(1e6, 100e6)
        }
        
        return investment_trends
    
    def _analyze_threat_of_new_entrants(self, industry: str) -> Dict[str, Any]:
        """Analyze threat of new entrants"""
        return {
            'level': 'Medium',
            'barriers': ['High capital requirements', 'Regulatory compliance', 'Brand loyalty'],
            'score': 6,  # 1-10 scale
            'description': 'Moderate barriers to entry due to capital and regulatory requirements'
        }
    
    def _analyze_supplier_power(self, industry: str) -> Dict[str, Any]:
        """Analyze bargaining power of suppliers"""
        return {
            'level': 'Low',
            'factors': ['Many suppliers available', 'Low switching costs', 'Standardized inputs'],
            'score': 3,  # 1-10 scale
            'description': 'Low supplier power due to competitive supplier market'
        }
    
    def _analyze_buyer_power(self, industry: str) -> Dict[str, Any]:
        """Analyze bargaining power of buyers"""
        return {
            'level': 'High',
            'factors': ['Price sensitivity', 'Many alternatives', 'Low switching costs'],
            'score': 8,  # 1-10 scale
            'description': 'High buyer power due to price sensitivity and alternatives'
        }
    
    def _analyze_threat_of_substitutes(self, industry: str) -> Dict[str, Any]:
        """Analyze threat of substitutes"""
        return {
            'level': 'Medium',
            'substitutes': ['Alternative technology', 'Traditional solutions', 'DIY approaches'],
            'score': 5,  # 1-10 scale
            'description': 'Moderate threat from alternative solutions and technologies'
        }
    
    def _analyze_competitive_rivalry(self, industry: str) -> Dict[str, Any]:
        """Analyze competitive rivalry"""
        return {
            'level': 'High',
            'factors': ['Many competitors', 'Slow market growth', 'High exit barriers'],
            'score': 8,  # 1-10 scale
            'description': 'High competitive rivalry due to market saturation and slow growth'
        }
    
    def _calculate_industry_attractiveness(self, industry: str) -> str:
        """Calculate overall industry attractiveness"""
        # Mock calculation based on Five Forces scores
        scores = [6, 3, 8, 5, 8]  # Average scores from Five Forces
        avg_score = sum(scores) / len(scores)
        
        if avg_score <= 4:
            return 'Low'
        elif avg_score <= 7:
            return 'Medium'
        else:
            return 'High'
    
    def export_analysis_to_excel(self, analysis_data: Dict[str, Any], filename: str) -> str:
        """Export analysis data to Excel format"""
        try:
            with pd.ExcelWriter(filename, engine='openpyxl') as writer:
                # Export competitors data
                if 'competitors' in analysis_data:
                    competitors_df = pd.DataFrame(analysis_data['competitors'])
                    competitors_df.to_excel(writer, sheet_name='Competitors', index=False)
                
                # Export market share data
                if 'market_share' in analysis_data:
                    market_share_df = pd.DataFrame(
                        list(analysis_data['market_share'].items()),
                        columns=['Company', 'Market Share (%)']
                    )
                    market_share_df.to_excel(writer, sheet_name='Market Share', index=False)
                
                # Export summary
                summary_data = {
                    'Metric': ['Industry', 'Analysis Date', 'Total Competitors'],
                    'Value': [
                        analysis_data.get('industry', 'N/A'),
                        analysis_data.get('analysis_date', 'N/A'),
                        analysis_data.get('total_competitors', 0)
                    ]
                }
                summary_df = pd.DataFrame(summary_data)
                summary_df.to_excel(writer, sheet_name='Summary', index=False)
            
            return f"Analysis exported to {filename}"
        except Exception as e:
            return f"Export failed: {str(e)}"
