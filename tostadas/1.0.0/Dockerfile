FROM nfcore/base:1.13.3
LABEL authors="Cole and Ankush Gupta" \
      description="Docker image containing all software requirements for mamba env"

ARG ENV_YML=environment.yml

#Install mamba at the conda base env
RUN conda install mamba -n base -c conda-forge

# Install the mamba environment
COPY $ENV_YML .

RUN mamba env create --quiet -f environment.yml && mamba clean -a

RUN echo "source activate tostadas" > ~/.bashrc

# Some checks to ensure that the env was properly activated
SHELL ["conda", "run", "-n", "tostadas", "/bin/bash", "-c"]
RUN echo "Checking if the env was properly created and activated"
RUN python -c "import pandas"
RUN python -c "import liftoff"
RUN python -c "import numpy"

# make sure permissions are fine at env location
RUN ["/bin/bash", "-c", "chmod -R a+rw /opt/conda/envs/tostadas"]

ENTRYPOINT ["conda", "run", "-n", "tostadas"]
