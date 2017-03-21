# !/usr/bin/python
import os
import sys
import hashlib

def calc_file_hash(file_path):
    """ :description: calculates hash (md5) of file_path
        :param file_path:file path
        :return: hash string
        :rtype: str
    """
    buffer_size = 65536
    md5 = hashlib.md5()
    with open(file_path, 'rb') as file_bin:
        while True:
            data = file_bin.read(buffer_size)
            if not data:
                break
            md5.update(data)
    hash_string = md5.hexdigest()
    return hash_string

def search_a_duplicate(folder_path):
    """ :description: search within folder_path for a duplicated file
        :param folder_path: root folder path
        :return: search result, files path if found
        :rtype: tuple(bool, tuple(str,str))
    """
    file_hash_dic = {}
    if not folder_path:
        raise ValueError('path is empty')

    for root, sub_dirs, files in os.walk(folder_path):
        print "Searching For A Duplicate in {}...".format(root)
        for file_name in files:
            file_path = os.path.join(root, file_name)
            file_hash = calc_file_hash(file_path)
            if file_hash in file_hash_dic:
                return (True, (file_path, file_hash_dic[file_hash]))
            else:
                file_hash_dic[file_hash] = file_path
    return (False, '')

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print "Usage: python search_a_duplicate.py [folder_path]"
    else:
        try:
            folder_path = sys.argv[1]
            search_result, dup_file_path = search_a_duplicate(folder_path)
            if search_result is True:
                print 'Found A Duplicate: {} , {}'.format(dup_file_path[0], dup_file_path[1])
            else:
                print 'Did Not Found A Duplicate.'
        except Exception as exeption:
            print "Failed", type(exeption), exeption
