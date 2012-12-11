%define name	vrflash
%define version	0.24
%define release	%mkrel 8

Summary:   Flash utility for the Agenda VR3 Linux PDA
Name:	   %{name}
Version:   %{version}
Release:   %{release}
URL:	   http://www.csee.umbc.edu/~acedil1/agenda/little.shtml
Source:    %{name}-%{version}.tar.bz2
Group:	   Development/Other
License:   GPL
BuildRoot: %{_tmppath}/%{name}-buildroot

%description
The purpose of this utility is to provide an easy way
to flash kernels and romdisks to the Agenda VR3.

For an overview of the flashing progress, please read
%{_docdir}/agenda-flashing-overview.txt

%prep
%setup -q
%configure

%build
make

%install
rm -rf ${RPM_BUILD_ROOT}
mkdir -p %{buildroot}/{%_bindir,%_docdir}
chmod 644 ${RPM_BUILD_DIR}/%name-%version/doc/*
%makeinstall

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(644,root,root,755)
%doc ChangeLog LICENSE README doc/*
%defattr(-,root,root)
%{_bindir}/%{name}



%changelog
* Wed Sep 09 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.24-8mdv2010.0
+ Revision: 434690
- rebuild

* Sun Aug 03 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.24-7mdv2009.0
+ Revision: 261890
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.24-6mdv2009.0
+ Revision: 255684
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tvignaud@mandriva.com> 0.24-4mdv2008.1
+ Revision: 129224
- kill re-definition of %%buildroot on Pixel's request
- import vrflash


* Thu Jan 05 2005 Lenny Cartier <lenny@mandriva.com> 0.24-4mdk
- rebuild

* Thu Sep 23 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.24-3mdk
- rebuild

* Tue Aug 12 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.24-2mdk
- rebuild

* Mon Jun 30 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.24-1mdk
- from Maxim Heijndijk <cchq@wanadoo.nl> :
	- 0.24
	- rm -rf RPM_BUILD_ROOT in %%install

* Sat Feb 01 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.20-2mdk
- rebuild

* Fri Jul 26 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.20-1mdk
- from Maxim Heijndijk <cchq@wanadoo.nl> :
	- Initial build.
