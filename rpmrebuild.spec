Name:           rpmrebuild
Version:        2.2.3
Release:        4
Epoch:          1
Summary:        Tool to build an RPM file from the RPM database
Group:          System/Configuration/Packaging
License:        GPLv2+
URL:            http://rpmrebuild.sourceforge.net/
Source0:        http://downloads.sourceforge.net/sourceforge/rpmrebuild/rpmrebuild-%version.tar.gz
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
%{_mandir}/man1/demofiles.plug.1rrp*
%{_mandir}/man1/file2pacDep.plug.1rrp*
%{_mandir}/man1/nodoc.plug.1rrp*
%{_mandir}/man1/rpmrebuild.1*
%{_mandir}/man1/rpmrebuild_plugins.1*
%{_mandir}/man1/set_tag.plug.1rrp*
%{_mandir}/man1/uniq.plug.1rrp*
%lang(fr) %{_mandir}/fr*/man1/demo.plug.1rrp*
%lang(fr) %{_mandir}/fr*/man1/demofiles.plug.1rrp*
%lang(fr) %{_mandir}/fr*/man1/file2pacDep.plug.1rrp*
%lang(fr) %{_mandir}/fr*/man1/nodoc.plug.1rrp*
%lang(fr) %{_mandir}/fr*/man1/rpmrebuild.1*
%lang(fr) %{_mandir}/fr*/man1/rpmrebuild_plugins.1*
%lang(fr) %{_mandir}/fr*/man1/set_tag.plug.1rrp*
%lang(fr) %{_mandir}/fr*/man1/uniq.plug.1rrp*

%defattr(-,root,root,0755)
%{_datadir}/rpmrebuild


%changelog
* Tue Sep 08 2009 Thierry Vignaud <tvignaud@mandriva.com> 1:2.2.3-3mdv2010.0
+ Revision: 433454
- rebuild

* Fri Aug 08 2008 Thierry Vignaud <tvignaud@mandriva.com> 1:2.2.3-2mdv2009.0
+ Revision: 269222
- rebuild early 2009.0 package (before pixel changes)

* Thu Aug 07 2008 Funda Wang <fundawang@mandriva.org> 1:2.2.3-1mdv2009.0
+ Revision: 266474
- New version 2.2.3

* Wed Apr 30 2008 David Walluck <walluck@mandriva.org> 1:2.2.2.1-1mdv2009.0
+ Revision: 199624
- 2.2.2 (2.2.2-1)

* Mon Apr 21 2008 David Walluck <walluck@mandriva.org> 1:2.2.1.1-1mdv2009.0
+ Revision: 196033
- 2.2.1-1
- remove old source

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Oct 30 2007 David Walluck <walluck@mandriva.org> 1:2.2.0.1-1mdv2008.1
+ Revision: 103980
- bump version
- bump version

* Thu Oct 25 2007 David Walluck <walluck@mandriva.org> 1:2.2.0-1mdv2008.1
+ Revision: 102120
- 2.2.0 (2.4 was 2.0.4)


* Thu Jan 25 2007 David Walluck <walluck@mandriva.org> 2.4-1mdv2007.0
+ Revision: 113074
- fix install location
  fix some rpmlint warnings
- Import rpmrebuild

* Wed Jan 24 2007 David Walluck <walluck@mandriva.org> 0:2.4-1mdv2007.1
- release

