# Genome Assembly and Gene Model Identifier Tool

This command-line tool facilitates the creation and validation of genome assembly and gene model identifiers based on specific patterns. It is part of the [AgBioData Genome Assembly and Annotation Nomenclature Working Group](https://github.com/AgBioData/Genome-Assembly-and-Annotation-Nomenclature_WG).

## Requirements

- Python 3.x

## Installation

To use GAAN, you need to install its dependencies. We recommend using Poetry for managing the project dependencies.

### Poetry Installation

If you don't have Poetry installed, you can do so by following the instructions on the [official Poetry website](https://python-poetry.org/docs/#installation).

### Install Dependencies

Once Poetry is installed, navigate to the project directory and run the following command to install the dependencies:

```bash
poetry install
```
Usage
GAAN provides command-line functionality for creating and validating genome assembly and gene model identifiers. Here are some examples of how to use GAAN:

## Create Genome Assembly Identifier
```bash
poetry run gaan create-assembly <tol_id> <sample_identifier> <consortium> <version> <subversion> --optional <optional>
```

## Validate Genome Assembly Identifier
```bash
poetry run gaan validate-assembly <assembly_id>
```

## Create Gene Model Identifier
```bash
poetry run gaan create-gene-model <assembly_prefix> <entity> <id_number>
```

## Validate Gene Model Identifier
```bash
poetry run gaan validate-gene-model <gene_model_id>
```

Replace the placeholders <tol_id>, <sample_identifier>, <consortium>, <version>, <subversion>, <optional>, <assembly_id>, <assembly_prefix>, <entity>, <id_number>, and <gene_model_id> with your specific values.

For more information and options, you can use the --help flag with any of the commands, for example:

```bash
poetry run gaan create-assembly --help
```

### Examples
For more examples, refer to the usage section above.

## Using Docker (Optional)

If you prefer to use Docker, you can build a Docker image locally. Ensure you have Docker installed on your machine.

```bash
# Build the Docker image
docker build -t gaan-tool .

# Run the GAAN tool inside a Docker container
docker run -it gaan-tool [command and arguments]
```

Replace [command and arguments] with the actual GAAN command and its arguments. 

### For example:

```bash
docker run -it gaan-tool create-assembly ABC123 Sample1 ProjectX 1 0
```
Note: The Docker image is built locally and not pushed to a container registry. This approach is suitable for local usage.
