FROM jpetazzo/dind

RUN curl -O https://bootstrap.pypa.io/get-pip.py
RUN python get-pip.py

WORKDIR /
ADD requirement.txt requirement.txt
RUN pip install virtualenv && \
    virtualenv env && \
    . ./env/bin/activate && \
    pip install -r requirement.txt

WORKDIR /docker-ui

CMD wrapdocker & \
    . /env/bin/activate && \
    python run.py

