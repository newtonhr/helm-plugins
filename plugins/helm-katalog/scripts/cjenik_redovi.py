#!/usr/bin/env python3
"""Read a supplier price list (CSV or XLSX) into one JSON row per article.

Usage: python3 cjenik_redovi.py <file> [--sheet NAME]

Output (stdout, JSON): {"rows": [{"sifra", "naziv", "cijena", "ean", "lalizas", "popust",
"red"}], "preskoceno": [{"red", "razlog"}], "stupci": {field: column header}}.
Column headers are matched loosely (Croatian and English names). XLSX needs openpyxl;
without it, save the sheet as CSV.
"""
import csv
import json
import re
import sys
from decimal import Decimal, InvalidOperation
from pathlib import Path

ALIASES = {
    "sifra": ["šifra", "sifra", "šifra artikla", "pos", "code", "item code", "article", "kod"],
    "naziv": ["naziv", "opis", "name", "description", "artikl"],
    "cijena": ["cijena", "mpc", "vpc", "price", "retail price", "neto"],
    "ean": ["ean", "barcode", "bar code", "ean13"],
    "lalizas": ["lalizas", "lalizas code", "lalizas šifra", "ref", "part no", "part number"],
    "popust": ["popust", "rabat", "discount", "%"],
}


def _norm(s: object) -> str:
    return re.sub(r"\s+", " ", str(s or "")).strip().lower()


def _map_columns(header: list[str]) -> dict[str, int]:
    found: dict[str, int] = {}
    for i, h in enumerate(header):
        hn = _norm(h)
        for field, names in ALIASES.items():
            if field not in found and any(hn == n or hn.startswith(n) for n in names):
                found[field] = i
    return found


def _price(v: object) -> str | None:
    s = re.sub(r"[^\d,.\-]", "", str(v or ""))
    if not s:
        return None
    if "," in s and "." in s:  # 1.234,56 or 1,234.56
        decimal_comma = s.rfind(",") > s.rfind(".")
        s = s.replace(".", "").replace(",", ".") if decimal_comma else s.replace(",", "")
    else:
        s = s.replace(",", ".")
    try:
        return str(Decimal(s).quantize(Decimal("0.01")))
    except InvalidOperation:
        return None


def _rows(path: Path, sheet: str | None) -> list[list[object]]:
    if path.suffix.lower() in (".xlsx", ".xlsm"):
        import openpyxl  # noqa: PLC0415 - optional dependency
        wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
        ws = wb[sheet] if sheet else wb.active
        return [list(r) for r in ws.iter_rows(values_only=True)]
    text = path.read_text(encoding="utf-8-sig", errors="replace")
    dialect = csv.Sniffer().sniff(text[:4096], delimiters=",;\t")
    return [list(r) for r in csv.reader(text.splitlines(), dialect)]


def main() -> None:
    args = sys.argv[1:]
    if not args:
        sys.exit(__doc__)
    sheet = args[args.index("--sheet") + 1] if "--sheet" in args else None
    raw = _rows(Path(args[0]), sheet)
    # header = first of the first 10 rows that names a code column
    hi, cols = next(((i, c) for i, r in enumerate(raw[:10])
                     if "sifra" in (c := _map_columns([str(x or "") for x in r]))), (None, {}))
    if hi is None:
        sys.exit("Nisam našao stupac sa šifrom (šifra / code / POS) u prvih 10 redova.")
    out, skipped = [], []
    for n, r in enumerate(raw[hi + 1:], start=hi + 2):
        if not any(str(x or "").strip() for x in r):
            continue
        def get(f: str, r: list[object] = r) -> object:
            return r[cols[f]] if f in cols and cols[f] < len(r) else None
        sifra = re.sub(r"\.0$", "", str(get("sifra") or "").strip())
        if not sifra:
            skipped.append({"red": n, "razlog": "nema šifre"})
            continue
        out.append({"red": n, "sifra": sifra, "naziv": str(get("naziv") or "").strip(),
                    "cijena": _price(get("cijena")), "ean": str(get("ean") or "").strip() or None,
                    "lalizas": str(get("lalizas") or "").strip() or None,
                    "popust": _price(get("popust"))})
    header = [str(x or "") for x in raw[hi]]
    print(json.dumps({"rows": out, "preskoceno": skipped,
                      "stupci": {f: header[i] for f, i in cols.items()}},
                     ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
