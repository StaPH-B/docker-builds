FROM ubuntu:noble AS app

ARG ARG ARBORVIEW_VER="0.1.3"

LABEL base.image="ubuntu:noble"
LABEL dockerfile.version="1"
LABEL software="ArborView"
LABEL software.version="${ARBORVIEW_VER}"
LABEL description="Visualize phylogenetic trees with associated sample metadata"
LABEL website="https://github.com/phac-nml/ArborView"
LABEL license="https://github.com/phac-nml/ArborView/tree/main?tab=readme-ov-file#legal-and-compliance-information"
LABEL maintainer="Kutluhan Incekara"
LABEL maintainer.email="kutluhan.incekara@ct.gov"

RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    python-is-python3 && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

RUN wget --no-check-certificate https://github.com/phac-nml/ArborView/archive/refs/tags/v${ARBORVIEW_VER}.tar.gz && \
    tar -xvf v${ARBORVIEW_VER}.tar.gz && rm v${ARBORVIEW_VER}.tar.gz &&\
    chmod +x /ArborView-${ARBORVIEW_VER}/scripts/inline_arborview.py

ENV PATH="/ArborView-${ARBORVIEW_VER}/scripts/:$PATH" \
    LC_ALL=C

CMD [ "inline_arborview.py", "--help" ]

WORKDIR /data

## Test ##
FROM app AS test

RUN inline_arborview.py --help

RUN inline_arborview.py -d /ArborView-${ARBORVIEW_VER}/example/ultrametric_simple_tree_metadata.tsv -n /ArborView-${ARBORVIEW_VER}/example/ultrametric_simple_tree.nwk -o test.html
