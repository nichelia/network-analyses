[![github latest release](https://badgen.net/github/release/nichelia/nwa?icon=github)](https://github.com/nichelia/nwa/releases/latest/)
[![pypi latest package](https://badgen.net/pypi/v/nwa?label=pypi%20pacakge)](https://pypi.org/project/nwa/)
[![docker latest image](https://img.shields.io/docker/v/nichelia/nwa?label=image&logo=docker&logoColor=white)](https://hub.docker.com/repository/docker/nichelia/nwa)
[![project license](https://badgen.net/github/license/nichelia/nwa?color=purple)](https://github.com/nichelia/nwa/blob/master/LICENSE)

![nwa CI](https://github.com/nichelia/nwa/workflows/nwa%20CI/badge.svg)
![nwa CD](https://github.com/nichelia/nwa/workflows/nwa%20CD/badge.svg)
[![security scan](https://badgen.net/dependabot/nichelia/nwa/?label=security%20scan)](https://github.com/nichelia/nwa/labels/security%20patch)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen)](https://github.com/pre-commit/pre-commit)


[![code coverage](https://badgen.net/codecov/c/github/nichelia/nwa?label=code%20coverage)](https://codecov.io/gh/nichelia/nwa)
[![code alerts](https://badgen.net/lgtm/alerts/g/nichelia/nwa?label=code%20alerts)](https://lgtm.com/projects/g/nichelia/nwa/alerts/)
[![code quality](https://badgen.net/lgtm/grade/g/nichelia/nwa?label=code%20quality)](https://lgtm.com/projects/g/nichelia/nwa/context:python)
[![code style](https://badgen.net/badge/code%20style/black/color=black)](https://github.com/ambv/black)

# nwa
nwa: A collection of network analyses

## Contents
1. [Use Case](#use-case)
2. [Configuration](#configuration)
3. [Development](#development)
4. [Testing](#testing)
5. [Versioning](#versioning)
6. [Deployment](#deployment)
7. [Production](#production)

## Use Case

A collection of network analyses implementations.  
Input: [TODO].  
Output: [TODO].

### Requirements

* [TODO]

### Assumptions

* [TODO]

### Design

[TODO]

## Configuration

Behaviour of the application can be configured via Environment Variables.

| Environment Variable | Description | Type | Default Value |
| -------------- | -------------- | -------------- | -------------- |
| `NWA_LOG_LEVEL` | Level of logging - overrides verbose/quiet flag | string | - |
| `NWA_LOG_DIR` | Directory to save logs | string | - |
| `NWA_BIN_DIR` | Directory to save any output (bin) | string | bin |

## Development

### Configure for local development

* Clone [repo](https://github.com/nichelia/nwa) on your local machine
* Install [`conda`](https://www.anaconda.com) or [`miniconda`](https://docs.conda.io/en/latest/miniconda.html)
* Create your local project environment (based on [`conda`](https://www.anaconda.com), [`poetry`](https://python-poetry.org), [`pre-commit`](https://pre-commit.com)):  
`$ make env`
* (Optional) Update existing local project environment:  
`$ make env-update`

### Run locally

On a terminal, run the following (execute on project's root directory):

* Activate project environment:  
`$ . ./scripts/helpers/environment.sh`
* Run the CLI using `poetry`:  
`$ poetry run nwa`

### Contribute

[ Not Available ]

## Testing
(part of CI/CD)

[ Work in progress... ]

To run the tests, open a terminal and run the following (execute on project's root directory):

* Activate project environment:  
`$ . ./scripts/helpers/environment.sh`
* To run pytest:  
`$ make test`
* To check test coverage:  
`$ make test-coverage`

## Versioning

Increment the version number:  
`$ poetry version {bump rule}`  
where valid bump rules are:

1. patch
2. minor
3. major
4. prepatch
5. preminor
6. premajor
7. prerelease

### Changelog

Use `CHANGELOG.md` to track the evolution of this package.  
The `[UNRELEASED]` tag at the top of the file should always be there to log the work until a release occurs.  

Work should be logged under one of the following subtitles:
* Added
* Changed
* Fixed
* Removed

On a release, a version of the following format should be added to all the current unreleased changes in the file.  
`## [major.minor.patch] - YYYY-MM-DD`

## Deployment

### Pip package

On a terminal, run the following (execute on project's root directory):

* Activate project environment:  
`$ . ./scripts/helpers/environment.sh`
* To build pip package:  
`$ make build-package`
* To publish pip package (requires credentials to PyPi):  
`$ make publish-package`

### Docker image

On a terminal, run the following (execute on project's root directory):

* Activate project environment:  
`$ . ./scripts/helpers/environment.sh`
* To build docker image:  
`$ make build-docker`

## Production

For production, a Docker image is used.
This image is published publicly on [docker hub](https://hub.docker.com/repository/docker/nichelia/nwa).

* First pull image from docker hub:  
`$ docker pull nichelia/nwa:[version]`
* First pull image from docker hub:  
`$ docker run --rm -it -v ~/nwa_bin:/usr/src/bin nichelia/nwa:[version]`  
This command mounts the application's bin (outcome) to user's root directory under nwa_bin folder.

where version is the published application version (e.g. 0.1.0)
