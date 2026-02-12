# API Setup Guide for Full Automation

This guide will help you set up the APIs needed for fully automated digest generation.

## Overview

The automated system uses:
- **Claude API** (Anthropic) - To compile and format the digest
- **Search API** - To fetch latest updates (SerpAPI or Google Custom Search)

## Step 1: Get Claude API Key

### Create Anthropic Account & Get API Key:

1. Go to **https://console.anthropic.com/**
2. Sign up or log in
3. Click on **"API Keys"** in the left sidebar
4. Click **"Create Key"**
5. Name it "Intranet Digest" or similar
6. Copy the API key (starts with `sk-ant-api03-...`)
7. **Save it securely** - you won't see it again!

### Pricing:
- **Claude Sonnet 4.5**: ~$3 per 1M input tokens, ~$15 per 1M output tokens
- **Estimated cost per digest**: $0.10 - $0.30 per day
- **Monthly estimate**: ~$3 - $9 for daily digests

## Step 2: Choose & Set Up Search API

### Option A: SerpAPI (Recommended - Easiest)

**Pros:**
- Simple to set up
- 100 free searches per month
- No complex configuration

**Setup:**
1. Go to **https://serpapi.com/**
2. Sign up for a free account
3. Go to **Dashboard** → **API Key**
4. Copy your API key
5. **Free tier**: 100 searches/month (enough for ~16 days of daily digests with 6 searches per day)
6. **Paid plans**: $50/month for 5,000 searches

### Option B: Google Custom Search API

**Pros:**
- 100 free queries per day (enough for 16 days)
- $5 per 1,000 additional queries

**Setup:**
1. **Enable the API:**
   - Go to **https://console.cloud.google.com/**
   - Create a new project or select existing
   - Enable **"Custom Search API"**
   - Create credentials (API key)

2. **Create Custom Search Engine:**
   - Go to **https://programmablesearchengine.google.com/**
   - Click **"Add"** to create a new search engine
   - For "Sites to search": Choose **"Search the entire web"**
   - Get your **Search engine ID (CX)**

3. **Copy both:**
   - API Key (from Google Cloud Console)
   - Search Engine ID / CX (from Programmable Search Engine)

## Step 3: Configure api_config.json

1. Copy the template:
   ```bash
   copy api_config.json.template api_config.json
   ```

2. Edit `api_config.json` with your API keys:

### For SerpAPI:
```json
{
  "claude_api_key": "sk-ant-api03-YOUR_CLAUDE_KEY_HERE",
  "search_provider": "serpapi",
  "search_api_key": "YOUR_SERPAPI_KEY_HERE"
}
```

### For Google Custom Search:
```json
{
  "claude_api_key": "sk-ant-api03-YOUR_CLAUDE_KEY_HERE",
  "search_provider": "google_custom",
  "search_api_key": "YOUR_GOOGLE_API_KEY_HERE",
  "google_cx": "YOUR_CUSTOM_SEARCH_ENGINE_ID"
}
```

3. **Security**: Add `api_config.json` to `.gitignore` (already done)

## Step 4: Install Python Dependencies

Run this command in your terminal:

```bash
cd "Intranet daily mail"
"C:\Users\krkavi\AppData\Local\Programs\Python\Python312\python.exe" -m pip install -r requirements.txt
```

This installs:
- `anthropic` - Claude API client
- `requests` - HTTP library for search APIs

## Step 5: Test the Automated Generation

Test the full automation:

```bash
cd "Intranet daily mail"
"C:\Users\krkavi\AppData\Local\Programs\Python\Python312\python.exe" generate_digest.py
```

You should see:
```
[timestamp] Starting web searches...
[timestamp] Search 1/6: enterprise intranet updates...
...
[timestamp] Generating digest with Claude API...
[timestamp] SUCCESS! Digest generated and saved
```

Check `latest_digest.html` to verify the content.

## Step 6: Update Task Scheduler (Done Automatically)

The setup script will update the scheduled task to:
1. Run `generate_digest.py` first (generates fresh content)
2. Then run `send_digest_email.py` (sends the email)

Both happen automatically at 8:00 AM Pacific Time.

## Cost Management

### Monitor Usage:

**Claude API:**
- Check usage: https://console.anthropic.com/settings/usage

**SerpAPI:**
- Check usage: https://serpapi.com/dashboard

**Google Custom Search:**
- Check usage: https://console.cloud.google.com/apis/dashboard

### Cost Optimization:

- Run digest less frequently (every 2-3 days instead of daily)
- Reduce number of searches (currently 6, could reduce to 4)
- Use shorter prompts to Claude
- Set up billing alerts

## Troubleshooting

### "API key invalid" errors:
- Verify keys are copied correctly (no extra spaces)
- Check that Claude API key starts with `sk-ant-api03-`
- Ensure billing is set up for Claude API

### "Rate limit exceeded":
- You've used up your free tier
- Wait until next month or upgrade to paid plan
- For SerpAPI: 100 searches/month = ~16 days of daily digests

### "Module not found" errors:
- Run: `pip install -r requirements.txt`
- Make sure you're using the correct Python path

### Search returns no results:
- Check your search API key
- Verify your internet connection
- Check API service status pages

## Security Best Practices

1. **Never commit api_config.json** (already in .gitignore)
2. **Rotate API keys** periodically (every 90 days)
3. **Monitor usage** for unexpected spikes
4. **Set spending limits** in API dashboards
5. **Restrict API key permissions** if available

## Support Links

- **Claude API Docs**: https://docs.anthropic.com/
- **SerpAPI Docs**: https://serpapi.com/docs
- **Google Custom Search Docs**: https://developers.google.com/custom-search/v1/overview
- **Anthropic Support**: https://support.anthropic.com/

---

Once configured, your digest will be **fully automated** with fresh content every day!
