FROM ubuntu:20.04
FROM python:3.8
EXPOSE 8501

RUN apt-get update
RUN pip3 install streamlit

ADD ./Project2/app.py  ./app/


CMD streamlit run ./app/app.py
