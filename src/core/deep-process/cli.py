"""
Deep Process Engine - CLI Interface
Version: 0.1
"""

import sys
from pathlib import Path
from engine.core import DeepProcessEngine
from engine.menu import MenuGenerator

def main():
    print("Initializing Deep Process Engine...")
    
    # Initialize components
    root_path = Path(__file__).parent.parent.parent.parent.parent # Adjust based on location
    engine = DeepProcessEngine(root_path)
    menu_gen = MenuGenerator(engine)

    # Try loading existing state
    if engine.load_state():
        print(f"Loaded project: {engine.current_state.get('project', {}).get('name')}")
    else:
        print("No active project found.")

    # Main Loop
    while True:
        print("\n--- AVAILABLE ACTIONS ---")
        options = menu_gen.generate_menu()
        
        for i, opt in enumerate(options):
            print(f"[{i+1}] {opt.label}")
        print("[0] Exit")

        # In a real CLI, we would ask for input()
        # For this demonstration, we will just show what WOULD happen
        print("\n(Waiting for user input...)")
        break

if __name__ == "__main__":
    main()

