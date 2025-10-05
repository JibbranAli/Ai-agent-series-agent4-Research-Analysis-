# 🔍 How to Enter Queries - Complete User Guide

## 📋 **All Ways to Enter Queries**

### **1. 🖥️ Interactive Menu Interface (Recommended)**
**File**: `query_interface.py`

**How to use**:
```bash
python query_interface.py
```

**Features**:
- ✅ User-friendly menu system
- ✅ Step-by-step guidance
- ✅ Multiple query types
- ✅ Real-time results
- ✅ Help system included

**Example**:
```
🔍 Research & Analysis Agent - Query Interface
============================================================
Created by: Syed Jibbran Ali
============================================================

📋 Available Query Types:
1. 🔍 Company Research
2. 📊 Market Analysis
3. 📈 Trend Tracking
4. 🏢 Competitor Analysis
5. 💰 Investment Research
6. 📰 News Search
7. 📋 Generate Report
8. ❓ Help
9. 🚪 Exit

🎯 Enter your choice (1-9): 1
Enter company name: Tesla
```

### **2. ⚡ Quick Command Line Interface**
**File**: `query_quick.py`

**How to use**:
```bash
python query_quick.py <command> <query>
```

**Available Commands**:
- `company <name>` - Research a company
- `market <industry>` - Analyze a market
- `trends <topic>` - Track trends
- `competitors <name>` - Find competitors
- `news <query>` - Search news
- `investment <name>` - Investment research

**Examples**:
```bash
# Research Tesla
python query_quick.py company Tesla

# Analyze EV market
python query_quick.py market Electric Vehicles

# Track AI trends
python query_quick.py trends AI

# Find Tesla competitors
python query_quick.py competitors Tesla

# Search Tesla news
python query_quick.py news Tesla

# Investment research for Apple
python query_quick.py investment Apple
```

### **3. 🐍 Python Code Interface**
**File**: `research_agent.py`

**How to use**:
```python
from research_agent import ResearchAgent

agent = ResearchAgent()

# Research company
info = agent.research_company("Tesla")
print(f"Tesla Market Cap: ${info['market_cap']:,}")

# Analyze market
market = agent.analyze_market("Electric Vehicles")
print(f"Market Size: ${market['market_size']:,}")

# Track trends
trends = agent.track_trends("AI")
print(f"Found {len(trends)} trends")

# Find competitors
competitors = agent.find_competitors("Tesla")
print(f"Found {len(competitors)} competitors")

# Generate report
report = agent.create_report("Tesla Analysis", {'company': info})
agent.save_report(report, "tesla_report.md")
```

### **4. 🎯 Individual Module Interface**
**Files**: `web_search.py`, `market_analyzer.py`, `trend_tracker.py`, `report_generator.py`

**How to use**:
```python
# Web search
from web_search import WebSearch
search = WebSearch()
results = search.find_info("Tesla news", 5)

# Market analysis
from market_analyzer import MarketAnalyzer
analyzer = MarketAnalyzer()
analysis = analyzer.analyze_company("Tesla")

# Trend tracking
from trend_tracker import TrendTracker
tracker = TrendTracker()
trends = tracker.find_trends("AI", 5)

# Report generation
from report_generator import ReportGenerator
generator = ReportGenerator()
report = generator.create_report("Analysis", data)
```

### **5. 📊 Demo and Examples**
**Files**: `demo.py`, `examples.py`

**How to use**:
```bash
# Run demo
python demo.py

# Run examples
python examples.py
```

## 🎯 **Query Types Available**

### **Company Research**
- **What**: Analyze any company's financials, strengths, opportunities
- **Examples**: Tesla, Apple, Microsoft, Google
- **Output**: Market cap, revenue, employees, strengths, opportunities

### **Market Analysis**
- **What**: Study industry trends, size, key players
- **Examples**: Electric Vehicles, Technology, Healthcare, Finance
- **Output**: Market size, growth rate, key players, trends

### **Trend Tracking**
- **What**: Identify and predict market trends
- **Examples**: AI, Blockchain, Electric Vehicles, Fintech
- **Output**: Current trends, growth rates, future predictions

### **Competitor Analysis**
- **What**: Find and compare competitors
- **Examples**: Tesla competitors, Apple competitors
- **Output**: Competitor list, market share, revenue comparison

### **Investment Research**
- **What**: Evaluate investment opportunities
- **Examples**: Tesla investment, Apple investment
- **Output**: Financial metrics, market analysis, investment assessment

### **News Search**
- **What**: Find recent news and articles
- **Examples**: Tesla news, AI news, market news
- **Output**: News articles, sources, credibility scores

### **Report Generation**
- **What**: Create professional reports
- **Examples**: Company reports, market reports, investment reports
- **Output**: Markdown, PDF, HTML reports

## 🚀 **Quick Start Guide**

### **For Beginners**:
1. **Start with**: `python query_interface.py`
2. **Choose**: Option 1 (Company Research)
3. **Enter**: Company name (e.g., "Tesla")
4. **View**: Results immediately

### **For Advanced Users**:
1. **Use**: `python query_quick.py company Tesla`
2. **Or**: Import modules in Python code
3. **Customize**: Create your own analysis scripts

### **For Developers**:
1. **Import**: `from research_agent import ResearchAgent`
2. **Create**: Custom analysis workflows
3. **Extend**: Add new analysis modules

## 📝 **Query Examples**

### **Company Queries**:
```bash
python query_quick.py company Tesla
python query_quick.py company Apple
python query_quick.py company Microsoft
python query_quick.py company Google
```

### **Market Queries**:
```bash
python query_quick.py market Electric Vehicles
python query_quick.py market Technology
python query_quick.py market Healthcare
python query_quick.py market Finance
```

### **Trend Queries**:
```bash
python query_quick.py trends AI
python query_quick.py trends Blockchain
python query_quick.py trends Electric Vehicles
python query_quick.py trends Fintech
```

### **News Queries**:
```bash
python query_quick.py news Tesla
python query_quick.py news AI
python query_quick.py news Market
python query_quick.py news Technology
```

## ✅ **What You Get**

### **Real Data** (with API keys):
- ✅ Live stock prices
- ✅ Current news articles
- ✅ Real market data
- ✅ Credible sources

### **Professional Reports**:
- ✅ Markdown format
- ✅ Executive summaries
- ✅ Source citations
- ✅ Actionable insights

### **Multiple Formats**:
- ✅ Command line output
- ✅ Interactive menus
- ✅ Python code integration
- ✅ File exports

## 🎉 **Ready to Use!**

**Choose your preferred method and start querying:**

1. **🖥️ Interactive**: `python query_interface.py`
2. **⚡ Quick**: `python query_quick.py company Tesla`
3. **🐍 Code**: Import and use modules
4. **📊 Demo**: `python demo.py`

**All methods work with your API keys for real data!** 🚀

---

**Created by: Syed Jibbran Ali**  
**Open Source (No License)**
