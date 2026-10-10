# Sample data

Four Counter-Strike 2 matches from 2026-10-09, as published in the
[PureSkill.gg Competitive CS2 Gameplay](https://docs.pureskill.gg/datascience/adx/cs2/csds/)
data set on the AWS Data Exchange. The tutorial in `notebooks/tutorial` uses them.

| Folder | Map | Servers | Rank in `player_info` |
| --- | --- | --- | --- |
| `csds/2026/10/09/6fddf4fa-…` | de_anubis | FACEIT | none (`rank_type` -1) |
| `csds/2026/10/09/83d933c3-…` | de_ancient | Valve, Premier | CS Rating (`rank_type` 11) |
| `csds/2026/10/09/e1013060-…` | de_dust2 | FACEIT | none (`rank_type` -1) |
| `csds/2026/10/09/f9b6c00e-…` | de_mirage | Valve, Premier | CS Rating (`rank_type` 11) |

Each match is 43 objects: 42 channels plus the `csds` index object that lists them.
The [CSDS spec](https://docs.pureskill.gg/datascience/adx/cs2/csds/spec) documents every channel and column.
Keep the `csds/yyyy/mm/dd/<match>/` folder layout: each match's index names its files by that path.

Personal data was removed before publishing, as described in
[PII removal](https://docs.pureskill.gg/datascience/adx/cs2/csds/pii-removal).
For these copies, the header channel's `match_date` was also cut to the minute,
to match the index object's `matchDate`.

## License

The data is licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/):
no commercial use, attribute PureSkill.gg, and share anything derived from it under the same license.
Anything you publish from it must carry the text "Data provided by PureSkill.gg."
