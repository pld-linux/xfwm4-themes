Summary: 	Additionnal themes for xfwm4
Name: 		xfwm4-themes
Version: 	3.90.0
Release: 	0.1
License:	GPL
URL: 		http://www.xfce.org/
Source0: 	http://belnet.dl.sourceforge.net/sourceforge/xfce/%{name}-%{version}.tar.gz
# Source0-md5:	e15b89a8c7cad7d010f53a590223fb62
Group: 		X11/Applications
Requires:	xfwm4
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A set of additionnal themes for the xfwm4 window manager.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README INSTALL TODO COPYING AUTHORS
%{_datadir}/xfwm4/themes
