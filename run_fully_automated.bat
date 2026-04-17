@echo off
REM Full automation script: Generate digest then send email
REM This script is called by Windows Task Scheduler

cd /d "%~dp0"

REM Set up logging
set LOG_FILE=automation_log.txt
echo. >> %LOG_FILE%
echo ============================================================ >> %LOG_FILE%
echo Run started: %DATE% %TIME% >> %LOG_FILE%
echo ============================================================ >> %LOG_FILE%

echo ============================================================
echo Intranet Weekly Digest - Full Automation
echo ============================================================
echo.
echo Step 1: Generating fresh digest content...
echo.
echo Step 1: Generating fresh digest content... >> %LOG_FILE%

"C:\Users\krkavi\AppData\Local\Programs\Python\Python312\python.exe" generate_digest.py >> %LOG_FILE% 2>&1

if %errorlevel% neq 0 (
    echo.
    echo ERROR: Digest generation failed!
    echo ERROR: Digest generation failed! >> %LOG_FILE%
    echo Email will NOT be sent.
    echo Email will NOT be sent. >> %LOG_FILE%
    exit /b 1
)

echo.
echo Step 2: Sending email...
echo.
echo Step 2: Sending email... >> %LOG_FILE%

"C:\Users\krkavi\AppData\Local\Programs\Python\Python312\python.exe" send_digest_email.py >> %LOG_FILE% 2>&1

if %errorlevel% neq 0 (
    echo.
    echo ERROR: Email sending failed!
    echo ERROR: Email sending failed! >> %LOG_FILE%
    exit /b 1
)

echo.
echo ============================================================
echo SUCCESS: Digest generated and email sent!
echo ============================================================
echo SUCCESS: Digest generated and email sent! >> %LOG_FILE%
echo ============================================================ >> %LOG_FILE%
