FROM staphb/roary:3.12.0

# metadata
LABEL base.image="staphb/roary:3.12.0"
LABEL dockerfile.version="1"
LABEL software="Piggy"
LABEL software.version="1.5"
LABEL description="Pipeline for analysing intergenic regions in bacteria"
LABEL website="https://github.com/harry-thorpe/piggy"
LABEL license="https://github.com/harry-thorpe/piggy/blob/master/LICENSE"
LABEL maintainer="Antonia Chalka"
LABEL maintainer.email="s1438773@ed.ac.uk"

WORKDIR /

# install wget then the piggy tarball
RUN apt-get -y update && apt-get install wget
RUN wget https://github.com/harry-thorpe/piggy/archive/refs/tags/v1.5.tar.gz && \
 tar -xzf v1.5.tar.gz && \
 rm v1.5.tar.gz

# add piggy executable to path
ENV PATH="/piggy-1.5/bin/:${PATH}" \ 
 LC_ALL=C

# set working directory
WORKDIR /data
