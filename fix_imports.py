from pathlib import Path

root = Path('utilities')
for path in sorted(root.rglob('*.py')):
    if path.name == '__init__.py':
        continue
    text = path.read_text(encoding='utf-8')
    original = text

    text = text.replace(
        'import sys\nfrom pathlib import Path\n\nsys.path.insert(0, str(Path(__file__).resolve().parents[2] / "python" / "lib"))\n\n',
        ''
    )

    text = text.replace('from avocet.widgets import Window, Label, Widget\n', 'from avocet_bootstrap import Label, Widget, Window\n')
    text = text.replace('from avocet.widgets import Window, Label\n', 'from avocet_bootstrap import Label, Window\n')

    if 'import avocet_core' in text and 'import avocet_bootstrap' not in text:
        text = text.replace('import avocet_core\n', 'import avocet_bootstrap\nfrom avocet_bootstrap import avocet_core\n', 1)

    if 'from avocet_bootstrap import avocet_bootstrap\n' in text:
        text = text.replace('from avocet_bootstrap import avocet_bootstrap\n', '')

    if text != original:
        path.write_text(text, encoding='utf-8')
