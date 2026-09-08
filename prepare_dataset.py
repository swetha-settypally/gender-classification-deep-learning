from pathlib import Path
import shutil

project_dir = Path(__file__).resolve().parent

source_path = input("Enter UTKFace folder path: ").strip().strip('"')
source_dir = Path(source_path)

male_dir = project_dir / "dataset" / "male"
female_dir = project_dir / "dataset" / "female"

male_dir.mkdir(parents=True, exist_ok=True)
female_dir.mkdir(parents=True, exist_ok=True)

male_count = 0
female_count = 0
skipped_count = 0

for image_path in source_dir.rglob("*"):
    if image_path.suffix.lower() not in [".jpg", ".jpeg", ".png"]:
        continue

    try:
        parts = image_path.name.split("_")
        gender = int(parts[1])
    except (IndexError, ValueError):
        skipped_count += 1
        continue

    if gender == 0:
        shutil.copy2(image_path, male_dir / image_path.name)
        male_count += 1

    elif gender == 1:
        shutil.copy2(image_path, female_dir / image_path.name)
        female_count += 1

    else:
        skipped_count += 1

print("\nDataset preparation completed!")
print("Male images:", male_count)
print("Female images:", female_count)
print("Skipped images:", skipped_count)