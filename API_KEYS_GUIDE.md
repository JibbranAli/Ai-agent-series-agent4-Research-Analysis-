# How to Add API Keys - Complete Guide

## 🔑 **Step 1: Get Your API Keys**

### **News API (Free)**
1. Go to: https://newsapi.org/
2. Click "Get API Key"
3. Sign up with email
4. Copy your API key (looks like: `abc123def456ghi789jkl012mno345pqr678stu901vwx234yz`)

### **Alpha Vantage (Free)**
1. Go to: https://www.alphavantage.co/support/#api-key
2. Enter your email address
3. Get your API key (looks like: `ALPHA_VANTAGE_ABC123DEF456GHI789JKL012MNO345PQR678`)

### **Polygon (Free Tier)**
1. Go to: https://polygon.io/
2. Sign up for free account
3. Get your API key (looks like: `polygon_abc123def456ghi789jkl012mno345pqr678stu901`)

## 📝 **Step 2: Edit config.json**

Open `config.json` and replace the placeholder text:

### **Before (with placeholders):**
```json
"api_keys": {
    "news_api": "YOUR_ACTUAL_NEWS_API_KEY",
    "polygon_api": "YOUR_ACTUAL_POLYGON_API_KEY", 
    "alpha_vantage": "YOUR_ACTUAL_ALPHA_VANTAGE_KEY"
}
```

### **After (with real keys):**
```json
"api_keys": {
    "news_api": "abc123def456ghi789jkl012mno345pqr678stu901vwx234yz",
    "polygon_api": "polygon_abc123def456ghi789jkl012mno345pqr678stu901",
    "alpha_vantage": "ALPHA_VANTAGE_ABC123DEF456GHI789JKL012MNO345PQR678"
}
```

## 🚀 **Step 3: Test Your API Keys**

After adding your keys, test them:

```bash
# Run the demo to test
python demo.py

# Run examples to see real data
python examples.py
```

## ⚠️ **Important Notes**

1. **Keep your API keys secret** - Don't share them publicly
2. **Free limits** - Each API has daily/monthly limits
3. **Works without keys** - System uses mock data if no keys provided
4. **One key at a time** - You can add just one key if you want

## 🔧 **Alternative: Environment Variables**

For better security, you can also use environment variables:

```bash
# Set environment variables
export NEWS_API_KEY="your_news_api_key_here"
export ALPHA_VANTAGE_KEY="your_alpha_vantage_key_here"
export POLYGON_API_KEY="your_polygon_key_here"
```

Then modify the code to read from environment variables instead of config.json.

## 📊 **What Each API Does**

- **News API**: Provides real news articles and headlines
- **Alpha Vantage**: Provides real stock prices and financial data
- **Polygon**: Provides real-time market data and company information

## ✅ **Testing Your Setup**

After adding API keys, you should see:
- Real news articles instead of mock data
- Actual stock prices and market data
- Current company information
- Live market trends

## 🆓 **Free API Limits**

- **News API**: 1,000 requests/day (free)
- **Alpha Vantage**: 5 requests/minute, 500 requests/day (free)
- **Polygon**: 5 requests/minute (free tier)

## 🎯 **Quick Start**

1. Get one API key (start with News API - easiest)
2. Add it to config.json
3. Run `python demo.py`
4. See the difference with real data!

---

**Remember**: The system works perfectly without API keys using mock data, so you can start using it immediately!
