# -*- coding: utf-8 -*-
from flask import Flask, Response
import requests
import yaml
import xml.etree.ElementTree as ET

app = Flask(__name__)

# Загружаем конфигурацию из config.yaml
with open("config.yaml", "r") as f:
    CONFIG = yaml.safe_load(f)

@app.route("/metrics")
def metrics():
    output = []
    for metric in CONFIG["metrics"]:
        try:
            print(f"Fetching: {metric['url']} -> {metric['path']}")
            response = requests.get(metric["url"], timeout=5)
            response.raise_for_status()

            xml_root = ET.fromstring(response.text)

            print("== All Tags and Values ==")
            value = None
            for elem in xml_root.iter():
                print(f"TAG: {repr(elem.tag)} VALUE: {repr(elem.text)}")
                if elem.tag.strip() == metric["path"].strip():
                    value = elem.text.strip() if elem.text is not None else None
                    break

            print(f"Parsed value: {value}")
            value = float(value)
            output.append(f"{metric['name']} {value}")
        except Exception as e:
            print(f"Error while processing metric {metric['name']}: {e}")
            return Response(f"# Exporter error: {e}", status=500)

    return Response("\n".join(output) + "\n", mimetype="text/plain")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9112, debug=True)
