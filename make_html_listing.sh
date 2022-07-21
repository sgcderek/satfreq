#!/usr/bin/env bash
(echo '<!DOCTYPE html><html><body><ul><li><a href="..">..</a></li>'
for i in *; do
    if [ "$i" != "index.html" ]; then
        echo "<li><a href=\"$i\">$i</a></li>"
    fi
done
echo '</ul></body></html>') > index.html
