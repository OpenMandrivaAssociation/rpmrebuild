Name:           rpmrebuild
Version:        2.11
Release:        4
Epoch:          1
Summary:        Tool to build an RPM file from the RPM database
Group:          System/Configuration/Packaging
License:        GPLv2+
URL:            https://rpmrebuild.sourceforge.net/
Source0:        http://downloads.sourceforge.net/sourceforge/rpmrebuild/rpmrebuild-%{version}.tar.gz
Patch0:		rpmrebuild-2.11-rpm5.patch
Requires:       rpm-build
BuildArch:      noarch

%description
rpmrebuild allows for the building of an RPM file from an installed RPM
or from another RPM file with or without changes (batch or interactive).
It can be extended by a plugin system.

Typical usage is the easy repackaging of software after a configuration
change.

%prep
%setup -c rpmrebuild
%patch0 -p1

%build
%make

%install
%makeinstall_std

%clean

%files -f rpmrebuild.files
