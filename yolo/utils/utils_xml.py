import os
from os import getcwd
from xml.etree import ElementTree as ET
from xml.etree.ElementTree import Element
from xml.etree.ElementTree import SubElement
from xml.etree.ElementTree import ElementTree


class XmlP:
    def __init__(self, file_name, width, height):
        self.root = self.create_xml(file_name, width, height)

    def __del__(self):
        self.save()

    def add_object(self, obj_name, xi, yi, xa, ya, score):
        """
        # 定义一个创建一级分支object的函数
        # 参数依次，树根，xmin，ymin，xmax，ymax
        :param root:
        :param obj_name:
        :param xi:
        :param yi:
        :param xa:
        :param ya:
        :param score:
        :return:
        """
        # 创建一级分支object
        _object = SubElement(self.root, 'object')
        # 创建二级分支
        name = SubElement(_object, 'name')
        print(obj_name)
        name.text = str(obj_name)
        confidence = SubElement(_object, 'confidence')
        confidence.text = str(score)
        truncated = SubElement(_object, 'truncated')
        truncated.text = '0'
        difficult = SubElement(_object, 'difficult')
        difficult.text = '0'
        # 创建bndbox
        bndbox = SubElement(_object, 'bndbox')
        xmin = SubElement(bndbox, 'xmin')
        xmin.text = '%s' % xi
        ymin = SubElement(bndbox, 'ymin')
        ymin.text = '%s' % yi
        xmax = SubElement(bndbox, 'xmax')
        xmax.text = '%s' % xa
        ymax = SubElement(bndbox, 'ymax')
        ymax.text = '%s' % ya

    def create_xml(self, file_name, width, height):
        # generate root node
        root = Element('annotation')

        # generate first child-node head
        folder = SubElement(root, 'folder')
        folder.text = 'photoAlbum'
        filen = SubElement(root, 'filename')
        filen.text = file_name

        size = SubElement(root, 'size')
        w = SubElement(size, 'width')
        w.text = str(width)
        h = SubElement(size, 'height')
        h.text = str(height)

        return root

    def save(self, name='result.xml'):
        tree = ElementTree(self.root)
        # write out xml data
        tree.write(name, encoding='utf-8')

    def to_str(self):
        return ET.tostring(self.root, encoding='utf-8')


if __name__ == '__main__':
    pass
