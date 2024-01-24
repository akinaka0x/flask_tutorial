# Flaskチュートリアル

## 使い方
ホスト側で実行する内容
```
cd docker
docker compose up -d dev
```
VSCodeのDocker拡張機能を使ってエディタをコンテナにattachする。

コンテナ側で実行する内容
```
cd /app
bash entrypoint.sh
```

ホスト側で実行する内容
```
curl -X GET http://localhost:8080
```
コマンド一覧が表示されるので、順にコマンドを実行して挙動を確認する。
基本的にGETはコンテンツを取得して、POSTはコンテンツを追加する。