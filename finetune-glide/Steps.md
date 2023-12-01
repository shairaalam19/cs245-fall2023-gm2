# Steps to use

1. Run Python 3.10.0
2. Create venv using `python -m .venv venv`
3. Activate venv by running `source .venv/Scripts/activate` (to deactivate just enter `deactivate`)
4. Install requirements using `pip install -r requirements.txt`
5. cd into `data/datasets` directory
6. Run `scripts/a.sh` (this will take a while to download)
7. Run `wandb offline`
8. Go back to root and run `python train_glide.py --data 'data/datasets/coco`