FROM python:3

WORKDIR /websiteChecker

ADD databaseconfig.py /
ADD URLlist.txt /
ADD URLReader.py /
ADD URLChecker.py /
ADD websiteChecker.py /

COPY requirements.txt requirements.txt
RUN pip install -r requrements.txt

EXPOSE 5000
COPY . .

CMD [ "python", "./websiteChecker.py" ]