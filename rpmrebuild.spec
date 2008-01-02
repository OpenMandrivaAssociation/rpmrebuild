Name:           rpmrebuild
Version:        2.2.0.1
Release:        %mkrel 1
Epoch:          1
Summary:        Tool to build an RPM file from the RPM database
Group:          System/Configuration/Packaging
License:        GPL
URL:            http://rpmrebuild.sourceforge.net/
Source0:        http://easynews.dl.sourceforge.net/sourceforge/rpmrebuild/rpmrebuild-2.2.0-1.tar.gz
Requires:       rpm-build
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

%description
rpmrebuild allows for the building of an RPM file from an installed RPM
or from another RPM file with or without changes (batch or interactive).
It can be extended by a plugin system.

Typical usage is the easy repackaging of software after a configuration
change.

%prep
%setup -q -c
%{__mv} rpmrebuild_parser.src rpmrebuild_parser.src.bak
/bin/echo '#!/bin/bash' > rpmrebuild_parser.src
%{__cat} rpmrebuild_parser.src.bak >> rpmrebuild_parser.src
%{__rm} rpmrebuild_parser.src.bak
%{__perl} -pi -e 's|%{_prefix}/lib/rpmrebuild|%{_datadir}/rpmrebuild|g' \
  rpmrebuild \
  popt-without-POPTdesc \
  popt-with-POPTdesc \
  spec.scripts.input \
  man/en/rpmrebuild.1.in \
  man/fr/rpmrebuild.1.in \
  Makefile.include \
  rpmrebuild.files \
  rpmrebuild.spec

%build
%{make}

%install
%{__rm} -rf %{buildroot}
%{makeinstall_std}
%{__chmod} 0755 %{buildroot}%{_datadir}/rpmrebuild/{*.s{h,rc},plugins/*.sh}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc AUTHORS Changelog COPYING COPYRIGHT LISEZ.MOI News README Release rpmrebuild.lsm Todo Version
%attr(0755,root,root) %{_bindir}/rpmrebuild
%{_mandir}/man1/demo.plug.1rrp*
%{_mandir}/man1/file2pacDep.plug.1rrp*
%{_mandir}/man1/nodoc.plug.1rrp*
%{_mandir}/man1/rpmrebuild.1*
%{_mandir}/man1/rpmrebuild_plugins.1*
%{_mandir}/man1/uniq.plug.1rrp*
%lang(fr) %{_mandir}/fr/man1/demo.plug.1rrp*
%lang(fr) %{_mandir}/fr/man1/file2pacDep.plug.1rrp*
%lang(fr) %{_mandir}/fr/man1/nodoc.plug.1rrp*
%lang(fr) %{_mandir}/fr/man1/rpmrebuild.1*
%lang(fr) %{_mandir}/fr/man1/rpmrebuild_plugins.1*
%lang(fr) %{_mandir}/fr/man1/uniq.plug.1rrp*
%defattr(-,root,root,0755)
%{_datadir}/rpmrebuild
