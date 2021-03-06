from os import EX_CANTCREAT
import sys
from zipfile import ZipFile
import json
from evaluate import evaluate
from datetime import datetime
from time import sleep

def extract_zip_contents(file, path):
     '''Extract all zip contents'''
     try:
          with ZipFile(file, 'r') as zip_ref:
               zip_ref.extractall(path)
               return path
     except Exception as e:
          raise Exception(f'Error unzipping {file} contents. Error: "{e}"')


def run_evaluation(data_reference_path, data_submission_path):
     '''Runs the evaluation procedure'''
     try:
          metrics = evaluate(data_reference_path, data_submission_path)
          return metrics
     except Exception as e:
          raise Exception(f'Error in evaluation script: {e}')

def print_tseo_success(metrics, elapsed_time):
     '''Send the Successful Task Submission Evaluation Object (TSEO) back to the server'''
     tseo = {
               "status": "S",
               "metrics": metrics,
               "evaluation_time": elapsed_time.total_seconds(),
               "error_report": ""
          }
     json_formatted_str = json.dumps(tseo, indent=2)
     print(json_formatted_str)


def print_tseo_failure(error, elapsed_time):
     '''Send the Failed Task Submission Evaluation Object (TSEO) back to the server'''
     tseo = {
               "status": "F",
               "metrics": {},
               "evaluation_time": elapsed_time.total_seconds(),
               "error_report": f"{error}"
          }
     json_formatted_str = json.dumps(tseo, indent=2)
     print(json_formatted_str)


if __name__ == '__main__':
     try:
          start_time = datetime.now()
          # Unzip
          data_reference_path = extract_zip_contents(sys.argv[1], path='data_reference')
          data_submission_path = extract_zip_contents(sys.argv[2], path='data_submission')
          metrics = run_evaluation(data_reference_path, data_submission_path)
          # Run evaluation
          elapsed_time = datetime.now() - start_time
          print_tseo_success(metrics, elapsed_time)
     except Exception as e:
          elapsed_time = datetime.now() - start_time
          print_tseo_failure(str(e), elapsed_time)