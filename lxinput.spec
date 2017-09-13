Summary:	Configure keyboard and mouse
Name:		lxinput
Version:	0.3.5
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Other
Url:		https://lxde.org/
Source0:	https://downloads.sourceforge.net/lxde/%{name}-%{version}.tar.xz

BuildRequires:	docbook-dtd412-xml
BuildRequires:	intltool
BuildRequires:	pkgconfig(gtk+-x11-2.0)
BuildRequires:	xsltproc

%description
Lightweight X11 Desktop Environment project (a.k.a LXDE) aimed to provide a
new desktop environment which is useful enough and keep resource usage lower
at the same time. Useabiliy, speed, and memory usage are our main concern.

Unlike other tightly integrated desktops LXDE strives to be modular, so each
component can be used independently with few dependencies. This makes
porting LXDE to different distributions and platforms easier.

LXInput is a small program used to configure keyboard and mouse for LXDE.

%files -f %{name}.lang
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.1*

#---------------------------------------------------------------------------

%prep
%setup -q
%apply_patches

%build
%configure
%make

%install
%makeinstall_std

# locales
%find_lang %{name}

