# Omeka Classic Back Up

## 設定

`.env.sample`ファイルおよび以下の例を参考に`.env`を作成してください。

```
api_url=https://jinmoncom2017.omeka.net/api
#key=
output_dir=../docs
```

`key`については、以下を参考に取得してください。

https://omeka.org/classic/docs/Admin/Settings/API_Settings/

## 実行

Python3の実行環境をご用意ください。

### ダウンロード

```
cd src
sh 100_download.sh
```
