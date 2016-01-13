FROM python:2.7
MAINTAINER "Bijia Lan <lbj.world@gmail.com>"

# setup env
ADD ./dj_demo /code
WORKDIR /code
RUN pip install -r requirements.txt

# run task
CMD ./entry-point.sh
