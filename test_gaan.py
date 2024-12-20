import unittest
from gaan.gaan import (
    sanitize_input, 
    create_gene_model_identifier, 
    validate_gene_model_identifier, 
    create_assembly_identifier
)

class TestGAANFunctions(unittest.TestCase):

    def test_sanitize_input(self):
        # Test valid input
        self.assertEqual(sanitize_input("test123", "field"), "test123")
        # Test input with invalid characters
        self.assertEqual(sanitize_input("test!@#123", "field"), "test123")
        # Test empty input
        self.assertEqual(sanitize_input("", "field"), "")
        # Test input with spaces
        self.assertEqual(sanitize_input(" test input ", "field"), "testinput")

    def test_create_gene_model_identifier(self):
        # Test with valid prefix, type, and ID
        result = create_gene_model_identifier("prefix", "g", 123)
        self.assertEqual(result, "prefix.g.000123")
        # Test edge-case ID: 0
        result = create_gene_model_identifier("prefix", "g", 0)
        self.assertEqual(result, "prefix.g.000000")
        # Test maximum ID number
        result = create_gene_model_identifier("prefix", "g", 999999)
        self.assertEqual(result, "prefix.g.999999")

    def test_create_assembly_identifier(self):
        # Test assembly identifier WITHOUT the optional field
        result = create_assembly_identifier(
            tol_id="TOL123", 
            sample_identifier="SAMPLE1", 
            consortium="GRP", 
            version=1, 
            subversion=0
        )
        self.assertEqual(result, "TOL123.SAMPLE1.GRP.1.0.fasta")

        # Test assembly identifier WITH the optional field
        result_with_optional = create_assembly_identifier(
            tol_id="TOL123", 
            sample_identifier="SAMPLE1", 
            consortium="GRP", 
            version=1, 
            subversion=0, 
            optional="EXTRA"
        )
        self.assertEqual(result_with_optional, "TOL123.SAMPLE1.GRP.1.0.EXTRA.fasta")

        # Test input sanitization
        result_sanitized = create_assembly_identifier(
            tol_id="TOL!@#123", 
            sample_identifier="SAM!@#PLE1", 
            consortium="GRP", 
            version=2, 
            subversion=1
        )
        self.assertEqual(result_sanitized, "TOL123.SAMPLE1.GRP.2.1.fasta")

        # Test empty optional field
        result_empty_optional = create_assembly_identifier(
            tol_id="TOL123", 
            sample_identifier="SAMPLE1", 
            consortium="GRP", 
            version=3, 
            subversion=2, 
            optional=""
        )
        self.assertEqual(result_empty_optional, "TOL123.SAMPLE1.GRP.3.2.fasta")

    def test_create_assembly_identifier_invalid(self):
        # Test invalid version (not a number)
        with self.assertRaises(ValueError):
            create_assembly_identifier(
                tol_id="TOL123", 
                sample_identifier="SAMPLE1", 
                consortium="GRP", 
                version="invalid", 
                subversion=0
            )

        # Test invalid subversion (not a number)
        with self.assertRaises(ValueError):
            create_assembly_identifier(
                tol_id="TOL123", 
                sample_identifier="SAMPLE1", 
                consortium="GRP", 
                version=1, 
                subversion="invalid"
            )

    def test_validate_gene_model_identifier(self):
        # Test valid gene model identifier
        valid_id = "assemblyprefix.g.000123"
        self.assertTrue(validate_gene_model_identifier(valid_id))

        # Test invalid gene model identifier
        invalid_id = "assemblyprefix.invalid.123"
        self.assertFalse(validate_gene_model_identifier(invalid_id))

if __name__ == "__main__":
    unittest.main()

