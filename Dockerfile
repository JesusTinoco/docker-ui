FROM jpetazzo/dind

RUN curl -O https://bootstrap.pypa.io/get-pip.py
RUN python get-pip.py

WORKDIR /docker-ui

CMD wrapdocker & \
    pip install virtualenv && \
    virtualenv env && \
    . ./env/bin/activate && \
    pip install -r requirement.txt && \
    python run.py

