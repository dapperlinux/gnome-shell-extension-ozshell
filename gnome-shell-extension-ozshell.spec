Name:       gnome-shell-extension-ozshell
Version:    3.22
Release:    1
Summary:    Gnome shell extension to interface the oz sandboxing framework
URL:        https://github.com/subgraph/gnome-shell-extension-ozshell
License:    GPLv3
BuildArch:  noarch
BuildRequires:   glib2-devel
BuildRequires:   gnome-common
BuildRequires:   intltool
BuildRequires:   pkgconfig
Source0:    %{name}-%{version}.tar.gz

%description
This is a Gnome Shell extension for interfacing with the OZ application sandboxing framework.

It allows viewing the running sandboxes, adding and removing user files into the sandboxes, terminating them, and opening a shell terminal inside the sandbox.

%prep
%autosetup

%build
./autogen.sh
./configure --prefix=/usr
make

%install
%make_install
mv $RPM_BUILD_ROOT/usr/@DATADIRNAME@/locale $RPM_BUILD_ROOT/usr/share/
rmdir $RPM_BUILD_ROOT/usr/@DATADIRNAME@

%post


%files
/usr/share/gnome-shell/extensions/ozshell@subgraph.com/*
/usr/share/locale/*

%changelog
* Wed Dec 14 2016 Matthew Ruffell <msr50@uclive.ac.nz>
- Initial packaging
