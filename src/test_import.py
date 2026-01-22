import sys
import traceback
sys.path.insert(0, 'a2a')

try:
    from agent.product_management_agent import AgentFrameworkProductManagementAgent
    print("SUCCESS: Import worked!")
    print(f"Class: {AgentFrameworkProductManagementAgent}")
except Exception as e:
    print(f"ERROR: {type(e).__name__}: {e}")
    traceback.print_exc()
