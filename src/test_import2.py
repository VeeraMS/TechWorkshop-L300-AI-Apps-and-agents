import sys
sys.path.insert(0, 'a2a')

print("Step 1: Importing module...")
import agent.product_management_agent as pma

print("\nStep 2: Module imported. Checking contents...")
print(f"Module attributes: {[x for x in dir(pma) if not x.startswith('_')]}")

print("\nStep 3: Checking for class...")
if hasattr(pma, 'AgentFrameworkProductManagementAgent'):
    print("SUCCESS: Class found!")
else:
    print("ERROR: Class not found in module")
    print("\nChecking for ResponseFormat:")
    if hasattr(pma, 'ResponseFormat'):
        print("ResponseFormat found")
    else:
        print("ResponseFormat NOT found - this suggests an exception during class definition")
