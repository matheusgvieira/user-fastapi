# 
FROM python:3.10

# 
WORKDIR /src

ENV PY_ENV=production

# 
COPY setup.py /src/setup.py

#
COPY app /src/app

# 
RUN pip install --no-cache-dir --upgrade .

# 
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

#
EXPOSE 8000