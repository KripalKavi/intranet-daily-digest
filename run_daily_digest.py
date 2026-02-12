#!/usr/bin/env python3
"""
Main automation script for daily digest
Generates digest and sends email
"""

import subprocess
import sys
from pathlib import Path
from datetime import datetime

SCRIPT_DIR = Path(__file__).parent

def log(message):
    """Print with timestamp"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {message}")

def main():
    """Main automation workflow"""
    log("=" * 60)
    log("Starting Daily Digest Automation")
    log("=" * 60)

    try:
        # Check if digest HTML exists
        digest_path = SCRIPT_DIR / "latest_digest.html"

        if not digest_path.exists():
            log("⚠️  Warning: latest_digest.html not found")
            log("Please generate the digest first using Claude Code:")
            log('  1. Open Claude Code in this directory')
            log('  2. Run: "run the digest"')
            log('  3. Save the HTML output to latest_digest.html')
            log("")
            log("For now, skipping email send.")
            return 1

        log(f"✓ Found digest file: {digest_path}")

        # Send email
        log("\nSending email...")
        result = subprocess.run(
            [sys.executable, str(SCRIPT_DIR / "send_digest_email.py")],
            capture_output=True,
            text=True
        )

        # Print output
        if result.stdout:
            print(result.stdout)
        if result.stderr:
            print(result.stderr, file=sys.stderr)

        if result.returncode == 0:
            log("\n✅ Daily digest automation completed successfully!")
            return 0
        else:
            log(f"\n❌ Email sending failed with code {result.returncode}")
            return result.returncode

    except Exception as e:
        log(f"\n❌ Error: {e}")
        return 1

if __name__ == "__main__":
    exit_code = main()
    log("=" * 60)
    sys.exit(exit_code)
