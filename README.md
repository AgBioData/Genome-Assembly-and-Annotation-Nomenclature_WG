# Genome Assembly and Gene Model Identifier Tool

This command-line tool facilitates the creation and validation of genome assembly and gene model identifiers based on specific patterns. It is part of the [AgBioData Genome Assembly and Annotation Nomenclature Working Group](https://github.com/AgBioData/Genome-Assembly-and-Annotation-Nomenclature_WG).

## Requirements

- Python 3.x

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/AgBioData/Genome-Assembly-and-Annotation-Nomenclature_WG.git
   ```

### Navigate to the tool's directory:

```bash
cd Genome-Assembly-and-Annotation-Nomenclature_WG/lib/gaan
```
## Run the tool using Python:

```bash
python gaan.py [command] [options]
```

## Usage
Creating a Genome Assembly Identifier
To create a genome assembly identifier, use the following command:

```bash
python gaan.py create-assembly <tol_id> <sample_identifier> <consortium> <version> <subversion> [--optional <optional>]
```
### Example:

```bash
python gaan.py create-assembly TOL123 sample123 consortiumX 1 0 --optional abc
```

## Validating a Genome Assembly Identifier
To validate a genome assembly identifier, use the following command:

```bash
python gaan.py validate-assembly <assembly_id>
```

### Example:

```bash
python gaan.py validate-assembly TOL123.sample123.consortiumX.1.0.abc.fasta
```

## Creating a Gene Model Identifier
To create a gene model identifier, use the following command:

```bash
python gaan.py create-gene-model <assembly_prefix> <entity> <id_number>
```

### Example:

```bash
python gaan.py create-gene-model TOL123g000001 gene 123456
```

## Validating a Gene Model Identifier
To validate a gene model identifier, use the following command:

```bash
python gaan.py validate-gene-model <gene_model_id>
```

### Example:

```bash
python gaan.py validate-gene-model TOL123g000001
```

## Command-Line Options
create-assembly: Create a genome assembly identifier.
validate-assembly: Validate a genome assembly identifier.
create-gene-model: Create a gene model identifier.
validate-gene-model: Validate a gene model identifier.

### Examples
For more examples, refer to the usage section above.
