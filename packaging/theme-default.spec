Name: theme-default
Group: Applications/Themes
Version: 6.5.10
Release: 1%{dist}
Summary: ClearOS 6 base theme
License: Copyright 2011-2015 ClearFoundation
Packager: ClearFoundation
Vendor: ClearFoundation
Source: %{name}-%{version}.tar.gz
Requires: clearos-framework >= 6.6.2
Requires: theme-default-driver
Buildarch: noarch

%description
ClearOS 6 base webconfig theme

%prep
%setup -q
%build

%install
mkdir -p -m 755 $RPM_BUILD_ROOT/usr/clearos/themes/default
cp -r * $RPM_BUILD_ROOT/usr/clearos/themes/default

rm -f $RPM_BUILD_ROOT/usr/clearos/themes/default/css/theme-extras.css
rm -f $RPM_BUILD_ROOT/usr/clearos/themes/default/images/login-green.png
rm -f $RPM_BUILD_ROOT/usr/clearos/themes/default/images/login-orange.png
rm -f $RPM_BUILD_ROOT/usr/clearos/themes/default/images/arrow-down-orange.png
rm -f $RPM_BUILD_ROOT/usr/clearos/themes/default/images/console-orange*.jpg
rm -f $RPM_BUILD_ROOT/usr/clearos/themes/default/images/favicon*.ico
rm -f $RPM_BUILD_ROOT/usr/clearos/themes/default/images/header-bg-orange.png
rm -f $RPM_BUILD_ROOT/usr/clearos/themes/default/images/help-orange.png
rm -f $RPM_BUILD_ROOT/usr/clearos/themes/default/images/logo-green.png
rm -f $RPM_BUILD_ROOT/usr/clearos/themes/default/images/logo-orange.png
rm -f $RPM_BUILD_ROOT/usr/clearos/themes/default/images/orange-stroke*.jpg
rm -f $RPM_BUILD_ROOT/usr/clearos/themes/default/images/tabs-nav-hover-orange.png
rm -f $RPM_BUILD_ROOT/usr/clearos/themes/default/images/tabs-nav-selected-orange.png
rm -f $RPM_BUILD_ROOT/usr/clearos/themes/default/images/user-guide-orange.png


%files
%defattr(-,root,root)
%dir /usr/clearos/themes/default
/usr/clearos/themes/default
