@echo off
echo ============================================================
echo Creating Intranet Daily Digest Scheduled Task
echo ============================================================
echo.

schtasks /Create /SC DAILY /TN "IntranetDailyDigest" /TR "\"C:\Users\krkavi\AppData\Local\Programs\Python\Python312\python.exe\" \"C:\Users\krkavi\OneDrive - Microsoft\Projects\99 - Professional development\06 - Claude Code Projects\Intranet daily mail\send_digest_email.py\"" /ST 08:00 /F /RL HIGHEST

if %errorlevel% equ 0 (
    echo.
    echo ============================================================
    echo SUCCESS! Task created successfully!
    echo ============================================================
    echo.
    echo Task Name: IntranetDailyDigest
    echo Schedule: Daily at 8:00 AM
    echo Action: Send email digest
    echo.
    echo The task will run tomorrow at 8:00 AM and every day after
    echo.
    echo To test it now, double-click: test_task.bat
    echo.
) else (
    echo.
    echo ============================================================
    echo ERROR! Failed to create task
    echo ============================================================
    echo.
    echo Please try running this file as Administrator:
    echo Right-click CREATE_TASK.bat and select "Run as administrator"
    echo.
)

pause
