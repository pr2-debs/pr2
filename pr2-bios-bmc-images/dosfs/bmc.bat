beep
beep
sleep 1
beep
echo 
choice /T:y,5 Starting BMC reflash in 5 seconds
if errorlevel 2 goto end
beep
beep
beep
BMC\BMCFU.EXE BMC\S2Av106.bin
:end
