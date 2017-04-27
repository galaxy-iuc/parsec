.. include:: ../README.rst


Get histories matching a phrase
-------------------------------

parsec histories_get_histories | \
    jq '.[] | select(.name | contains("2017.04.27")) | .id'  -r | \
    xargs parsec histories_update_history --importable true
