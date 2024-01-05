import csv
import os
import heapq

# Define o tamanho do buffer em memória principal
BUFFER_SIZE = 1000

def merge_sort(input_filename, output_filename):
    # Divide o arquivo em "runs" e ordena cada run individualmente
    runs = divide_runs(input_filename)
    sorted_runs = [sort_run(run) for run in runs]

    # Realiza o merge externo dos runs ordenados
    merged_run = merge_runs(sorted_runs)

    # Escreve o run final ordenado no arquivo de saída
    write_run(output_filename, merged_run)

    # Remove os arquivos temporários (runs)
    for run in runs:
        os.remove(run)

def divide_runs(input_filename):
    runs = []
    with open(input_filename, 'r') as input_file:
        reader = csv.DictReader(input_file)
        run_number = 0
        while True:
            run = []
            for _ in range(BUFFER_SIZE):
                try:
                    record = next(reader)
                    run.append(record)
                except StopIteration:
                    break
            if not run:
                break
            run.sort(key=lambda x: x['chave_de_ordenacao'])  # Ordena o run internamente
            run_filename = f'run_{run_number}.csv'
            write_run(run_filename, run)
            runs.append(run_filename)
            run_number += 1
    return runs

def sort_run(run):
    run.sort(key=lambda x: x['chave_de_ordenacao'])
    return run

def merge_runs(runs):
    merged_run = []

    run_files = [open(run, 'r') for run in runs]
    run_readers = [csv.DictReader(run_file) for run_file in run_files]

    heap = []
    for i, reader in enumerate(run_readers):
        try:
            record = next(reader)
            heapq.heappush(heap, (record['chave_de_ordenacao'], i, record))
        except StopIteration:
            pass

    while heap:
        _, i, record = heapq.heappop(heap)
        merged_run.append(record)

        try:
            new_record = next(run_readers[i])
            heapq.heappush(heap, (new_record['chave_de_ordenacao'], i, new_record))
        except StopIteration:
            pass

    # Fecha os arquivos temporários
    for run_file in run_files:
        run_file.close()

    return merged_run

def write_run(output_filename, run):
    with open(output_filename, 'w', newline='') as output_file:
        fieldnames = run[0].keys()
        writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(run)

if __name__ == "__main__":
    input_filename = "exemplo.csv"
    output_filename = "arquivo_ordenado.csv" 

    merge_sort(input_filename, output_filename)
    print(f"Arquivo {input_filename} foi ordenado com sucesso e salvo como {output_filename}.")
