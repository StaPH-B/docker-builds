# Dorado Docker Image

This Dockerfile sets up an environment for running **Dorado**, a tool for basecalling Fast5/Pod5 files from Oxford Nanopore sequencing.

## Table of Contents

- [Introduction](#introduction)
- [Requirements](#requirements)
- [Building the Docker Image](#building-the-docker-image)
- [Running the Docker Container](#running-the-docker-container)
- [Testing the Docker Image](#testing-the-docker-image)
- [Basecalling Test](#basecalling-test)
- [Verifying the Output](#verifying-the-output)
- [Additional Notes](#additional-notes)
- [License](#license)

## Introduction

This Docker image includes:

- **Dorado**: Version **0.8.3**, a tool for basecalling Oxford Nanopore sequencing data.
- **NVIDIA CUDA**: Version **12.2.0**, for GPU acceleration (requires NVIDIA GPU).
- **Pigz**: Version **2.6**, for parallel compression and decompression.
- **Pre-downloaded basecalling models**: All models are downloaded during the build process for basecalling.

## Requirements

- **Docker**: Installed on your system.
- **NVIDIA GPU and Drivers**: Installed and configured.
- **NVIDIA Container Toolkit**: To enable GPU support in Docker containers.

## Running the Docker Container

To run the Dorado tool within the Docker container, use the following command:

```bash
docker run --gpus all -it dorado-image dorado --help
```

This command will display the help information for Dorado, confirming that it's installed correctly.

## Testing the Docker Image

To test that Dorado is working correctly, you will need to download a sample Pod5 file and perform a basecalling operation using the pre-downloaded basecalling models.

```bash
wget -O dna_r10.4.1_e8.2_260bps-FLO_PRO114-SQK_NBD114_96_260-4000.pod5 \
  https://github.com/nanoporetech/dorado/raw/release-v0.7/tests/data/pod5/dna_r10.4.1_e8.2_260bps/dna_r10.4.1_e8.2_260bps-FLO_PRO114-SQK_NBD114_96_260-4000.pod5


### Basecalling Test

Run the following command:

```bash
docker run --gpus all -v $(pwd):/usr/src/app -it dorado-image bash -c "\
  dorado basecaller /dorado_models/dna_r10.4.1_e8.2_260bps_sup@v3.5.2 \
  /usr/src/app/dna_r10.4.1_e8.2_260bps-FLO_PRO114-SQK_NBD114_96_260-4000.pod5 \
  --emit-moves > /usr/src/app/basecalled.sam"
```

**Explanation:**

- `--gpus all`: Enables GPU support.
- `-v $(pwd):/usr/src/app`: Mounts the current directory to `/usr/src/app` inside the container.
- `bash -c "...":` Runs the basecalling command inside the container.
- `> /usr/src/app/basecalled.sam`: Redirects the output to `basecalled.sam` in your current directory.

### Verifying the Output

Check the output file to ensure basecalling was successful:

```bash
samtools view basecalled.sam
```

You should see SAM-formatted basecalling results.

## Additional Notes

- **Sample Data**: The sample Pod5 file is downloaded to `/usr/src/app` during the build.
- **Internal Testing**: An internal test stage is included in the Dockerfile to verify installation.
- **Basecalling Models**: All models are downloaded to `/dorado_models` during the build process.
  Below is the list of basecalling models included in the Docker image:
  ```yaml

  modification models:
    - "dna_r9.4.1_e8_fast@v3.4_5mCG@v0.1"
    - "dna_r9.4.1_e8_hac@v3.3_5mCG@v0.1"
    - "dna_r9.4.1_e8_sup@v3.3_5mCG@v0.1"
    - "dna_r9.4.1_e8_fast@v3.4_5mCG_5hmCG@v0"
    - "dna_r9.4.1_e8_hac@v3.3_5mCG_5hmCG@v0"
    - "dna_r9.4.1_e8_sup@v3.3_5mCG_5hmCG@v0"
    - "dna_r10.4.1_e8.2_260bps_fast@v3.5.2_5mCG@v2"
    - "dna_r10.4.1_e8.2_260bps_hac@v3.5.2_5mCG@v2"
    - "dna_r10.4.1_e8.2_260bps_sup@v3.5.2_5mCG@v2"
    - "dna_r10.4.1_e8.2_400bps_fast@v3.5.2_5mCG@v2"
    - "dna_r10.4.1_e8.2_400bps_hac@v3.5.2_5mCG@v2"
    - "dna_r10.4.1_e8.2_400bps_sup@v3.5.2_5mCG@v2"
    - "dna_r10.4.1_e8.2_260bps_fast@v4.0.0_5mCG_5hmCG@v2"
    - "dna_r10.4.1_e8.2_260bps_hac@v4.0.0_5mCG_5hmCG@v2"
    - "dna_r10.4.1_e8.2_260bps_sup@v4.0.0_5mCG_5hmCG@v2"
    - "dna_r10.4.1_e8.2_400bps_fast@v4.0.0_5mCG_5hmCG@v2"
    - "dna_r10.4.1_e8.2_400bps_hac@v4.0.0_5mCG_5hmCG@v2"
    - "dna_r10.4.1_e8.2_400bps_sup@v4.0.0_5mCG_5hmCG@v2"
    - "dna_r10.4.1_e8.2_260bps_fast@v4.1.0_5mCG_5hmCG@v2"
    - "dna_r10.4.1_e8.2_260bps_hac@v4.1.0_5mCG_5hmCG@v2"
    - "dna_r10.4.1_e8.2_260bps_sup@v4.1.0_5mCG_5hmCG@v2"
    - "dna_r10.4.1_e8.2_400bps_fast@v4.1.0_5mCG_5hmCG@v2"
    - "dna_r10.4.1_e8.2_400bps_hac@v4.1.0_5mCG_5hmCG@v2"
    - "dna_r10.4.1_e8.2_400bps_sup@v4.1.0_5mCG_5hmCG@v2"
    - "dna_r10.4.1_e8.2_400bps_fast@v4.2.0_5mCG_5hmCG@v2"
    - "dna_r10.4.1_e8.2_400bps_hac@v4.2.0_5mCG_5hmCG@v2"
    - "dna_r10.4.1_e8.2_400bps_sup@v4.2.0_5mCG_5hmCG@v2"
    - "dna_r10.4.1_e8.2_400bps_sup@v4.2.0_5mCG_5hmCG@v3.1"
    - "dna_r10.4.1_e8.2_400bps_sup@v4.2.0_5mC@v2"
    - "dna_r10.4.1_e8.2_400bps_sup@v4.2.0_6mA@v2"
    - "dna_r10.4.1_e8.2_400bps_sup@v4.2.0_6mA@v3"
    - "dna_r10.4.1_e8.2_400bps_sup@v4.2.0_5mC_5hmC@v1"
    - "dna_r10.4.1_e8.2_400bps_hac@v4.3.0_5mC_5hmC@v1"
    - "dna_r10.4.1_e8.2_400bps_sup@v4.3.0_5mC_5hmC@v1"
    - "dna_r10.4.1_e8.2_400bps_hac@v4.3.0_6mA@v1"
    - "dna_r10.4.1_e8.2_400bps_sup@v4.3.0_6mA@v1"
    - "dna_r10.4.1_e8.2_400bps_hac@v4.3.0_6mA@v2"
    - "dna_r10.4.1_e8.2_400bps_sup@v4.3.0_6mA@v2"
    - "dna_r10.4.1_e8.2_400bps_hac@v4.3.0_5mCG_5hmCG@v1"
    - "dna_r10.4.1_e8.2_400bps_sup@v4.3.0_5mCG_5hmCG@v1"
    - "dna_r10.4.1_e8.2_400bps_hac@v5.0.0_4mC_5mC@v1"
    - "dna_r10.4.1_e8.2_400bps_sup@v5.0.0_4mC_5mC@v1"
    - "dna_r10.4.1_e8.2_400bps_hac@v5.0.0_4mC_5mC@v2"
    - "dna_r10.4.1_e8.2_400bps_sup@v5.0.0_4mC_5mC@v2"
    - "dna_r10.4.1_e8.2_400bps_hac@v5.0.0_5mC_5hmC@v1"
    - "dna_r10.4.1_e8.2_400bps_sup@v5.0.0_5mC_5hmC@v1"
    - "dna_r10.4.1_e8.2_400bps_hac@v5.0.0_5mC_5hmC@v2"
    - "dna_r10.4.1_e8.2_400bps_sup@v5.0.0_5mC_5hmC@v2"
    - "dna_r10.4.1_e8.2_400bps_hac@v5.0.0_5mCG_5hmCG@v1"
    - "dna_r10.4.1_e8.2_400bps_sup@v5.0.0_5mCG_5hmCG@v1"
    - "dna_r10.4.1_e8.2_400bps_hac@v5.0.0_5mCG_5hmCG@v2"
    - "dna_r10.4.1_e8.2_400bps_sup@v5.0.0_5mCG_5hmCG@v2"
    - "dna_r10.4.1_e8.2_400bps_hac@v5.0.0_6mA@v1"
    - "dna_r10.4.1_e8.2_400bps_sup@v5.0.0_6mA@v1"
    - "dna_r10.4.1_e8.2_400bps_hac@v5.0.0_6mA@v2"
    - "dna_r10.4.1_e8.2_400bps_sup@v5.0.0_6mA@v2"
    - "rna004_130bps_sup@v3.0.1_m6A_DRACH@v1"
    - "rna004_130bps_hac@v5.0.0_m6A@v1"
    - "rna004_130bps_sup@v5.0.0_m6A@v1"
    - "rna004_130bps_hac@v5.0.0_m6A_DRACH@v1"
    - "rna004_130bps_sup@v5.0.0_m6A_DRACH@v1"
    - "rna004_130bps_hac@v5.0.0_pseU@v1"
    - "rna004_130bps_sup@v5.0.0_pseU@v1"
    - "rna004_130bps_hac@v5.1.0_m5C@v1"
    - "rna004_130bps_sup@v5.1.0_m5C@v1"
    - "rna004_130bps_hac@v5.1.0_inosine_m6A@v1"
    - "rna004_130bps_sup@v5.1.0_inosine_m6A@v1"
    - "rna004_130bps_hac@v5.1.0_m6A_DRACH@v1"
    - "rna004_130bps_sup@v5.1.0_m6A_DRACH@v1"
    - "rna004_130bps_hac@v5.1.0_pseU@v1"
    - "rna004_130bps_sup@v5.1.0_pseU@v1"
  stereo models:
    - "dna_r10.4.1_e8.2_4khz_stereo@v1.1"
    - "dna_r10.4.1_e8.2_4khz_stereo@v1.1"
    - "dna_r10.4.1_e8.2_5khz_stereo@v1.1"
    - "dna_r10.4.1_e8.2_5khz_stereo@v1.2"
    - "dna_r10.4.1_e8.2_5khz_stereo@v1.3"
  simplex models:
    - "dna_r9.4.1_e8_fast@v3.4"
    - "dna_r9.4.1_e8_hac@v3.3"
    - "dna_r9.4.1_e8_sup@v3.3"
    - "dna_r9.4.1_e8_sup@v3.6"
    - "dna_r10.4.1_e8.2_260bps_fast@v3.5.2"
    - "dna_r10.4.1_e8.2_260bps_hac@v3.5.2"
    - "dna_r10.4.1_e8.2_260bps_sup@v3.5.2"
    - "dna_r10.4.1_e8.2_400bps_fast@v3.5.2"
    - "dna_r10.4.1_e8.2_400bps_hac@v3.5.2"
    - "dna_r10.4.1_e8.2_400bps_sup@v3.5.2"
    - "dna_r10.4.1_e8.2_260bps_fast@v4.0.0"
    - "dna_r10.4.1_e8.2_260bps_hac@v4.0.0"
    - "dna_r10.4.1_e8.2_260bps_sup@v4.0.0"
    - "dna_r10.4.1_e8.2_400bps_fast@v4.0.0"
    - "dna_r10.4.1_e8.2_400bps_hac@v4.0.0"
    - "dna_r10.4.1_e8.2_400bps_sup@v4.0.0"
    - "dna_r10.4.1_e8.2_260bps_fast@v4.1.0"
    - "dna_r10.4.1_e8.2_260bps_hac@v4.1.0"
    - "dna_r10.4.1_e8.2_260bps_sup@v4.1.0"
    - "dna_r10.4.1_e8.2_400bps_fast@v4.1.0"
    - "dna_r10.4.1_e8.2_400bps_hac@v4.1.0"
    - "dna_r10.4.1_e8.2_400bps_sup@v4.1.0"
    - "dna_r10.4.1_e8.2_400bps_fast@v4.2.0"
    - "dna_r10.4.1_e8.2_400bps_hac@v4.2.0"
    - "dna_r10.4.1_e8.2_400bps_sup@v4.2.0"
    - "dna_r10.4.1_e8.2_400bps_fast@v4.3.0"
    - "dna_r10.4.1_e8.2_400bps_hac@v4.3.0"
    - "dna_r10.4.1_e8.2_400bps_sup@v4.3.0"
    - "dna_r10.4.1_e8.2_400bps_fast@v5.0.0"
    - "dna_r10.4.1_e8.2_400bps_hac@v5.0.0"
    - "dna_r10.4.1_e8.2_400bps_sup@v5.0.0"
    - "dna_r10.4.1_e8.2_apk_sup@v5.0.0"
    - "rna002_70bps_fast@v3"
    - "rna002_70bps_hac@v3"
    - "rna004_130bps_fast@v3.0.1"
    - "rna004_130bps_hac@v3.0.1"
    - "rna004_130bps_sup@v3.0.1"
    - "rna004_130bps_fast@v5.0.0"
    - "rna004_130bps_hac@v5.0.0"
    - "rna004_130bps_sup@v5.0.0"
    - "rna004_130bps_fast@v5.1.0"
    - "rna004_130bps_hac@v5.1.0"
    - "rna004_130bps_sup@v5.1.0"
  ```

## License

Dorado is licensed under [Oxford Nanopore Technologies' License](https://github.com/nanoporetech/dorado/blob/master/LICENSE).


---

**Note**: Please ensure that you have the necessary NVIDIA drivers and the NVIDIA Container Toolkit installed to utilize GPU acceleration.

---
