@echo off
echo ============================================================
echo Intranet Weekly Digest - Task Scheduler Setup
echo ============================================================
echo.
echo This will delete any existing digest task and create a new
echo weekly scheduled task (Mondays at 8:00 AM PT).
echo.
pause

echo Removing any existing task...
schtasks /Delete /TN "IntranetWeeklyDigest" /F 2>nul
schtasks /Delete /TN "IntranetDailyDigest" /F 2>nul

echo Creating weekly task...
schtasks /Create /SC WEEKLY /D MON /TN "IntranetWeeklyDigest" /TR "\"C:\Users\krkavi\OneDrive - Microsoft\Projects\99 - Professional development\06 - Claude Code Projects\Intranet daily mail\run_fully_automated.bat\"" /ST 08:00 /F /RL HIGHEST

if %errorlevel% equ 0 (
    echo.
    echo ============================================================
    echo SUCCESS! Task created successfully.
    echo ============================================================
    echo.
    echo Task Name: IntranetWeeklyDigest
    echo Schedule:  Every Monday at 8:00 AM Pacific Time
    echo Actions:   Generate fresh digest ^(web searches + Claude API^)
    echo            Send email via Gmail SMTP to krkavi@microsoft.com
    echo.
    echo To test it now, double-click: test_task.bat
    echo.
) else (
    echo.
    echo ============================================================
    echo ERROR! Failed to create task.
    echo ============================================================
    echo.
    echo Right-click setup_task.bat and select "Run as administrator"
    echo.
)

pause
