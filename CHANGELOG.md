# Change Log

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/)
and this project adheres to [Semantic Versioning](https://semver.org/).

## 0.5.2

### Changed

- Pin workflow runners to `ubuntu-24.04`.

- Require `pureskillgg-dsdk` 4. Its `build_basic_tomes` builds tomes that mix older and newer matches; `make_tome` still fails on a page that mixes their flag columns. The lock moves to dsdk 4.0.1 and csgo-dsdk 3.3.1.

- Tutorial notebook 5 builds the footsteps-by-rank table with `build_basic_tomes` first, then the `make_tome` way, with the flag pitfall and its fix. The template notebook gets a `build_basic_tomes` cell ahead of its `make_tome` loop.

- The tutorial is for Counter-Strike 2. It runs on four CS2 matches from 2026-10-09 that now ship in `sample_data/`, instead of downloading seven CS:GO matches from 2022. Notebook 2 becomes "The sample data". The footsteps example uses `wins`, `rank` and `rank_type` (CS2 has no `commends_friendly`), and notebook 6 plots footsteps against the Premier CS Rating. Notebook 7 describes the CS2 product and its current volumes. Notebook 8, which exported the 2021 CS:GO tomes, is removed.

- `simplify_player_info` returns `rank_type` in place of `commends_friendly`.

- The template notebook runs as-is on the sample data.

- The README's setup steps say Python 3.14 and `cd makenew-pyskill`.

- Harden the deploy workflows: pass the version input through `env:` instead of interpolating it into the shell line; give the dispatch and tag workflows readable run titles.

- GitHub Actions updated to Node 24 runtimes: `actions/checkout` v5 to v7; `astral-sh/setup-uv` v8.2.0 to v9.0.0.

### Added

- Tests that run tutorial notebooks 1 to 6 and the template notebook on the sample data, and unit tests for the tutorial's footsteps functions.

### Fixed

- Stage uv.lock in the version commit.

- Notebook 7's cost calculator used an undefined `number_of_revisions`, its terms check named a variable that didn't exist, `ClientError` was never imported, and the bucket's expiry rule was only set when no expiry was wanted.

- Notebook 1 wrote a different `.env` format on macOS than intended, because Python reports the platform as "Darwin", not "Mac". It now writes one format everywhere.
