# Setup Instructions for Automated Email Digest

This guide will help you set up automated daily email delivery using Gmail SMTP.

## Prerequisites

- Python 3.7 or higher installed
- A Gmail account for sending emails
- Windows Task Scheduler (for automation)

## Step 1: Set Up Gmail App Password

Gmail requires an "App Password" for SMTP access (not your regular password).

### How to Create a Gmail App Password:

1. Go to your Google Account: https://myaccount.google.com/
2. Select **Security** from the left menu
3. Under "How you sign in to Google," select **2-Step Verification**
   - If not enabled, you must enable it first
4. Scroll down and select **App passwords**
5. Select app: Choose "Mail"
6. Select device: Choose "Windows Computer" or "Other (Custom name)"
7. Click **Generate**
8. Copy the 16-character password (it will look like: `abcd efgh ijkl mnop`)

**Important:** Save this password securely - you won't be able to see it again!

## Step 2: Configure Email Settings

1. Copy `email_config.json.template` to `email_config.json`:
   ```bash
   copy email_config.json.template email_config.json
   ```

2. Edit `email_config.json` with your details:
   ```json
   {
     "gmail_address": "your-sending-email@gmail.com",
     "gmail_app_password": "abcdefghijklmnop",
     "recipient_email": "krkavi@microsoft.com",
     "smtp_server": "smtp.gmail.com",
     "smtp_port": 587
   }
   ```

3. **Security Note:** Add `email_config.json` to `.gitignore` if using version control:
   ```
   email_config.json
   ```

## Step 3: Test Email Sending

Before automating, test the email sending manually:

1. First, generate a test digest (run the agent in Claude Code)
2. Make sure `latest_digest.html` exists
3. Run the Python script:
   ```bash
   python send_digest_email.py
   ```

If successful, you should see:
```
✅ Email sent successfully!
```

Check your inbox at krkavi@microsoft.com to verify.

## Step 4: Set Up Windows Task Scheduler

To run the digest automatically every day at 8:00 AM Pacific Time:

### Create the Task:

1. Open **Task Scheduler** (search in Start menu)
2. Click **Create Task** (not "Create Basic Task")
3. **General Tab:**
   - Name: `Intranet Daily Digest`
   - Description: `Sends daily digest email at 8 AM PT`
   - Select: "Run whether user is logged on or not"
   - Check: "Run with highest privileges"

4. **Triggers Tab:**
   - Click **New**
   - Begin the task: "On a schedule"
   - Settings: Daily
   - Start: Choose a date
   - Time: **08:00:00** (adjust for Pacific Time zone)
   - Check: "Enabled"
   - Click **OK**

5. **Actions Tab:**
   - Click **New**
   - Action: "Start a program"
   - Program/script: `cmd.exe`
   - Add arguments:
     ```
     /c cd /d "C:\Users\krkavi\OneDrive - Microsoft\Projects\99 - Professional development\06 - Claude Code Projects\Intranet daily mail" && python run_daily_digest.py >> digest_log.txt 2>&1
     ```
   - Click **OK**

6. **Conditions Tab:**
   - Uncheck: "Start the task only if the computer is on AC power"
   - Check: "Wake the computer to run this task" (if you want)

7. **Settings Tab:**
   - Check: "Allow task to be run on demand"
   - Check: "Run task as soon as possible after a scheduled start is missed"
   - If the task fails, restart every: **10 minutes**
   - Attempt to restart up to: **3 times**

8. Click **OK** to save the task

### Test the Scheduled Task:

1. In Task Scheduler, find your task
2. Right-click and select **Run**
3. Check if the email arrives
4. Check `digest_log.txt` for any errors

## Step 5: Create the Main Automation Script

The `run_daily_digest.py` script will:
1. Generate the digest using Claude Code
2. Save it to `latest_digest.html`
3. Send the email using `send_digest_email.py`

**Note:** Full automation requires Claude Code API access. For now, you can:
- Manually generate the digest in Claude Code
- Save the HTML to `latest_digest.html`
- Let Task Scheduler automatically send it

## Troubleshooting

### "Authentication failed" error:
- Verify you're using an App Password (not your regular Gmail password)
- Ensure 2-Step Verification is enabled on your Google account
- Check that the app password is correct (16 characters, no spaces)

### "Connection refused" error:
- Check your internet connection
- Verify firewall isn't blocking port 587
- Try using port 465 with SSL instead (update script)

### Email not received:
- Check spam/junk folder
- Verify recipient email address is correct
- Check Gmail "Sent" folder to confirm it was sent

### Task Scheduler not running:
- Ensure Python is in your system PATH
- Check Task Scheduler History for error details
- Verify file paths are absolute (not relative)
- Check `digest_log.txt` for error messages

## File Structure

After setup, your directory should contain:

```
Intranet daily mail/
├── intranet_daily_digest_agent.md
├── intranet_daily_digest_config.json
├── email_config.json (your credentials - DO NOT COMMIT)
├── email_config.json.template
├── send_digest_email.py
├── run_daily_digest.py
├── latest_digest.html (generated by agent)
├── digest_log.txt (created by Task Scheduler)
├── SETUP_INSTRUCTIONS.md (this file)
└── README.md
```

## Security Best Practices

1. **Never commit `email_config.json` to version control**
2. **Use App Passwords, not your main Gmail password**
3. **Restrict file permissions on `email_config.json`**
4. **Regularly rotate your App Password**
5. **Monitor Gmail account for suspicious activity**

## Next Steps

Once automated:
- Monitor the first few days to ensure reliability
- Check `digest_log.txt` for any errors
- Adjust search queries in the agent if needed
- Customize email formatting as desired

## Support

If you encounter issues:
1. Check `digest_log.txt` for error messages
2. Test components individually (generation, then sending)
3. Verify all prerequisites are met
4. Review Gmail security settings
