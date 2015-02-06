%define filever 2006-08-30

Summary:	A general purpose circuit simulator
Name:		gnucap
Version:	20060830
Release:	8
License:	GPLv2+
Group:		Development/Other
Url:		http://www.geda.seul.org/tools/gnucap/index.html
Source0:	%{name}-%{filever}.tar.bz2
Source10:	%{name}.rpmlintrc
Patch0:		gnucap-2006-08-30-fix-build.patch
BuildRequires:	readline-devel
BuildRequires:	ncurses-devel

%description
GNUCAP is a general purpose circuit simulator. It performs nonlinear dc and
transient analyses, Fourier analysis, and ac analysis linearized at an
operating point. It is fully interactive and command driven. It can also be
run in batch mode or as a server. The output is produced as it simulates.
Spice compatible models for the MOSFET (level 1,2,3) and diode are included
in this release.

%files
%doc COPYING
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/%{name}

#----------------------------------------------------------------------------

%prep
%setup -q -n %{name}-%{filever}
%patch0 -p1

%build
%configure2_5x
%make

%install
%makeinstall_std

mkdir -p %{buildroot}/%{_mandir}/man1/
cp doc/gnucap.1 %{buildroot}/%{_mandir}/man1/

