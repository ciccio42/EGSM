#ifndef UTILS_CONFIG_H
#define UTILS_CONFIG_H


#define GRID_DIM 1024u
#define BLOCK_DIM 512u
#define WARP_SIZE 32u
#define WARP_PER_BLOCK (BLOCK_DIM/WARP_SIZE)

#define MAX_VCOUNT 16u
#define MAX_ECOUNT 32u

#define MAX_CUCKOO_LOOP 64u
#define BUCKET_DIM 8u
#define CUCKOO_SCALE_PER_TABLE 2u

#define MAX_RES_MEM_SPACE 6000000000ul

#endif //UTILS_CONFIG_H
