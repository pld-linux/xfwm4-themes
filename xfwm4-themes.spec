Summary:	Additional themes for xfwm4
Summary(pl):	Dodatkowe motywy do xfwm4
Name:		xfwm4-themes
Version:	4.1.99.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.berlios.de/pub/xfce-goodies/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	63c091efdba452191ea990f92c7302d2
Source1:	http://lo1sanok.eu.org/~troll/PLD/xfwm4-themes/xfwm4-theme-crystal.tar.gz
# Source1-md5:	80b0e81b4e70e530d5679f5a5dd41395
Source2:	http://lo1sanok.eu.org/~troll/PLD/xfwm4-themes/xfwm4-theme-plastik.tar.gz
# Source2-md5:	a71c676a10ba4b9d1aab4028ef435510
URL:		http://www.xfce.org/
BuildRequires:  autoconf
BuildRequires:  automake
Requires:	xfwm4
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A set of additional themes for the xfwm4 window manager.

%description -l pl
Zbiór dodatkowych tematów dla zarz±dcy okien xfwm4.

%prep
%setup -q -a1 -a2

%build
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
mv plastik-xfce plastik
cp -a plastik $RPM_BUILD_ROOT%{_datadir}/xfwm4/themes
cp -a crystal $RPM_BUILD_ROOT%{_datadir}/xfwm4/themes

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README TODO
%{_datadir}/themes/*
