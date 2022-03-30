FROM mambaorg/micromamba:0.20.0

# build and run as root users since micromamba image has 'mambauser' set as the $USER
USER root
# set workdir to default for building; set to /data at the end
WORKDIR /

# ARG variables only persist during build time
# had to include the v for some of these due to GitHub tags. 
# thankfully pangolearn github tag is simply a date
ARG WF_ARTIC_VER="0.3.10"

LABEL base.image="mambaorg/micromamba:0.20.0"
LABEL dockerfile.version="1"
LABEL software="epi2me-labs/wf-artic"
LABEL software.version="$WF_ARTIC_VER"
LABEL description="Conda environment for epi2me-labs/wf-artic"
LABEL website="https://github.com/epi2me-labs/wf-artic/"
LABEL license="MPL 2.0"
LABEL license.url="https://github.com/epi2me-labs/wf-artic/blob/master/LICENSE"
LABEL maintainer1="Curtis Kapsak"
LABEL maintainer1.email="kapsakcj@gmail.com"

# install dependencies; cleanup apt garbage
RUN apt-get update && apt-get install -y --no-install-recommends \
 wget \
 ca-certificates && \
 apt-get autoclean && rm -rf /var/lib/apt/lists/* 

# download epi2me/wf-artic code
RUN wget "https://github.com/epi2me-labs/wf-artic/archive/refs/tags/v${WF_ARTIC_VER}.tar.gz" && \
 tar -xzf v${WF_ARTIC_VER}.tar.gz && \
 rm v${WF_ARTIC_VER}.tar.gz 

# create the conda environment using environment.yml; clean up garbage
RUN micromamba create -n wf-artic-epi2me -y -f /wf-artic-${WF_ARTIC_VER}/environment.yaml && \
 micromamba clean -a -y 

# set the environment; set ENV_NAME so micromamba knows to activate this env during docker image build
ENV LC_ALL=C.UTF-8 \
 ENV_NAME="wf-artic-epi2me"
ARG MAMBA_DOCKERFILE_ACTIVATE=1

# list conda env now that environment is built and active; download medaka model for guppy 3.6.0 high accuracy
# included models:
# r103_fast_g507
# r103_hac_g507
# r103_sup_g507
# r941_min_fast_g507
# r941_min_hac_g507
# r941_min_sup_g507
# r941_prom_fast_g507
# r941_prom_hac_g507
# r941_prom_hac_snp_g507
# r941_prom_hac_variant_g507
# r941_prom_sup_g507
RUN micromamba list && \
 medaka tools download_models --models r941_min_high_g360 

# to ensure the conda environment is active always
ENV PATH=/opt/conda/envs/wf-artic-epi2me/bin:${PATH}

WORKDIR /data
