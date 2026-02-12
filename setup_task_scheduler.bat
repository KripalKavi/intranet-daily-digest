@echo off
echo ============================================================
echo Intranet Daily Digest - Task Scheduler Setup
echo ============================================================
echo.
echo This will create a scheduled task to run daily at 8:00 AM PT
echo.
pause

schtasks /Create /XML "IntranetDailyDigest_Task.xml" /TN "IntranetDailyDigest" /F

if %errorlevel% equ 0 (
    echo.
    echo ============================================================
    echo SUCCESS! Task created successfully
    echo ============================================================
    echo.
    echo The task will run daily at 8:00 AM Pacific Time
    echo.
    echo To test the task now, run:
    echo   schtasks /Run /TN "IntranetDailyDigest"
    echo.
    echo To view the task:
    echo   Open Task Scheduler and look for "IntranetDailyDigest"
    echo.
    echo To disable the task:
    echo   schtasks /Change /TN "IntranetDailyDigest" /DISABLE
    echo.
    echo To delete the task:
    echo   schtasks /Delete /TN "IntranetDailyDigest"
    echo.
) else (
    echo.
    echo ============================================================
    echo ERROR! Failed to create task
    echo ============================================================
    echo.
    echo Make sure you run this script as Administrator
    echo Right-click and select "Run as administrator"
    echo.
)

pause
