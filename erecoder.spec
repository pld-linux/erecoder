Summary:	31337 recoder is a text/data recoder swiss army knife for h4x0rz
Name:		erecoder
Version:	0.2.1
Release:	1
License:	GPL v2
Group:		Applications/Text
Source0:	http://eleet.veuu.eu.org/erecoder-0.2.1.tar.gz
URL:		http://eleet.veuu.eu.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
31337 recoder (erecoder) is a text/data recoder swiss army knife for h4x0rz;).

Its features include:

    * Input from stdin, file or command line
    * Encoding byte values to numeric systems from binary to 36-ary;)
    * Encoding to escaped hexadecimal or octal
    * Encoding with ROT-x and Base64 encodings
    * Decoding of all above ;)
    * Mixing many different encodings


%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
