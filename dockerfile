FROM python:3.11.0

# 必要なパッケージやライブラリをインストール
RUN apt-get update
RUN apt-get -y install locales && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm
COPY requirements.txt /
RUN pip install -r /requirements.txt

# コンテナ内に作業ディレクトリを作成
WORKDIR /app

# ホストマシンの特定のディレクトリをコンテナ内のディレクトリにマウント
VOLUME [" C:/Users/iwamatsutakumi/Documents/python/Django/Filofax:/app"]

# コンテナ内で実行するコマンド
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
