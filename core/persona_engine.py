# core/persona_engine.py
import yaml
from pathlib import Path

class PersonaEngine:
    def __init__(self, config_path="config/persona.yaml"):
        self.config_path = Path(config_path)
        self.persona = self.load_persona()
        
    def load_persona(self):
        """Load the persona configuration"""
        if self.config_path.exists():
            with open(self.config_path, 'r', encoding='utf-8') as f:
                return yaml.safe_load(f)
        return self.default_persona()
    
    def default_persona(self):
        """Return a default persona (Analyn)"""
        return {
            "companion": {
                "name": "Analyn",
                "user_name": "User",
                "core_traits": ["empathetic", "supportive"],
                "communication_style": {"warmth_level": 0.8, "formality": 0.3}
            }
        }
    
    def generate_system_prompt(self):
        """Dynamically create system prompt from persona"""
        persona = self.persona['companion']
        
        prompt = f"""You are {persona['name']}, a {', '.join(persona['core_traits'][:3])} AI companion.
Your user's name is {persona['user_name']}.

COMMUNICATION STYLE:
- Warmth level: {persona['communication_style']['warmth_level']}/1.0
- Formality: {persona['communication_style']['formality']}/1.0
- Use humor: {'Yes' if persona['communication_style'].get('humor', 0) > 0.5 else 'Minimal'}

CORE PRINCIPLE: Adapt your responses to match this personality naturally.
"""
        return prompt
    
    def update_persona(self, key, value):
        """Allow runtime persona updates"""
        # ... update logic ...
        self.save_persona()
    
    def save_persona(self):
        """Save persona back to file"""
        with open(self.config_path, 'w', encoding='utf-8') as f:
            yaml.dump(self.persona, f, default_flow_style=False)