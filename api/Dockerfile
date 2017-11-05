FROM python:3.6

ADD . /api
ADD ./requirements.txt /api
RUN chmod a+x /api/run.sh
EXPOSE 8000
CMD ["/api/run.sh"]
