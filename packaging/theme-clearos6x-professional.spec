Name: theme-clearos6x-professional
Group: Applications/Themes
Version: 6.2.0.beta3.2
Release: 1%{dist}
Summary: ClearOS Professional 6 theme
License: Copyright 2011-2012 ClearCenter
Packager: ClearCenter
Vendor: ClearCenter
Source: %{name}-%{version}.tar.gz
Requires: theme-clearos6x
Provides: theme-clearos6x-driver
Provides: system-theme
Obsoletes: app-theme-clearos5x
Buildarch: noarch

%description
ClearOS Professional 6 webconfig theme

%prep
%setup -q
%build

%install
mkdir -p -m 755 $RPM_BUILD_ROOT/usr/clearos/themes/clearos6x
cp -r * $RPM_BUILD_ROOT/usr/clearos/themes/clearos6x

%files
%defattr(-,root,root)
%dir /usr/clearos/themes/clearos6x
/usr/clearos/themes/clearos6x
