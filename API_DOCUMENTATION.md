# Research & Analysis Agent API Documentation

## Overview

The Research & Analysis Agent provides a comprehensive API for data gathering, analysis, and market research. This documentation covers all available classes, methods, and their usage.

## Core Classes

### ResearchAgent

Main agent class that orchestrates all research capabilities.

```python
from research_agent import ResearchAgent

agent = ResearchAgent()
```

#### Methods

##### `search_web_sources(query, content_type='all', max_results=10)`
Search for credible web sources based on query.

**Parameters:**
- `query` (str): Search query
- `content_type` (str): Type of content ('all', 'news', 'reports', 'journals')
- `max_results` (int): Maximum number of results to return

**Returns:** List[ResearchSource]

**Example:**
```python
sources = agent.search_web_sources("AI market trends", "news", 5)
```

##### `analyze_competitive_landscape(company_name, industry)`
Analyze competitive landscape for a given company.

**Parameters:**
- `company_name` (str): Name of the company to analyze
- `industry` (str): Industry sector

**Returns:** Dict[str, Any]

**Example:**
```python
analysis = agent.analyze_competitive_landscape("Tesla", "Electric Vehicles")
```

##### `track_trends(topic, timeframe='6months')`
Track trends for a given topic.

**Parameters:**
- `topic` (str): Topic to track trends for
- `timeframe` (str): Time period for trend analysis

**Returns:** Dict[str, Any]

**Example:**
```python
trends = agent.track_trends("Artificial Intelligence", "12months")
```

##### `generate_market_report(sector, report_type='comprehensive')`
Generate a comprehensive market report.

**Parameters:**
- `sector` (str): Market sector to analyze
- `report_type` (str): Type of report ('comprehensive', 'summary', 'trends')

**Returns:** str (Markdown formatted report)

**Example:**
```python
report = agent.generate_market_report("Fintech", "comprehensive")
```

### WebResearchEngine

Enhanced web research engine with real API integrations.

```python
from web_research import WebResearchEngine

web_research = WebResearchEngine(config)
```

#### Methods

##### `search_web_content(query, content_type='all', max_results=10)`
Search web content using multiple sources.

**Parameters:**
- `query` (str): Search query
- `content_type` (str): Type of content to search for
- `max_results` (int): Maximum number of results

**Returns:** List[Dict[str, Any]]

**Example:**
```python
results = web_research.search_web_content("climate tech funding", "news", 10)
```

##### `extract_content_from_url(url)`
Extract content from a given URL.

**Parameters:**
- `url` (str): URL to extract content from

**Returns:** Dict[str, Any]

**Example:**
```python
content = web_research.extract_content_from_url("https://example.com/article")
```

##### `verify_source_credibility(url)`
Verify the credibility of a source based on domain reputation.

**Parameters:**
- `url` (str): URL to verify

**Returns:** float (credibility score 0-1)

**Example:**
```python
credibility = web_research.verify_source_credibility("https://reuters.com/article")
```

### MarketAnalyzer

Comprehensive market analysis engine.

```python
from market_analysis import MarketAnalyzer

market_analyzer = MarketAnalyzer(config)
```

#### Methods

##### `analyze_company(company_name, industry=None)`
Analyze a specific company and create a comprehensive profile.

**Parameters:**
- `company_name` (str): Name of the company to analyze
- `industry` (str): Industry sector (optional)

**Returns:** CompanyProfile

**Example:**
```python
profile = market_analyzer.analyze_company("Tesla", "Electric Vehicles")
```

##### `analyze_competitive_landscape(industry, focus_company=None)`
Analyze the competitive landscape for an industry.

**Parameters:**
- `industry` (str): Industry to analyze
- `focus_company` (str): Specific company to focus on (optional)

**Returns:** Dict[str, Any]

**Example:**
```python
landscape = market_analyzer.analyze_competitive_landscape("AI", "OpenAI")
```

##### `analyze_market_opportunities(industry, geographic_scope='global')`
Identify market opportunities within an industry.

**Parameters:**
- `industry` (str): Industry to analyze
- `geographic_scope` (str): Geographic scope of analysis

**Returns:** Dict[str, Any]

**Example:**
```python
opportunities = market_analyzer.analyze_market_opportunities("Fintech", "India")
```

##### `perform_porter_five_forces(industry)`
Perform Porter's Five Forces analysis for an industry.

**Parameters:**
- `industry` (str): Industry to analyze

**Returns:** Dict[str, Any]

**Example:**
```python
five_forces = market_analyzer.perform_porter_five_forces("Electric Vehicles")
```

### TrendTracker

Advanced trend tracking and analysis engine.

```python
from trend_tracking import TrendTracker

trend_tracker = TrendTracker(config)
```

#### Methods

##### `track_trends(topic, timeframe='6months', max_trends=10)`
Track and analyze trends for a given topic.

**Parameters:**
- `topic` (str): Topic to track trends for
- `timeframe` (str): Time period for trend analysis
- `max_trends` (int): Maximum number of trends to identify

**Returns:** TrendAnalysis

**Example:**
```python
trends = trend_tracker.track_trends("Artificial Intelligence", "12months", 5)
```

##### `analyze_emerging_technologies(industry)`
Analyze emerging technologies in a specific industry.

**Parameters:**
- `industry` (str): Industry to analyze

**Returns:** List[Trend]

**Example:**
```python
tech_trends = trend_tracker.analyze_emerging_technologies("Healthcare")
```

##### `predict_trend_evolution(trend_name, prediction_horizon='12months')`
Predict the evolution of a specific trend.

**Parameters:**
- `trend_name` (str): Name of the trend to predict
- `prediction_horizon` (str): Time horizon for prediction

**Returns:** Dict[str, Any]

**Example:**
```python
prediction = trend_tracker.predict_trend_evolution("AI", "18months")
```

##### `monitor_trend_sentiment(trend_name, sources=None)`
Monitor sentiment around a specific trend.

**Parameters:**
- `trend_name` (str): Name of the trend to monitor
- `sources` (List[str]): List of sources to monitor (optional)

**Returns:** Dict[str, Any]

**Example:**
```python
sentiment = trend_tracker.monitor_trend_sentiment("Blockchain")
```

### DataStructurer

Advanced data structuring and formatting engine.

```python
from data_structuring import DataStructurer

data_structurer = DataStructurer(config)
```

#### Methods

##### `structure_research_data(research_data, output_type='comprehensive')`
Structure research data into organized output.

**Parameters:**
- `research_data` (Dict[str, Any]): Raw research data
- `output_type` (str): Type of output ('comprehensive', 'summary', 'detailed')

**Returns:** StructuredOutput

**Example:**
```python
structured = data_structurer.structure_research_data(market_data, "comprehensive")
```

##### `create_comparison_table(entities, comparison_fields)`
Create a comparison table for multiple entities.

**Parameters:**
- `entities` (List[Dict[str, Any]]): List of entities to compare
- `comparison_fields` (List[str]): Fields to compare

**Returns:** DataTable

**Example:**
```python
table = data_structurer.create_comparison_table(companies, ['name', 'revenue', 'employees'])
```

##### `create_summary_statistics(data, numeric_fields)`
Create summary statistics table.

**Parameters:**
- `data` (List[Dict[str, Any]]): Raw data
- `numeric_fields` (List[str]): Fields to calculate statistics for

**Returns:** DataTable

**Example:**
```python
stats = data_structurer.create_summary_statistics(financial_data, ['revenue', 'profit'])
```

##### `generate_bar_chart(data, config)`
Generate bar chart visualization.

**Parameters:**
- `data` (Dict[str, Any]): Data to visualize
- `config` (ChartConfig): Chart configuration

**Returns:** Dict[str, Any]

**Example:**
```python
chart = data_structurer.generate_bar_chart(market_share_data, chart_config)
```

### ReportGenerator

Comprehensive report generation engine.

```python
from reporting import ReportGenerator, ReportConfig

report_generator = ReportGenerator(config)
```

#### Methods

##### `generate_report(structured_data, report_config)`
Generate comprehensive report.

**Parameters:**
- `structured_data` (Dict[str, Any]): Structured research data
- `report_config` (ReportConfig): Report configuration

**Returns:** str (Path to generated report file)

**Example:**
```python
config = ReportConfig(title="Market Analysis", format="pdf")
report_file = report_generator.generate_report(data, config)
```

##### `generate_executive_summary(structured_data)`
Generate executive summary.

**Parameters:**
- `structured_data` (Dict[str, Any]): Structured research data

**Returns:** str (Executive summary text)

**Example:**
```python
summary = report_generator.generate_executive_summary(market_data)
```

##### `generate_market_brief(market_data)`
Generate market brief report.

**Parameters:**
- `market_data` (Dict[str, Any]): Market analysis data

**Returns:** str (Path to generated market brief)

**Example:**
```python
brief_file = report_generator.generate_market_brief(fintech_data)
```

## Data Classes

### ResearchSource
Represents a research source with metadata.

```python
@dataclass
class ResearchSource:
    title: str
    url: str
    domain: str
    publication_date: str
    content_type: str
    credibility_score: float
```

### CompanyProfile
Represents a company profile with key metrics.

```python
@dataclass
class CompanyProfile:
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
```

### Trend
Represents a trend with key metrics.

```python
@dataclass
class Trend:
    name: str
    category: str
    description: str
    growth_rate: float
    adoption_level: str
    impact_level: str
    timeframe: str
    key_indicators: List[str]
    supporting_evidence: List[str]
    sources: List[str]
    confidence_score: float
    first_detected: str
    last_updated: str
```

### ReportConfig
Configuration for report generation.

```python
@dataclass
class ReportConfig:
    title: str
    subtitle: Optional[str] = None
    author: str = "Research & Analysis Agent"
    company: str = "Research Agency"
    format: str = "markdown"
    template: str = "default"
    include_charts: bool = True
    include_tables: bool = True
    include_sources: bool = True
    page_size: str = "A4"
    font_size: int = 12
    color_scheme: str = "professional"
```

## Configuration

### API Keys
Configure API keys in `config.json`:

```json
{
    "api_keys": {
        "news_api": "YOUR_NEWS_API_KEY",
        "polygon_api": "YOUR_POLYGON_API_KEY",
        "alpha_vantage": "YOUR_ALPHA_VANTAGE_KEY"
    }
}
```

### Credible Domains
Customize trusted sources:

```json
{
    "credible_domains": {
        "news": ["reuters.com", "bloomberg.com", "wsj.com"],
        "reports": ["mckinsey.com", "deloitte.com", "pwc.com"],
        "journals": ["nature.com", "science.org"],
        "government": ["sec.gov", "federalreserve.gov"]
    }
}
```

## Error Handling

All methods include comprehensive error handling:

```python
try:
    analysis = market_analyzer.analyze_company("Tesla", "EV")
except Exception as e:
    logger.error(f"Analysis failed: {str(e)}")
    # Handle error appropriately
```

## Rate Limiting

The WebResearchEngine includes built-in rate limiting:

```python
# Automatically handles rate limiting
results = web_research.search_web_content("query", max_results=100)
```

## Output Formats

### Markdown
```python
config = ReportConfig(format="markdown")
report = report_generator.generate_report(data, config)
```

### PDF
```python
config = ReportConfig(format="pdf")
report = report_generator.generate_report(data, config)
```

### Excel
```python
config = ReportConfig(format="excel")
report = report_generator.generate_report(data, config)
```

### JSON
```python
structured = data_structurer.structure_research_data(data)
json_output = json.dumps(asdict(structured), indent=2)
```

## Best Practices

1. **Always handle exceptions** when calling API methods
2. **Use appropriate timeouts** for web requests
3. **Respect rate limits** for external APIs
4. **Validate input data** before processing
5. **Use structured outputs** for consistent data handling
6. **Include source citations** in all reports
7. **Regularly update** credible domain lists
8. **Monitor API usage** and costs

## Examples

### Complete Market Analysis
```python
# Initialize components
market_analyzer = MarketAnalyzer(config)
trend_tracker = TrendTracker(config)
report_generator = ReportGenerator(config)

# Analyze market
market_analysis = market_analyzer.analyze_competitive_landscape("AI", "OpenAI")
trends = trend_tracker.track_trends("Artificial Intelligence", "12months")

# Generate report
config = ReportConfig(
    title="AI Market Analysis",
    format="pdf"
)
report_file = report_generator.generate_report({
    'market_analysis': market_analysis,
    'trends': trends
}, config)
```

### Trend Monitoring
```python
# Track and predict trends
trends = trend_tracker.track_trends("Climate Tech", "6months")
prediction = trend_tracker.predict_trend_evolution("Climate Tech", "12months")
sentiment = trend_tracker.monitor_trend_sentiment("Climate Tech")

# Export results
data_structurer.export_trends_to_csv(trends, "climate_trends.csv")
```

This documentation provides comprehensive coverage of the Research & Analysis Agent API. For additional examples and use cases, refer to the `examples.py` file.
