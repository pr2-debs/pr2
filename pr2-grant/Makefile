pr2-grant: pr2_grant.cpp
	g++ -o pr2-grant pr2_grant.cpp -lcap

install: pr2_grant
	install pr2-grant ${DESTDIR}/usr/bin/
	install pr2_grant ${DESTDIR}/usr/bin/

clean:
	-rm pr2-grant