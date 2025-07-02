import os 

class TemplateParser:

    def __init__(self, language: str, default_language: str = "en"):
        self.current_path = os.path.dirname(os.path.abspath(__file__))
        self.default_language = default_language
        self.language = None

        self.set_language(language=language)


    def set_language(self, language: str):

        if not language:
            self.language = self.default_language

        lang_path = os.path.join(self.current_path, language)

        if os.path.exists(lang_path):
            self.language = language
        else: 
            self.language = self.default_language
            

    def get_template(self, group: str, key: str, vars: dict={}):
        if not group or not key: 
            return None 
        
        target_language = self.language
        group_path = os.path.join(self.current_path, self.language, f"{group}.py")

        if not group_path:
            group_path = os.path.join(self.current_path, target_language, f"{group}.py")
            target_language = self.default_language

        if not group_path:
            return None 
        
        module = __import__(f"llm.templates.{target_language}.{group}", fromlist=[group])

        attr = getattr(module, key)
        return attr.substitute(vars)

        