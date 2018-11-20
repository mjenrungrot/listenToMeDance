#!/usr/bin/env bash

for i in ~/listenToMeDance/preprocessing/*.mp4; do
  fname=$(echo "$i" | cut -f 1 -d '.')
  fname=$(basename ${fname})
  saveDir="/home/adriansanchez/listenToMeDance/pose_preprocessing/pose_keypoints/$fname"
  echo "Saving to $saveDir ..."
  /home/adriansanchez/openpose/build/examples/openpose/openpose.bin -display 0 -model_pose "COCO" -video     $i -tracking 10  -number_people_max 1 -write_json $saveDir -render_pose 0
  
  
done