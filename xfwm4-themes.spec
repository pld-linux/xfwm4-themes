Summary:	Additional themes for xfwm4
Summary(pl):	Dodatkowe motywy do xfwm4
Name:		xfwm4-themes
Version:	4.2.3
Release:	1
License:	GPL
Group:		X11/Applications
Source0:        http://hannelore.f1.fhtw-berlin.de/mirrors/xfce4/xfce-%{version}/src/%{name}-%{version}.tar.gz
# Source0-md5:	98dbf2f80f30206ca1bcaff9358bedfd
Source1:	http://ep09.pld-linux.org/~havner/xfwm4-theme-crystal.tar.gz
# Source1-md5:	2968f2cb73e8157868dd4ec683bc8e21
Source2:	http://ep09.pld-linux.org/~havner/xfwm4-theme-plastik.tar.gz
# Source2-md5:	abd9c2a105ccddf08dec8f860e37abb2
URL:		http://www.xfce.org/
BuildRequires:	autoconf
BuildRequires:	automake
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
cp -a plastik $RPM_BUILD_ROOT%{_datadir}/themes
cp -a crystal $RPM_BUILD_ROOT%{_datadir}/themes

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README TODO
%{_datadir}/themes/*
