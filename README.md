# 498L_Final_Project
Generative Adversarial Networks and Their Applications

# Getting the Data
## Spirits
We have made the data available in this repo itself, so it can be used immediately when cloned into a Jupyter Notebook.

If you want to run the scraping script on your local machine, simply run `python spirit_data.py` to download the images into a new `img/` folder.

## CIFAR-10 and STL-10
We use Pytorch's builtin Dataset object: https://pytorch.org/docs/stable/torchvision/datasets.html#cifar
Setting download=True will automatically download the data to your specified root directory.

Notes: we experimented with Celeb-A and LSUN, but ran into issues with Colab crashing.
