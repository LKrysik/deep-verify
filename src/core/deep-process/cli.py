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
    # cli.py is in src/core/deep-process/
    # root is 3 levels up from cli.py's directory? No, let's trace carefully.
    # __file__ = .../src/core/deep-process/cli.py
    # .parent = .../src/core/deep-process
    # .parent.parent = .../src/core
    # .parent.parent.parent = .../src
    # .parent.parent.parent.parent = .../deep-verify (ROOT)
    
    root_path = Path(__file__).parent.parent.parent.parent
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

        # Simulate user choice for demonstration
        # In real usage: choice = input("Select option: ")
        
        # DEMO: Auto-select logic
        if options:
            selected = options[0] # Default
            
            # Prefer dynamic EPIC action for demo if exists
            for opt in options:
                if "EPIC-001" in opt.id:
                    selected = opt
                    break
            
            print(f"\n> User selected: {selected.label}")
            
            if selected.type == "action" and selected.id.startswith("exec:"):
                # Execute the step!
                from engine.executor_impl import TaskExecutor
                executor = TaskExecutor()
                contract = selected.context["contract"]
                variables = selected.context.get("variables", {})
                result = executor.execute(contract, variables)
                
                # In real app: Update state based on result
                
            elif selected.type == "action" and selected.id.startswith("init:"):
                # Initialize project!
                proc_id = selected.id.split(":")[1]
                if engine.initialize_project(proc_id, "Demo Project"):
                    print(f"✅ Project initialized with process: {proc_id}")
                else:
                    print("❌ Initialization failed.")
        
        break

if __name__ == "__main__":
    main()

