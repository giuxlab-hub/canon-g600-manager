# Canon G600 Manager for Linux

**GTK3 desktop frontend for Canon G600-series network printers, built around the standard Linux CUPS tools and Canon's official Remote UI.**

**Version:** 0.2.1 (Italian/English localization and desktop-launch fix) · **Package:** `canon-g600-manager_0.2.1_all.deb` · **License:** GPL-3.0-or-later · **Operating system:** Linux (Debian-family package)

[Download the Debian package](https://github.com/giuxlab-hub/canon-g600-manager/releases/tag/v0.2.1) · [Giux-Lab](https://giux-lab.it/) · [Original source README](README.original.md)

This is an **independent community utility developed by Giux-Lab**. It is not official Canon software, is not affiliated with or endorsed by Canon Inc., and does not implement undocumented maintenance protocols.

## Features

- View CUPS printer state, queue connection details, current jobs and effective `lpoptions`.
- Set or change the CUPS queue name and the printer's IP address/hostname directly in the interface.
- Inspect available CUPS printer options.
- Choose a quality setting (Draft, Normal or High) for an **optional A4 text diagnostic print**, with a confirmation dialog before submission.
- Open the printer's official **Canon Remote UI** in the browser for maintenance operations.
- Open the official Canon G600-series online manual and the optional XSane scanner application.
- Check whether the configured printer's web interface responds.

**Important limitations:** Print quality is passed as a CUPS job option; its effect depends on the installed driver/PPD and may require driver-specific values. This program does not itself clean print heads, query ink-tank levels independently, implement native scanning drivers or change printer firmware. Maintenance remains in the Canon web interface and may require a printer administrator password.

## Install on Debian

Download `canon-g600-manager_0.2.1_all.deb` from [GitHub Releases](https://github.com/giuxlab-hub/canon-g600-manager/releases/tag/v0.2.1), then run:

```bash
sudo apt install ./canon-g600-manager_0.2.1_all.deb
```

The Debian package declares these dependencies: `python3`, `python3-gi`, `gir1.2-gtk-3.0`, `cups-client`, `xdg-utils`. It recommends `xsane` for the optional scanner launcher. A configured CUPS printer queue is required for printing.

Open **Canon G600 Manager** from the desktop's applications menu, or run:

```bash
canon-g600-manager
```

The program initially proposes the original author's CUPS queue `Canon_G600_series` and local device address `192.168.1.107`. **Change both entries to your own printer details**; the supplied values are examples from the original development setup, not automatic printer discovery.

A working graphical GTK3 session is required. The printer must be reachable through the configured local network, and CUPS must be configured with a compatible printer/driver.

## Build from source

The expanded, readable source is included directly in this repository:

```bash
git clone https://github.com/giuxlab-hub/canon-g600-manager.git
cd canon-g600-manager
./build-deb.sh
```

The build script requires `dpkg-deb` and produces `./canon-g600-manager_0.2.1_all.deb`. It stages the Python executable, a `.desktop` launcher, SVG icon and README. It does **not** install the package or print a page.

Version 0.2.1 is a corrective distribution of the author's bilingual v0.2.0 source. The corrected source tarball and the new Debian package are available on the v0.2.1 release; both preserve the program's interface and workflows. The original v0.2.0 Debian package and source archive remain separately available as historical assets. See [source provenance](SOURCE_PROVENANCE.md).

## License and attribution

The program declares **GNU General Public License v3 or later** (`GPL-3.0-or-later`). See [LICENSE](LICENSE).

Canon and related printer/model names are used solely to identify compatibility. They are trademarks of their respective owners. **Not affiliated with Canon Inc.**

---

## Italiano

**Canon G600 Manager** è un'utilità indipendente Giux-Lab per Linux, sviluppata in **Python 3 e GTK3**, che utilizza i comandi CUPS e l'interfaccia web ufficiale delle stampanti Canon serie G600.

La versione pubblicata è **0.2.1**, disponibile come pacchetto Debian installabile e come codice sorgente completo.

### Funzionalità

- Consulta stato della coda CUPS, connessione, lavori e opzioni di stampa.
- Permette di modificare nome della coda e indirizzo IP/hostname della stampante.
- Elenca le opzioni CUPS e permette una stampa diagnostica A4, soltanto dopo conferma.
- Apre nel browser l'interfaccia **Canon Remote UI** per le operazioni di manutenzione.
- Apre il manuale Canon e avvia XSane se installato.
- Non esegue autonomamente pulizie delle testine né accede a comandi di manutenzione non documentati.

### Installazione e utilizzo

Scaricare il file `canon-g600-manager_0.2.1_all.deb` dalla [release v0.2.1](https://github.com/giuxlab-hub/canon-g600-manager/releases/tag/v0.2.1), quindi installarlo:

```bash
sudo apt install ./canon-g600-manager_0.2.1_all.deb
```

Avviare l'applicazione dal menu oppure con `canon-g600-manager`. **Adattare la coda CUPS e l'indirizzo della stampante** ai valori della propria rete. La qualità di stampa effettiva dipende dal driver CUPS installato.

Per ricompilare il pacchetto Debian dal repository, eseguire `./build-deb.sh`: l'archivio viene generato nella directory corrente. La sorgente Python, lo script di compilazione, gli asset e i test sono inclusi nel repository e nel tarball della release v0.2.1; gli archivi originali della v0.2.0 restano conservati separatamente.

**Licenza:** GNU GPL-3.0-or-later. Il progetto non è un software ufficiale Canon e non è affiliato a Canon Inc.

[Sito Giux-Lab](https://giux-lab.it/) · [Note di provenienza](SOURCE_PROVENANCE.md)

## Italian and English GUI localization (v0.2.0)

Version 0.2.0 adds automatic language selection based on the desktop locale and a language selector in the application header. The original Debian package has a missing interpreter shebang, so direct launch from a desktop menu may fail. The corrected release is v0.2.1.

### Language selection / Scelta lingua

The application chooses Italian for a desktop locale starting with `it` and English otherwise. The header selector can switch between **Italiano** and **English** during use, retaining the current printer queue, host and print-quality selection. Maintenance and printing confirmation messages are localized in v0.2.1.

L’interfaccia seleziona italiano per i sistemi con locale `it*`, inglese negli altri casi. Il selettore nell’intestazione cambia lingua mantenendo coda, indirizzo stampante e qualità di stampa scelta. La v0.2.1 traduce anche le informazioni di manutenzione e i messaggi di conferma della stampa.
