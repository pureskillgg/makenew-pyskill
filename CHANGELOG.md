# Change Log

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/)
and this project adheres to [Semantic Versioning](https://semver.org/).

## Unreleased

### Changed

- Harden the deploy workflows: pass the version input through `env:` instead of interpolating it into the shell line; give the dispatch and tag workflows readable run titles; serialize deploys with a concurrency group and give every job a timeout.

- GitHub Actions updated to Node 24 runtimes: `actions/checkout` v5 to v7; `astral-sh/setup-uv` v8.2.0 to v9.0.0.

### Fixed

- Stage uv.lock in the version commit.
