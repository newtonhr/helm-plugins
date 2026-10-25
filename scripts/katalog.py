"""Write tests/katalog.json: the Studio topics, Studio tools and all Helm tools a marina-ops-mcp
checkout serves.

Usage: python3 scripts/katalog.py /path/to/marina-ops-mcp
Run it after a Studio change is merged into marina-ops-mcp main, then commit the file.
The plugin tests check every topic and tool a skill names against it.
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "tests" / "katalog.json"
# An MCP tool: `@mcp.tool` (other decorators may follow), then `async def <name>(`.
TOOL = re.compile(r"@mcp\.tool(?:\([^)]*\))?[ \t]*\n(?:[ \t]*@[^\n]+\n)*[ \t]*async def (\w+)\(")


def main(server: Path) -> None:
    znanje = server / "src" / "marina_ops" / "studio" / "znanje"
    teme = sorted(
        m.group(1)
        for f in znanje.glob("*.md")
        if (m := re.search(r"^tema:\s*(\S+)", f.read_text("utf-8"), re.M))
    )
    tools = (server / "src" / "marina_ops" / "tools" / "studio.py").read_text("utf-8")
    alati = sorted(set(re.findall(r"async def (studio_\w+)\(", tools)))
    helm_alati = sorted({
        name
        for f in (server / "src" / "marina_ops" / "tools").rglob("*.py")
        for name in TOOL.findall(f.read_text("utf-8"))
    })
    commit = subprocess.run(["git", "-C", str(server), "rev-parse", "--short", "HEAD"],
                            capture_output=True, text=True, check=True).stdout.strip()
    old = json.loads(OUT.read_text("utf-8")) if OUT.exists() else {}
    data = {"izvor": f"grgur/marina-ops-mcp@{commit}", "teme": teme, "alati": alati,
            "helm_alati": helm_alati,
            "na_cekanju": {k: v for k, v in old.get("na_cekanju", {}).items()
                           if k not in teme}}
    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", "utf-8")
    print(f"{len(teme)} tema, {len(alati)} alata Studija, {len(helm_alati)} alata Helma "
          f"iz {data['izvor']}")


if __name__ == "__main__":
    main(Path(sys.argv[1]))
