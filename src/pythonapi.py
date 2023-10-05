import base64
import json

import js
import pyodide.ffi.wrappers
import pyodide.http


async def upload_raw_file_content(content):
    js.console.log("Uploading to file-content-monitor")
    response = await pyodide.http.pyfetch(url=f"{js.window.location.href}api/file-content-monitor/update",
                                          method="POST",
                                          body=base64.b64encode(json.dumps(content, default=str).encode()),
                                          )
    if response.ok:
        js.console.log("Uploaded to file-content-monitor")
        return response.ok


async def download_file_content():
    js.console.log("Downloading from file-content")
    response = await pyodide.http.pyfetch(url=f"{js.window.location.href}api/file-content",
                                          method="GET",
                                          )
    if response.ok:
        js.console.log("Downloaded from file-content")
        return json.loads(base64.b64decode(await response.json()).decode())
