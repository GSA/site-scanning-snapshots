import os
import re
import ssl
import pandas as pd

dirname = os.path.dirname(__file__)

config = {
    'all_snapshot_url': 'https://api.gsa.gov/technology/site-scanning/data/weekly-snapshot-all.csv',
    'slices_archive_folder': os.path.join(dirname, '../by_agency/')
}

def to_snake_case(s):
    s = re.sub(r"\W+", '_', s)
    return s.lower()

def main():
    ssl._create_default_https_context = ssl._create_unverified_context

    df = pd.read_csv(config['all_snapshot_url'])

    agency_list = df['target_url_agency_owner'].unique().tolist()

    for agency in agency_list:
        subset_df = df[df['target_url_agency_owner'] == agency]
        filename = to_snake_case(agency) + '.csv'
        subset_df.to_csv(config['slices_archive_folder'] + filename, index=False)

if __name__ == '__main__':
    main()
