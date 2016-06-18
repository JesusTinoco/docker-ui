FROM jpetazzo/dind

RUN curl -O https://bootstrap.pypa.io/get-pip.py
RUN python get-pip.py

WORKDIR /docker-ui

#RUN . ./env/bin/activate && pip install -r requirement.txt
#CMD ["python", "run.py"]


