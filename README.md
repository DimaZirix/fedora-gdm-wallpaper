# Fedora GDM Login screen background changer
Script for changing wallpaper on login (GNOME Display Manager / GDM) screen.

Tested on:
Fedora 28, Fedora 29, Fedora 29 Silverblue

# Install
```shell
$ wget https://github.com/DimaZirix/fedora-gdm-wallpaper/releases/download/set-gdm-wallpaper-1-1.fc29/set-gdm-wallpaper-1-1.fc29.noarch.rpm
$ sudo dnf install set-gdm-wallpaper-1-1.fc29.noarch.rpm
```

OR
```shell
$ wget https://github.com/DimaZirix/fedora-gdm-wallpaper/releases/download/set-gdm-wallpaper-1-1.fc29/set-gdm-wallpaper-1-1.fc29.noarch.rpm
$ sudo rpm-ostree install set-gdm-wallpaper-1-1.fc29.noarch.rpm
```

# Usage
Fedora 28+:
```shell
$ sudo set-gdm-wallpaper /path/to/image.png

Requires: glib2-devel
$ sudo dnf install glib2-devel
```
Fedora Silverblue
```shell
Fedora Silverblue have immutable file system. GDM wallpaper can be changed only by install/reinstall rpm.

$ sudo rpm-ostree install set-gdm-wallpaper-1-1.fc29.noarch.rpm

This will change GDM wallpaper to wallpaper-gnome.png inside .rpm file.
If you want change this image, you need to Build new .rpm file.
```

# Recovering

If GDM load failed, then press ALT+F6 and:

```shell
# dnf remove set-gdm-wallpaper
OR 
# rpm-ostree uninstall set-gdm-wallpaper
OR
# cp /usr/share/gnome-shell/gnome-shell-theme.gresource.backup /usr/share/gnome-shell/gnome-shell-theme.gresource
```

# Build from source
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
