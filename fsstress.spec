%define name fsstress
%define version 1.0
%define release %mkrel 3

Summary: A filesystem stressing tool
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.gz
License: GPL
Group: System/Kernel and hardware 
Url: http://cvs.sourceforge.net/viewcvs.py/ltp/ltp/testcases/kernel/fs/fsstress/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot


%description
A filesystem stessing tool

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

