# Next Steps for Full Automation

## ✅ What's Already Done

1. ✅ **Python installed** (Python 3.12.10)
2. ✅ **Required packages installed** (anthropic, requests)
3. ✅ **Gmail SMTP configured** (intranetemailsender@gmail.com)
4. ✅ **Automation scripts created**:
   - `generate_digest.py` - Web search + Claude API
   - `send_digest_email.py` - Gmail SMTP sending
   - `run_fully_automated.bat` - Runs both in sequence
5. ✅ **Documentation created**:
   - `API_SETUP_GUIDE.md` - Complete API setup instructions
   - `README.md` - Updated with full automation info

## 🚀 To Enable Full Automation (3 Steps)

### Step 1: Get API Keys (15 minutes)

#### Claude API Key:
1. Go to **https://console.anthropic.com/**
2. Sign up / log in
3. Click **"API Keys"** → **"Create Key"**
4. Copy key (starts with `sk-ant-api03-...`)
5. **Save it securely!**

#### Search API Key (Choose ONE):

**Option A: SerpAPI** (Recommended - Simplest)
1. Go to **https://serpapi.com/**
2. Sign up for free account
3. Copy API key from Dashboard
4. **Free tier**: 100 searches/month (~16 days of daily digests)

**Option B: Google Custom Search**
1. Go to **https://console.cloud.google.com/**
2. Enable "Custom Search API"
3. Create API key
4. Go to **https://programmablesearchengine.google.com/**
5. Create search engine (select "Search entire web")
6. Copy Search Engine ID (CX)
7. **Free tier**: 100 queries/day (~16 days)

### Step 2: Configure API Keys (5 minutes)

1. Open Command Prompt in the "Intranet daily mail" folder

2. Copy template:
   ```bash
   copy api_config.json.template api_config.json
   ```

3. Open `api_config.json` in a text editor

4. **For SerpAPI**, paste your keys:
   ```json
   {
     "claude_api_key": "sk-ant-api03-YOUR_CLAUDE_KEY",
     "search_provider": "serpapi",
     "search_api_key": "YOUR_SERPAPI_KEY"
   }
   ```

   **For Google Custom Search**, paste your keys:
   ```json
   {
     "claude_api_key": "sk-ant-api03-YOUR_CLAUDE_KEY",
     "search_provider": "google_custom",
     "search_api_key": "YOUR_GOOGLE_API_KEY",
     "google_cx": "YOUR_SEARCH_ENGINE_ID"
   }
   ```

5. Save and close

### Step 3: Test & Enable (5 minutes)

1. **Test the full automation**:
   - Double-click `run_fully_automated.bat`
   - Wait for it to complete (~30-60 seconds)
   - Check your email at krkavi@microsoft.com

2. **If successful, update Task Scheduler**:
   - Double-click `UPDATE_TASK_SCHEDULER.bat`
   - Press any key when prompted
   - Task is now configured for full automation!

3. **Done!** Starting tomorrow at 8:00 AM, you'll receive fresh digests automatically.

## 📊 What to Expect

### First Run:
- Takes ~30-60 seconds
- Performs 6 web searches
- Claude API processes results
- Email arrives with 15-20 curated items

### Daily Operation:
- Runs automatically at 8:00 AM Pacific Time
- No manual intervention needed
- Fresh content every day
- Costs ~$0.10-$0.30 per day (Claude API)

## 💰 Cost Management

### Monitor Usage:
- **Claude API**: https://console.anthropic.com/settings/usage
- **SerpAPI**: https://serpapi.com/dashboard
- **Google**: https://console.cloud.google.com/apis/dashboard

### Free Tier Limits:
- **SerpAPI**: 100 searches/month (1 digest uses 6 searches)
  - You can run ~16 digests/month free
- **Google Custom Search**: 100 queries/day (more than enough)
- **Claude API**: Pay-as-you-go (~$0.10-$0.30 per digest)

### If You Hit Limits:
- Run digest less frequently (every 2-3 days)
- Reduce number of searches in `generate_digest.py`
- Upgrade to paid tier (SerpAPI: $50/month for 5,000 searches)

## 🔧 Ongoing Management

### Test Manually Anytime:
```bash
run_fully_automated.bat
```

### Check Task Status:
```powershell
schtasks /Query /TN "IntranetDailyDigest"
```

### Temporarily Disable:
```powershell
schtasks /Change /TN "IntranetDailyDigest" /DISABLE
```

### Re-enable:
```powershell
schtasks /Change /TN "IntranetDailyDigest" /ENABLE
```

## 📚 Documentation

- **API_SETUP_GUIDE.md** - Detailed API setup instructions
- **README.md** - Complete project documentation
- **SETUP_INSTRUCTIONS.md** - Gmail SMTP setup (already done)
- **intranet_daily_digest_agent.md** - Agent instructions

## ❓ Need Help?

### Common Issues:

**"API key invalid"**
- Double-check keys in `api_config.json`
- Ensure no extra spaces
- Verify billing is set up for Claude API

**"Module not found"**
- Run: `pip install -r requirements.txt`

**"No search results"**
- Check internet connection
- Verify search API key
- Check API quota hasn't been exceeded

### Documentation:
- **Full API setup**: See `API_SETUP_GUIDE.md`
- **Troubleshooting**: See `README.md` section
- **Agent usage**: See `intranet_daily_digest_agent.md`

---

## 🎯 Summary

**Current Status:**
- ✅ Email automation working
- ⏳ API keys needed for full automation

**Time to Full Automation:** ~25 minutes
1. Get API keys (15 min)
2. Configure (5 min)
3. Test & enable (5 min)

**Result:** Fresh, curated daily digest delivered automatically at 8:00 AM with zero manual work!

---

**Ready to proceed?** Start with **API_SETUP_GUIDE.md** for detailed step-by-step instructions!
