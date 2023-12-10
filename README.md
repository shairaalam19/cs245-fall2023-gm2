# GM2: Improving Caption Similarity with GLIDE Generative Models

- [GM2: Improving Caption Similarity with GLIDE Generative Models](#gm2-improving-caption-similarity-with-glide-generative-models)
  - [Project report](#project-report)
  - [Dataset](#dataset)
  - [Run our own trained models](#run-our-own-trained-models)
  - [Train your own models](#train-your-own-models)
  - [Results](#results)
  - [Evaluation](#evaluation)
  - [Project presentation slides](#project-presentation-slides)
  - [Team](#team)

## Project report

Find the report [here](./final_report.pdf).

## Dataset

We used a small subset of the Google Dreambooth dataset. We captioned all images ourselves. Here the link to our pruned database: <https://github.com/shairaalam19/cs245-fall2023-gm2-datasets/>

Google Dreambooth dataset: <https://github.com/google/dreambooth/tree/main/dataset>

## Run our own trained models

Testing Colab:
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shairaalam19/cs245-fall2023-gm2/blob/maniknarang%2Fsubmission/glide_finetuned_testing.ipynb)

Download base and upsampler models and export to your own Google Drive: <https://drive.google.com/drive/folders/1qKwaRCI5w88VQKvAfKTuGIQkI0qGRNZw?usp=drive_link>

Update `glide_path` and `sr_glide_path` parameters with the paths to base and upsampler models respectively. Use paths from your own Google Drive.

## Train your own models

Base model Colab:
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shairaalam19/cs245-fall2023-gm2/blob/maniknarang%2Fsubmission/glide_finetuned_train_model.ipynb)

Upsampler model Colab:
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shairaalam19/cs245-fall2023-gm2/blob/maniknarang%2Fsubmission/glide_finetuned_train_model_upsampler.ipynb)

## Results

All results are exported to [`images/`](./images/) directory.

[Captions](./images/captions.txt)

- [Real photographs](./images/real_photos/)
- [OpenAI's GLIDE generated photographs](./images/original_glide/)
- [Our finetuned GLIDE generated photographs](./images/finetuned_glide/)

## Evaluation

Use FID score evaluation to compare image quality between realm images and generated images. You can find that code in [`evaluator/calculate_fid.py`](./evaluator/calculate_fid.py) file.

## Project presentation slides

Find slides [here](./project-presentation.pdf).

## Team

- Harshil Bhullar
- Manik Narang
- Shaira Alam
- William Santosa
