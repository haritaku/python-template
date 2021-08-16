# 環境構築

1. Makefileの`PACKAGEDIR`を適切な場所に変更する。
2. conf.pyの`project`, `copyright`, `author`を適切な値に変更する。

## Make Command
基本的には以下のコマンド群を利用する。

| command      | description                                                                    |
| ------------ | ------------------------------------------------------------------------------ |
| `make html`  | _build以下にhtmlファイルを作成。                                               |
| `make clean` | _build内のhtmlファイルを削除                                                   |
| `make live`  | 自動で生成されるファイルを削除してから、リアルタイムでhtmlを作成するコマンド。 |

## Markdown Tips
記述方法は[Markdown Guide](https://www.markdownguide.org/basic-syntax/#images-1)を参考にする。

- コードブロックの中にバッククォートを3つ書くときは、外側のバッククォートを4つにする。

    ````markdown
    ```
    sample
    ```
    ````

## ReStructuredText Tips
記述方法は[reStructuredText入門](https://www.sphinx-doc.org/ja/master/usage/restructuredtext/basics.html)を参考にする。

## MyST Tips
記述方法は[MyST Syntax Reference](https://myst-parser.readthedocs.io/en/latest/syntax/reference.html)を参考にする。

reStructuredTextのディレクティブの記述は、MySTでは以下のように書く。

- reStructuredTextでの記述

    ```reStructuredText
    .. directivename:: arguments
    :key1: val1
    :key2: val2

    This is
    directive content
    ```

- MySTでの記述

    ````MyST
    ```{directivename} arguments
    ---
    key1: val1
    key2: val2
    ---
    This is
    directive content
    ```
    ````

## Docstring Tips
記述方法は[GoogleスタイルのPython Docstringの入門](https://qiita.com/11ohina017/items/118b3b42b612e527dc1d)を参考にする。

- Docstring内で使えるセクションは[Docstring Section](https://www.sphinx-doc.org/ja/master/usage/extensions/napoleon.html#docstring-sections)を参考にする。
- 改行は`<br>`ではなく、`\n`を使う。
- 数式を記述するときはディレクティブを使って記述する。`\`は2回重ねることに注意する。
  - 例1

    ```docstring
    .. math::
        \\sum_{i=1}^{\\infty} x_{i}
    ```

  - 例2

    ```docstring
    .. math::
        \\begin{gather*}
            a_1=b_1+c_1 \\\\ ← 2回重ねていることに注意
            a_2=b_2+c_2-d_2+e_2
        \\end{gather*}
    ```
