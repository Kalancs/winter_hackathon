FROM python:3.7

ARG project_dir=/project/

ADD ./requirements.txt $project_dir

WORKDIR $project_dir

RUN pip install -r requirements.txt

RUN export FLASK_ENV=development

RUN export FLASK_APP='start.py'