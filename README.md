- Using dbnomics normal module: https://youtu.be/Q1wwFB6OlRI
- Using this: https://youtu.be/5g86gReJ7Sc

#### What the DBNOMICS module does:

    -> fetch_series: filter and prepare queries

        -> fetch_series_by_api_link:

            -> iter_series_infos: while loop with series_offset

                -> fetch_series_page: calls HTTP request
                -> yield series: gives back series during the loop (however using lists after)

            -> flatten_dbnomics_series: synchronous code

                -> normalize_period
                -> normalize_value
                -> without_keys

            -> filter_series:

                -> iter_filtered_series: calls HTTP request on the previous series
                (API Time Series Editor https://editor.nomics.world/filters)

                    -> grouper: synchronous code
                    -> flatten_editor_series:

                        -> normalize_period
                        -> normalize_value
                        -> without_keys

#### what we do :

- generate a list of urls
- async generator with coroutines result
- clean the downloaded data
- add a few headers lines and save to csv

#### what we don't do (yet):

- filters
- parse and validate user input for errors
- dynamic fetch of the table of contents
