# SloBENCH evaluation script - translation

All commands should be run from the root directory of this repository.

## Build docker image 
```
docker buildx build --platform linux/amd64 -t slobench/eval:translation_sl -f evaluation_scripts/eval_translation_sl/Dockerfile .
```

## Run evaluation 

Evaluation within SloBENCH will be run as follows:

```
docker run -it --name eval-container_translation_en --rm \
-v $PWD/evaluation_scripts/eval_translation_sl/reference.zip:/reference_dataset.zip \
-v $PWD/evaluation_scripts/eval_translation_sl/submission.zip:/submission.zip \
slobench/eval:translation_sl_1.1 reference_dataset.zip submission.zip
```

As `reference.zip` is not available, you can do manual testing as follows:


```
docker run -it --name eval-container_translation_sl --rm \
-v $PWD/evaluation_scripts/eval_translation_sl/sample_reference.zip:/reference_dataset.zip \
-v $PWD/evaluation_scripts/eval_translation_sl/sample_submission.zip:/submission.zip \
slobench/eval:translation_sl_1.1 reference_dataset.zip submission.zip
```

This command should result in an output like this:


```
{
  "status": "S",
  "metrics": {
    "BLEU (avg)": 0.540459638826303,
    "METEOR (avg)": 0.6818485042165279,
    "CHRF (avg)": 0.632641023976876,
    "BLEU (corpus)": 0.5815499689913606,
    "CHRF (corpus)": 0.6326410239768762,
    "BERT score": 0.5326410239768762
  },
  "evaluation_time": 1.876391,
  "error_report": ""
}
```