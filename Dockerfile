FROM python:3

ADD . /WebsiteChecker

WORKDIR /WebsiteChecker

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

ENV SLACK_BOT_TOKEN=xoxb-2256225158097-2240634984229-ed3DDfBiOK1zNevRIYyHaXYK
ENV CHANNEL=C027BNN46GL

CMD [ "python", "./websiteChecker.py" ]