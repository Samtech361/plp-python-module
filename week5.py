class ProgrammingLanguage:
    """Base class representing a programming language"""
    
    def __init__(self, name, year_created, creator, paradigm):
        # Encapsulation: attributes are initialized through constructor
        self.name = name
        self.year_created = year_created
        self.creator = creator
        self.paradigm = paradigm
        self.popularity_score = 0
    
    def execute_code(self):
        """Base method for code execution - to be overridden"""
        return f"{self.name} is executing code..."
    
    def compile(self):
        """Base method for compilation process"""
        return f"{self.name} is processing code..."
    
    def get_info(self):
        """Method to display language information"""
        return f"""
Language: {self.name}
Created: {self.year_created}
Creator: {self.creator}
Paradigm: {self.paradigm}
Popularity Score: {self.popularity_score}/10
        """
    
    def set_popularity(self, score):
        """Setter method with validation"""
        if 0 <= score <= 10:
            self.popularity_score = score
        else:
            print("Popularity score must be between 0 and 10!")


class CompiledLanguage(ProgrammingLanguage):
    """Inherited class for compiled languages"""
    
    def __init__(self, name, year_created, creator, paradigm, compiler_name):
        # Call parent constructor
        super().__init__(name, year_created, creator, paradigm)
        self.compiler_name = compiler_name
        self.is_compiled = True
    
    def compile(self):
        """Polymorphism: Override compile method"""
        return f" {self.name} is being compiled using {self.compiler_name}..."
    
    def execute_code(self):
        """Polymorphism: Override execute method"""
        return f" {self.name} executes lightning-fast compiled machine code!"


class InterpretedLanguage(ProgrammingLanguage):
    """Inherited class for interpreted languages"""
    
    def __init__(self, name, year_created, creator, paradigm, interpreter):
        super().__init__(name, year_created, creator, paradigm)
        self.interpreter = interpreter
        self.is_compiled = False
    
    def compile(self):
        """Polymorphism: Override compile method"""
        return f"{self.name} doesn't need compilation - ready to interpret!"
    
    def execute_code(self):
        """Polymorphism: Override execute method"""
        return f" {self.name} is being interpreted line by line by {self.interpreter}!"


class WebLanguage(InterpretedLanguage):
    """Further inheritance for web-focused languages"""
    
    def __init__(self, name, year_created, creator, paradigm, interpreter, runs_in_browser=True):
        super().__init__(name, year_created, creator, paradigm, interpreter)
        self.runs_in_browser = runs_in_browser
    
    def execute_code(self):
        """Polymorphism: Override for web-specific execution"""
        location = "browser" if self.runs_in_browser else "server"
        return f" {self.name} is running dynamic web code in the {location}!"
    
    def manipulate_dom(self):
        """Web-specific method"""
        if self.runs_in_browser:
            return f" {self.name} is manipulating the DOM and creating interactive experiences!"
        else:
            return f"{self.name} runs on the server and doesn't directly manipulate the DOM."


def demonstrate_polymorphism(languages):
    """Function to demonstrate polymorphism in action"""
    print(" POLYMORPHISM DEMONSTRATION ")
    print("=" * 50)
    
    for language in languages:
        print(f"\n--- {language.name} ---")
        print(language.compile())
        print(language.execute_code())
        
        # Check if it's a web language and call web-specific method
        if isinstance(language, WebLanguage):
            print(language.manipulate_dom())


def main():
    print(" PROGRAMMING LANGUAGES CLASS SYSTEM  ")
    print("=" * 55)
    
    # Creating objects using constructors with unique values
    python = InterpretedLanguage("Python", 1991, "Guido van Rossum", "Multi-paradigm", "CPython")
    python.set_popularity(9)
    
    cpp = CompiledLanguage("C++", 1985, "Bjarne Stroustrup", "Object-oriented", "GCC/Clang")
    cpp.set_popularity(8)
    
    javascript = WebLanguage("JavaScript", 1995, "Brendan Eich", "Multi-paradigm", "V8 Engine", True)
    javascript.set_popularity(10)
    
    rust = CompiledLanguage("Rust", 2010, "Mozilla Foundation", "Systems programming", "rustc")
    rust.set_popularity(7)
    
    nodejs = WebLanguage("Node.js", 2009, "Ryan Dahl", "Event-driven", "V8 Engine", False)
    nodejs.set_popularity(8)
    
    # Display information about each language
    languages = [python, cpp, javascript, rust, nodejs]
    
    print("\n LANGUAGE INFORMATION ")
    print("=" * 35)
    for lang in languages:
        print(lang.get_info())
        print("-" * 30)
    
    # Demonstrate polymorphism
    print("\n")
    demonstrate_polymorphism(languages)
    
    # Demonstrate encapsulation and method usage
    print(f"\n ENCAPSULATION EXAMPLE ")
    print("=" * 35)
    print(f"Accessing Python's attributes:")
    print(f"Name: {python.name}")
    print(f"Year: {python.year_created}")
    print(f"Is Compiled: {python.is_compiled}")
    print(f"Interpreter: {python.interpreter}")
    
    # Demonstrate inheritance hierarchy
    print(f"\n INHERITANCE HIERARCHY ")
    print("=" * 35)
    print(f"JavaScript instanceof WebLanguage: {isinstance(javascript, WebLanguage)}")
    print(f"JavaScript instanceof InterpretedLanguage: {isinstance(javascript, InterpretedLanguage)}")
    print(f"JavaScript instanceof ProgrammingLanguage: {isinstance(javascript, ProgrammingLanguage)}")
    print(f"C++ instanceof CompiledLanguage: {isinstance(cpp, CompiledLanguage)}")
    print(f"C++ instanceof InterpretedLanguage: {isinstance(cpp, InterpretedLanguage)}")


if __name__ == "__main__":
    main()