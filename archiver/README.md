# Site Scanning Snapshots: Archiver

This script pulls the most recent snapshot containing all scan results and saves
it as a CSV file in the `../snapshots` directory.

This script is set to run on a continual bases by the
[`archive-snapshot.yml`](https://github.com/GSA/site-scanning-snapshots/blob/main/.github/workflows/archive-snapshot.yml)
workflow.

To run locally, install the necessary dependencies and run the script.

```shell
pip install -r requirements.txt
python3 main.py
```
