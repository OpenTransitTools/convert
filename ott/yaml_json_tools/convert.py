import yaml
import json

from pathlib import Path
conf = yaml.safe_load(Path('data/trip-form/fr.yml').read_text())
out=json.dumps(conf, indent=2, ensure_ascii=False)
print(out)
