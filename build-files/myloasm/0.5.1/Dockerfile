ARG MYLOASM_VER="0.5.1"

FROM ubuntu:noble AS app
ARG MYLOASM_VER

LABEL base.image="ubuntu:noble"
LABEL dockerfile.version="1"
LABEL software="myloasm"
LABEL software.version="${MYLOASM_VER}"
LABEL description="A de novo metagenome assembler for long-read sequencing data"
LABEL website="https://github.com/bluenote-1577/myloasm"
LABEL license="https://github.com/bluenote-1577/myloasm/blob/main/LICENSE"
LABEL maintainer="Kutluhan Incekara"
LABEL maintainer.email="kutluhan.incekara@ct.gov"
LABEL maintainer2="Raheel Ahmed"
LABEL maintainer2.email="raheelsyedahmed@gmail.com"

RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    ca-certificates \
    procps && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

RUN wget https://github.com/bluenote-1577/myloasm/releases/download/v${MYLOASM_VER}/myloasm-${MYLOASM_VER}-x86_64-avx2 && \
    chmod +x myloasm-${MYLOASM_VER}-x86_64-avx2 && \
    mv ./myloasm-${MYLOASM_VER}-x86_64-avx2 /usr/local/bin/myloasm

ENV LC_ALL=C

WORKDIR /data

RUN myloasm --help

CMD [ "myloasm", "--help" ]



FROM app AS test
ARG MYLOASM_VER

WORKDIR /test

RUN myloasm --version && myloasm --help

# Test datasets for mmlong2 - https://zenodo.org/records/12168493
RUN wget -q -O mmlong2_np.fastq.gz https://zenodo.org/records/12168493/files/mmlong2_np.fastq.gz?download=1 && \
    wget -q -O mmlong2_pb.fastq.gz https://zenodo.org/records/12168493/files/mmlong2_pb.fastq.gz?download=1

RUN myloasm mmlong2_np.fastq.gz -o np_test -t 50

RUN myloasm mmlong2_pb.fastq.gz -o pb_test -t 50 --hifi

RUN rm mmlong2_np.fastq.gz && rm mmlong2_pb.fastq.gz

