import sys
sys.path.insert(0, 'a2a')

# Patch the module to add debugging
import agent.product_management_agent as pma_module

# Add a test to see if we can manually create the ResponseFormat class
print("Testing ResponseFormat...")
try:
    from pydantic import BaseModel
    from typing import Literal
    
    class ResponseFormat(BaseModel):
        status: Literal['input_required', 'completed', 'error'] = 'input_required'
        message: str
    
    print("ResponseFormat class created successfully in test")
    print(f"ResponseFormat: {ResponseFormat}")
except Exception as e:
    print(f"Error creating ResponseFormat: {e}")
    import traceback
    traceback.print_exc()

# Now try to see what's in the actual module
print(f"\nChecking if 'Literal' is available in module: {hasattr(pma_module, 'Literal')}")
print(f"Literal value: {getattr(pma_module, 'Literal', 'NOT FOUND')}")
