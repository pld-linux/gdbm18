Summary:	GNU database library for C
Summary(de):	GNU-Datenbank-Library für C
Summary(fr):	La librairie GNU de bases de données pout le langage C.
Summary(pl):	GNU biblioteka bazy danych la jêzyka C
Name:		gdbm
Version:	1.7.3
Release:	22
Copyright:	GPL
Group:		Libraries
Group(pl):	Biblioteki
Source:		ftp://prep.ai.mit.edu/pub/gnu/%{name}-%{version}.tar.gz
Patch0:		gdbm-shlib.patch
Patch1:		gdbm-info.patch
Patch2:		gdbm-configure.patch
Buildroot:	/tmp/%{name}-%{version}-root

%description
This is a database indexing library. It is useful for those who need 
to write C applications and need access to a simple and efficient
database or build C applications which use it.

%description -l de
Dies ist eine Datenbank-Index-Library für Programmierer, die 
C-Anwendungen schreiben und eine einfache und leistungsfähige
Datenbank benötigen oder diese in C-Anwendungen einsetzen möchten.

%description -l fr
Une librairie d'indexation de bases de données. Elle est utile pour ceux
qui désirent écrivent des applications en C et ont besion d'accéder à
une base de données simple et efficace ou de construire une application
en C qui l'utilise.

%description -l pl
W pakiecie znajduje siê biblioteka indeksowania bazy danych. Biblioteka
ta jest szczególnie uzyteczna dla ludzi, którzy pisz± oprogramowanie w C
i potrzebuj± prostej i szybkiej bazy danych, lub dla tych którzy pisz±
programy w C z wykorzystaniem tej biblioteki. 

%description -l tr
gdbm bir veri tabaný dizinleme kitaplýðýdýr. C uygulamalarý yazýp basit ve
etkin bir þekilde veri tabanýna ulaþmak isteyenler için yararlý olacaktýr.

%package devel
Summary:	development libraries and header files for gdbm
Summary(de):	Entwicklungs-Libraries und Header-Dateien für gdbm 
Summary(fr):	Bibliothèques de développement et en-têtes pour gdbm
Summary(pl):	Biblioteki i pliki nag³ówkowe dla gdbm
Summary(tr):	gdbm için baþlýk dosyalarý ve geliþtirme kitaplýklarý
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}
Prereq:		/sbin/install-info

%description devel
These are the development libraries and header files for gdbm, the
GNU database system.  These are required if you plan to do 
development using the gdbm database.

%description -l de devel
Dies sind die Entwicklungs-Libraries und Header-Dateien für gdbm, das
GNU-Datenbanksystem. Sie sind darauf angewiesen, wenn Sie vorhaben,
die gdbm-Datenbank für Entwicklungsarbeiten zu benutzen.

%description -l fr devel
Ce sont les librairies de développement et les fichiers d'en-tête pour gdbm,
le système de base de données GNU. Ceci est nécessaire si vous désirez 
développer en utilisant la base de données gdbm.

%description -l pl devel
W pakiecie tym znajduj± siê pliki nag³ówkowe i biblioteki dla GNU
systemu bazy danych.

%description -l tr devel
GNU veri tabaný sistemi gdbm ile program geliþtirmek için gereken baþlýk
dosyalarý ve kitaplýklar.

%package static
Summary:	Static gdbm library
Summary(pl):	Biblioteki statyczne gdbm
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Static gdbm library.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
mkdir shared
aclocal
autoheader
%configure

make CFLAGS="$RPM_OPT_FLAGS"
make CFLAGS="$RPM_OPT_FLAGS" shared

makeinfo gdbm.texinfo

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/{lib,include,info,man/man3}

make install prefix=$RPM_BUILD_ROOT/usr

ln -sf libgdbm.so.2.0.0 $RPM_BUILD_ROOT/usr/lib/libgdbm.so

strip --strip-unneeded $RPM_BUILD_ROOT/usr/lib/lib*.so.*.*

gzip -fn9 $RPM_BUILD_ROOT/usr/{info/gdbm*info*,man/man3/*}

%post -p /sbin/ldconfig

%post devel
/sbin/install-info /usr/info/gdbm.info.gz /etc/info-dir

%postun -p /sbin/ldconfig

%preun devel
if [ "$1" = "0" ]; then
	/sbin/install-info --delete /usr/info/gdbm.info.gz /etc/info-dir
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) /usr/lib/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) /usr/lib/lib*.so
/usr/man/man3/*
/usr/include/*
/usr/info/gdbm*

%files static
%defattr(644,root,root,755)
/usr/lib/lib*.a

%changelog
* Thu Apr 29 1999 Artur Frysiak <wiget@pld.org.pl>
  [1.7.3-22]
- used %%configure macro
- added gdbm-configure.patch

* Sun Mar 14 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.7.3-21]
- added --strip-unneeded parameter on striping shared libraries,
- removed man group from man pages.

* Mon Jan 04 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.7.3-20]
- standarized {un}registering info pages (added gdbm-info.patch),
- added gzipping man pages.

* Sun Nov 22 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.7.3-19]
- removed "Prereq: /sbin/install-info" from static,
- fixed --entry text on {un}registering info page for ed in %post
  %preun in devel.

* Wed Sep 30 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
- build against glibc-2.1,
- translation modified for pl.

* Sun Aug 30 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.7.3-18]
- added -q %setup parameter,
- changed Buildroot to /tmp/%%{name}-%%{version}-root,
- added using %%{name} and %%{version} in Source,
- added static subpackage,
- changed dependencies to "Requires: %%{name} = %%{version}" in devel
  subpackage,
- added stripping shared libraries,
- added %attr and %defattr macros in %files (allows build package from
  non-root account).

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Apr 30 1998 Cristian Gafton <gafton@redhat.com>
- gdbm-devel moved to Development/Libraries

* Wed Apr 08 1998 Cristian Gafton <gafton@redhat.com>
- buildroot and built for Manhattan

* Tue Oct 14 1997 Donnie Barnes <djb@redhat.com>
- spec file cleanups

* Thu Jun 12 1997 Erik Troan <ewt@redhat.com>
- built against glibc
