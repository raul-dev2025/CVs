#!/bin/bash
for prefix in rrhh talent careers info people contact; do
    echo "--- Testing: ${prefix}@voxelgroup.net ---"
    (
        sleep 1
        echo "HELO raulvilchez.org"
        sleep 1
        echo "MAIL FROM:<r4u1974@gmail.com>"
        sleep 1
        echo "RCPT TO:<${prefix}@voxelgroup.net>"
        sleep 1
        echo "QUIT"
    ) | nc -C aspmx.l.google.com 25 | grep -E "250|550"
done