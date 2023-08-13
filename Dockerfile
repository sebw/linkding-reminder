FROM python:3

LABEL repository="https://github.com/sebw/linkding-reminder"

WORKDIR /opt

RUN pip install --no-cache-dir asyncio aiolinkding

COPY remind.py /opt

CMD ["python", "/opt/remind.py"]