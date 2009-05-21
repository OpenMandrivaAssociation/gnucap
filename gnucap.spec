%define name    gnucap
%define version 20060830
%define release %mkrel 5

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

