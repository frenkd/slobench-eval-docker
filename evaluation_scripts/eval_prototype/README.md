# eval_prototype slobench evaluation script
This folder also contains reference dataset (ground truth) and submission .zip files for mock testing
(these obviously won't be included in the public repo).

## Build docker image (from the root directory of this repo):
```
docker buildx build --platform linux/amd64 -t slobench/eval:prototype -f evaluation_scripts/eval_prototype/Dockerfile .
```

## Run mock evaluation (from the root directory of this repo)
```
docker run -it --name eval_prototype --rm \
-v $PWD/evaluation_scripts/eval_prototype/reference_dataset.zip:/reference_dataset.zip \
-v $PWD/evaluation_scripts/eval_prototype/submission.zip:/submission.zip \
slobench/eval:prototype reference_dataset.zip submission.zip
```