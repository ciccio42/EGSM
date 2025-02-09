#!/bin/bash
export CUDA_VISIBLE_DEVICES=1
cd ../
result1=result.log/
file1=result
rm -rf result.log/*.*

QUERY_TARGET_NAMES=("connected_query_0_64.sub.grf data_64.grf")

for i in "${QUERY_TARGET_NAMES[@]}"; do
    # Split the element into two parts
    QUERY_NAME=$(echo $i | awk '{print $1}')
    TARGET_NAME=$(echo $i | awk '{print $2}')

    # Print the two strings
    echo "Query: $QUERY_NAME - Target string: $TARGET_NAME"

    QUERY_TEST=/dataset/DBLP/EGSM_format/8/node_induced/label_64/${QUERY_NAME}
    TARGET_TEST=/dataset/DBLP/EGSM_format/${TARGET_NAME}

    ./build/EGSM -q ${QUERY_TEST} -d ${TARGET_TEST}

    echo $'\n######################################\n'
done

cd bash
