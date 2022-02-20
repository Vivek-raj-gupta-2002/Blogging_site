FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir blog_site
WORKDIR blog_site
COPY requriment.txt /blog_site
RUN pip install -r requriment.txt
COPY . /blog_site

