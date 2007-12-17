%define name    gnucap
%define version 20060830
%define release %mkrel 1

%define filever 2006-08-30

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        A general purpose circuit simulator
Source0:        %{name}-%{filever}.tar.bz2
License:        GPL
Group:          Development/Other
Url:            http://www.geda.seul.org/tools/gnucap/index.html
BuildRequires:	readline-devel termcap-devel tetex-latex tetex-dvipdfm

%description
GNUCAP is a general purpose circuit simulator. It performs nonlinear dc and 
transient analyses, Fourier analysis, and ac analysis linearized at an 
operating point. It is fully interactive and command driven. It can also be 
run in batch mode or as a server. The output is produced as it simulates. 
Spice compatible models for the MOSFET (level 1,2,3) and diode are included 
in this release. 

%prep
%setup -q -n %{name}-%{filever}
%build

./configure --prefix=$RPM_BUILD_ROOT/%{_prefix}  
%make
make install

%install
rm -rf $RPM_BUILD_ROOT
make install
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man1/
cp doc/gnucap.1 $RPM_BUILD_ROOT/%{_mandir}/man1/
pushd man
make pdf
popd



%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc doc/COPYING man/gnucap-man.pdf
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/%name

