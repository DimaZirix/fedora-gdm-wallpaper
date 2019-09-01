Name:    gdm-wallpaper
Version: 1
Release: 2
Summary: gdm-wallpaper

Source0: wallpaper-gnome.png
Source1: set-gdm-wallpaper.sh

License: Public Domain

Requires(post): info
Requires(preun): info

Requires: glib2-devel

BuildArch: noarch

%description
gdm-wallpaper

%install
mkdir -p %{buildroot}/usr/share/gnome-shell/wallpaper/
install -p -m 644 %{SOURCE0} %{buildroot}/usr/share/gnome-shell/wallpaper/

mkdir -p %{buildroot}/%{_bindir}
install -p -m 755 %{SOURCE1} %{buildroot}/%{_bindir}

%post
set-gdm-wallpaper.sh --rpm

%files
%{_bindir}/set-gdm-wallpaper.sh
/usr/share/gnome-shell/wallpaper/wallpaper-gnome.png

%preun 
set-gdm-wallpaper.sh --uninstall

%changelog
