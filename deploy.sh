#! /bin/bash

conda activate Pano3D

CUDA_VISIBLE_DEVICES=0 WANDB_MODE=dryrun python main.py configs/pano3d_igibson.yaml --model.scene_gcn.relation_adjust True --mode test --demo_path /home/lmf/tmp/repf_pano_client/1666520115/input.png.deep/input