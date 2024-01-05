# File system

A file system is a set of rules that manage the way files are stored and retrieved on a disk. It defines how data is written to disk.

## Cluster - Allocation unit

This is the smallest allocation unit imposed by the file system. It is made up of multiple sectors (the smallest physical part: ~512 bytes).
The cluster is the smallest space a file can occupy on a disk.

For example: if the cluster size is 4 Kb, to store a 10 Kb file, 3 clusters are needed (for a total of 12 Kb). The remaining 2 Kb is lost. The space lost is included in the file size.

## External disk

- FAT32
  - Compatible with all major operating systems
  - Maximum file size is 4 GB
  - Minimum allocation size is 512 bytes

- ExFAT (enhanced FAT32)
  - No file size limit
  - Minimum file size for allocation is 4 Kb

- NTFS
  - Proprietary file system developed by Windows
  - Free drivers available for Linux
  - No file size limit
  - Minimum allocation size is 512 bytes (for small volumes)

[Default cluster size for NTFS, FAT, and exFAT](https://support.microsoft.com/en-us/topic/default-cluster-size-for-ntfs-fat-and-exfat-9772e6f1-e31a-00d7-e18f-73169155af95)