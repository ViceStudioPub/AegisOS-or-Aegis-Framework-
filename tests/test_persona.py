import sys
import os

# Add the parent directory to Python's path so we can import core
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.persona_engine import PersonaEngine

engine = PersonaEngine()
print(f"✅ Loaded persona: {engine.persona.get('companion', {}).get('name', 'Unknown')}")

# Test system prompt generation
prompt = engine.generate_system_prompt()
print(f"\n📝 Generated system prompt (first 200 chars):")
print(prompt[:200] + "...")