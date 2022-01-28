#!/usr/bin/env python3
import json
import os
from glob import glob
from string import Template
from xml.dom.minidom import Document, parse

SVG = "svg"
OUTFILE = os.path.join("dist", "thermal_comfort_icons.js")


def get_path(dom: Document) -> str:
    """Get the path of the svg file."""
    return dom.getElementsByTagName("path")[0].getAttribute("d")


def get_id(dom: Document) -> str:
    """Get the id of the svg file."""
    return dom.getElementsByTagName(SVG)[0].getAttribute("id")


def get_keywords(dom: Document) -> str:
    """Get the keywords of the svg file."""
    desc = dom.getElementsByTagName("desc")[0]
    if desc.firstChild is not None:
        return desc.firstChild.nodeValue
    else:
        return []


doms = [parse(file) for file in glob(os.path.join(SVG, f"*.{SVG}"))]

icons = {
    get_id(dom): {
        "path": get_path(dom),
        "keywords": get_keywords(dom).split(" "),
    }
    for dom in doms
}

template = Template(
    """const TC_ICONS_MAP = $icons;

async function getIcon(name) {
  return {path: TC_ICONS_MAP[name]?.path};
}
async function getIconList() {
  return Object.entries(TC_ICONS_MAP).map(([icon, content]) => ({
    name: icon,
    keywords: content.keywords,
  }));
}

window.customIcons = window.customIcons || {};
window.customIcons["tc"] = { getIcon, getIconList };

window.customIconsets = window.customIconsets || {};
window.customIconsets["tc"] = getIcon;
"""
)

js = template.substitute(icons=json.dumps(icons, sort_keys=True, indent=2))

with open(OUTFILE, "w") as outfile:
    outfile.write(js)
