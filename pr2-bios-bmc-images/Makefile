pr2-reflash-bmc.img: dosfs/bmc.bat
	./makeimage.sh pr2-reflash-bmc.img dosfs/bmc.bat

pr2-reflash-bios1.img: dosfs/bios1.bat
	./makeimage.sh pr2-reflash-bios1.img dosfs/bios1.bat

pr2-reflash-bios2.img: dosfs/bios2.bat
	./makeimage.sh pr2-reflash-bios2.img dosfs/bios2.bat

pr2-reflash-biosopt1.img: dosfs/biosopt1.bat
	./makeimage.sh pr2-reflash-biosopt1.img dosfs/biosopt1.bat

pr2-reflash-biosopt2.img: dosfs/biosopt2.bat
	./makeimage.sh pr2-reflash-biosopt2.img dosfs/biosopt2.bat

pr2-reflash-biosbmc1.img: dosfs/biosbmc1.bat
	./makeimage.sh pr2-reflash-biosbmc1.img dosfs/biosbmc1.bat

pr2-reflash-biosbmc2.img: dosfs/biosbmc2.bat
	./makeimage.sh pr2-reflash-biosbmc2.img dosfs/biosbmc2.bat

pr2-reflash-prompt.img: dosfs/prompt.bat
	./makeimage.sh pr2-reflash-prompt.img dosfs/prompt.bat

pr2-reflash-saveopt1.img: dosfs/saveopt1.bat
	./makeimage.sh pr2-reflash-saveopt1.img dosfs/saveopt1.bat

pr2-reflash-saveopt2.img: dosfs/saveopt2.bat
	./makeimage.sh pr2-reflash-saveopt2.img dosfs/saveopt2.bat

user-nvram/user-nvram: user-nvram/user-nvram.c
	gcc -O2 -g -Wall user-nvram/user-nvram.c -o user-nvram/user-nvram

install: pr2-reflash-bmc.img pr2-reflash-bios1.img pr2-reflash-bios2.img pr2-reflash-biosopt1.img pr2-reflash-biosopt2.img pr2-reflash-biosbmc1.img pr2-reflash-biosbmc2.img pr2-reflash-prompt.img pr2-reflash-saveopt1.img pr2-reflash-saveopt2.img user-nvram/user-nvram dosfs/biosopt/C1-BIOS.BIN dosfs/biosopt/C2-BIOS.BIN
	mkdir -p ${DESTDIR}/var/lib/tftpboot/
	mkdir -p ${DESTDIR}/usr/lib/pr2-biosopt/
	install *.img ${DESTDIR}/var/lib/tftpboot/
	install user-nvram/user-nvram ${DESTDIR}/usr/bin/
	install dosfs/biosopt/C1-BIOS.BIN ${DESTDIR}/usr/lib/pr2-biosopt/
	install dosfs/biosopt/C1-BIOS-HD.BIN ${DESTDIR}/usr/lib/pr2-biosopt/
	install dosfs/biosopt/C2-BIOS.BIN ${DESTDIR}/usr/lib/pr2-biosopt/


clean:
	rm *.img
	rm user-nvram/user-nvram