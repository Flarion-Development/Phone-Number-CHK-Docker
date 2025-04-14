FROM python:3.13

WORKDIR /opt/app

COPY Project /opt/app/

RUN pip install -r /opt/app/requirements.txt
RUN pip install fastapi[standard]

COPY entrypoint.sh /opt/app/
RUN chmod +x /opt/app/entrypoint.sh
CMD ["/opt/app/entrypoint.sh"]