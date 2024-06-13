FROM python:3.12-slim-bookworm

WORKDIR /app

# install requirements
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the files we need
COPY src/ .
COPY data ./data

# install pytest
RUN pip install pytest

# run the unit tests \
ENTRYPOINT ["pytest"]
CMD ["test"]
