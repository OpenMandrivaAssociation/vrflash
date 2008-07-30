%define name	vrflash
%define version	0.24
%define release	%mkrel 6

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

