import yaml
from pathlib import Path
from itertools import groupby

config_path = Path("dinghy.yaml")
output_path = Path("build")

header = """
<!DOCTYPE html>
<html>
<head>
    <title>CTA-Observatory dinghy digests</title>
     <link rel="icon" href="https://raw.githubusercontent.com/primer/octicons/main/icons/code-24.svg" type="image/svg+xml">
    <style>
        body {
            font-family: "Fira Sans", sans-serif;
            max-width: 60em;
            margin: auto;
            line-height: 1.3;
        }
    </style>
</head>
<body>
<h1>CTA-Observatory Github Auto Digests</h1>
<p>Powered by <a href="https://github.com/nedbat/dinghy">dinghy</a>

"""
footer = """
</body>
</html>
"""

with config_path.open("r") as f:
    config = yaml.safe_load(f)

output_path.mkdir(exist_ok=True)

lines = []

for section, digests in groupby(config['digests'], key=lambda d: d['section']):
    lines.append(f"<h2>{section}</h2>")
    lines.append("<ul>")
    for digest in digests:
        path = Path(digest["digest"]).relative_to(output_path)
        title = digest["title"]
        lines.append(f'    <li><a href="{path}">{title}</a></li>')
    lines.append("</ul>")

lines = "\n".join(lines)

with (output_path / "index.html").open("w") as f:
    f.write(header)
    f.write(lines)
    f.write(footer)
