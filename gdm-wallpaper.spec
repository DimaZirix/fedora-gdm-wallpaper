Name:    gdm-wallpaper
Version: 1
Release: 4
Summary: gdm-wallpaper

Source0: set-gdm-wallpaper.sh

License: Public Domain

Requires(post): info
Requires(preun): info

Requires: glib2-devel

BuildArch: noarch

%description
Script for GNOME 3.16+ with GNOME Shell themes packed inside /usr/share/gnome-shell/gnome-shell-theme.gresource.

%install
mkdir -p %{buildroot}/%{_bindir}
install -p -m 755 %{SOURCE0} %{buildroot}/%{_bindir}

%post
if [ -f "/usr/bin/set-gdm-wallpaper" ]; then
 unlink /usr/bin/set-gdm-wallpaper
fi
cp -s /usr/bin/set-gdm-wallpaper.sh /usr/bin/set-gdm-wallpaper

%preun
if [ -f "/usr/bin/set-gdm-wallpaper" ]; then
 unlink /usr/bin/set-gdm-wallpaper
fi

%files
%{_bindir}/set-gdm-wallpaper.sh

%changelog
