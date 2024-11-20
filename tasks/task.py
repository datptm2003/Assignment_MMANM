from my_rsa import RSA

class Task:
    def __init__(self, rsa: RSA, description: str, typecasts: dict[str, type], callback):
        self.rsa = rsa
        self.description = description
        self.typecasts = typecasts
        self.callback = callback

    def show_description(self):
        return self.description
    
    def execute(self, *args):
        self.rsa.reset()
        return self.callback(self.rsa, *args)
    
    def perform(self):
        print(f"Task: {self.description}")
        args = []
        for param, cast_type in self.typecasts.items():
            while True:
                try:
                    user_input = input(f"Enter {param} ({cast_type.__name__}): ")
                    value = cast_type(user_input)  # Cast the input to the specified type
                    args.append(value)
                    break
                except ValueError:
                    print(f"Invalid input! {param} must be of type {cast_type.__name__}.")
        
        # Execute the callback with the collected arguments
        result, duration = self.execute(*args)
        print(">> Result:", result.show())
        print(f">> Execution time: {duration:.4f} seconds")

