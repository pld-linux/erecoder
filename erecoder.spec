Summary:	31337 recoder is a text/data recoder swiss army knife for h4x0rz
Summary(pl.UTF-8):	31337 recoder to wszechstronny program do przekodowywania tekstu/danych dla h4x0rów
Name:		erecoder
Version:	0.4.1
Release:	2
License:	GPL v2
Group:		Applications/Text
Source0:	http://eleet.czad.org/%{name}-%{version}.tar.gz
# Source0-md5:	74c6b9f5cf01d487d632429dfa02c17b
Patch0:		%{name}-po.patch
URL:		http://eleet.czad.org/
BuildRequires:	automake
BuildRequires:	gettext-tools
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
31337 recoder (erecoder) is a text/data recoder swiss army knife for
h4x0rz;).

Its features include:
 - Input from stdin, file or command line
 - Encoding byte values to numeric systems from binary to 36-ary;)
 - Encoding to escaped hexadecimal or octal
 - Encoding with ROT-x and Base64 encodings
 - Decoding of all above ;)
 - Mixing many different encodings

%description -l pl.UTF-8
31337 recoder (erecoder) to wszechstronne narzędzie do przekodowywania
tekstu i danych dla hax0rów ;)

Jego możliwości to m.in.:
 - czytanie ze standardowego wejścia, pliku lub linii poleceń
 - kodowanie wartości bajtów w systemach liczenia od binarnego do
   36-go
 - kodowanie w notacji szesnastkowej lub ósemkowej z backslashem
 - kodowanie ROT-x oraz Base64
 - dekodowanie wszystkiego powyższego ;)
 - mieszanie wielu różnych kodowań.

%prep
%setup -q
%patch0 -p1

%build
cp /usr/share/automake/config.sub .
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README AUTHORS
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
