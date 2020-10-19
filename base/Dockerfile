FROM lambci/lambda:build-python3.8

RUN pip install setuptools
RUN pip install wheel
RUN pip install twine

RUN mkdir -p /app
WORKDIR /app
COPY Makefile /app/
COPY define_version.py /app/
COPY get_github_description.py /app/
COPY pip_install.py /app/
RUN ls
