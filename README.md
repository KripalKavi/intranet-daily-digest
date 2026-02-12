# Intranet Daily Digest Agent

Fully automated daily email digest covering enterprise intranets, employee experience platforms, website builders, and AI-native prototype-to-code tools.

## 🎯 Features

- **Automated Web Searches**: Uses Search APIs to find latest updates
- **AI-Powered Compilation**: Claude API formats and summarizes content
- **Gmail SMTP Delivery**: Automatic email sending
- **Windows Task Scheduler**: Runs daily at 8:00 AM Pacific Time
- **100% Hands-Off**: No manual intervention needed once configured

## 🚀 Quick Start - Full Automation

### Step 1: Set Up API Keys
See detailed instructions in **`API_SETUP_GUIDE.md`**

1. **Claude API Key** - Get from https://console.anthropic.com/
2. **Search API Key** - Choose one:
   - **SerpAPI** (recommended): https://serpapi.com/ - 100 free searches/month
   - **Google Custom Search**: https://console.cloud.google.com/

### Step 2: Configure APIs

1. Copy template:
   ```bash
   copy api_config.json.template api_config.json
   ```

2. Edit `api_config.json` with your API keys:
   ```json
   {
     "claude_api_key": "sk-ant-api03-YOUR_KEY",
     "search_provider": "serpapi",
     "search_api_key": "YOUR_SERPAPI_KEY"
   }
   ```

3. Configure Gmail (from earlier setup):
   - Already configured in `email_config.json`
   - Uses: intranetemailsender@gmail.com

### Step 3: Install Dependencies

Already done! (anthropic and requests packages installed)

### Step 4: Test Full Automation

```bash
cd "Intranet daily mail"
run_fully_automated.bat
```

This will:
1. Perform 6 web searches
2. Use Claude API to generate digest
3. Send email to krkavi@microsoft.com

### Step 5: Update Task Scheduler

Double-click: **`UPDATE_TASK_SCHEDULER.bat`**

This updates the scheduled task to run full automation daily at 8:00 AM.

## 📁 Files

### Core Scripts:
- **generate_digest.py** - Automated web search + Claude API generation
- **send_digest_email.py** - Gmail SMTP email sending
- **run_fully_automated.bat** - Runs both scripts in sequence

### Configuration:
- **api_config.json** - Claude API + Search API keys (create from template)
- **email_config.json** - Gmail SMTP credentials (already configured)
- **intranet_daily_digest_config.json** - Search topics and settings

### Documentation:
- **API_SETUP_GUIDE.md** - Complete API setup instructions
- **SETUP_INSTRUCTIONS.md** - Gmail SMTP setup instructions
- **intranet_daily_digest_agent.md** - Agent instructions for manual use

### Templates:
- **api_config.json.template** - API configuration template
- **email_config.json.template** - Email configuration template

## 🔄 How It Works

### Automated Workflow (Daily at 8:00 AM):

```
1. Task Scheduler triggers run_fully_automated.bat
   ↓
2. generate_digest.py executes:
   - Performs 6 web searches (SerpAPI or Google Custom Search)
   - Sends results to Claude API
   - Claude compiles 15-20 items into HTML digest
   - Saves to latest_digest.html
   ↓
3. send_digest_email.py executes:
   - Reads latest_digest.html
   - Sends via Gmail SMTP
   - Delivers to krkavi@microsoft.com
   ↓
4. Email arrives with fresh content!
```

## 📊 Search Topics

The digest covers 4 categories with 6 searches:

- 🏢 **Enterprise Intranets** (5 items)
  - SharePoint, Viva Connections, employee portals

- 👥 **Employee Experience Platforms** (4 items)
  - Digital workplace, Viva, employee engagement

- 🌐 **Consumer Website Builders** (4 items)
  - Wix, Squarespace, Webflow, Framer

- 🤖 **AI-Native Builders & Prototype-to-Code** (6 items)
  - v0.dev, Bolt.new, Lovable, Figma-to-code, generative UI

## 💰 Cost Estimates

### Daily Digest Cost:
- **Claude API**: ~$0.10 - $0.30 per digest
- **SerpAPI**: 100 free searches/month (enough for ~16 days)
  - OR $50/month for 5,000 searches
- **Google Custom Search**: 100 free queries/day (enough for 16 days)
  - OR $5 per 1,000 queries

### Monthly Total (if running daily):
- **With free tiers**: ~$3 - $9 (Claude only)
- **With paid tiers**: ~$8 - $59 (Claude + SerpAPI)

## 🛠️ Management Commands

### Test Full Automation:
```bash
run_fully_automated.bat
```

### Test Just Email Sending:
```bash
python send_digest_email.py
```

### Check Scheduled Task Status:
```powershell
schtasks /Query /TN "IntranetDailyDigest"
```

### Trigger Task Manually:
```powershell
schtasks /Run /TN "IntranetDailyDigest"
```

### Disable Automation:
```powershell
schtasks /Change /TN "IntranetDailyDigest" /DISABLE
```

### Re-enable Automation:
```powershell
schtasks /Change /TN "IntranetDailyDigest" /ENABLE
```

## 🔧 Configuration

### Modify Search Topics:
Edit `intranet_daily_digest_config.json`:
```json
{
  "search_topics": [
    "your custom topic here",
    "another topic"
  ]
}
```

### Change Email Template:
Edit `intranet_daily_digest_agent.md` (lines 66-98) to customize:
- Subject line
- Greeting text
- Section headers
- Footer text

### Adjust Item Count:
In `intranet_daily_digest_config.json`:
```json
{
  "item_limit": {
    "min": 10,
    "target": 15,
    "max": 20
  }
}
```

## 🔐 Security

- **Never commit these files to version control:**
  - `api_config.json` (has API keys)
  - `email_config.json` (has Gmail password)
  - Both are already in `.gitignore`

- **Best Practices:**
  - Rotate API keys every 90 days
  - Monitor API usage for unexpected spikes
  - Set spending limits in API dashboards
  - Use Gmail App Passwords (not main password)

## 🐛 Troubleshooting

### Digest generation fails:
- Check API keys in `api_config.json`
- Verify you have API credits/quota remaining
- Check internet connection

### Email not sent:
- Verify `email_config.json` credentials
- Check Gmail App Password is correct
- Ensure `latest_digest.html` exists

### Task doesn't run:
- Check Task Scheduler history
- Verify task is enabled
- Check file paths are correct

### "Module not found" errors:
```bash
pip install -r requirements.txt
```

## 📚 Documentation

- **API_SETUP_GUIDE.md** - Step-by-step API configuration
- **SETUP_INSTRUCTIONS.md** - Gmail SMTP setup
- **intranet_daily_digest_agent.md** - Manual agent usage

## 💡 Tips

1. **Monitor API usage** in first week to understand costs
2. **Adjust search frequency** if costs are too high
3. **Review digest quality** periodically and tune search queries
4. **Set billing alerts** in API dashboards

## 📧 Recipient

**Current recipient:** krkavi@microsoft.com

To change, edit `email_config.json`:
```json
{
  "recipient_email": "new-recipient@example.com"
}
```

---

**Status:** ✅ Fully Automated - Fresh content generated and delivered daily!
