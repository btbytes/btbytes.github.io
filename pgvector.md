An open source extension that:  
adds support for storage, indexing, searching, metadata with choice of distance


| k        | v                        |
| -------- | ------------------------ |
| storage  | vector data type         |
| indexing | [[IVFFlat]] and [[HNSW]] |
|          |                          |

##  Vector support in [[PostgreSQL]]

### Array datatype
- data types -- int4, int8, float4, float8
- unlimited dimensions
- *no native* distance operations - can add using PL/XX language. eg: PL/Rust
- *no native indexing*

### Cube datatype
* data types - float8 
* distance operations
	* Euclidean
	* Manhattan
	* Chebyshev
	* K-NN GiST index - **Exact** nearest neighbor search
	* Limited to 100 dimensions


