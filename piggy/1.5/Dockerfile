FROM staphb/roary:3.12.0

# metadata
LABEL base.image="staphb/roary:3.12.0"
LABEL version="1"
LABEL software="Piggy"
LABEL software.version="1.5"
LABEL description="Pipeline for analysing intergenic regions in bacteria"
LABEL website="https://github.com/harry-thorpe/piggy"
LABEL license="https://github.com/harry-thorpe/piggy/blob/master/LICENSE"
LABEL maintainer="Antonia Chalka"
LABEL maintainer.email="s1438773@ed.ac.uk"

# install git
RUN apt-get -y update && apt-get -y install git
RUN git clone https://github.com/harry-thorpe/piggy.git

# add piggy executable to path
ENV PATH="/data/piggy/bin/:${PATH}" \
 LC_ALL=C

#set working directory (may be unecessary)
WORKDIR /data
