import argparse
import glob
import os
from collections import OrderedDict


def convert(src_file_path, dest_file_path):

    # open file
    with open(src_file_path) as f:

        # read lines
        lines = f.readlines()

        num_nodes = 0
        # num_edges = 0
        nodes_dict = OrderedDict()
        edges_dict = OrderedDict()
        node_degree = OrderedDict()
        num_edges = 0
        
        for line_indx, line in enumerate(lines):
            if 't' in line:
                num_nodes = int(line.split(' ')[-2])
                num_edges = int(line.split(' ')[-1])
            if 'v' in line:
                node_id = int(line.split(' ')[1])
                node_label = int(line.split(' ')[2])
                nodes_dict[node_id] = node_label
                node_degree[node_id] =  int(line.split(' ')[3])
                
            if 'e' in line:
                src = int(line.split(' ')[1])
                dest = int(line.split(' ')[2])
                if src not in edges_dict.keys():
                    edges_dict[src] = []
                edges_dict[src].append(dest)
                num_edges += 1

    print(edges_dict) 
    
    # start convertion
    print(dest_file_path)
    with open(dest_file_path, 'w') as f:
        
        # write number of nodes
        f.write(f"{num_nodes}\n")
        
        # write nodes
        for node_id, node_label in nodes_dict.items():
            f.write(f"{node_id} {node_label}\n")
        
        for node_id in nodes_dict.keys():
            if node_id in edges_dict.keys():
                f.write(f"{len(edges_dict[node_id])}\n")
                for dest in edges_dict[node_id]:
                    f.write(f"{node_id} {dest}\n")
            else:
                f.write(f"0\n")
                
    f.close()
        


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--src_folder_path', type=str,
                        default='/graph-matching-analysis/baseline_algorithms/Database/EGSM_datasets_and_querysets/enron/label_16')
    parser.add_argument('--dest_folder_path', type=str,
                        default='/dataset/DBLP/EGSM_datasets_and_querysets')
    parser.add_argument('--graph_path', type=str,
                        default='')
    args = parser.parse_args()

    print(f"Loading files from {args.src_folder_path}")
    
    dataset_name =args.src_folder_path.split('/')[-2]
    print(f"Dataset name: {dataset_name}")
    label_size = args.src_folder_path.split('/')[-1].split('_')[-1]
    print(f"\tLabel size: {label_size}")
   
    # check folders with query size
    folders_different_query_size = glob.glob(os.path.join(args.src_folder_path, 'query_graph') + '/*')
    
    # print(f"Found {len(folders_different_query_size)} folders with different query sizes")
    
    for folder_query_size in folders_different_query_size:
        print(f"\t\t{folder_query_size}")
        query_size = folder_query_size.split('/')[-1]
        # find queries in folder
        queries = glob.glob(folder_query_size + '/*')
        # print(f"\t\t\tFound {len(queries)} queries")
        
        # convert queries
        for query in queries:
            print(f"\t{query}")
            query_name = query.split('/')[-1]

            # create folder for converted queries
            dest_file_path = os.path.join(args.dest_folder_path, dataset_name, f"label_{label_size}", "query_graph", query_size)
            os.makedirs(dest_file_path, exist_ok=True)
            dest_file_path = os.path.join(dest_file_path, query_name + '.sub.grf')
            
            convert(query, dest_file_path)
    
    # convert data graph
    print(f"Converting data graph")
    data_path = os.path.join(args.src_folder_path, 'data.graph')
    print(data_path)
    data_path_dest = os.path.join(args.dest_folder_path, dataset_name, f"label_{label_size}", "data.grf")
    convert(data_path, data_path_dest)
    