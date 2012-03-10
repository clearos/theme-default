Name: theme-default
Group: Applications/Themes
Version: 6.2.0.beta3.5
Release: 1%{dist}
Summary: ClearOS 6 base theme
License: Copyright 2011 ClearFoundation
Packager: ClearFoundation
Vendor: ClearFoundation
Source: %{name}-%{version}.tar.gz
Requires: clearos-framework >= 6.2.0.beta3.4
Requires: theme-default-driver
# TODO: Beta only obsoletes, remove after 6 Final
Obsoletes: theme-clearos6x
Buildarch: noarch

%description
ClearOS 6 base webconfig theme

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
