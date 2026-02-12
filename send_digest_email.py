#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Intranet Daily Digest Email Sender
Sends the generated digest via Gmail SMTP
"""

import smtplib
import json
import os
import sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from pathlib import Path

# Fix Windows console encoding
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

# Get the directory where this script is located
SCRIPT_DIR = Path(__file__).parent

# Load configuration
def load_config():
    """Load email configuration from JSON file"""
    config_path = SCRIPT_DIR / "email_config.json"

    if not config_path.exists():
        raise FileNotFoundError(
            f"Configuration file not found: {config_path}\n"
            "Please create email_config.json with your Gmail credentials."
        )

    with open(config_path, 'r') as f:
        config = json.load(f)

    # Validate required fields
    required_fields = ['gmail_address', 'gmail_app_password', 'recipient_email']
    missing_fields = [field for field in required_fields if field not in config]

    if missing_fields:
        raise ValueError(f"Missing required fields in email_config.json: {', '.join(missing_fields)}")

    return config

def load_digest_content():
    """Load the generated digest content"""
    digest_path = SCRIPT_DIR / "latest_digest.html"

    if not digest_path.exists():
        raise FileNotFoundError(
            f"Digest content not found: {digest_path}\n"
            "Please run the digest generation first."
        )

    with open(digest_path, 'r', encoding='utf-8') as f:
        return f.read()

def send_email(config, html_content):
    """Send email via Gmail SMTP"""

    # Create message
    msg = MIMEMultipart('alternative')
    msg['From'] = config['gmail_address']
    msg['To'] = config['recipient_email']
    msg['Subject'] = f"Intranet Daily Digest - {datetime.now().strftime('%B %d, %Y')}"

    # Attach HTML content
    html_part = MIMEText(html_content, 'html')
    msg.attach(html_part)

    # Connect to Gmail SMTP server
    print("Connecting to Gmail SMTP server...")
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Secure the connection

            print("Logging in...")
            server.login(config['gmail_address'], config['gmail_app_password'])

            print(f"Sending email to {config['recipient_email']}...")
            server.send_message(msg)

            print("✅ Email sent successfully!")

    except smtplib.SMTPAuthenticationError:
        print("❌ Authentication failed. Please check your Gmail address and app password.")
        raise
    except smtplib.SMTPException as e:
        print(f"❌ SMTP error occurred: {e}")
        raise
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        raise

def main():
    """Main function to send the digest email"""
    try:
        print("=" * 60)
        print("Intranet Daily Digest Email Sender")
        print("=" * 60)

        # Load configuration
        print("\nLoading configuration...")
        config = load_config()
        print(f"✓ Configuration loaded")
        print(f"  From: {config['gmail_address']}")
        print(f"  To: {config['recipient_email']}")

        # Load digest content
        print("\nLoading digest content...")
        html_content = load_digest_content()
        print(f"✓ Digest content loaded ({len(html_content)} characters)")

        # Send email
        print("\nSending email...")
        send_email(config, html_content)

        print("\n" + "=" * 60)
        print("Process completed successfully!")
        print("=" * 60)

    except Exception as e:
        print(f"\n❌ Error: {e}")
        return 1

    return 0

if __name__ == "__main__":
    exit(main())
