#
%define		snap 20040616
#
Summary:	Additional themes for xfwm4
Summary(pl):	Dodatkowe motywy do xfwm4
Name:		xfwm4-themes
Version:	4.1.0
Release:	0.%{snap}.1
License:	GPL
Group:		X11/Applications
Source0:	%{name}-snap-%{snap}.tar.bz2
# Source0-md5:	8e8878dd011e2ee16a78f575e1b527b6
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
%setup -q -n %{name} -a1 -a2

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README TODO
%{_datadir}/themes/*
