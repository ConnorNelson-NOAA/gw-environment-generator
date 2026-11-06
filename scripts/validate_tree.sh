#!/bin/bash

ROOT="$1"

find "$ROOT" -type f | while read exe
do
    if file "$exe" | grep -q ELF; then

        missing=$(ldd "$exe" 2>/dev/null | grep "not found")

        if [ -n "$missing" ]; then
            echo
            echo "FAILED: $(basename "$exe")"
            echo "$missing"
        fi
    fi
done
