# 環境構築

1. Makefileの`PACKAGEDIR`を適切な場所に変更する。
2. conf.pyの`project`, `copyright`, `author`を適切な値に変更する。

`make init`コマンドを実行する。

## コマンド

基本的には以下のコマンド群を利用する。

| command     | description                                                                                                                         |
| ----------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| `make init` | 環境構築するコマンド。以下のフォルダ・ファイルを作成。<br>index.rst, \[package\].rst, \[module\].rst, \_html, \_statics, \_template |
| `make live` | リアルタイムでhtmlを作成するコマンド。                                                                                              |
| `make m_up` | apidocによりmoduleのドキュメントをアップデートするコマンド。                                                                        |
