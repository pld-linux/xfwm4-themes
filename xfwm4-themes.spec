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
Source1:	http://www.prox.pl/~troll/PLD/xfwm4-themes/xfwm4-theme-crystal.tar.gz
# Source1-md5:	80b0e81b4e70e530d5679f5a5dd41395
Source2:	http://www.prox.pl/~troll/PLD/xfwm4-themes/xfwm4-theme-plastik.tar.gz
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

mv plastik-xfce plastik

for THEME in plastik crystal; do
  install -d $RPM_BUILD_ROOT%{_datadir}/themes/$THEME/xfce4
  cp -a $THEME $RPM_BUILD_ROOT%{_datadir}/themes/$THEME/xfwm4
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README TODO
%{_datadir}/themes/*
