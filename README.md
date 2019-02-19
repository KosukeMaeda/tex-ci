<h1 align="center">
	<br>
	<img width="200" src="https://github.com/KosukeMaeda/tex-ci/raw/master/figures/shimekiri_report_hakui_man.png">
	<br>
</h1>

# tex-CI
circleCIを使って自動的にtexファイルをコンパイルする

[![CircleCI](https://circleci.com/gh/KosukeMaeda/tex-ci.svg?style=svg)](https://circleci.com/gh/KosukeMaeda/tex-ci)
←ここがPASSEDならコンパイルできてるよ

コンパイルができていたら
[ここ](https://circleci.com/api/v1.1/project/github/KosukeMaeda/tex-ci/latest/artifacts/0/home/circleci/repo/main.pdf)からコンパイル済みPDFをダウンロードできる。

## Motivation
- texのコンパイルを自動的に行う
- バージョン管理とコンパイルが同時にできる
- texの環境構築が不要


# setup
### 1.リポジトリを作る or このリポジトリをフォークする(プライベートでフォークしたければ[ここ](https://qiita.com/emono/items/4c3e464dba7f880e0208)とか参照)

### 2.[circleCI](https://circleci.com/signup/)に登録する


### 3.circleCIにプロジェクトを追加する
.circleは [.circle](https://github.com/KosukeMaeda/tex-ci/tree/master/.circleci)を参考に

### 4.circleCIのstatus Badgeと、pdfへのリンクを変更する。
pdfへのリンクはこんな感じ
```
https://circleci.com/api/v1.1/project/github/:username/:project/latest/artifacts/0/roject/main.pdf
```
|:user-name|:project|
|:--:|:--:|
|githubのユーザ名|リポジトリ名|

詳しくは[ここ](https://circleci.com/docs/2.0/artifacts/#downloading-all-artifacts-for-a-build-on-circleci)を参考
特にプライベートリポジトリだとtokenが必要となるので注意

### 5.masterブランチにpushするとコンパイルされる


## tips
 - Slackと連携するとビルドの結果を通知してくれる
