# -*- codeing:utf-8 -*-
# __author__ = 'Buguin'
import os


def get_fist_tag(parent_tag, child_tag_name):
    """
    According to the name of child tag name, find the first tag of child
    :param parent_tag: the paten tag
    :param child_tag_name: the name of child tag
    :return: first tag of child
    """
    child_tags = parent_tag.getElementsByTagName(child_tag_name)
    return child_tags[0]


def get_childtag_data(parent_tag, child_tag_name):
    """
    Get the content of the child tag
    :param parent_tag: the parent of tag
    :param child_tag_name: the name of child
    :return: the content in child tag
    """
    child_tag = get_fist_tag(parent_tag, child_tag_name)
    if child_tag.firstChild is None:
        return ""
    else:
        tag_data = child_tag.firstChild.data.strip()
        # fixme The txt data extracted directly from XML include the double escape character
        return tag_data


def path_connect(first_path, second_path):
    osname = os.name
    if osname == "nt":
        return first_path + "" + second_path
    elif osname == "posix":
        return first_path + "" + second_path
