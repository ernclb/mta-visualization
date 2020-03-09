# mta-visualization
A project that cleans MTA Turnstile and Train Lateness data, maps and visualizes it

The first file that runs is the python executible 'TurnstileDataCleaner.py'
This program fethces the weekly data and adds it to the dataframe stored in csv format
It also deletes the same week from last year so as to keep the data up to date and not too large.

Station GEO Data Collector needs to be run to update the geolocation of the stations however
does not need to be ran if there are no anomalies or new stations to map

Then this CSV data is plugged into the Tableau workbook to visualize
