FROM python:3
ADD *.py *.txt /
RUN pip install -r requirements.txt
CMD [ "python", "./encodebot.py" ]
