### Reporting Dashboard v1.0
<hr/>


###### Description
It is the combination of few services which gets/crawls the reports and manage the report on the disk as well as in to the database; it keeps cleaning the old records and keeps last 20-30(as configured) records.


###### There are three section of this application
1. Crawler
2. Reports data Manager
3. Dashboard Server


###### Setup
Just clone the repo/code and install the requirements;
> `python3 -m pip install requirements.txt`


###### Application Usage
> Usage to start a crawling:
> 
> `python3 main.py --debug-mode --crawl=crawl_directory`
 
> Server Usage:
> 
> `python3 main.py --debug-mode --start-server --port=port_no`

> Separate Usage:
> 
> `python3 crawler.py --crawl=crawl_directory --verbose`
> 
> `python3 server.py --port=port_no --verbose`

<!-- Do not Edit below this line -->
<hr/>

###### Other things
Simply goes here