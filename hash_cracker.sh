#!/bin/bash
TARGET_HASH=$1
while read WORD; do
        WORD_HASH=$(echo $WORD | md5sum | awk '{print $1}')
        if [ "$WORD_HASH" == "$TARGET_HASH" ]; then
                echo "Found match!"
                echo "Password is : $WORD"
                exit
        fi
done < /usr/share/dict/words

