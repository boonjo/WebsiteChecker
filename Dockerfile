FROM python:3

RUN groupadd --gid 1000 user && \
    useradd --uid 1000 --gid 1000 --create-home --shell /bin/bash user

RUN mkdir /home/user/app
ADD setup.py /home/user/app
ADD requirements.txt /home/user/app
ADD app /home/user/app/app
RUN cd /home/user/app && \
    pip install --no-cache-dir .
RUN cd /home/user/app && \ 
    pip install -r requirements.txt

RUN chown -R "1000:1000" /home/user
USER user
WORKDIR /home/user/app

ENV SITE_LIST=URLlist.txt
ENV SLACK_BOT_TOKEN=
ENV CHANNEL=C0275RZNWSW

CMD tail -f /dev/null
