#! /usr/bin/env python3

import argparse
import hashlib

# BUF_SIZE is totally arbitrary, change for your app!
BUF_SIZE = 65536  # lets read stuff in 64kb chunks!

parser = argparse.ArgumentParser()
parser.add_argument('file', help='the file you want to hash')

args = parser.parse_args()

md5 = hashlib.md5()
sha1 = hashlib.sha1()
sha256 = hashlib.sha256()
sha512 = hashlib.sha512()
sha224 = hashlib.sha224()
sha348 = hashlib.sha384()
blake2b = hashlib.blake2b()
blake2s = hashlib.blake2s()
sha3_224 = hashlib.sha3_224()
sha3_256 = hashlib.sha3_256()
sha3_384 = hashlib.sha3_384()
sha3_512 = hashlib.sha3_512()
# shake_128 = hashlib.shake_128()
# shake_256 = hashlib.shake_256()


HASH_ALGORITHM = {
    'MD5': md5,
    'SHA1': sha1,
    'SHA224': sha224,
    'SHA256': sha256,
    'SHA348': sha348,
    'SHA512': sha512,
    'BLAKE2B': blake2b,
    'BLAKE2S': blake2s,
    'SHA3_224': sha3_224,
    'SHA3_256': sha3_256,
    'SHA3_384': sha3_384,
    'SHA3_512': sha3_512,
    # 'SHAKE_128': shake_128,
    # 'SHAKE_256': shake_256
}

with open(args.file, 'rb') as f:
    while True:
        data = f.read(BUF_SIZE)
        if not data:
            break
        for hash_var in HASH_ALGORITHM.values():
            hash_var.update(data)

for hash_name, hash_var in HASH_ALGORITHM.items():
    print('{}:\t{}'.format(hash_name, hash_var.hexdigest()).expandtabs(10))
