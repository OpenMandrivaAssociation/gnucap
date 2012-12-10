%define name    gnucap
%define version 20060830
%define release %mkrel 6

%define filever 2006-08-30

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        A general purpose circuit simulator
Source0:        %{name}-%{filever}.tar.bz2
Patch:          gnucap-2006-08-30-fix-build.patch
License:        GPL
Group:          Development/Other
Url:            http://www.geda.seul.org/tools/gnucap/index.html
BuildRequires:	readline-devel
BuildRequires:	termcap-devel
BuildRequires:	tetex-latex
BuildRequires:	tetex-dvipdfm
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
GNUCAP is a general purpose circuit simulator. It performs nonlinear dc and 
transient analyses, Fourier analysis, and ac analysis linearized at an 
operating point. It is fully interactive and command driven. It can also be 
run in batch mode or as a server. The output is produced as it simulates. 
Spice compatible models for the MOSFET (level 1,2,3) and diode are included 
in this release. 

%prep
%setup -q -n %{name}-%{filever}
%patch -p 1

%build
./configure --prefix=%{buildroot}/%{_prefix}  
%make
make install

%install
rm -rf %{buildroot}
make install
mkdir -p %{buildroot}/%{_mandir}/man1/
cp doc/gnucap.1 %{buildroot}/%{_mandir}/man1/
pushd man
make pdf
popd

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc doc/COPYING man/gnucap-man.pdf
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/%name



%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 20060830-6mdv2011.0
+ Revision: 619207
- the mass rebuild of 2010.0 packages

* Thu May 21 2009 Guillaume Rousse <guillomovitch@mandriva.org> 20060830-5mdv2010.0
+ Revision: 378342
- fix build

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 20060830-1mdv2008.1
+ Revision: 126081
- kill re-definition of %%buildroot on Pixel's request
- import gnucap


* Thu Aug 31 2006 Couriousous <couriousous@mandriva.org> 20060830-1mdv2007.0
- 20060830 version from geda

* Sat Apr 15 2006 Couriousous <couriousous@mandriva.org> 20060117-1mdk
- 20060117 version from geda

* Fri Mar 17 2006 Couriousous <couriousous@mandriva.org> 0.34-3mdk
- Fix buildrequires

* Fri Mar 17 2006 Couriousous <couriousous@mandriva.org> 0.34-2mdk
- Rebuild

* Sun Feb 06 2005 Couriousous <couriousous@mandrake.org> 0.34-1mdk
- First Mandrakelinux release

