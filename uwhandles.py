#!/usr/bin/env python
"""
Simple functions to load and merge the UWHandles dataset annotations and reparse them into an iterable dictionary
format. The "is_fisheye" flag in the code indicates whether the raw fisheye or center rectified images should be
loaded.
"""

import json
import os.path as osp

def parse_annotations(file):
    with open(file, 'r') as f:
        annotations = json.load(f) 
    return annotations

def refactor_annotations(annotations, start_index, setpath, is_fisheye):
    images = {}
    classes = {}
    id_map = {}
    index = start_index
    for i in range(len(annotations['images'])):
        id_map[annotations['images'][i]['id']] = index
        annotations['images'][i]['id'] = index
        index += 1
        if is_fisheye:
            annotations['images'][i]['file_name'] = setpath + '/images/raw/' + annotations['images'][i]['file_name']
        else:
            annotations['images'][i]['file_name'] = setpath + '/images/rect/' + annotations['images'][i]['file_name']
    for c in annotations['categories']:
        classes[c['id']] = c['name']
    for image in annotations['images']:
        image_id = image['id']
        images[image_id] = {}
        images[image_id]['file_name'] = image['file_name']
        images[image_id]['annotations'] = []
    for ann in annotations['annotations']:
        if ann['area'] > 0:
            ann['image_id'] = id_map[ann['image_id']]
            image_id = ann['image_id']
            classname = classes[ann['category_id']]
            assert classname in self._classes, \
                'class type does not exist: {}'.format(classname)
            ann['category_id'] = self._class_to_ind[classname]
            images[image_id]['annotations'].append(ann)
    return images

def load_annotations(dataset_path, image_set, is_fisheye=False):
    images = {}
    file = osp.join(dataset_path, 'image_sets', image_set + '.txt')
    with open(file, 'r') as f:
        for setpath in f:
            setpath = setpath.strip()
            if is_fisheye:
                annfile = osp.join(dataset_path, 'data', setpath + '/images/annotations_fisheye_culled.json')
            else:
                annfile = osp.join(dataset_path, 'data', setpath + '/images/annotations_culled.json')
            annotations = parse_annotations(annfile)
            # refactor annotations
            images.update(refactor_annotations(annotations, len(images), setpath, is_fisheye))
    return images

if __name__ == '__main__':
    path = '/path/to/UWHandles/root/directory'
    image_set = 'test'
    annotations = load_annotations(path, image_set, is_fisheye=True)
    print("Number of annotations: {}".format(len(annotations)))
