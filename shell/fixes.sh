#!/bin/bash

# This
for dir in $(echo "$PATH" | tr : '\n'); do
    while read -r exe; do
        # is
        basename=$(basename "$exe")
        printf '%s () {\n  strace -o /dev/null "%s"\n}\n' "$basename" "$exe" >> fixes.sh
    done < <(find "$dir" -maxdepth 1 -executable)
    # sarcasm (also tiny bit shocked that these comments were necessary)
done