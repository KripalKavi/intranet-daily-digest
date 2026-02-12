@echo off
echo ============================================================
echo Updating Task Scheduler for Full Automation
echo ============================================================
echo.
echo This will update the scheduled task to:
echo   1. Generate fresh digest content (web searches + Claude API)
echo   2. Send email automatically
echo.
echo Current task will be replaced.
echo.
pause

schtasks /Delete /TN "IntranetDailyDigest" /F 2>nul

schtasks /Create /SC DAILY /TN "IntranetDailyDigest" /TR "\"C:\Users\krkavi\OneDrive - Microsoft\Projects\99 - Professional development\06 - Claude Code Projects\Intranet daily mail\run_fully_automated.bat\"" /ST 08:00 /F /RL HIGHEST

if %errorlevel% equ 0 (
    echo.
    echo ============================================================
    echo SUCCESS! Task updated for full automation!
    echo ============================================================
    echo.
    echo IMPORTANT: Before this works, you must:
    echo   1. Set up API keys (see API_SETUP_GUIDE.md)
    echo   2. Create api_config.json with your keys
    echo   3. Test with: run_fully_automated.bat
    echo.
    echo Task Name: IntranetDailyDigest
    echo Schedule: Daily at 8:00 AM
    echo Actions:
    echo   - Generate fresh digest (web searches + Claude API)
    echo   - Send email via Gmail SMTP
    echo.
    echo To test now: double-click run_fully_automated.bat
    echo.
) else (
    echo.
    echo ============================================================
    echo ERROR! Failed to update task
    echo ============================================================
    echo.
    echo Try running as Administrator:
    echo Right-click UPDATE_TASK_SCHEDULER.bat and select "Run as administrator"
    echo.
)

pause
