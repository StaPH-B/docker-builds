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

- **Dorado**: Version **0.8.0**, a tool for basecalling Oxford Nanopore sequencing data.
- **NVIDIA CUDA**: Version **12.2.0**, for GPU acceleration (requires NVIDIA GPU).
- **Pre-downloaded basecalling models**: All models are downloaded during the build.
- **Sample Pod5 test file**: Included for testing the basecalling process.

## Requirements

- **Docker**: Installed on your system.
- **NVIDIA GPU and Drivers**: Installed and configured.
- **NVIDIA Container Toolkit**: To enable GPU support in Docker containers.

## Building the Docker Image

 **Build the Docker image** using the following command:

   ```bash
   docker build -t dorado-image .
   ```

## Running the Docker Container

To run the Dorado tool within the Docker container, use the following command:

```bash
docker run --gpus all -it dorado-image dorado --help
```

This command will display the help information for Dorado, confirming that it's installed correctly.

## Testing the Docker Image

To test that Dorado is working correctly, perform a basecalling operation using the provided sample Pod5 file and basecalling models.

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
less basecalled.sam
```

You should see SAM-formatted basecalling results.

## Additional Notes

- **Basecalling Models**: All models are downloaded to `/dorado_models` during the build process.
- **Sample Data**: The sample Pod5 file is downloaded to `/usr/src/app` during the build.
- **Internal Testing**: An internal test stage is included in the Dockerfile to verify installation.

## License

Dorado is licensed under [Oxford Nanopore Technologies' License](https://github.com/nanoporetech/dorado/blob/master/LICENSE).


---

**Note**: Please ensure that you have the necessary NVIDIA drivers and the NVIDIA Container Toolkit installed to utilize GPU acceleration.

---
