from data_structures.hashtable.probing import HashTable


def calculate_hash(key):
    return key**3 + 7 * key**2 + 3*key + 5


def probe_func_linear(x, k, size):
    return x


def probe_func_quadratic(x, k, size):
    return x**2


def probe_func_double_hashing(x, k, size):
    def second_hash_func(key):
        return key**3
    d = second_hash_func(k) % size
    if d == 0:
        d = 1
    return (d + x) * second_hash_func(k)


def main():
    # hash table resolution by linear probing
    print('Linear Probing')
    htlinear = HashTable(
        8, hash_func=calculate_hash, probe_func=probe_func_linear)
    htlinear.display()
    htlinear.insert(22, 'qwve')
    htlinear.insert(11, 'sdf')
    htlinear.insert(83, 'qwere')
    htlinear.display()
    htlinear.insert(41, 'vnn')
    htlinear.insert(33, 'pohv')
    htlinear.insert(89, 'braxe')
    htlinear.display()
    # removing an item. creates a zombie
    htlinear.remove(33)
    htlinear.display()

    print('\n\nQuadratic Probing')
    htquad = HashTable(
        8, hash_func=calculate_hash, probe_func=probe_func_quadratic, threshold_factor=0.33)
    htquad.display()
    htquad.insert(22, 'qwve')
    htquad.insert(22, 'qwve')
    htquad.insert(11, 'sdf')
    htquad.insert(83, 'qwere')
    htquad.display()
    htquad.insert(41, 'vnn')
    htquad.insert(33, 'pohv')
    htquad.insert(89, 'braxe')
    # htquad.insert(51)
    htquad.display()

    print('\n\nDouble hashing')
    htdouble = HashTable(
        8, hash_func=calculate_hash, probe_func=probe_func_double_hashing)
    htdouble.display()
    htdouble.insert(22, 'qwve')
    htdouble.insert(11, 'sdf')
    htdouble.insert(83, 'qwere')
    htdouble.display()
    htdouble.insert(41, 'vnn')
    htdouble.insert(33, 'pohv')
    htdouble.insert(89, 'braxe')
    # htdouble.insert(51)
    htdouble.display()


if __name__ == "__main__":
    main()
