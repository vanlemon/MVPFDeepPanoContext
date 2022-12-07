#! /bin/bash

read -p "Do you want to put the file? (y/n) " answer

cd $(dirname $0)
cd ..

#sftp lab << EOF
#put -r ./DeformYolov5Sftp /home/mm
#EOF

sftp lab724 << EOF
#put -r ./DeformYolov5 /home/lmf/PycharmProjects
#put -r ./Multi-View_Projection_Fusion_Object_Detection /home/lmf/PycharmProjects
put -r ./MVPFDeepPanoContext /home/lmf/PycharmProjects
EOF
