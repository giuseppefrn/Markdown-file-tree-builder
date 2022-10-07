import os
import argparse

def get_ignore_list(filepath):
    ignore_list = []
    with open(filepath, 'r') as f:
        lines = f.readlines()
        l = len(lines)
        for i,line in enumerate(lines):
            name = line.split('/')[-1]
            if i < l-1:
                name = name[:-1]
            ignore_list.append(name)
    print(ignore_list)
    return ignore_list

def list_files(startpath, ignore_path, project_name):
    ignore_list = []
    if ignore_path:
        ignore_list = get_ignore_list(ignore_path)

    print('<pre>')
    for root, dirs, files in os.walk(startpath):
        files = [f for f in files if not (f[0] == '.' or 'git' in f or f in ignore_list) ]
        dirs[:] = [d for d in dirs if not (d[0] == '.' or 'git' in d or d in ignore_list) ]
        level = root.replace(startpath, '').count(os.sep)
        indent = '  ' * 1 * (level)
        if root == '.':
            print(indent + "&#128193; <a href=#>" + project_name + "</a>")
        else:
            print(indent + "&#128193; <a href=" + root + ">" +os.path.basename(root) + "</a>")
        subindent = '   ' * 1 * (level + 1)
        for f in files:
            print(subindent + "&#x1F5CE; <a href=" + os.path.join(root,f) + ">" + f + "</a>")
    print('</pre>')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--ignore_path", type=str, help='path to ignore name', default=None)
    parser.add_argument("--dir_path", type=str, required=True, help="Directory to walk")
    parser.add_argument("--project_name", type=str, help="Name for the root", default='root')

    opt = parser.parse_args()

    list_files(opt.dir_path, opt.ignore_path, opt.project_name)