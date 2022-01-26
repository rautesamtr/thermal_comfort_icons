#!/usr/bin/env python3
import json
import os
from glob import glob
from string import Template
from xml.dom.minidom import parse

SVG = "svg"
OUTFILE = os.path.join("dist", "thermal_comfort_icons.js")

icons = {
    dom.getElementsByTagName("svg")[0].getAttribute("id"): {
        "path": dom.getElementsByTagName("path")[0].getAttribute("d"),
        "keywords": dom.getElementsByTagName("desc")[0].firstChild.nodeValue.split(" "),
    }
    for dom in [parse(file) for file in glob(os.path.join(SVG, f"*.{SVG}"))]
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
window.customIcons["tc"] = { getIcon, getIconList };"""
)

js = template.substitute(icons=json.dumps(icons, sort_keys=True, indent=2))

with open(OUTFILE, "w") as outfile:
    outfile.write(js)
