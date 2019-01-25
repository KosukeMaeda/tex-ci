<h1 align="center">
	<br>
	<img width="200" src="https://github.com/KosukeMaeda/tex-ci/raw/master/figures/shimekiri_report_hakui_man.png">
	<br>
</h1>

# tex-CI
circleCIを使って自動的にtexファイルをコンパイルする

[![CircleCI](https://circleci.com/gh/KosukeMaeda/tex-ci.svg?style=svg)](https://circleci.com/api/v1.1/project/github/KosukeMaeda/tex-ci/latest/artifacts/0/roject/main.pdf)
←ここからコンパイルしたpdfファイルをひらける

# setup
### 1.リポジトリを作る or このリポジトリをフォークする(プライベートでフォークしたければ[ここ](https://qiita.com/emono/items/4c3e464dba7f880e0208)とか参照)

### 2.[circleCI](https://circleci.com/signup/)に登録する

### 3.circleCIにプロジェクトを追加する
.circleは [.circle](https://github.com/KosukeMaeda/tex-ci/tree/master/.circleci)を参考に

### 4.READMEを編集してバッチのurlを変更する
https://circleci.com/docs/2.0/status-badges/
バッチのリンク先をコンパイル済みpdfへのリンクにする
pdfへのリンクはこんな感じ
```
https://circleci.com/api/v1.1/project/github/:username/:project/latest/artifacts/0/roject/main.pdf?circle-token=$CIRCLE_TOKEN
```
|:user-name|:project|
|:--:|:--:|
|githubのユーザ名|リポジトリ名|

詳しくは[ここ](https://circleci.com/docs/2.0/artifacts/#downloading-all-artifacts-for-a-build-on-circleci)を参考

### 5.masterブランチにpushするとコンパイルされる
