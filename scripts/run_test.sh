# QUERY_SIZE 8
taskset -c 9 python3 run_test.py \
    --database_foder="/dataset/DBLP/EGSM_format" \
    --dataset_name=DBLP \
    --query_size=8 \
    --cuda_indx=2 \
    --resume=True \
    --resume_file="/graph-matching-analysis/baseline_algorithms/EGSM/scripts/DBLP_query_size_8.json"

#### EGSM Query ####
taskset -c 9 python3 run_test.py \
    --database_foder=/dataset/EGSM_datasets_and_querysets_EGSM_format/dblp/label_16 \
    --dataset_name=dblp \
    --query_size=12 \
    --cuda_indx=2 \
    --resume=True \
    --resume_file="/graph-matching-analysis/baseline_algorithms/EGSM/scripts/dblp_query_size_12.json"

taskset -c 9 python3 run_test.py \
    --database_foder=/dataset/EGSM_datasets_and_querysets_EGSM_format/enron/label_16 \
    --dataset_name=enron \
    --query_size=8 \
    --cuda_indx=2 \
    --resume=True \
    --resume_file="/graph-matching-analysis/baseline_algorithms/EGSM/scripts/enron_query_size_8.json"

taskset -c 9 python3 run_test.py \
    --database_foder=/dataset/EGSM_datasets_and_querysets_EGSM_format/enron/label_16 \
    --dataset_name=enron \
    --query_size=10 \
    --cuda_indx=2 \
    --resume=True \
    --resume_file="/graph-matching-analysis/baseline_algorithms/EGSM/scripts/enron_query_size_10.json"

taskset -c 9 python3 run_test.py \
    --database_foder=/dataset/EGSM_datasets_and_querysets_EGSM_format/dblp/label_16 \
    --dataset_name=enron \
    --query_size=12 \
    --cuda_indx=2 \
    --resume=True \
    --resume_file="/graph-matching-analysis/baseline_algorithms/EGSM/scripts/enron_query_size_12.json"

taskset -c 9 python3 run_test.py \
    --database_foder=/dataset/EGSM_datasets_and_querysets_EGSM_format/enron/label_16 \
    --dataset_name=enron \
    --query_size=14 \
    --cuda_indx=2 \
    --resume=True \
    --resume_file="/graph-matching-analysis/baseline_algorithms/EGSM/scripts/enron_query_size_14.json"

taskset -c 9 python3 run_test.py \
    --database_foder=/dataset/EGSM_datasets_and_querysets_EGSM_format/enron/label_16 \
    --dataset_name=enron \
    --query_size=16 \
    --cuda_indx=2 \
    --resume=True \
    --resume_file="/graph-matching-analysis/baseline_algorithms/EGSM/scripts/enron_query_size_16.json"
