#!/bin/sh
set -eu
cd "$(dirname "$0")"
VERSION=0.2.1
STAGE="$(mktemp -d)"
trap 'rm -rf "$STAGE"' EXIT
mkdir -p "$STAGE/DEBIAN" "$STAGE/usr/bin" "$STAGE/usr/share/applications" "$STAGE/usr/share/icons/hicolor/scalable/apps" "$STAGE/usr/share/doc/canon-g600-manager"
install -m 755 canon-g600-manager "$STAGE/usr/bin/canon-g600-manager"
cat > "$STAGE/DEBIAN/control" <<'CONTROL'
Package: canon-g600-manager
Version: 0.2.1
Section: utils
Priority: optional
Architecture: all
Maintainer: GiuxLab <noreply@giux-lab.it>
Depends: python3, python3-gi, gir1.2-gtk-3.0, cups-client, xdg-utils
Recommends: xsane
Description: Canon G600 series print and maintenance frontend
 GTK3 interface for CUPS printing and official Canon Remote UI.
 Includes printer diagnostics, print quality selection, and access
 to maintenance through Canon's own web interface.
CONTROL
cat > "$STAGE/usr/share/applications/canon-g600-manager.desktop" <<'DESKTOP'
[Desktop Entry]
Type=Application
Name=Canon G600 Manager
Name[it]=Gestione Canon G600
Comment=Manage Canon G600 printing and access official maintenance
Comment[it]=Gestisci stampa Canon G600 e manutenzione ufficiale
Exec=canon-g600-manager
Icon=canon-g600-manager
Terminal=false
Categories=System;GTK;
Keywords=Canon;CUPS;Printer;Maintenance;Stampante;
StartupNotify=true
DESKTOP
cat > "$STAGE/usr/share/icons/hicolor/scalable/apps/canon-g600-manager.svg" <<'SVG'
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="12" fill="#263b50"/><rect x="10" y="21" width="44" height="29" rx="5" fill="#e6ebef"/><rect x="17" y="9" width="30" height="23" rx="2" fill="#fff"/><path d="M22 15h20M22 20h20M22 25h13" stroke="#566b7b" stroke-width="2"/><rect x="17" y="39" width="30" height="16" rx="2" fill="#fff"/><rect x="22" y="44" width="6" height="7" fill="#28c6dd"/><rect x="29" y="44" width="6" height="7" fill="#d840a8"/><rect x="36" y="44" width="6" height="7" fill="#f4c542"/><circle cx="47" cy="28" r="2" fill="#48ba6a"/></svg>
SVG
install -m 644 README.md "$STAGE/usr/share/doc/canon-g600-manager/README.md"
find "$STAGE" -type d -exec chmod 755 {} +
dpkg-deb --build --root-owner-group "$STAGE" "./canon-g600-manager_0.2.1_all.deb"
