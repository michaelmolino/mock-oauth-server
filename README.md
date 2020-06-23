## Mock Oauth Server

[![GitHub](https://img.shields.io/github/license/michaelmolino/fotrino-frontend?style=for-the-badge)](https://www.gnu.org/licenses/gpl-3.0.en.html)
[![Libraries.io dependency status for GitHub repo](https://img.shields.io/librariesio/github/michaelmolino/mock-oauth-server?style=for-the-badge)](https://libraries.io/github/michaelmolino/mock-oauth-server)
[![Docker Cloud Build Status](https://img.shields.io/docker/cloud/build/michaelmolino/mock-oauth-server?style=for-the-badge)](https://hub.docker.com/repository/docker/michaelmolino/mock-oauth-server)
[![Docker Image Size (tag)](https://img.shields.io/docker/image-size/michaelmolino/mock-oauth-server/latest?label=Docker%20Image%20Size&style=for-the-badge)](https://hub.docker.com/repository/docker/michaelmolino/mock-oauth-server)

This is a mock and very insecure oauth 2 server. It's completely accessible, doesn't validate any tokens, and always returns the same hardcoded user info. Based on docs [here](https://medium.com/@darutk/diagrams-and-movies-of-all-the-oauth-2-0-flows-194f3c3ade85). I've implemented the bare minimum to get it working with [Fotrino](https://www.fotrino.com/).  It might be useful for other projects.
