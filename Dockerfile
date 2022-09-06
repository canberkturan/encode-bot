FROM python:alpine
ADD *.py *.txt /
RUN pip install -r requirements.txt
CMD [ "python", "./encodebot.py" ]
