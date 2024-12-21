import os, subprocess, json
from tkinter import Tk, Label, Entry, Checkbutton, BooleanVar, Button, messagebox, LabelFrame

PARTS_CONFIG = {
    "HOOD": ["STYLE01", "STYLE02", "STYLE03", "STYLE04", "STYLE05", "STYLE06", "STYLE07", "STYLE08", "STYLE09", "STYLE10", "STYLE11", "STYLE12", "STYLE13", "STYLE14", "STYLE15"],
    "HOOD_CF": ["STYLE01", "STYLE02", "STYLE03", "STYLE04", "STYLE05", "STYLE06", "STYLE07", "STYLE08", "STYLE09", "STYLE10", "STYLE11", "STYLE12", "STYLE13", "STYLE14", "STYLE15"],
    "SPOILER": ["STYLE01", "STYLE02", "STYLE03", "STYLE04", "STYLE05", "STYLE06", "STYLE07", "STYLE08", "STYLE09", "STYLE10", "STYLE11", "STYLE12", "STYLE13", "STYLE14", "STYLE15"],
    #"FRONT_TIRE": ["STYLE01", "STYLE02", "STYLE03", "STYLE04", "STYLE05", "STYLE06", "STYLE07", "STYLE08", "STYLE09", "STYLE10", "STYLE11", "STYLE12", "STYLE13", "STYLE14", "STYLE15"],
    # Mais tipos de peças serão adicionados, falta finalizar as rodas (FRONT_TIRE) e tambem os KIT/KITW
    # Caso necessario o uso alem dos STYLE15, é só adicionar mais entradas (STYLE16, 17, 18....) nas chaves acima e rodar o script, simples assim.
}

def load_templates(file_path):
    with open(file_path, 'r') as file:
        templates = json.load(file)
        for key in templates:
            templates[key] = "".join(templates[key])
    return templates

def replace_placeholders(template, replacements):
    for key, value in replacements.items():
        template = template.replace(key, value)
    return template

def execute_quickhasher(item_name, car):
    work_dir = os.path.dirname(os.path.abspath(__file__))

    qh_exe = os.path.join(work_dir, 'resources', f"quickhashercli.exe bin-int:{item_name} commerce:{item_name} bin-int:{car}")
    qh_run = subprocess.run(qh_exe, stdout=subprocess.PIPE)
    return qh_run.stdout.decode("utf-8").split(" ")

def process_part(car, part_type, style, templates, output_files):
    style_number = int(style.split('STYLE')[1])
    replacements = {
        '!car!': car,
        '!style!': style,
        '!priority!': str(100 - style_number),
        '!partName!': f"{car}_{style}_{part_type.upper()}",
        '!partTitle!': style,
        '!shortdesc!': f"CAR_MDL_{car.upper()}"
    }
    #part_name = car + '_' + style + '_' + part_type
    part_name = f"{car}_{style}_{part_type}".upper()

    quickhasher_output = execute_quickhasher(part_name, car)
    print(part_name)
    replacements.update({
        '!partHash!': quickhasher_output[0],
        '!vltNode!': quickhasher_output[1],
        '!baseCar!': quickhasher_output[2]
    })

    with open(output_files['nfsms'], "a+") as outF1:
        outF1.write(replace_placeholders(templates['nfsms'][part_type.lower()], replacements))

    with open(output_files['xml'], "a+") as outF2:
        outF2.write(replace_placeholders(templates['xml'][part_type.lower()], replacements))

# GUI Setup
app = Tk()
app.title("Car Visual Parts Generator")
app.geometry("600x550")

Label(app, text="Car Name:").pack(pady=1)
car_name_entry = Entry(app, width=30)
car_name_entry.pack(pady=1)

frames_container = LabelFrame(app, text="", padx=1, pady=1)
frames_container.pack(pady=10, fill="both")

# Dicionário para armazenar as variáveis de seleção das peças
part_vars = {}

# Criar dinamicamente as seções para cada tipo de peça
for part, styles in PARTS_CONFIG.items():
    frame = LabelFrame(frames_container, text=part.upper(), padx=1, pady=1)
    frame.pack(side="left", padx=10, pady=5, fill="both")
    
    part_vars[part] = []  # Lista de BooleanVars para cada tipo de peça
    for style in styles:
        var = BooleanVar()
        part_vars[part].append((style, var))
        Checkbutton(frame, text=style, variable=var).pack(anchor="w")

def generate():
    car_name = car_name_entry.get()
    if not car_name:
        messagebox.showwarning("Input Error", "Please enter the car name.")
        return

    selected_parts = {}

    # Coletar os estilos selecionados para cada tipo de peça
    for part, style_vars in part_vars.items():
        selected_styles = [style for style, var in style_vars if var.get()]
        if selected_styles:
            selected_parts[part] = selected_styles

    if not any(selected_parts.values()):
        messagebox.showwarning("Selection Error", "Please select at least one style.")
        return

    work_dir = os.path.dirname(os.path.abspath(__file__))
    templates = {
        'nfsms': load_templates(os.path.join(work_dir, 'resources', 'nfsms_template.json')),
        'xml': load_templates(os.path.join(work_dir, 'resources', 'xml_template.json'))
    }

    output_files = {
        'nfsms': os.path.join(work_dir, f"{car_name}_visualparts.nfsms"),
        'xml': os.path.join(work_dir, f"{car_name}_visualparts_catalog.xml")
    }

    for part_type, styles in selected_parts.items():
        for style in styles:
            process_part(car_name, part_type, style, templates, output_files)

    messagebox.showinfo("Success", f"Files generated for car: {car_name}")

Button(app, text="Generate", command=generate).pack(pady=10)

app.mainloop()