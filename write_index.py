import yaml
from pathlib import Path

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

<ul>
"""
footer = """
</ul>
</body>
</html>
"""

with config_path.open("r") as f:
    config = yaml.safe_load(f)

output_path.mkdir(exist_ok=True)

digests = []

for digest in config["digests"]:
    path = Path(digest["digest"]).relative_to(output_path)
    title = digest["title"]
    digests.append(f'    <li><a href="/{path}">{title}</a></li>')

digests = "\n".join(digests)

with (output_path / "index.html").open("w") as f:
    f.write(header)
    f.write(digests)
    f.write(footer)
