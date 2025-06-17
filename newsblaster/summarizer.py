import os
from concurrent.futures import ProcessPoolExecutor 

def summarize_file(file_path, max_chars = 500):
    try:
        with open(file_path, "r", encoding='utf-8') as file:
            text = file.read()

        summary = text[:max_chars].strip() +"\n..."

        os.makedirs("summaries", exist_ok = True)
        base_name = os.path.basename(file_path)
        save_path = os.path.join("summaries", base_name)

        with open(save_path, "w", encoding='utf-8') as f:
            f.write(summary)
        print(f"Summary saved to {save_path}")
    except Exception as e:
        print(f"Error summarizing {file_path}: {e}")

def parallel_summarize(raw_dir = "raw_articles"):
    all_files = [os.path.join(raw_dir,f) for f in os.listdir(raw_dir) if f.endswith(".txt")]
    with ProcessPoolExecutor(max_workers=4) as executor:
        executor.map(summarize_file, all_files)


   
        