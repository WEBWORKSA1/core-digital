"""Reads the curated video list from assets/js/config.js (single source of truth)."""
import re, os
_src = open(os.path.join(os.path.dirname(__file__), "..", "assets", "js", "config.js"), encoding="utf-8").read()
VIDEOS = [dict(id=m[0], title=m[1], by=m[2], cat=m[3]) for m in
          re.findall(r'\{ id: "([^"]+)", title: "([^"]+)", by: "([^"]+)", cat: "([^"]+)" \}', _src)]
