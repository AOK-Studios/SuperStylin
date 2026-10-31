import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HTML = (ROOT / "index.html").read_text()


def test_no_external_resources():
    # Total isolation: the demo must not call out to anything.
    assert "http://" not in HTML
    assert "https://" not in HTML
    assert "<script src" not in HTML
    assert "<link" not in HTML
    assert "url(" not in HTML


def test_demo_data_is_synthetic():
    assert "DEMO_ITEMS" in HTML
    assert "DEMO - SAMPLE WARDROBE" in HTML
    count = len(re.findall(r'id:"d\d+"', HTML))
    assert count >= 10


def test_core_features_present():
    for needle in ["buildOutfit", "renderTrends", "addForm", "localStorage",
                   "Style me", "casual", "work", "night", "event"]:
        assert needle in HTML, needle


def test_photo_guidance_copy():
    assert "laid out on the floor or bed" in HTML
    assert "Not pictures of an open closet" in (ROOT / "README.md").read_text()


def test_script_parses():
    script = re.search(r"<script>(.*)</script>", HTML, re.S).group(1)
    tmp = Path("/tmp/superstylin_check.js")
    tmp.write_text(script)
    proc = subprocess.run(["node", "--check", str(tmp)], capture_output=True, text=True)
    assert proc.returncode == 0, proc.stderr


if __name__ == "__main__":
    sys.exit(0)
