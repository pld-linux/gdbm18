Summary:	GNU database library for C - version 1.8
Summary(de.UTF-8):	GNU-Datenbank-Library für C v1.8
Summary(fr.UTF-8):	La librairie GNU de bases de données pout le langage C v1.8
Summary(pl.UTF-8):	Biblioteka GNU bazy danych dla języka C - wersja 1.8
Summary(ru.UTF-8):	Библиотека базы данных GNU для C v1.8
Summary(uk.UTF-8):	Бібліотека бази даних GNU для C v1.8
Name:		gdbm18
Version:	1.8.3
Release:	2
License:	GPL v2+
Group:		Libraries
Source0:	http://ftp.gnu.org/gnu/gdbm/gdbm-%{version}.tar.gz
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
Obsoletes:	gdbm < 1.9
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gdbm is a GNU database indexing library, including routines which use
extensible hashing. gdbm works in a similar way to standard UNIX dbm
routines. gdbm is useful for developers who write C applications and
need access to a simple and efficient database or who are building C
applications which will use such a database.

This package contains gdbm 1.8.x libraries for compatibility.

%description -l pl.UTF-8
W pakiecie znajduje się biblioteka indeksowania bazy danych.
Biblioteka ta jest szczególnie użyteczna dla ludzi, którzy piszą
oprogramowanie w C i potrzebują prostej i szybkiej bazy danych, lub
dla tych którzy piszą programy w C z wykorzystaniem tej biblioteki.

Ten pakiet zawiera biblioteki gdbm w wersji 1.8.x dla zachowania
kompatybilności.

%package devel
Summary:	Header files for gdbm 1.8
Summary(de.UTF-8):	Header-Dateien für gdbm 1.8
Summary(fr.UTF-8):	Bibliothèques de développement et en-têtes pour gdbm 1.8
Summary(pl.UTF-8):	Pliki nagłówkowe dla gdbm 1.8
Summary(ru.UTF-8):	Библиотека и хедеры gdbm 1.8 для разработчиков
Summary(tr.UTF-8):	gdbm 1.8 için başlık dosyaları ve geliştirme kitaplıkları
Summary(uk.UTF-8):	Бібліотека та хедери gdbm 1.8 для програмістів
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	libgdbm2-devel

%description devel
These are the header files for gdbm 1.8, the GNU database system.
These are required if you plan to do development using the gdbm
database.

%description devel -l pl.UTF-8
W pakiecie tym znajdują się pliki nagłówkowe dla systemu bazy danych
GNU w wersji 1.8.

%package static
Summary:	Static gdbm 1.8 libraries
Summary(pl.UTF-8):	Biblioteki statyczne gdbm 1.8
Summary(ru.UTF-8):	Статическая библиотека gdbm 1.8
Summary(uk.UTF-8):	Статична бібліотека gdbm 1.8
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static gdbm 1.8 libraries.

%description static -l pl.UTF-8
Biblioteki statyczne gdbm 1.8.

%description static -l ru.UTF-8
Это статическая библиотека gdbm 1.8, базы данных GNU.

%description static -l uk.UTF-8
Це статична бібліотека gdbm 1.8, бази даних GNU.

%prep
%setup -q -n gdbm-%{version}
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

install -d $RPM_BUILD_ROOT%{_includedir}/gdbm-1.8
mv $RPM_BUILD_ROOT%{_includedir}/*.h $RPM_BUILD_ROOT%{_includedir}/gdbm-1.8
for ext in so a ; do
	mv $RPM_BUILD_ROOT%{_libdir}/libgdbm.${ext} $RPM_BUILD_ROOT%{_libdir}/libgdbm-1.8.${ext}
	mv $RPM_BUILD_ROOT%{_libdir}/libgdbm_compat.${ext} $RPM_BUILD_ROOT%{_libdir}/libgdbm_compat-1.8.${ext}
done
# don't mess with library name different from .so/.la, just drop libtool files
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libgdbm*.la
# provided by main gdbm
%{__rm} $RPM_BUILD_ROOT{%{_mandir}/man3/gdbm.3,%{_infodir}/gdbm.info*}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post	devel -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	devel -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libgdbm.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgdbm.so.3
%attr(755,root,root) %{_libdir}/libgdbm_compat.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgdbm_compat.so.3

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgdbm-1.8.so
%attr(755,root,root) %{_libdir}/libgdbm_compat-1.8.so
%{_includedir}/gdbm-1.8

%files static
%defattr(644,root,root,755)
%{_libdir}/libgdbm-1.8.a
%{_libdir}/libgdbm_compat-1.8.a
