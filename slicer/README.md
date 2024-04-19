# Site Scanning Snapshots: Slicer

This script pulls the most recent snapshot containing all scan results, splits
them up by agency, and saves CSV files containing the results for each agency
to the `../by_agency` directory.

This script is set to run on a continual bases by the
[`save-agency-slices.yml`](https://github.com/GSA/site-scanning-snapshots/blob/main/.github/workflows/save-agency-slices.yml)
workflow.

To run locally, install the necessary dependencies and run the script.

```shell
pip install -r requirements.txt
python3 main.py
```
