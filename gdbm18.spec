Summary:	GNU database library for C
Summary(de):	GNU-Datenbank-Library für C
Summary(fr):	La librairie GNU de bases de données pout le langage C
Summary(pl):	Biblioteka GNU bazy danych dla jêzyka C
Summary(ru):	âÉÂÌÉÏÔÅËÁ ÂÁÚÙ ÄÁÎÎÙÈ GNU ÄÌÑ C
Summary(uk):	â¦ÂÌ¦ÏÔÅËÁ ÂÁÚÉ ÄÁÎÉÈ GNU ÄÌÑ C
Name:		gdbm
Version:	1.8.3
Release:	7
License:	GPL
Group:		Libraries
Source0:	ftp://ftp.gnu.org/pub/gnu/gdbm/%{name}-%{version}.tar.gz
# Source0-md5:	1d1b1d5c0245b1c00aff92da751e9aa1
Patch0:		%{name}-info.patch
Patch1:		%{name}-jbj.patch
Patch2:		%{name}-linking.patch
Patch3:		%{name}-link-compat.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	texinfo
Obsoletes:	libgdbm2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gdbm is a GNU database indexing library, including routines which use
extensible hashing. gdbm works in a similar way to standard UNIX dbm
routines. gdbm is useful for developers who write C applications and
need access to a simple and efficient database or who are building C
applications which will use such a database.

%description -l de
Dies ist eine Datenbank-Index-Library für Programmierer, die
C-Anwendungen schreiben und eine einfache und leistungsfähige
Datenbank benötigen oder diese in C-Anwendungen einsetzen möchten.

%description -l fr
Une librairie d'indexation de bases de données. Elle est utile pour
ceux qui désirent écrivent des applications en C et ont besion
d'accéder à une base de données simple et efficace ou de construire
une application en C qui l'utilise.

%description -l pl
W pakiecie znajduje siê biblioteka indeksowania bazy danych.
Biblioteka ta jest szczególnie u¿yteczna dla ludzi, którzy pisz±
oprogramowanie w C i potrzebuj± prostej i szybkiej bazy danych, lub
dla tych którzy pisz± programy w C z wykorzystaniem tej biblioteki.

%description -l tr
gdbm bir veri tabaný dizinleme kitaplýðýdýr. C uygulamalarý yazýp
basit ve etkin bir þekilde veri tabanýna ulaþmak isteyenler için
yararlý olacaktýr.

%description -l ru
üÔÏ ÂÉÂÌÉÏÔÅËÁ ÄÌÑ ÒÁÂÏÔÙ Ó ÉÎÄÅËÓÉÒÏ×ÁÎÎÏÊ ÂÁÚÏÊ ÄÁÎÎÙÈ. ðÏÌÅÚÎÁ ÄÌÑ
ÔÅÈ, ËÔÏ ÒÁÚÒÁÂÁÔÙ×ÁÅÔ ÐÒÏÇÒÁÍÍÙ ÎÁ C É ËÏÍÕ ÎÕÖÅÎ ÄÏÓÔÕÐ Ë ÐÒÏÓÔÏÊ É
ÜÆÆÅËÔÉ×ÎÏÊ ÂÁÚÅ ÄÁÎÎÙÈ ÌÉÂÏ ÔÒÅÂÕÅÔÓÑ ÎÁÐÉÓÁÔØ ÐÒÏÇÒÁÍÍÕ, ËÏÔÏÒÁÑ ÅÅ
ÉÓÐÏÌØÚÕÅÔ.

%description -l uk
ãÅ Â¦ÂÌ¦ÏÔÅËÁ ÄÌÑ ÒÏÂÏÔÉ Ú ¦ÎÄÅËÓÏ×ÁÎÏÀ ÂÁÚÏÀ ÄÁÎÉÈ. ëÏÒÉÓÎÁ ÄÌÑ ÔÉÈ,
ÈÔÏ ÒÏÚÒÏÂÌÑ¤ ÐÒÏÇÒÁÍÉ ÎÁ C ¦ ËÏÍÕ ÐÏÔÒ¦ÂÅÎ ÄÏÓÔÕÐ ÄÏ ÐÒÏÓÔÏ§ ÔÁ
ÅÆÅËÔÉ×ÎÏ§ ÂÁÚÉ ÄÁÎÉÈ ÁÂÏ ÐÏÔÒ¦ÂÎÏ ÎÁÐÉÓÁÔÉ ÐÒÏÇÒÁÍÕ, ÝÏ §§
×ÉËÏÒÉÓÔÏ×Õ¤.

%package devel
Summary:	development libraries and header files for gdbm
Summary(de):	Entwicklungs-Libraries und Header-Dateien für gdbm
Summary(fr):	Bibliothèques de développement et en-têtes pour gdbm
Summary(pl):	Biblioteki i pliki nag³ówkowe dla gdbm
Summary(ru):	âÉÂÌÉÏÔÅËÁ É ÈÅÄÅÒÙ gdbm ÄÌÑ ÒÁÚÒÁÂÏÔÞÉËÏ×
Summary(tr):	gdbm için baþlýk dosyalarý ve geliþtirme kitaplýklarý
Summary(uk):	â¦ÂÌ¦ÏÔÅËÁ ÔÁ ÈÅÄÅÒÉ gdbm ÄÌÑ ÐÒÏÇÒÁÍ¦ÓÔ¦×
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	libgdbm2-devel

%description devel
These are the development libraries and header files for gdbm, the GNU
database system. These are required if you plan to do development
using the gdbm database.

%description devel -l de
Dies sind die Entwicklungs-Libraries und Header-Dateien für gdbm, das
GNU-Datenbanksystem. Sie sind darauf angewiesen, wenn Sie vorhaben,
die gdbm-Datenbank für Entwicklungsarbeiten zu benutzen.

%description devel -l fr
Ce sont les librairies de développement et les fichiers d'en-tête pour
gdbm, le système de base de données GNU. Ceci est nécessaire si vous
désirez développer en utilisant la base de données gdbm.

%description devel -l pl
W pakiecie tym znajduj± siê pliki nag³ówkowe i biblioteki dla systemu
bazy danych GNU.

%description devel -l tr
GNU veri tabaný sistemi gdbm ile program geliþtirmek için gereken
baþlýk dosyalarý ve kitaplýklar.

%description devel -l ru
üÔÏ ÂÉÂÌÉÏÔÅËÁ ÄÌÑ ÒÁÚÒÁÂÏÔÞÉËÏ× É ÈÅÄÅÒÙ gdbm, ÂÁÚÙ ÄÁÎÎÙÈ GNU. ïÎÉ
ÎÕÖÎÙ, ÅÓÌÉ ×Ù ÓÏÂÉÒÁÅÔÅÓØ ÒÁÚÒÁÂÁÔÙ×ÁÔØ ÐÒÏÇÒÁÍÍÙ Ó ÉÓÐÏÌØÚÏ×ÁÎÉÅÍ
gdbm.

%description devel -l uk
ãÅ Â¦ÂÌ¦ÏÔÅËÁ ÄÌÑ ÐÒÏÇÒÁÍ¦ÓÔ¦× ÔÁ ÈÅÄÅÒÉ gdbm, ÂÁÚÉ ÄÁÎÉÈ GNU. ÷ÏÎÉ
ÐÏÔÒ¦ÂÎ¦, ÑËÝÏ ×É ÚÂÉÒÁ¤ÔÅÓØ ÒÏÚÒÏÂÌÑÔÉ ÐÒÏÇÒÁÍÉ Ú ×ÉËÏÒÉÓÔÁÎÎÑÍ gdbm.

%package static
Summary:	Static gdbm library
Summary(pl):	Biblioteki statyczne gdbm
Summary(ru):	óÔÁÔÉÞÅÓËÁÑ ÂÉÂÌÉÏÔÅËÁ gdbm
Summary(uk):	óÔÁÔÉÞÎÁ Â¦ÂÌ¦ÏÔÅËÁ gdbm
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static gdbm library.

%description static -l pl
Biblioteka statyczna gdbm.

%description static -l ru
üÔÏ ÓÔÁÔÉÞÅÓËÁÑ ÂÉÂÌÉÏÔÅËÁ gdbm, ÂÁÚÙ ÄÁÎÎÙÈ GNU.

%description static -l uk
ãÅ ÓÔÁÔÉÞÎÁ Â¦ÂÌ¦ÏÔÅËÁ gdbm, ÂÁÚÉ ÄÁÎÉÈ GNU.

%prep
%setup  -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install install-compat \
	INSTALL_ROOT=$RPM_BUILD_ROOT \
	BINOWN=`id -u` BINGRP=`id -g`

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_mandir}/man3/*
%{_includedir}/*
%{_infodir}/gdbm*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
