# Change Log

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/)
and this project adheres to [Semantic Versioning](https://semver.org/).

## 0.5.2

### Changed

- Pin workflow runners to `ubuntu-24.04`.

- Require `pureskillgg-dsdk` 4. Its `build_basic_tomes` builds tomes that mix older and newer matches; `make_tome` still fails on a page that mixes their flag columns. The lock moves to dsdk 4.0.1 and csgo-dsdk 3.3.1.

- Tutorial notebook 5 builds the footsteps-by-rank table with `build_basic_tomes` first, then the `make_tome` way, with the flag pitfall and its fix. The template notebook gets a `build_basic_tomes` cell ahead of its `make_tome` loop.

- Harden the deploy workflows: pass the version input through `env:` instead of interpolating it into the shell line; give the dispatch and tag workflows readable run titles.

- GitHub Actions updated to Node 24 runtimes: `actions/checkout` v5 to v7; `astral-sh/setup-uv` v8.2.0 to v9.0.0.

### Fixed

- Stage uv.lock in the version commit.
