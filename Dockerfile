FROM python:3

WORKDIR /WebsiteChecker

ADD URLlist.txt /
ADD URLReader.py /
ADD URLChecker.py /
ADD websiteChecker.py /

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5000
COPY . .


ENV SLACK_BOT_TOKEN=xoxb-2256225158097-2240634984229-ed3DDfBiOK1zNevRIYyHaXYK
ENV CHANNEL=C027BNN46GL

CMD [ "python", "./websiteChecker.py" ]