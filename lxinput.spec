Summary:	Configure keyboard and mouse
Name:		lxinput
Version:	0.3.1
Release:	%mkrel 1
License:	GPLv2+
Group:		Graphical desktop/Other
Source0:	http://dfn.dl.sourceforge.net/sourceforge/lxde/%name-%version.tar.gz
# restore broked system changes for GTK3
URL:		http://www.lxde.org
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
BuildRequires:	gtk+2-devel
BuildRequires:	intltool >= 0.40.0
BuildRequires:	docbook-dtd412-xml xsltproc

%description
LXInput is a small program used to configure keyboard and mouse for LXDE.

%prep
%setup -q

%build
%configure2_5x --enable-man
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%{find_lang} %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root)
%{_bindir}/%name
%{_datadir}/applications/*.desktop
%{_datadir}/%name
%{_mandir}/man1/*.1.*


%changelog
* Wed Aug 03 2011 Александр Казанцев <kazancas@mandriva.org> 0.3.1-1mdv2012.0
+ Revision: 692948
- update to 0.3.1

* Sat Aug 07 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.3.0-1mdv2011.0
+ Revision: 567442
- update to 0.3.0
- add --enable-man and add BR docbook-dtd412-xml, xsltproc to build the manpages

* Sat Aug 08 2009 Funda Wang <fwang@mandriva.org> 0.1.1-1mdv2010.0
+ Revision: 411583
- fix file list
- new version 0.1.1

* Fri May 01 2009 Funda Wang <fwang@mandriva.org> 0.1-1mdv2010.0
+ Revision: 369559
- import lxinput


