Summary:	Additional themes for xfwm4
Summary(pl):	Dodatkowe motywy do xfwm4
Name:		xfwm4-themes
Version:	3.99.2
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://linux.imp.mx/xfce4/rc2/xfce4-rc2/src/%{name}-%{version}.tar.gz
# Source0-md5:	0554fa59d6c2d136eeb36aff616d4db2
URL:		http://www.xfce.org/
Requires:	xfwm4
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A set of additional themes for the xfwm4 window manager.

%description -l pl
Zbiór dodatkowych tematów dla zarz±dcy okien xfwm4.

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
