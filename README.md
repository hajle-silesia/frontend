## About

Repository for frontend app, based on [PyScript](https://pyscript.net/) platform.

## Architecture

### Video streaming

[SRS](https://ossrs.io/lts/en-us/) is used as a realtime video server for HTTP-FLV streaming on a webpage using the srs-player - a HTML5-based player. [Oryx](https://ossrs.io/lts/en-us/docs/v6/doc/getting-started-oryx) serves as a cloud solution for SRS, providing additional features. See configuration details for [SRS](https://github.com/ossrs/srs#usage) and [Oryx](https://github.com/ossrs/oryx).
