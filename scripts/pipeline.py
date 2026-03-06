import subprocess
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    filename="logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

print("Starting Retail Data Engineering Pipeline\n")
logging.info("Pipeline Started")


def run_step(script_name, step_name):
    try:
        print(f"\nRunning {step_name}...")
        logging.info(f"Starting {step_name}")

        subprocess.run(["python", f"scripts/{script_name}"], check=True)

        logging.info(f"{step_name} completed successfully")

    except subprocess.CalledProcessError:
        logging.error(f"{step_name} failed")
        print(f"{step_name} failed. Check logs.")
        exit()


# Pipeline Steps
run_step("ingest_data.py", "Data Ingestion")
run_step("clean_data.py", "Data Cleaning")
run_step("feature_engineering.py", "Feature Engineering")
run_step("load_database.py", "Database Loading")
run_step("analysis_queries.py", "Data Analysis")
run_step("visualization.py", "Data Visualization")
run_step("ml_models.py", "Machine Learning Models")

print("\nPipeline Completed Successfully")
logging.info("Pipeline Completed Successfully")