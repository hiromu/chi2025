#!/usr/bin/env python

import csv
import pathlib
import qrcode
import string
import sys


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f"{sys.argv[0]} input.csv")
        sys.exit(-1)

    output_dir = pathlib.Path(__file__).parent / "dist"
    template_dir = pathlib.Path(__file__).parent / "templates"

    with open(template_dir / "redirect.html") as redirect_html:
        redirect_template = string.Template(redirect_html.read())
    with open(template_dir / "qr.html") as qr_html:
        qr_template = string.Template(qr_html.read())

    with open(sys.argv[1]) as input_csv:
        for item in csv.DictReader(input_csv):
            for mode, url in [("paper", item["paper_url"]), ("pwa", item["pwa_url"])]:
                redirect_dir = output_dir / "link" / mode / item["id"]
                redirect_dir.mkdir(parents=True, exist_ok=True)
                with open(redirect_dir / "index.html", "w") as output_html:
                    output_html.write(redirect_template.substitute(url=url))

                qr_dir = output_dir / "qr" / mode / item["id"]
                qr_dir.mkdir(parents=True, exist_ok=True)
                with open(qr_dir / "index.html", "w") as output_html:
                    output_html.write(qr_template.substitute(url=url))
                qrcode.make(url).save(str(qr_dir / "qr.png"))
