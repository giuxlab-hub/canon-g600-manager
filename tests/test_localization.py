#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
"""Read-only GUI translation and packaging contract checks; no printer is contacted."""
from pathlib import Path
import ast
import os
import stat
from types import SimpleNamespace
import unittest

ROOT = Path(__file__).resolve().parents[1]
APP = ROOT / "canon-g600-manager"
SOURCE = APP.read_text(encoding="utf-8")
TREE = ast.parse(SOURCE, filename=str(APP))


def extract_translation_environment(lang):
    """Execute only the original translation declarations, never the GTK application."""
    bindings = []
    for node in TREE.body:
        if isinstance(node, ast.Assign) and any(
            isinstance(target, ast.Name) and target.id in {"ACTIVE_LANGUAGE", "TRANSLATIONS"}
            for target in node.targets
        ):
            bindings.append(node)
        elif isinstance(node, ast.FunctionDef) and node.name == "tr":
            bindings.append(node)
    assert len(bindings) == 4
    module = ast.fix_missing_locations(ast.Module(body=bindings, type_ignores=[]))
    namespace = {"_locale_os": SimpleNamespace(environ={"LANG": lang})}
    exec(compile(module, str(APP), "exec"), namespace)
    return namespace


class LocalizedGUIContracts(unittest.TestCase):
    def test_executable_header(self):
        self.assertTrue(SOURCE.startswith("#!/usr/bin/python3\n"))
        self.assertIn("# SPDX-License-Identifier: GPL-3.0-or-later", SOURCE[:150])
        self.assertTrue(APP.stat().st_mode & stat.S_IXUSR)

    def test_english_translation(self):
        strings = extract_translation_environment("en_GB.UTF-8")
        self.assertEqual(strings["ACTIVE_LANGUAGE"], "en")
        tr = strings["tr"]
        expected = {
            "Stampante CUPS:": "CUPS printer:",
            "Verifica stato": "Refresh status",
            "Apri Remote UI": "Open Remote UI",
            "Stampa": "Printing",
            "Manutenzione": "Maintenance",
            "La manutenzione avviene nella Remote UI ufficiale Canon.\n": "Maintenance is performed through the official Canon Remote UI.\n",
            "Potrebbe essere richiesta la password amministratore della stampante.\n": "A printer administrator password may be required.\n",
            "Questo programma non invia comandi di pulizia non documentati.": "This application does not send undocumented cleaning commands.",
            "Stampare una pagina di prova?": "Print a test page?",
            "\nFormato: A4, carta normale\nQualità: ": "\nPaper: A4, plain paper\nQuality: ",
            "\nSarà consumato un foglio e dell'inchiostro.": "\nPaper and ink will be consumed.",
            "Invio riuscito:\n": "Job submitted:\n",
            "Errore stampa:\n": "Printing error:\n",
        }
        for original, translated in expected.items():
            with self.subTest(original=original):
                self.assertEqual(tr(original), translated)

    def test_italian_translation(self):
        strings = extract_translation_environment("it_IT.UTF-8")
        self.assertEqual(strings["ACTIVE_LANGUAGE"], "it")
        for original in ["Stampante CUPS:", "La manutenzione avviene nella Remote UI ufficiale Canon.\n", "Errore stampa:\n"]:
            self.assertEqual(strings["tr"](original), original)

    def test_new_GUI_strings_are_translated(self):
        required = [
            "tr('La manutenzione avviene nella Remote UI ufficiale Canon.",
            "tr('Potrebbe essere richiesta la password amministratore della stampante.",
            "tr('Questo programma non invia comandi di pulizia non documentati.",
            "tr('\\nFormato: A4, carta normale\\nQualità: ')",
            "tr('Invio riuscito:",
            "tr('Errore stampa:",
        ]
        for s in required:
            with self.subTest(s=s):
                self.assertIn(s, SOURCE)

    def test_builder_identity(self):
        text = (ROOT / "build-deb.sh").read_text(encoding="utf-8")
        self.assertIn("VERSION=0.2.1", text)
        self.assertIn("Version: 0.2.1", text)
        self.assertIn("./canon-g600-manager_0.2.1_all.deb", text)
        self.assertNotIn("/home/giu/", text)


if __name__ == "__main__":
    unittest.main()
