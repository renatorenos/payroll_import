FROM renatorenos/clientoracledb21-python310

RUN useradd -m user
USER user

COPY ora/* /usr/lib/oracle/21/client64/lib/network/admin/

COPY *.py /app/
COPY .env /app/

RUN python3.10 -m pip install --upgrade pip
RUN pip install loguru
RUN pip install python-dotenv

WORKDIR /app

CMD ["tail", "-f", "/dev/null"]