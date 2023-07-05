import datetime
import os
import ssl
import pandas as pd

dirname = os.path.dirname(__file__)

config = {
    'all_snapshot_url': 'https://api.gsa.gov/technology/site-scanning/data/weekly-snapshot-all.csv',
    'snapshots_archive_folder': os.path.join(dirname, '../snapshots/')
}

def main():
    ssl._create_default_https_context = ssl._create_unverified_context

    today = datetime.date.today()
    timestamp = today.strftime("%-m-%-d-%-y")
    filename = 'weekly-snapshot-all-' + timestamp + '.csv'

    df = pd.read_csv(config['all_snapshot_url'])
    df.to_csv(config['snapshots_archive_folder'] + filename, index=False)

if __name__ == '__main__':
    main()
