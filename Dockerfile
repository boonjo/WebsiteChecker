FROM python:3

ADD databaseconfig.py /
ADD URLlist.txt /
ADD URLReader.py /
ADD URLChecker.py /
ADD websiteChecker.py /

RUN pip install preprocessing
RUN pip install pyyaml
RUN pip install requests
RUN pip install slack_sdk

CMD [ "python", "./websiteChecker.py" ]