# -*- codeing:utf-8 -*-
# __author__ = 'Buguin'


def file_name_connect(target_abspath, exclude_class):
    file_paths = set()
    for file in exclude_class.files:
        temp = target_abspath + '\\' + file
        # exclude_class.files.discard(file)
        file_paths.add(temp)
    exclude_class.files = file_paths
    print(exclude_class.files)
    return exclude_class
