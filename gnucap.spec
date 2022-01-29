%define filever 2006-08-30
%define _disable_rebuild_configure 1

Summary:	A general purpose circuit simulator
Name:		gnucap
Version:	20210107
Release:	1
License:	GPLv2+
Group:		Development/Other
Url:		http://www.gnucap.org
Source0:  https://git.savannah.gnu.org/cgit/gnucap.git/snapshot/gnucap-%{version}.tar.gz
#Source0:	http://www.gnucap.org/devel/%{name}-%{filever}.tar.bz2
Patch0:   gnucap-fix-install-dirs-openmandriva.patch

BuildRequires:	readline-devel
BuildRequires:	ncurses-devel
BuildRequires: termcap-devel

%description
GNUCAP is a general purpose circuit simulator. It performs nonlinear dc and
transient analyses, Fourier analysis, and ac analysis linearized at an
operating point. It is fully interactive and command driven. It can also be
run in batch mode or as a server. The output is produced as it simulates.
Spice compatible models for the MOSFET (level 1,2,3) and diode are included
in this release.

%files
%doc COPYING
%{_bindir}/gnucap*
%{_prefix}/lib/gnucap/gnucap-default-plugins.so
%{_prefix}/lib/libgnucap.so
%{_includedir}/gnucap/*
%{_sysconfdir}/gnucap.conf

#----------------------------------------------------------------------------

%prep
%setup -q -n %{name}-%{version}
%autopatch -p1

%build
#export CC=gcc
#export CXX=g++
%configure
%make_build

%install
%make_install

