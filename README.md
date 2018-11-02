# Fedora GDM wallpaper changer
Script for changing wallpaper on login (GNOME Display Manager / GDM) screen.

Tested on:
Fedora 28, Fedora 29, Fedora 29 Silverblue

# Usage
```shell
$ sudo set-gdm-wallpaper /path/to/image.png

Requires: glib2-devel
$ sudo dnf install glib2-devel
```

# Build from source
```shell
$ cd /path/to/source
$ fedpkg --release f29 local
$ fedpkg --release f29 lint

Requires: fedora-packager and fedora-review
$ sudo dnf install fedora-packager fedora-review
$ sudo rpm-ostree install fedora-packager fedora-review
See: https://docs.fedoraproject.org/en-US/quick-docs/creating-rpm-packages/index.html
```

# Install
```shell
$ sudo dnf install set-gdm-wallpaper-1-1.fc29.noarch.rpm
```

OR
```shell
$ sudo rpm-ostree install
```

# Fedora 29 Silverblue
Fedora Silverblue have immutable file system. GDM wallpaper can be changed only by install/reinstall rpm.

