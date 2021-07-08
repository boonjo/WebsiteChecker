FROM python:3

ADD . /WebsiteChecker

WORKDIR /WebsiteChecker

COPY . .

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

ENV SITE_LIST=URLlist.txt
ENV SLACK_BOT_TOKEN=xoxb-1488964595344-2240858379797-jFLzBfhggKp5rVFX0gfNiAkx
ENV CHANNEL=C0275RZNWSW

CMD [ "python", "./websiteChecker.py" ]
