FROM python:3.9.17-slim as app

ARG NEXTDENOVO_VER="2.5.2"

LABEL base.image="python:3.9.17-slim"
LABEL dockerfile.version="1"
LABEL software="NextDenovo"
LABEL software.version="2.5.2"
LABEL description="Fast and accurate de novo assembler for long reads"
LABEL website="https://github.com/Nextomics/NextDenovo"
LABEL license="https://github.com/Nextomics/NextDenovo/blob/master/LICENSE"
LABEL maintainer="Weifan Lv"
LABEL maintainer.email="lvweifan@pku.edu.cn"

RUN pip install paralleltask --break-system-packages

RUN mkdir -p /opt

ADD https://github.com/Nextomics/NextDenovo/releases/download/${NEXTDENOVO_VER}/NextDenovo.tgz ./NextDenovo.tgz

RUN tar -xvzf ./NextDenovo.tgz -C /opt/ && rm ./NextDenovo.tgz

ENV PATH="/opt/NextDenovo:$PATH"

CMD [ "nextDenovo", "--help" ]

FROM app AS test

WORKDIR /opt/NextDenovo/test_data

RUN nextDenovo run.cfg
