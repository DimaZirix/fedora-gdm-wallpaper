Name:    gdm-wallpaper
Version: 1
Release: 3
Summary: gdm-wallpaper

Source0: wallpaper-gnome.png
Source1: set-gdm-wallpaper.sh

License: Public Domain

Requires(post): info
Requires(preun): info

Requires: glib2-devel

BuildArch: noarch

%description
Script for GNOME 3.16+ with GNOME Shell themes packed inside /usr/share/gnome-shell/gnome-shell-theme.gresource.

%install
mkdir -p %{buildroot}/usr/share/gnome-shell/wallpaper/
install -p -m 644 %{SOURCE0} %{buildroot}/usr/share/gnome-shell/wallpaper/

mkdir -p %{buildroot}/%{_bindir}
install -p -m 755 %{SOURCE1} %{buildroot}/%{_bindir}

%post
set-gdm-wallpaper.sh /usr/share/gnome-shell/wallpaper/wallpaper-gnome.png

%files
%{_bindir}/set-gdm-wallpaper.sh
/usr/share/gnome-shell/wallpaper/wallpaper-gnome.png

%preun
set-gdm-wallpaper.sh --uninstall

%changelog
