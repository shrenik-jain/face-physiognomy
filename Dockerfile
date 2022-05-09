FROM python:3.9
ADD . /app
WORKDIR /app
RUN apt-get update && apt-get install -y python3-opencv
RUN pip install -r requirements.txt
ENV PORT 5000
EXPOSE 5000
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]