Name:           rpmrebuild
Version:        2.4
Release:        %mkrel 1
Epoch:          0
Summary:        Tool to build an RPM file from a package that has already been installed
Group:          System/Configuration/Packaging
License:        GPL
URL:            http://rpmrebuild.sourceforge.net/
Source0:        http://umn.dl.sourceforge.net/sourceforge/rpmrebuild/rpmrebuild.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch:      noarch
Requires:       rpm

%description
rpmrebuild is a tool to build an RPM file from a package that has
already been installed. For basic use, rpmrebuild does not require
any RPM building knowledge. On debian, the equivalent program is
dpkg-repack.

%prep
%setup -q -c
%{__mv} rpmrebuild_parser.src rpmrebuild_parser.src.bak
/bin/echo '#!/bin/bash' > rpmrebuild_parser.src
%{__cat} rpmrebuild_parser.src.bak >> rpmrebuild_parser.src
%{__rm} rpmrebuild_parser.src.bak
%{__perl} -pi -e 's|%{_prefix}/lib/rpmrebuild|%{_datadir}/rpmrebuild|g' \
  Makefile.include \
  popt-with-POPTdesc \
  popt-without-POPTdesc \
  rpmrebuild \
  rpmrebuild.1 \
  rpmrebuild.1.in \
  spec.scripts \
  spec.scripts.input

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
%{_mandir}/man1/rpmrebuild.1*
%{_mandir}/man1/demo.plug.1rrp*
%{_mandir}/man1/file2pacDep.plug.1rrp*
%{_mandir}/man1/nodoc.plug.1rrp*
%{_mandir}/man1/rpmrebuild_plugins.1*
%{_mandir}/man1/uniq.plug.1rrp*
%defattr(-,root,root,0755)
%{_datadir}/rpmrebuild


