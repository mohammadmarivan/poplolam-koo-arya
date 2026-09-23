import os, re, json, pathlib
root = pathlib.Path(".").resolve()
skip_dirs = {".git", "build", ".gradle", "node_modules", ".idea"}
text_ext = {".xml",".gradle",".kts",".properties",".kt",".java",".md",".txt",".json",".pro",".yml",".yaml",".toml",".html"}
cfg = json.loads(pathlib.Path("rebrand.config.json").read_text(encoding="utf-8"))
old_id = cfg["detected"]["applicationId"] or "com.original.package"
new_id = cfg["identity"]["packageId"]
old_name = cfg["detected"]["appName"] or cfg["source"]["repo"].split("/")[-1]
new_name = cfg["identity"]["appName"]
vname = cfg["identity"]["versionName"]
vcode = str(cfg["identity"]["versionCode"])
def should(p):
    if any(part in skip_dirs for part in p.parts):
        return False
    return p.suffix.lower() in text_ext or p.name in {"gradlew","CMakeLists.txt","AndroidManifest.xml"}
changed = 0
for p in root.rglob('*'):
    if not p.is_file() or not should(p):
        continue
    try:
        text = p.read_text(encoding="utf-8")
    except Exception:
        continue
    orig = text
    if old_id:
        text = text.replace(old_id, new_id)
    text = re.sub(
        r'(<string\s+name=["\']app_name["\']>)(.*?)(</string>)',
        lambda m: m.group(1) + new_name + m.group(3),
        text,
        flags=re.S,
    )
    if p.suffix == '.kts':
        text = re.sub(r'versionName\s*=\s*["\'][^"\']+["\']', 'versionName = "%s"' % vname, text)
        text = re.sub(r'versionCode\s*=\s*\d+', 'versionCode = %s' % vcode, text)
    else:
        text = re.sub(r'versionName\s+["\'][^"\']+["\']', 'versionName "%s"' % vname, text)
        text = re.sub(r'versionCode\s+\d+', 'versionCode %s' % vcode, text)
    if text != orig:
        p.write_text(text, encoding="utf-8")
        changed += 1
        print("  edited", p.relative_to(root))
print("files changed:", changed)
if old_id and old_id != new_id:
    old_parts = old_id.split('.')
    new_parts = new_id.split('.')
    for src_root in root.rglob('src'):
        if not src_root.is_dir():
            continue
        for flavor in src_root.iterdir():
            for lang in ('java', 'kotlin'):
                base = flavor / lang
                old_dir = base.joinpath(*old_parts)
                new_dir = base.joinpath(*new_parts)
                if old_dir.exists() and old_dir.is_dir() and old_dir != new_dir:
                    new_dir.parent.mkdir(parents=True, exist_ok=True)
                    os.renames(old_dir, new_dir)
                    print("  moved", old_dir.relative_to(root), "->", new_dir.relative_to(root))
