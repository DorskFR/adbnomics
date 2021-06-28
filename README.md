"""
What DBNOMICS do:

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

"""

"""
Logic we might want to speed the process:

1. url generation
2. json download
3. json parsing

then

4. save to csv

or

4. saving to db
5. pulling from db
6. saving to csv

"""

list of urls
-> async generator with coroutines result
-> build chain of command with the result
