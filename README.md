# mypython
ディレクトリ構造を意識したpython実行ラッパー

# インストール
```
    pip install https://github.com/Nkzono99/mypython.git
```

# 使い方
1. .mypythonディレクトリを配置
2. .mypython直下にpythonファイルを配置
3. 以下のコマンドを実行
```
    mypython <python-filename>
```

# 実行例
ディレクトリ構造
```
    <current-directory>
    └─.mypython
        └─hello.py [execute by 'mypython hello.py']

or

    parent
    ├─.mypython
    │  └─hello.py [execute by 'mypython hello.py']
    └─<current-directory>

or

    parent-parent
    ├─.mypython
    |  ├─ hello2.py [execute by 'mypython hello2.py']
    │  └─ hello.py
    └─parent
        ├─.mypython
        │  └─ hello.py [execute by 'mypython hello.py']
        └─<current-directory>

```
