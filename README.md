# GDM Login screen background changer
Script for GNOME 3.16+ with GNOME Shell themes packed inside /usr/share/gnome-shell/gnome-shell-theme.gresource.

This script allows change background on login screen.

# Tested on:
Fedora 28, 29, 30, 31 and Fedora Silverblue

But should work on any distro with /usr/share/gnome-shell/gnome-shell-theme.gresource file.

# Usage
```shell
set-gdm-wallpaper.sh /path/to/image.png
# (use --resize N option for fixing multiple monitor issues)

# Script requires gresource binary (glib2 or glib2-devel library):
# Fedora: 
dnf install glib2-devel
```
Fedora Silverblue
```shell
Fedora Silverblue have immutable file system. GDM wallpaper can be changed only by install/reinstall rpm.

# rpm-ostree install set-gdm-wallpaper-1-2.noarch.rpm

This will change GDM wallpaper to wallpaper-gnome.png inside .rpm file.
If you want change this image, you need to Build new .rpm file.
```

# Install
```
$ dnf copr enable zirix/gdm-wallpaper 
$ dnf install gdm-wallpaper
$ set-gdm-wallpaper /path/to/image.png
```

OR

```shell
# dnf install set-gdm-wallpaper-1-2.noarch.rpm
```

Fedora Silverblue
```shell
# rpm-ostree install set-gdm-wallpaper-1-2.noarch.rpm
```
# Recovering

If GDM load failed, then press ALT+F6 and:

```shell
# set-gdm-wallpaper.sh --uninstall
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
# dnf install fedora-packager fedora-review
OR
# rpm-ostree install fedora-packager fedora-review
See: https://docs.fedoraproject.org/en-US/quick-docs/creating-rpm-packages/index.html
```

# Credit and Licences
wallpaper-gnome.png: https://www.opendesktop.org/s/Gnome/p/1071929/
