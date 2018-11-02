Name:    set-gdm-wallpaper
Version: 1
Release: 1%{?dist}
Summary: set-gdm-wallpaper

Source0: wallpaper-gnome.png
Source1: set-gdm-wallpaper

License: Public Domain

Requires(post): info
Requires(postun): info

Requires: glib2-devel

BuildArch: noarch

%description
set-gdm-wallpaper

%install
mkdir -p %{buildroot}/usr/share/gnome-shell/wallpaper/
install -p -m 755 %{SOURCE0} %{buildroot}/usr/share/gnome-shell/wallpaper/

mkdir -p %{buildroot}/%{_bindir}
install -p -m 755 %{SOURCE1} %{buildroot}/%{_bindir}

%post
set-gdm-wallpaper

%files
%{_bindir}/set-gdm-wallpaper
/usr/share/gnome-shell/wallpaper/wallpaper-gnome.png

%postun
if [ $1 -gt 0 ] ; then
  cp -f /usr/share/gnome-shell/gnome-shell-theme.gresource.backup /usr/share/gnome-shell/gnome-shell-theme.gresource
fi


%changelog
