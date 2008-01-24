Summary:	GNU database library for C
Summary(de.UTF-8):	GNU-Datenbank-Library für C
Summary(fr.UTF-8):	La librairie GNU de bases de données pout le langage C
Summary(pl.UTF-8):	Biblioteka GNU bazy danych dla języka C
Summary(ru.UTF-8):	Библиотека базы данных GNU для C
Summary(uk.UTF-8):	Бібліотека бази даних GNU для C
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
Patch4:		%{name}-make-jN.patch
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

%description -l de.UTF-8
Dies ist eine Datenbank-Index-Library für Programmierer, die
C-Anwendungen schreiben und eine einfache und leistungsfähige
Datenbank benötigen oder diese in C-Anwendungen einsetzen möchten.

%description -l fr.UTF-8
Une librairie d'indexation de bases de données. Elle est utile pour
ceux qui désirent écrivent des applications en C et ont besion
d'accéder à une base de données simple et efficace ou de construire
une application en C qui l'utilise.

%description -l pl.UTF-8
W pakiecie znajduje się biblioteka indeksowania bazy danych.
Biblioteka ta jest szczególnie użyteczna dla ludzi, którzy piszą
oprogramowanie w C i potrzebują prostej i szybkiej bazy danych, lub
dla tych którzy piszą programy w C z wykorzystaniem tej biblioteki.

%description -l tr.UTF-8
gdbm bir veri tabanı dizinleme kitaplığıdır. C uygulamaları yazıp
basit ve etkin bir şekilde veri tabanına ulaşmak isteyenler için
yararlı olacaktır.

%description -l ru.UTF-8
Это библиотека для работы с индексированной базой данных. Полезна для
тех, кто разрабатывает программы на C и кому нужен доступ к простой и
эффективной базе данных либо требуется написать программу, которая ее
использует.

%description -l uk.UTF-8
Це бібліотека для роботи з індексованою базою даних. Корисна для тих,
хто розробляє програми на C і кому потрібен доступ до простої та
ефективної бази даних або потрібно написати програму, що її
використовує.

%package devel
Summary:	development libraries and header files for gdbm
Summary(de.UTF-8):	Entwicklungs-Libraries und Header-Dateien für gdbm
Summary(fr.UTF-8):	Bibliothèques de développement et en-têtes pour gdbm
Summary(pl.UTF-8):	Biblioteki i pliki nagłówkowe dla gdbm
Summary(ru.UTF-8):	Библиотека и хедеры gdbm для разработчиков
Summary(tr.UTF-8):	gdbm için başlık dosyaları ve geliştirme kitaplıkları
Summary(uk.UTF-8):	Бібліотека та хедери gdbm для програмістів
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	libgdbm2-devel

%description devel
These are the development libraries and header files for gdbm, the GNU
database system. These are required if you plan to do development
using the gdbm database.

%description devel -l de.UTF-8
Dies sind die Entwicklungs-Libraries und Header-Dateien für gdbm, das
GNU-Datenbanksystem. Sie sind darauf angewiesen, wenn Sie vorhaben,
die gdbm-Datenbank für Entwicklungsarbeiten zu benutzen.

%description devel -l fr.UTF-8
Ce sont les librairies de développement et les fichiers d'en-tête pour
gdbm, le système de base de données GNU. Ceci est nécessaire si vous
désirez développer en utilisant la base de données gdbm.

%description devel -l pl.UTF-8
W pakiecie tym znajdują się pliki nagłówkowe i biblioteki dla systemu
bazy danych GNU.

%description devel -l tr.UTF-8
GNU veri tabanı sistemi gdbm ile program geliştirmek için gereken
başlık dosyaları ve kitaplıklar.

%description devel -l ru.UTF-8
Это библиотека для разработчиков и хедеры gdbm, базы данных GNU. Они
нужны, если вы собираетесь разрабатывать программы с использованием
gdbm.

%description devel -l uk.UTF-8
Це бібліотека для програмістів та хедери gdbm, бази даних GNU. Вони
потрібні, якщо ви збираєтесь розробляти програми з використанням gdbm.

%package static
Summary:	Static gdbm library
Summary(pl.UTF-8):	Biblioteki statyczne gdbm
Summary(ru.UTF-8):	Статическая библиотека gdbm
Summary(uk.UTF-8):	Статична бібліотека gdbm
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static gdbm library.

%description static -l pl.UTF-8
Biblioteka statyczna gdbm.

%description static -l ru.UTF-8
Это статическая библиотека gdbm, базы данных GNU.

%description static -l uk.UTF-8
Це статична бібліотека gdbm, бази даних GNU.

%prep
%setup  -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install install-compat \
	INSTALL_ROOT=$RPM_BUILD_ROOT \
	BINOWN=`id -u` BINGRP=`id -g`

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post devel	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun devel	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

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
