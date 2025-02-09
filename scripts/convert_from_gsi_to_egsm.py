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
        nodes = OrderedDict()
        dest_per_node = OrderedDict()
        edges = []
        num_edges = 0
        for line_indx, line in enumerate(lines):
            line_elements = line.split('\n')[0].split(' ')
            if line_elements[0] == 't' and line_elements[1] == '#' and line_elements[2] == '0':
                continue
            
            if line_indx == 1:
                num_nodes = int(line_elements[0])
                num_edges = int(line_elements[1])
                print(f"Num nodes {num_nodes} - Num edges {num_edges}")

            if line_elements[0] == 'v':
                nodes[int(line_elements[1])] = [int(line_elements[2]), 0] # label, degree
                
            if line_elements[0] == 'e':
                edges.append(
                    (int(line_elements[1]), int(line_elements[2])))  # id_src, id_dest
                
                # increase degree
                nodes[int(line_elements[1])][1] += 1
                nodes[int(line_elements[2])][1] += 1

                if dest_per_node.get(int(line_elements[1]), None) is None:
                    dest_per_node[int(line_elements[1])] = []

                dest_per_node[int(line_elements[1])].append(
                    int(line_elements[2]))

    print(dest_per_node)
    # start convertion
    edge_offset = 0
    with open(dest_file_path, 'w') as f:
        f.write(f"t {num_nodes} {num_edges}\n")
        
        for node_id in range(num_nodes):
            f.write(f"v {node_id} {nodes[node_id][0]} {nodes[node_id][1]}\n")
            
        for node_id in dest_per_node.keys():
            for dest_node in dest_per_node[node_id]:
                f.write(f"e {node_id} {dest_node}\n")
        f.close()
        


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--src_folder_path', type=str,
                        default='/graph-matching-analysis/baseline_algorithms/GSI/data')
    parser.add_argument('--dest_folder_path', type=str,
                        default='/graph-matching-analysis/baseline_algorithms/EGSM/data')
    parser.add_argument('--graph_path', type=str,
                        default='final_test')
    args = parser.parse_args()

    src_graph_paths = glob.glob(os.path.join(
        args.src_folder_path, args.graph_path, "*.grf"))
    print(src_graph_paths)

    out_folder = os.path.join(os.path.join(
        args.dest_folder_path, args.graph_path))
    if not os.path.isdir(out_folder):
        os.makedirs(out_folder, exist_ok=True)

    for indx, graph_path in enumerate(src_graph_paths):
        # if indx == 0:
        file_name = graph_path.split('/')[-1]
        print(f"Converting file {graph_path}")
        convert(src_file_path=graph_path,
                dest_file_path=os.path.join(out_folder, file_name))
