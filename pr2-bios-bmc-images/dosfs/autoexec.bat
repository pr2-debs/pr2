@echo off 
SET dosdir=C:\FDOS
set PATH=%dosdir%\bin
set NLSPATH=%dosdir%\NLS 
set HELPPATH=%dosdir%\HELP
set temp=%dosdir%\temp
set tmp=%dosdir%\temp
SET BLASTER=A220 I5 D1 H5 P330
REM ShsuCDhd /QQ /F:C:\FDBOOTCD.ISO
if not "%config%"=="4" REM LH VIAUDIO
if not "%config%"=="4" REM LH VIAFMTSR
if not "%config%"=="4" LH FDAPM APMDOS
if "%config%"=="2" LH SHARE
if not "%config%"=="4" ShsuCDX /QQ /~ /D:?FDCD0002 /D:?FDCD0003 /D:?CDRCACH0
SET autofile=C:\autoexec.bat 
alias reboot=fdapm warmboot 
alias halt=fdapm poweroff 
SET CFGFILE=C:\fdconfig.sys 
echo type HELP to get support on commands and navigation
echo.
echo Welcome to FreeDOS
echo.
rem if not "%config%"=="4" mouse 
call default.bat
:endloop
beep
beep 
beep 
beep 
beep
choice /C:bpw /T:w,5 Do you want to Boot, get a Prompt or keep Waiting?
if errorlevel 3 goto endloop
if errorlevel 2 goto prompt
reboot
:prompt

