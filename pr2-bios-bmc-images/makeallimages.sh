#! /bin/sh
./makeimage.sh pr2-reflash-bmc.img dosfs/bmc.bat
./makeimage.sh pr2-reflash-bios1.img dosfs/bios1.bat
./makeimage.sh pr2-reflash-bios2.img dosfs/bios2.bat
./makeimage.sh pr2-reflash-biosopt1.img dosfs/biosopt1.bat
./makeimage.sh pr2-reflash-biosopt2.img dosfs/biosopt2.bat
./makeimage.sh pr2-reflash-biosopt1.img dosfs/biosbmc1.bat
./makeimage.sh pr2-reflash-biosopt2.img dosfs/biosbmc2.bat
./makeimage.sh pr2-reflash-prompt.img dosfs/prompt.bat
./makeimage.sh pr2-reflash-saveopt1.img dosfs/saveopt1.bat
./makeimage.sh pr2-reflash-saveopt2.img dosfs/saveopt2.bat
