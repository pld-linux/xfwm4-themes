Summary:	Additional themes for xfwm4
Summary(pl):	Dodatkowe motywy do xfwm4
Name:		xfwm4-themes
Version:	3.99.4
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.xfce.org/archive/xfce4-rc4/src/%{name}-%{version}.tar.gz
# Source0-md5:	b44bad7c82e5cf1123ff8e557844726d
URL:		http://www.xfce.org/
Requires:	xfwm4
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A set of additional themes for the xfwm4 window manager.

%description -l pl
Zbi�r dodatkowych temat�w dla zarz�dcy okien xfwm4.

%prep
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README TODO
%{_datadir}/xfwm4/themes/*
