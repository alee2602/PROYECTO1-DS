import os
import pandas as pd


def unir_dataframes(
    input_dir = "../data/csv",
    output_dir = ".",
    output_file = "data_unificada.csv"
    ):
    

    os.makedirs(output_dir, exist_ok=True)

    # Lista para los DataFrames
    dataframes = []

    for filename in os.listdir(input_dir):
        if filename.endswith(".csv"):
            filepath = os.path.join(input_dir, filename)
            df = pd.read_csv(filepath)
            dataframes.append(df)

    # Verificar que sí se cargaron archivos
    if not dataframes:
        print("No se encontraron archivos CSV en el directorio.")
    else:
        merged_df = pd.concat(dataframes, ignore_index=True)

        output_path = os.path.join(output_dir, output_file)
        merged_df.to_csv(output_path, index=False)
        print(f"CSV combinado guardado en: {output_path}")



if __name__ == "__main__":
    unir_dataframes(
    input_dir = "../data/csv",
    output_dir = ".",
    output_file = "data_unificada.csv"
    )