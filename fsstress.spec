%define name fsstress
%define version 1.0
%define release 10

Summary: A filesystem stressing tool
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.gz
License: GPL v2
Group: System/Kernel and hardware 
Url: http://cvs.sourceforge.net/viewcvs.py/ltp/ltp/testcases/kernel/fs/fsstress/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot


%description
fsstress is a filesystem stressing tool.


%prep
%setup -q

%build
%make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}/
cp fsstress $RPM_BUILD_ROOT%{_bindir}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/fsstress



%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0-9mdv2011.0
+ Revision: 618362
- the mass rebuild of 2010.0 packages

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 1.0-8mdv2010.0
+ Revision: 428925
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.0-7mdv2009.0
+ Revision: 245585
- put a real description

  + Michael Scherer <misc@mandriva.org>
    - fix License
    - fix description

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.0-5mdv2009.0
+ Revision: 245431
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.0-3mdv2008.1
+ Revision: 136423
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - import fsstress


* Thu Jun 22 2006 Erwan Velu <erwan@seanodes.com> 1.0-3
- Rebuild

* Mon Mar 20 2006 Erwan Velu <erwan@seanodes.com> 1.0-2mdk
- mkrel
- rebuild

* Thu Jan 06 2005 Erwan Velu <erwan@seanodes.com> 1.0-1mdk
- Initial rpm, assuming its a 1.0 release (no clue in the code itself)
