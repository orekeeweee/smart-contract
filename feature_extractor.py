import solcx
import re
from collections import Counter
import numpy as np

# Install solcx if needed
solcx.install_solc(version="0.8.0")  # Adjust to the desired Solidity version

def extract_features_from_raw_code(source_code):
    """
    Extracts features from raw Solidity code text.
    """
    # Compile the Solidity code
    compiled_sol = solcx.compile_source(source_code, output_values=["abi", "bin", "ast"])
    
    # Replace '<stdin>:<ContractName>' with the contract's name dynamically
    contract_name = list(compiled_sol.keys())[0]
    bytecode = compiled_sol[contract_name]["bin"]
    bytecode_len = len(bytecode)
    
    # Bytecode character weights
    bytecode_chars = Counter(bytecode)
    total_chars = sum(bytecode_chars.values())
    char_weights = {f"Weight bytecode_character_{char}": bytecode_chars.get(char, 0) / total_chars for char in "0123456789abcdef"}
    
    # Opcode weights
    opcodes = re.findall(r"[A-Z]+", bytecode)  # Simplistic extraction of opcodes
    opcode_weights = Counter(opcodes)
    total_opcodes = sum(opcode_weights.values())
    opcode_weights_normalized = {f"Opcode weight {op}": opcode_weights[op] / total_opcodes for op in opcode_weights}
    
    # Bytecode entropy
    bytecode_entropy = -sum((count / total_chars) * np.log2(count / total_chars) for count in bytecode_chars.values())
    
    # AST features
    ast = compiled_sol[contract_name]["ast"]
    ast_len_nodes = len(ast["nodes"])
    
    # Combine features into a dictionary
    features = {
        "bytecode_len": bytecode_len,
        "bytecode_entropy": bytecode_entropy,
        "ast_len_nodes": ast_len_nodes,
        **char_weights,
        **opcode_weights_normalized,
    }
    
    return features