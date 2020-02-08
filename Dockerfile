FROM python:3.6-slim

MAINTAINER nandumpilicode@gmail.com
USER root


WORKDIR /app
ADD . /app



RUN apt-get update
RUN apt-get install -y tesseract-ocr



RUN pip install --trusted-host pypi.python.org -r requirements.txt
RUN apt-get update
RUN apt-get install -y libsm6 libxext6 libxrender-dev libglib2.0-0
RUN pip install opencv-python


EXPOSE 5000
ENV NAME World

CMD ["python", "application.py"]
