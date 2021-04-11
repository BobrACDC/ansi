#!/usr/bin/python

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

from ansible.module_utils.basic import AnsibleModule
import os


def direct(path, content):
    changed = False
    if not os.path.exists(path):
        os.mkdir(path)
    myfile = os.path.join(path, 'myfile.txt')
    with open(myfile, 'w') as f:
        f.write(content)
        changed = True

    return {'path': path, 'changed': changed}


def run_module():
    module = AnsibleModule(
        argument_spec=dict(
            path=dict(type='str', required=True),
            content=dict(type='str', required=True)
        )
    )
    params = module.params
    path = params['path']
    content = params['content']
    if module.params:
        result = direct(path, content)

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
