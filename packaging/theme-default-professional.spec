Name: theme-default-professional
Group: Applications/Themes
Version: 6.2.1
Release: 1%{dist}
Summary: ClearOS Professional 6 theme
License: Copyright 2011-2012 ClearCenter
Packager: ClearCenter
Vendor: ClearCenter
Source: %{name}-%{version}.tar.gz
Requires: theme-default
Provides: theme-default-driver
Provides: system-theme
Obsoletes: app-theme-clearos5x
Obsoletes: theme-default-community
# TODO: Beta only obsoletes, remove after 6 Final
Obsoletes: theme-clearos6x-community
Obsoletes: theme-clearos6x-professional
Buildarch: noarch

%description
ClearOS Professional 6 webconfig theme

%prep
%setup -q
%build

%install
mkdir -p -m 755 $RPM_BUILD_ROOT/usr/clearos/themes/default
cp -r * $RPM_BUILD_ROOT/usr/clearos/themes/default

%files
%defattr(-,root,root)
%dir /usr/clearos/themes/default
/usr/clearos/themes/default
