# persona_builder.py - First-run experience
def setup_wizard():
    print("""
    ╔══════════════════════════════════════╗
    ║   Welcome to AegisOS Companion Setup  ║
    ╚══════════════════════════════════════╝
    """)
    
    companion_name = input("What would you like to name your AI companion? [Analyn]: ").strip()
    if not companion_name:
        companion_name = "Analyn"
    
    your_name = input("What should your companion call you? [User]: ").strip()
    if not your_name:
        your_name = "User"
    
    print(f"\n✨ Perfect! Meet {companion_name}, your personal AI companion.")
    print(f"   They'll be there for you, {your_name}.")
    
    # Save to config
    persona = {
        "companion": {
            "name": companion_name,
            "user_name": your_name,
            # ... more defaults
        }
    }
    
    # Save and launch...