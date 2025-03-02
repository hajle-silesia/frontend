## About

Repository for frontend app, based on [PyScript](https://pyscript.net/) platform.

## Architecture

### Sensors

IoT devices publish the data to the MQTT topics using `<device-type>/<device-id>/<property-name>` format (e.g. `ispindel/ispindel000/temperature`). The same syntax allows to map device properties with HTML tree elements.
Most commonly, units are not included in the published data. Units setting is configured within device itself.  

### Video streaming

[SRS](https://ossrs.io/lts/en-us/) is used as a realtime video server for HTTP-FLV streaming on a webpage using the srs-player - a HTML5-based player. [Oryx](https://ossrs.io/lts/en-us/docs/v6/doc/getting-started-oryx) serves as a cloud solution for SRS, providing additional features. See configuration details for [SRS](https://github.com/ossrs/srs#usage) and [Oryx](https://github.com/ossrs/oryx).
