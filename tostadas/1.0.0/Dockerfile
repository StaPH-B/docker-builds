FROM nfcore/base:1.13.3 as app

LABEL authors="Cole and Ankush Gupta"
LABEL base.image="nfcore/base:1.13.3"
LABEL dockerfile.version="1"
LABEL software="tostadas"
LABEL software.version=$SOFTWARENAME_VER
LABEL description="Image for the TOSTADAS: Toolkit for Open Sequence Triage, Annotation and DAtabase Submission pipeline"
LABEL website="https://github.com/CDCgov/tostadas"
LABEL license="https://github.com/CDCgov/tostadas/LICENSE"
LABEL maintainer="Ankush Gupta, Kyle O'Connell, and Cole Tindall"
LABEL maintainer.email="ankushkgupta@deloitte.com"

ARG ENV_YML=environment.yml

#Install mamba at the conda base env
RUN conda install mamba -n base -c conda-forge

# Install the mamba environment
COPY $ENV_YML .

RUN mamba env create --quiet -f environment.yml && mamba clean -a

RUN echo "source activate tostadas" > ~/.bashrc

# make sure permissions are fine at env location
RUN ["/bin/bash", "-c", "chmod -R a+rw /opt/conda/envs/tostadas"]

ENTRYPOINT ["conda", "run", "-n", "tostadas"]


FROM app as test

# Some checks to ensure that the env was properly activated
SHELL ["conda", "run", "-n", "tostadas", "/bin/bash", "-c"]
RUN echo "Checking if the env was properly created and activated"
RUN python -c "import pandas"
RUN python -c "import liftoff"
RUN python -c "import numpy


