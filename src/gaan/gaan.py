import argparse
import re
from typing import Optional

# Constants
MAX_ID_NUMBER: int = 999999

# Allowed characters in inputs (alphanumeric and hyphens)
SANITIZE_REGEX: re.Pattern = re.compile(r'[^A-Za-z0-9\-]')

# This pattern matches a valid genome assembly identifier as per the given guideline
VALID_ASSEMBLY_REGEX = re.compile(
    r"""
    ^([A-Za-z0-9]+)      # tol_id: Alphanumeric
    \.([A-Za-z0-9]+)     # sample_identifier: Alphanumeric
    \.([A-Za-z0-9]+)     # consortium: Alphanumeric
    \.(\d+)              # version: Digits
    \.(\d+)              # subversion: Digits
    (\.([A-Za-z0-9]+))?  # optional: Alphanumeric (optional)
    \.fasta$             # Ends with .fasta
    """, re.VERBOSE
)

# This pattern matches a valid gene model identifier as per the given guideline
VALID_GENE_MODEL_REGEX: re.Pattern = re.compile(
    r'^([A-Za-z0-9]+)\.(pan|g|p|t)\.(\d{6})$'
)

# Assembly identifier template
ASSEMBLY_ID_TEMPLATE: str = "{tol_id}.{sample_identifier}.{consortium}.{version}.{subversion}{optional}.fasta"

# Gene model identifier template
GENE_MODEL_ID_TEMPLATE: str = "{assembly_prefix}.{entity}.{id_number}"


def sanitize_input(input_str: str, field_name: str) -> str:
    """
    Remove any invalid characters from input strings and notify if changes occurred.
    Only allows alphanumeric characters and hyphens.
    """
    sanitized_str = SANITIZE_REGEX.sub('', input_str)
    if sanitized_str != input_str:
        print(f"Warning: Invalid characters removed from '{field_name}'. "
              f"Original: '{input_str}', Sanitized: '{sanitized_str}'")
    return sanitized_str


def create_assembly_identifier(tol_id: str, sample_identifier: str, consortium: str, version: int,
                               subversion: int, optional: Optional[str] = '') -> str:
    """Construct a valid assembly identifier based on the provided components."""
    # Sanitize inputs with field names
    tol_id = sanitize_input(tol_id, "tol_id")
    sample_identifier = sanitize_input(sample_identifier, "sample_identifier")
    consortium = sanitize_input(consortium, "consortium")
    optional = sanitize_input(optional, "optional")

    # Ensure version and subversion are numbers
    version = int(version)
    subversion = int(subversion)

    return ASSEMBLY_ID_TEMPLATE.format(
        tol_id=tol_id,
        sample_identifier=sample_identifier,
        consortium=consortium,
        version=version,
        subversion=subversion,
        optional=f".{optional}" if optional else ""
    )


def validate_assembly_identifier(assembly_id: str) -> bool:
    """Validate the given assembly identifier against the pattern."""
    return bool(VALID_ASSEMBLY_REGEX.match(assembly_id))


def create_gene_model_identifier(assembly_prefix: str, entity: str, id_number: int) -> str:
    """Construct a valid gene model identifier based on the provided components."""
    # Sanitize inputs with field names
    assembly_prefix = sanitize_input(assembly_prefix, "assembly_prefix")
    entity = sanitize_input(entity, "entity")

    # Ensure id_number is an integer and within range
    id_number = int(id_number)
    if not 0 <= id_number <= MAX_ID_NUMBER:
        raise ValueError(f"ID number '{id_number}' is out of range. It must be between 0 and {MAX_ID_NUMBER}.")

    return GENE_MODEL_ID_TEMPLATE.format(
        assembly_prefix=assembly_prefix,
        entity=entity,
        id_number=str(id_number).zfill(6)  # Fill with zeros to ensure 6 digits
    )


def validate_gene_model_identifier(gene_model_id: str) -> bool:
    """Validate the given gene model identifier against the pattern."""
    return bool(VALID_GENE_MODEL_REGEX.match(gene_model_id))


def main():
    parser = argparse.ArgumentParser(description="Genome Assembly and Gene Model Identifier Tool")
    subparsers = parser.add_subparsers(dest='command')

    # Create assembly identifier
    parser_assembly = subparsers.add_parser(
        'create-assembly',
        help='Create a genome assembly identifier. Example: gaan create-assembly TOL123 SAMPLE1 GRP 1 0')
    parser_assembly.add_argument('tol_id', type=str, help='Tree of Life Identifier')
    parser_assembly.add_argument('sample_identifier', type=str, help='Sample Identifier')
    parser_assembly.add_argument('consortium', type=str, help='Consortium/Project/Group')
    parser_assembly.add_argument('version', type=int, help='Assembly Version Number')
    parser_assembly.add_argument('subversion', type=int, help='Assembly Subversion Number')
    parser_assembly.add_argument('--optional', type=str, help='Optional Naming Component', default='')

    # Validate assembly identifier
    parser_validate_assembly = subparsers.add_parser('validate-assembly', help='Validate a genome assembly identifier')
    parser_validate_assembly.add_argument('assembly_id', type=str, help='Assembly Identifier to validate')

    # Create gene model identifier
    parser_gene_model = subparsers.add_parser('create-gene-model', help='Create a gene model identifier')
    parser_gene_model.add_argument('assembly_prefix', type=str, help='Assembly Prefix')
    parser_gene_model.add_argument('entity', type=str, help='Entity (e.g., g for gene)')
    parser_gene_model.add_argument('id_number', type=int, help='Unique Identifier Number')

    # Validate gene model identifier
    parser_validate_gene_model = subparsers.add_parser('validate-gene-model', help='Validate a gene model identifier')
    parser_validate_gene_model.add_argument('gene_model_id', type=str, help='Gene Model Identifier to validate')

    args = parser.parse_args()

    if args.command == 'create-assembly':
        assembly_id = create_assembly_identifier(
            args.tol_id,
            args.sample_identifier,
            args.consortium,
            args.version,
            args.subversion,
            args.optional
        )
        print(f"Generated Assembly Identifier: {assembly_id}")

    elif args.command == 'validate-assembly':
        is_valid = validate_assembly_identifier(args.assembly_id)
        if is_valid:
            print("Assembly Identifier: Valid")
        else:
            print("Assembly Identifier: Not Valid")

    elif args.command == 'create-gene-model':
        gene_model_id = create_gene_model_identifier(
            args.assembly_prefix,
            args.entity,
            args.id_number
        )
        print(f"Generated Gene Model Identifier: {gene_model_id}")

    elif args.command == 'validate-gene-model':
        is_valid = validate_gene_model_identifier(args.gene_model_id)
        if is_valid:
            print("Gene Model Identifier: Valid")
        else:
            print("Gene Model Identifier: Not Valid")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()

