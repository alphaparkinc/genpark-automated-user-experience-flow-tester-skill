from client import AutomatedUserExperienceFlowTesterClient

def main():
    client = AutomatedUserExperienceFlowTesterClient()
    res = client.test_ux_flow("https://store.example.com", "Add product to cart and proceed to checkout")
    print(f"Flow Status: {res['flow_status']}")
    print(f"Friction Score: {res['ux_friction_score']}")

if __name__ == "__main__":
    main()
