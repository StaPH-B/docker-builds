#!/bin/bash
# tests for mash container
# if anything has an exit code > 0, travis should fail 
set -e
docker run mash:2.3 mash
docker run mash:2.3 mash info /db/RefSeqSketchesDefaults.msh > mashdb.info

echo 'md5sum mashdb.info = '$(md5sum mashdb.info | cut -d ' ' -f 1)

[ "$(md5sum mashdb.info | cut -d ' ' -f 1)" == "a1214deaaa03ef288f4bd063aab8eebd" ]
