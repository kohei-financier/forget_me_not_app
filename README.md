### 忘れ物防止アプリ

【開発環境での使い方】
1. toolsフォルダに行き、npm run buildをターミナルで動かす
```
cd tools
npm run build
```
2. 別ウィンドウでコマンドプロンプトを開き、そちらで開発環境に入る。そのままrunserver。
```
venv/Scripts/activate
↓
仮想環境に入ったら、
python manage.py runserver
```
3. `localhost://8000`で確認

【デプロイする際は】
・pip freeze > requirements.txt
・開発環境DB→本番環境DBへの切り替え
・ALLOWED_HOSTS = []の切り替え