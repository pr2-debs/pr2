beep
beep
sleep 1
beep
beep
choice /T:y,5 Starting Bios reflash in 5 seconds
if errorlevel 2 goto end
beep
beep
beep
bios\Afudos bios\S2A_3A05.ROM /P /B /K /X /C /L2
:end
