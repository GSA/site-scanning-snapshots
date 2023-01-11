1. `1_govt_urls_full.csv` was combined with `double.checking.the.unique.links.txt`.  
2. The file was then normalized to the necessary file structure for our scanning engine.  One ambiguity though was whether to scan against what the original files thought of as websites vs. domains.  So, we made 2 versions, one to target each of them.  These files to be scanned were `1_govt_urls_full - URL-centric.csv` and `1_govt_urls_full - domain-centric.csv`.  
3. The resulting scan data are in the `1_govt_urls_full - URL-centric - results.csv` and 1_govt_urls_full - domain-centric - results.csv` files.  

Details of the original ask are [here](https://github.com/GSA/site-scanning/issues/342).  
