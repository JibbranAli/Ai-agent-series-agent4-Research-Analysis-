#!/usr/bin/env python3
"""
Test Suite for Research & Analysis Agent
Basic functionality tests to verify system integrity
"""

import unittest
import json
import sys
import os
from datetime import datetime

# Add the current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

class TestResearchAgent(unittest.TestCase):
    """Test cases for Research Agent functionality"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.config = {
            "agent_name": "Research & Analysis Agent",
            "version": "1.0.0",
            "credible_domains": {
                "news": ["reuters.com", "bloomberg.com", "wsj.com"],
                "reports": ["mckinsey.com", "deloitte.com", "pwc.com"]
            }
        }
        
        # Import modules
        try:
            from research_agent import ResearchAgent
            from web_research import WebResearchEngine
            from market_analysis import MarketAnalyzer
            from trend_tracking import TrendTracker
            from data_structuring import DataStructurer
            from reporting import ReportGenerator, ReportConfig
        except ImportError as e:
            self.skipTest(f"Required modules not available: {e}")
        
        self.agent = ResearchAgent()
        self.web_research = WebResearchEngine(self.config)
        self.market_analyzer = MarketAnalyzer(self.config)
        self.trend_tracker = TrendTracker(self.config)
        self.data_structurer = DataStructurer(self.config)
        self.report_generator = ReportGenerator(self.config)
    
    def test_research_agent_initialization(self):
        """Test ResearchAgent initialization"""
        self.assertIsNotNone(self.agent)
        self.assertIsInstance(self.agent.session, type(self.agent.session))
    
    def test_web_research_initialization(self):
        """Test WebResearchEngine initialization"""
        self.assertIsNotNone(self.web_research)
        self.assertIsInstance(self.web_research.config, dict)
    
    def test_market_analyzer_initialization(self):
        """Test MarketAnalyzer initialization"""
        self.assertIsNotNone(self.market_analyzer)
        self.assertIsInstance(self.market_analyzer.config, dict)
    
    def test_trend_tracker_initialization(self):
        """Test TrendTracker initialization"""
        self.assertIsNotNone(self.trend_tracker)
        self.assertIsInstance(self.trend_tracker.config, dict)
    
    def test_data_structurer_initialization(self):
        """Test DataStructurer initialization"""
        self.assertIsNotNone(self.data_structurer)
        self.assertIsInstance(self.data_structurer.config, dict)
    
    def test_report_generator_initialization(self):
        """Test ReportGenerator initialization"""
        self.assertIsNotNone(self.report_generator)
        self.assertIsInstance(self.report_generator.config, dict)
    
    def test_web_search_functionality(self):
        """Test web search functionality"""
        try:
            sources = self.web_research.search_web_content("test query", "news", 5)
            self.assertIsInstance(sources, list)
            self.assertLessEqual(len(sources), 5)
        except Exception as e:
            self.fail(f"Web search failed: {e}")
    
    def test_source_credibility_verification(self):
        """Test source credibility verification"""
        credibility = self.web_research.verify_source_credibility("https://reuters.com/test")
        self.assertIsInstance(credibility, float)
        self.assertGreaterEqual(credibility, 0.0)
        self.assertLessEqual(credibility, 1.0)
    
    def test_company_analysis(self):
        """Test company analysis functionality"""
        try:
            profile = self.market_analyzer.analyze_company("Test Company", "Technology")
            self.assertIsNotNone(profile)
            self.assertEqual(profile.name, "Test Company")
            self.assertEqual(profile.industry, "Technology")
        except Exception as e:
            self.fail(f"Company analysis failed: {e}")
    
    def test_competitive_landscape_analysis(self):
        """Test competitive landscape analysis"""
        try:
            analysis = self.market_analyzer.analyze_competitive_landscape("Technology", "Test Company")
            self.assertIsInstance(analysis, dict)
            self.assertIn('industry', analysis)
            self.assertIn('competitors', analysis)
        except Exception as e:
            self.fail(f"Competitive analysis failed: {e}")
    
    def test_trend_tracking(self):
        """Test trend tracking functionality"""
        try:
            trends = self.trend_tracker.track_trends("Technology", "6months", 5)
            self.assertIsNotNone(trends)
            self.assertIn('topic', trends.__dict__)
            self.assertIn('trends', trends.__dict__)
        except Exception as e:
            self.fail(f"Trend tracking failed: {e}")
    
    def test_data_table_creation(self):
        """Test data table creation"""
        try:
            test_data = [
                {"name": "Company A", "revenue": 1000000},
                {"name": "Company B", "revenue": 2000000}
            ]
            table = self.data_structurer.create_comparison_table(test_data, ["name", "revenue"])
            self.assertIsNotNone(table)
            self.assertEqual(len(table.columns), 2)
            self.assertEqual(len(table.data), 2)
        except Exception as e:
            self.fail(f"Data table creation failed: {e}")
    
    def test_chart_generation(self):
        """Test chart generation"""
        try:
            from data_structuring import ChartConfig
            test_data = {"Company A": 100, "Company B": 200}
            config = ChartConfig(
                chart_type="bar",
                title="Test Chart",
                x_axis="Companies",
                y_axis="Values",
                color_scheme="default",
                width=600,
                height=400,
                show_legend=True,
                show_grid=True
            )
            chart = self.data_structurer.generate_bar_chart(test_data, config)
            self.assertIsInstance(chart, dict)
            self.assertIn('chart_type', chart)
            self.assertIn('title', chart)
        except Exception as e:
            self.fail(f"Chart generation failed: {e}")
    
    def test_report_config_creation(self):
        """Test report configuration creation"""
        try:
            config = ReportConfig(
                title="Test Report",
                subtitle="Test Subtitle",
                format="markdown"
            )
            self.assertEqual(config.title, "Test Report")
            self.assertEqual(config.subtitle, "Test Subtitle")
            self.assertEqual(config.format, "markdown")
        except Exception as e:
            self.fail(f"Report config creation failed: {e}")
    
    def test_executive_summary_generation(self):
        """Test executive summary generation"""
        try:
            test_data = {
                'market_share': {'Company A': 50, 'Company B': 30},
                'trends': [{'name': 'Trend 1', 'growth_rate': 25}],
                'competitors': [{'name': 'Competitor 1'}]
            }
            summary = self.report_generator.generate_executive_summary(test_data)
            self.assertIsInstance(summary, str)
            self.assertGreater(len(summary), 0)
        except Exception as e:
            self.fail(f"Executive summary generation failed: {e}")
    
    def test_config_loading(self):
        """Test configuration loading"""
        try:
            # Test with valid config
            self.assertIsInstance(self.config, dict)
            self.assertIn('agent_name', self.config)
            self.assertIn('credible_domains', self.config)
        except Exception as e:
            self.fail(f"Config loading failed: {e}")
    
    def test_data_export_functionality(self):
        """Test data export functionality"""
        try:
            test_data = {
                'competitors': [
                    {'name': 'Company A', 'revenue': 1000000},
                    {'name': 'Company B', 'revenue': 2000000}
                ]
            }
            result = self.data_structurer.export_to_json(test_data, "test_export.json")
            self.assertIn("exported", result.lower())
            
            # Clean up test file
            if os.path.exists("test_export.json"):
                os.remove("test_export.json")
        except Exception as e:
            self.fail(f"Data export failed: {e}")

class TestIntegration(unittest.TestCase):
    """Integration tests for the complete system"""
    
    def setUp(self):
        """Set up integration test fixtures"""
        self.config = {
            "agent_name": "Research & Analysis Agent",
            "version": "1.0.0",
            "credible_domains": {
                "news": ["reuters.com", "bloomberg.com", "wsj.com"],
                "reports": ["mckinsey.com", "deloitte.com", "pwc.com"]
            }
        }
    
    def test_end_to_end_market_analysis(self):
        """Test complete market analysis workflow"""
        try:
            from market_analysis import MarketAnalyzer
            from trend_tracking import TrendTracker
            from reporting import ReportGenerator, ReportConfig
            
            market_analyzer = MarketAnalyzer(self.config)
            trend_tracker = TrendTracker(self.config)
            report_generator = ReportGenerator(self.config)
            
            # Perform market analysis
            market_analysis = market_analyzer.analyze_competitive_landscape("Technology")
            
            # Track trends
            trends = trend_tracker.track_trends("Technology", "6months", 3)
            
            # Generate report
            config = ReportConfig(
                title="Technology Market Analysis",
                format="markdown"
            )
            
            report_data = {
                'market_analysis': market_analysis,
                'trends': trends.__dict__
            }
            
            report_file = report_generator.generate_report(report_data, config)
            
            # Verify report was created
            self.assertTrue(os.path.exists(report_file))
            
            # Clean up
            if os.path.exists(report_file):
                os.remove(report_file)
                
        except Exception as e:
            self.fail(f"End-to-end market analysis failed: {e}")
    
    def test_data_flow_integrity(self):
        """Test data flow through the system"""
        try:
            from web_research import WebResearchEngine
            from data_structuring import DataStructurer
            
            web_research = WebResearchEngine(self.config)
            data_structurer = DataStructurer(self.config)
            
            # Search for data
            search_results = web_research.search_web_content("test query", "news", 3)
            
            # Structure the data
            structured_data = {
                'search_results': search_results,
                'analysis_date': datetime.now().isoformat()
            }
            
            structured_output = data_structurer.structure_research_data(structured_data)
            
            # Verify data integrity
            self.assertIsNotNone(structured_output)
            self.assertIn('title', structured_output.__dict__)
            self.assertIn('summary', structured_output.__dict__)
            
        except Exception as e:
            self.fail(f"Data flow integrity test failed: {e}")

def run_tests():
    """Run all tests"""
    print("Running Research & Analysis Agent Tests")
    print("=" * 50)
    
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add test cases
    suite.addTests(loader.loadTestsFromTestCase(TestResearchAgent))
    suite.addTests(loader.loadTestsFromTestCase(TestIntegration))
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Print summary
    print("\n" + "=" * 50)
    print(f"Tests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    
    if result.failures:
        print("\nFailures:")
        for test, traceback in result.failures:
            print(f"  {test}: {traceback}")
    
    if result.errors:
        print("\nErrors:")
        for test, traceback in result.errors:
            print(f"  {test}: {traceback}")
    
    if result.wasSuccessful():
        print("\nAll tests passed!")
    else:
        print(f"\n{len(result.failures + result.errors)} test(s) failed")
    
    return result.wasSuccessful()

if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
