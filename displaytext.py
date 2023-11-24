from IPython import display

def displaytotext(file_path):
    try:
        from IPython import display
        with open(file_path, 'r') as file:
            latex_content = file.read()
            display.display(display.Latex(latex_content))
    except ImportError:
        def print_content():
            with open(file_path, 'r') as file:
                latex_content = file.read()
                print(latex_content)

        try:
            print_content()
        except FileNotFoundError:
            print(f"Error: File not found - {file_path}")