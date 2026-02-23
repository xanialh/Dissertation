import os
import soundfile as sf
from datasets import load_dataset

def download_data(num_samples=5):
    print(f"Downloading data. {num_samples} samples")

    dataset = load_dataset("techiaith/banc-trawsgrifiadau-bangor", split="test", trust_remote_code=True)

    audio_dir = "./data/raw_audio"
    text_dir = "./data/ground_truth"

    for i, item in enumerate(dataset.take(num_samples)):
        filename = f"clip_{i}"
        audio_path = os.path.join(audio_dir, f"{filename}.wav")
        sf.write(audio_path, item['audio']['array'], item['audio']['sampling_rate'])

        text_path = os.path.join(text_dir, f"{filename}.txt")
        with open(text_path, "w", encoding="utf-8") as f:
            f.write(item['sentence'])

        print(f"file saved: {filename}")

if __name__ == '__main__':
    download_data(5)