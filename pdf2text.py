import subprocess

def pdftotext(pdf_path, output_dir):
    command = f"nougat --markdown pdf '{pdf_path}' --out '{output_dir}'"
    
    try:
        subprocess.run(command, shell=True, check=True)
        print(f"PDF generated successfully in the '{output_dir}' directory.")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
