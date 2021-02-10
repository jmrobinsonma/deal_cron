FROM ubuntu:latest
WORKDIR /dealcron
COPY . /dealcron
VOLUME /dealcron
RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip3 install -r requirements.txt
ENV EMAIL_USER=blazeini2k@gmail.com
ENV EMAIL_PASS=fewcydzcbmtwvhtb
CMD ["python3", "dealcron.py", "free-stuff", "blazeini2k@gmail.com", "-u", "'https://westernmass.craigslist.org/search/zip?hasPic=1'"]
