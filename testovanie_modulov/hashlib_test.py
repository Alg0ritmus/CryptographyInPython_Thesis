import hashlib
data=b"000000000000000000"

test_vec="435e9a36c232f8b02abf69b3163324b02963665ca5a0e9884fd197c0d7deb069d7be114369e3ac0133314fe0f284ad21e60072b12db4ef6770351f154ca89186"
hasher = hashlib.blake2b(digest_size=64) # 8 to 512 bits
hasher.update(data)
digest = hasher.digest()
print("Test Blake2b:","PASSED" if test_vec==digest.hex() else "FAILED")

test_vec="e0496eaa8a43de45384aa8ad23e6027b3434001ff4ba1679b8aae0549efe8dc4"
hasher = hashlib.blake2s(digest_size=32)
hasher.update(data)
digest = hasher.digest()
print("Test Blake2s:","PASSED" if test_vec==digest.hex() else "FAILED")

test_vec="66d054c44b918a4b3f0e6c60b17ec393f6af80d441fe57d74bd34f9e"
hasher = hashlib.sha224()
hasher.update(data)
digest = hasher.digest()
print("Test SHA224:","PASSED" if test_vec==digest.hex() else "FAILED")

test_vec="1bd2b169a9e74a32133550e72e053aecd00500161bf87eb33d921a0dc63d1a71"
hasher = hashlib.sha256()
hasher.update(data)
digest = hasher.digest()
print("Test SHA256:","PASSED" if test_vec==digest.hex() else "FAILED")

test_vec="394ac0e9442b9b4b7b874adc64b061459324ee7582a45f7a5e3e639a550a5916589692a2207f61f6869e742fce463a1e"
hasher = hashlib.sha384()
hasher.update(data)
digest = hasher.digest()
print("Test SHA384:","PASSED" if test_vec==digest.hex() else "FAILED")

test_vec="fe547e78d9b2909bd79c3ad5ebc35dc112a2f8db8b0680a15ddefb82965641e02afd94f2240363f3767bbcac334db4ea842aef3c5f61c101bd26ad5626a669ac"
hasher = hashlib.sha512()
hasher.update(data)
digest = hasher.digest()
print("Test SHA512:","PASSED" if test_vec==digest.hex() else "FAILED")

test_vec="f160dcb312fa3896f222325b3368bdcec4a193295a575fe440a40e58"
hasher = hashlib.sha3_224()
hasher.update(data)
digest = hasher.digest()
print("Test SHA3-224:","PASSED" if test_vec==digest.hex() else "FAILED")

test_vec="9ed52b0131fbdf6969048e9c487f9159ab7796a188a71cac7d373852d679336d"
hasher = hashlib.sha3_256()
hasher.update(data)
digest = hasher.digest()
print("Test SHA3-256:","PASSED" if test_vec==digest.hex() else "FAILED")

test_vec="4d4a3dc36eecbd9b3feba306ff6e999435eb369ac4518a204f84a84f6aab1994493eb47666bf4b0e11944c52372f5de6"
hasher = hashlib.sha3_384()
hasher.update(data)
digest = hasher.digest()
print("Test SHA3-386:","PASSED" if test_vec==digest.hex() else "FAILED")

test_vec="1e6258431a10fbd4cd6e3f0c8f14cbe59b126cbfba4583e6bb7c48b6ab17c9a0fa1ca3686d97d723f9ed305eb0a6e317fbece9340d78f2ea6d257dc44303b0c9"
hasher = hashlib.sha3_512()
hasher.update(data)
digest = hasher.digest()
print("Test SHA3-512:","PASSED" if test_vec==digest.hex() else "FAILED")







