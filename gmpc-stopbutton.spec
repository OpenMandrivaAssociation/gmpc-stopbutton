Summary:	A stop button plugin for gmpc
Name:		gmpc-stopbutton
Version:	0.15.5.0
Release:	%mkrel 5
License:	GPLv2+
Group:		Sound
Url:		http://www.sarine.nl//gmpc-plugins-stopbutton
Source0:	http://download.sarine.nl/download/gmpc-0.15.5/%{name}-%{version}.tar.bz2
BuildRequires:	libmpd-devel
BuildRequires:	libxml2-devel
BuildRequires:	libglade2.0-devel
BuildRequires:	gmpc-devel
Requires:	gmpc

%description
This is the simplest plugin of the lot, it adds a stop 
button to the controls in the main window. It's an easy 
solution to keep everybody happy.

%prep
%setup -q

%build
%configure2_5x

%make

%install
%makeinstall_std

%files
%defattr(-,root,root)
%{_datadir}/gmpc/plugins/libstopbutton.so


%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.15.5.0-5mdv2011.0
+ Revision: 618978
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.15.5.0-4mdv2010.0
+ Revision: 429222
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.15.5.0-3mdv2009.0
+ Revision: 246327
- rebuild

* Wed Jan 30 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.15.5.0-1mdv2008.1
+ Revision: 160452
- add spec file
- add source
- Created package structure for gmpc-stopbutton.

