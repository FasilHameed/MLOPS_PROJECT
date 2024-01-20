import os
from pathlib import Path
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# List of files to create
list_of_files = [
    ".github/workflows/.gitkeep",
    "src/__init__.py",
    "src/components/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_transformation.py",
    "src/components/model_trainer.py",
    "src/components/model_evaluation.py",  # Corrected the typo
    "src/pipeline/__init__.py",
    "src/pipeline/training.py",
    "src/pipeline/prediction_pipeline.py",
    "src/utils/__init__.py",
    "src/utils.py",
    "test/unit/__init__.py",
    "test/integration/__init__.py",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "experiment/experiments.ipynb",
    "src/logger/logging.py",
    "src/exception/exception" 
]

# Loop through the list of files
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    # Create directories if they don't exist
    if filedir and not os.path.exists(filedir):
        os.makedirs(filedir, exist_ok=True)

    # Check if the file doesn't exist or is empty
    if not filepath.exists() or filepath.stat().st_size == 0:
        try:
            # Create an empty file
            with open(filepath, "w") as f:
                logging.info(f"Created file: {filepath}")
        except Exception as e:
            logging.error(f"Error creating file {filepath}: {e}")
