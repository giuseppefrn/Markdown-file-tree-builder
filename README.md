# Keep your project tidy!

Simple python script that automatically builds a tree structure (with links) of your GitHub project.

# Usage

1. Run:
```
        python3 markdown_file_tree.py --dir_path [path-to-folder] --project_name [project-name]
```

1. Copy the results on your terminal/console to your readme.md
   
2. Enjoy the tidiness: 
<pre>
&#128193; <a href=#>Markdown-file-tree-builder</a>
   &#x1F5CE; <a href=./README.md>README.md</a>
   &#x1F5CE; <a href=./markdown_file_tree.py>markdown_file_tree.py</a>
</pre>


## ARGS
The list of arguments is:

```
        --dir_path required, Directory to walk
        --ignore_path path to ignore name, can be a .gitignore file
        --project_name Name for the root, your repo name, default='root'
```

Note that it ignores automatically git files and hidden directory.

You can create your own ignore file where each row is the pathname or the name of the file to ignore.
