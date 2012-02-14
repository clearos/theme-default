Name: theme-clearos6x
Group: Applications/Themes
Version: 6.2.0.beta3.2
Release: 1%{dist}
Summary: ClearOS 6 base theme
License: Copyright 2011 ClearFoundation
Packager: ClearFoundation
Vendor: ClearFoundation
Source: %{name}-%{version}.tar.gz
Requires: theme-clearos6x-driver
Buildarch: noarch

%description
ClearOS 6 base webconfig theme

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
