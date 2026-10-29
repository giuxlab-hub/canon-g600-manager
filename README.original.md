# Canon G600 Manager for Linux

GTK3 desktop frontend for Canon G600-series network printers using standard CUPS commands and the Canon Remote UI.

Features: CUPS status, printing options, selectable quality test printing, access to official Canon Remote UI maintenance, Canon manual, XSane launcher.

**Limitations:** This application does not reverse engineer Canon maintenance protocols, execute nozzle cleaning commands directly, or read tank levels independently. Maintenance is managed through the printer's own official Remote UI, which may require an administrator password. The network address and queue are editable in the app. Printing is via CUPS.

Build on Debian: `bash build-deb.sh`

License: GNU GPL v3 or later. Not affiliated with Canon Inc.

## Languages
The application supports Italian and English, automatically choosing the desktop language at launch. The language can also be switched directly from the application header without restarting.
