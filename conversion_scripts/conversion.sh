#/bin/bash

python3 from_vf_to_egsm.py \
    --src_folder_path="/dataset/DBLP" \
    --graph_path="8/node_induced/original_labels" \
    --dest_folder_path="/dataset/DBLP/EGSM_format"

python3 from_vf_to_egsm.py \
    --src_folder_path="/dataset/DBLP" \
    --graph_path="8/node_induced/label_64" \
    --dest_folder_path="/dataset/DBLP/EGSM_format"

python3 from_vf_to_egsm.py \
    --src_folder_path="/dataset/DBLP" \
    --graph_path="8/node_induced/label_32" \
    --dest_folder_path="/dataset/DBLP/EGSM_format"

python3 from_vf_to_egsm.py \
    --src_folder_path="/dataset/DBLP" \
    --graph_path="8/node_induced/label_16" \
    --dest_folder_path="/dataset/DBLP/EGSM_format"

python3 from_vf_to_egsm.py \
    --src_folder_path="/dataset/DBLP" \
    --graph_path="8/node_induced/label_8" \
    --dest_folder_path="/dataset/DBLP/EGSM_format"

python3 from_vf_to_egsm.py \
    --src_folder_path="/dataset/DBLP" \
    --graph_path="8/node_induced/label_4" \
    --dest_folder_path="/dataset/DBLP/EGSM_format"

python3 from_vf_to_egsm.py \
    --src_folder_path="/dataset/DBLP" \
    --graph_path="8/node_induced/label_2" \
    --dest_folder_path="/dataset/DBLP/EGSM_format"

# python3 from_egsm_to_vf.py \
#     --src_folder_path="/dataset/EGSM_datasets_and_querysets_EGSM_format/dblp/label_16" \
#     --graph_path="query_graph/12" \
#     --dest_folder_path="/dataset/EGSM_datasets_and_querysets"

# python3 from_vf_to_egsm.py \
#     --src_folder_path="/dataset/DBLP" \
#     --graph_path="8/node_induced/label_2" \
#     --dest_folder_path="/dataset/DBLP/EGSM_format"
