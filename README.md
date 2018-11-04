# GDM Login screen background changer
Script for GNOME 3.16+ with GNOME Shell themes packed inside /usr/share/gnome-shell/gnome-shell-theme.gresource.

This script allows change background on login screen.

# Tested on:
Fedora 28, Fedora 29, Fedora 29 Silverblue
But should work with any distro with /usr/share/gnome-shell/gnome-shell-theme.gresource file.

# Usage
```shell
$ sudo set-gdm-wallpaper.sh /path/to/image.png

Requires gresource binary (glib2 or glib2-devel library):
Fedora: 
# dnf install glib2-devel
```
Fedora Silverblue
```shell
Fedora Silverblue have immutable file system. GDM wallpaper can be changed only by install/reinstall rpm.

$ sudo rpm-ostree install set-gdm-wallpaper-1-2.noarch.rpm

This will change GDM wallpaper to wallpaper-gnome.png inside .rpm file.
If you want change this image, you need to Build new .rpm file.
```

# Install
For fedora 28+
```shell
$ wget https://github.com/DimaZirix/fedora-gdm-wallpaper/releases/download/1.2/set-gdm-wallpaper-1-2.noarch.rpm
$ sudo dnf install set-gdm-wallpaper-1-2.noarch.rpm
```

OR
```shell
$ wget https://github.com/DimaZirix/fedora-gdm-wallpaper/releases/download/1.2/set-gdm-wallpaper-1-2.noarch.rpm
$ sudo rpm-ostree install set-gdm-wallpaper-1-2.noarch.rpm
```
# Recovering

If GDM load failed, then press ALT+F6 and:

```shell
# set-gdm-wallpaper --uninstall
OR
# cp /usr/share/gnome-shell/gnome-shell-theme.gresource.backup /usr/share/gnome-shell/gnome-shell-theme.gresource

OR delete RPM:
# dnf remove set-gdm-wallpaper
OR 
# rpm-ostree uninstall set-gdm-wallpaper
```

# Build RPM from source
```shell
$ cd /path/to/source
$ fedpkg --release f29 local
$ fedpkg --release f29 lint

Requires: fedora-packager and fedora-review
$ sudo dnf install fedora-packager fedora-review
OR
$ sudo rpm-ostree install fedora-packager fedora-review
See: https://docs.fedoraproject.org/en-US/quick-docs/creating-rpm-packages/index.html
```

# Credit and Licences
wallpaper-gnome.png: https://www.opendesktop.org/s/Gnome/p/1071929/
