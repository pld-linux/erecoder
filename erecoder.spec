Summary:	31337 recoder is a text/data recoder swiss army knife for h4x0rz
Summary(pl):	31337 recoder to wszechstronny program do przekodowywania tekstu/danych dla h4x0rów
Name:		erecoder
Version:	0.3.0
Release:	1
License:	GPL v2
Group:		Applications/Text
Source0:	http://eleet.veuu.eu.org/%{name}-%{version}.tar.gz
# Source0-md5:	1931fb52a73c70275131211f3e0795c6
URL:		http://eleet.veuu.eu.org/
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

%description -l pl
31337 recoder (erecoder) to wszechstronne narzêdzie do przekodowywania
tekstu i danych dla hax0rów ;)

Jego mo¿liwo¶ci to m.in.:
 - czytanie ze standardowego wej¶cia, pliku lub linii poleceñ
 - kodowanie warto¶ci bajtów w systemach liczenia od binarnego do
   36-go
 - kodowanie w notacji szesnastkowej lub ósemkowej z backslashem
 - kodowanie ROT-x oraz Base64
 - dekodowanie wszystkiego powy¿szego ;)
 - mieszanie wielu ró¿nych kodowañ.

%prep
%setup -q

%build
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
