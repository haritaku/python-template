# 環境構築

1. Makefileの`PACKAGEDIR`を適切な場所に変更する。
2. conf.pyの`project`, `copyright`, `author`を適切な値に変更する。

## コマンド
基本的には以下のコマンド群を利用する。

| command      | description                                                                    |
| ------------ | ------------------------------------------------------------------------------ |
| `make html`  | _build以下にhtmlファイルを作成。                                               |
| `make clean` | _build内のhtmlファイルを削除                                                   |
| `make live`  | 自動で生成されるファイルを削除してから、リアルタイムでhtmlを作成するコマンド。 |
